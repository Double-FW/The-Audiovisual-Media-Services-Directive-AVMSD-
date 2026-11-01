#!/usr/bin/env python3
"""Small offline package and record validator. No external writes or legal certification."""
from pathlib import Path
import argparse,copy,hashlib,json,re,sys
from datetime import date
import yaml
from jsonschema import Draft202012Validator

ROOT=Path(__file__).resolve().parents[1]
TODAY='2026-11-01'  # deterministic fixture date; CLI overrides for real authority expiry
TYPES={}
def digest(r):
    return hashlib.sha256(json.dumps({k:v for k,v in r.items() if k not in ['status','approval_id']},sort_keys=True,separators=(',',':'),ensure_ascii=False).encode()).hexdigest()
def dependencies(r,by):
    found=set()
    def visit(value):
        if isinstance(value,str) and value in by and value!=r['id']:
            if value not in found:
                found.add(value);visit(by[value]['data']);visit(by[value]['relationships'])
        elif isinstance(value,dict):
            for v in value.values():visit(v)
        elif isinstance(value,list):
            for v in value:visit(v)
    visit(r['data']);visit(r['relationships']);return found
def load(p):
    return json.loads(p.read_text()) if p.suffix=='.json' else yaml.safe_load(p.read_text())
def records_errors(bundle,schema,sources,today,workflows=None):
    errors=[]
    def err(code,id,msg):errors.append((code,id,msg))
    records=bundle.get('records',[]);by={r.get('id'):r for r in records}
    if len(by)!=len(records):err('E_ID','bundle','duplicate record ID')
    validator=Draft202012Validator(schema)
    for r in records:
        for e in validator.iter_errors(r):err('E_SCHEMA',r.get('id','?'),f'{list(e.path)}: {e.message}')
    if errors:return errors
    # Direct typed references. Generic relationships/provenance are checked separately.
    types={
      'jurisdiction_id':['jurisdiction'],'requirement_id':['requirement'],'target_id':['target'],
      'programme_id':['programme'],'feature_id':['feature'],'rights_id':['rights'],'supplier_id':['supplier'],
      'route_id':['route'],'plan_id':['action_plan'],'baseline_id':['coverage'],'current_id':['coverage'],
      'retest_id':['delivery','quality'],'report_id':['report'],'delegation_id':['delegation'],
      'classification_id':['classification'],'conclusion_id':['conclusion'],'approval_id':['approval'],
      'coverage_id':['coverage'],'accessible_contact_test_id':['delivery','quality'],'issue_id':['issue'],
      'evidence_ids':['evidence'],'visual_audit_evidence_ids':['evidence'],'quality_ids':['quality'],
      'viewer_ids':['viewer'],'coverage_ids':['coverage'],'baseline_coverage_ids':['coverage'],
      'target_ids':['target'],'action_ids':['issue'],'conclusion_ids':['conclusion'],'delivery_ids':['delivery'],
      'feature_ids':['feature'],'requirement_ids':['requirement'],'unresolved_issues':['issue']}
    def ref(id,owner,allowed=None):
        target=by.get(id)
        if not target:err('E_REF',owner,'unknown record '+str(id));return None
        if allowed and target['record_type'] not in allowed:err('E_TYPE',owner,'wrong type for '+id)
        return target
    def walk(data,owner):
        if isinstance(data,dict):
            for k,v in data.items():
                if k=='target_id' and by[owner]['record_type']=='approval':ref(v,owner)
                elif k=='protocol_id':ref(v,owner,['delegation'])
                elif k in types:
                    for id in v if isinstance(v,list) else [v]:ref(id,owner,types[k])
                elif k in ['origin_id','target_id','affected_ids']:
                    for id in v if isinstance(v,list) else [v]:ref(id,owner)
                elif k in ['source_id','national_source_ids']:
                    for id in v if isinstance(v,list) else [v]:
                        if id not in sources:err('E_SOURCE',owner,'unknown source '+id)
                        elif sources[id]['status'] in ['unavailable','superseded']:err('E_STALE',owner,'unusable source '+id)
                else:walk(v,owner)
        elif isinstance(data,list):
            for v in data:walk(v,owner)
    for r in records:
        id=r['id'];d=r['data'];t=r['record_type']
        for related in r['relationships']:ref(related,id)
        for p in r['provenance']:
            if p=='SYNTHETIC' and r['synthetic']:continue
            if p not in sources and p not in by:err('E_SOURCE',id,'unknown provenance '+p)
        walk(d,id)
        if 'approval_id' in r:ref(r['approval_id'],id,['approval'])
        if r['created']>r['updated']:err('E_DATE',id,'updated predates creation')
        for key in ['created','updated']:
            try:date.fromisoformat(r[key])
            except ValueError:err('E_DATE',id,'invalid ISO date '+key)
        for key in ['valid_from','expires','approval_date','valid_until','review_date','due_date','review_due']:
            if key in d:
                try:date.fromisoformat(d[key])
                except ValueError:err('E_DATE',id,'invalid ISO date '+key)
        if t=='evidence' and ((d['kind']=='synthetic')!=r['synthetic']):err('E_SYNTHETIC',id,'synthetic evidence label mismatch')
        if t=='evidence' and d['kind']=='participant' and d['access']=='public_synthetic':err('E_PRIVACY',id,'participant evidence in public synthetic area')
    if any(x[0] in ['E_REF','E_TYPE','E_SOURCE'] for x in errors):return errors
    def get(id):return by[id]
    def same_scope(a,b):return a['scope']==b['scope']
    for r in records:
        id=r['id'];d=r['data'];t=r['record_type']
        if t=='source' and d['source_state']=='superseded' and r['status'] in ['active','approved']:err('E_STALE',id,'superseded source active')
        if t=='classification':
            jur=get(d['jurisdiction_id'])
            if d['applicability']=='applicable' and not jur['data']['resolved']:err('E_SCOPE',id,'missing resolved national adapter')
            if d['mode']=='mixed' and d['applicability']!='unresolved':err('E_SCOPE',id,'split mixed services into individual classifications')
        if t=='target':
            req=get(d['requirement_id'])['data']
            if '13' in req['clause'] or '23' in req['clause']:err('E_TARGET',id,'European-works/advertising provision is not an accessibility target')
            if d['authority']=='national' and req['national_dependency']!='verified':err('E_SCOPE',id,'national target lacks verified national requirement')
        if t=='requirement':
            source=sources[d['source_id']]
            if not r['synthetic'] and d['applicability']=='applicable' and source['status'] in ['partial_official_index','navigation_verified','unavailable']:err('E_PRIMARY',id,'primary provision review incomplete')
        if t in ['feature','editorial','rights','route','delivery','quality','viewer','issue']:
            p=get(d['programme_id'])
            if d['programme_version']!=p['data']['asset_version']:err('E_ASSET',id,'programme edition/version mismatch')
            if r['scope']['region']!=p['data']['region']:err('E_ASSET',id,'programme region mismatch')
        if t=='feature':
            rights=get(d['rights_id'])['data']
            if d['availability']=='present' and (d['language'] not in rights['languages'] or r['scope']['region'] not in rights['regions'] or rights['rights_state']!='confirmed'):err('E_RIGHTS',id,'feature not covered by confirmed rights')
            if rights['programme_id']!=d['programme_id'] or rights['programme_version']!=d['programme_version']:err('E_ASSET',id,'rights concern different edition')
        if t=='editorial' and d['route_choice']=='no_separate_ad' and d['conflicts_with_obligation']:err('E_EDITORIAL',id,'editorial choice cannot override legal obligation')
        if t=='route':
            f=get(d['feature_id'])['data']
            if f['programme_id']!=d['programme_id'] or f['programme_version']!=d['programme_version'] or f['asset_version']!=d['feature_version']:err('E_ASSET',id,'route binds wrong programme/feature version')
            p=get(d['programme_id'])['data']
            if f['language']!=d['expected_language'] or f['feature']!=d['expected_feature'] or p['episode']!=d['expected_episode'] or p['edition']!=d['expected_edition']:err('E_ASSET',id,'route language/feature/episode/edition differs from expected target')
        if t in ['delivery','quality']:
            route=get(d['route_id'])['data'];f=get(d['feature_id'])['data']
            if any(d[k]!=route[k] for k in ['programme_id','programme_version','feature_id']):err('E_ASSET',id,'test differs from route asset')
            if d['result']=='pass' and not d['assumptions_valid']:err('E_ASSUMPTION',id,'invalid assumptions cannot pass')
            if d['source_result'].lower() in ['error','tool_error','invalid','not_tested','cannot tell','incomplete','needs review'] and d['result']=='pass':err('E_ADAPTER',id,'adapter converted invalid/error/uncertainty into pass')
            if d['result']=='pass' and f['availability']!='present':err('E_DELIVERY',id,'absent/unknown feature cannot pass')
        if t=='acceptance' and d['result']=='accepted':
            if any(get(i)['data']['result']!='pass' for i in d['quality_ids']):err('E_SUPPLIER',id,'supplier acceptance lacks passing assessment')
        if t=='viewer':
            if d['children_protection_data'] and d['commercial_reuse']:err('E_PRIVACY',id,'children protection data commercial reuse prohibited')
            if d['finding']=='supported' and (d['negative_cases'] or d['missing_viewers']):err('E_VIEWER',id,'unqualified supported finding hides negative/missing cases; split scope or constrain')
        if t=='coverage':
            target=get(d['target_id'])['data']
            if d['numerator_unit']!=d['denominator_unit']:err('E_UNITS',id,'numerator/denominator units differ')
            if d['numerator']>d['denominator']:err('E_COUNT',id,'numerator exceeds denominator')
            if d['feature']!=target['feature'] or d['method_version']!=target['method_version']:err('E_COUNT',id,'target feature/method mismatch')
            if d['stage']=='usable' and not d['delivery_ids']:err('E_DELIVERY',id,'usable provision lacks delivery tests')
            eligible={};den_seconds=0
            for interval in d['denominator_inventory']:
                p=get(interval['programme_id'])['data'];start,end=interval['start'],interval['end'];key=(interval['programme_id'],interval['programme_version'])
                if interval['programme_version']!=p['asset_version'] or not 0<=start<end<=p['duration_seconds']:err('E_COUNT',id,'invalid denominator interval/version')
                for a,b in eligible.setdefault(key,[]):
                    if max(start,a)<min(end,b):err('E_OVERLAP',id,'denominator overlap/repeat double count')
                eligible[key].append((start,end));den_seconds+=end-start
            expected_den=den_seconds/60 if d['denominator_unit']=='minutes' else len(eligible)
            if abs(expected_den-d['denominator'])>1e-8:err('E_COUNT',id,'denominator differs from declared eligible inventory')
            seen={};total=0
            for interval in d['intervals']:
                p=get(interval['programme_id']);pd=p['data'];start,end=interval['start'],interval['end'];key=(p['id'],interval['programme_version'])
                if interval['programme_version']!=pd['asset_version'] or end>pd['duration_seconds'] or end<=start:err('E_COUNT',id,'invalid interval/version')
                if key not in eligible or not any(a<=start<end<=b for a,b in eligible[key]):err('E_COUNT',id,'numerator interval outside eligible denominator')
                for a,b in seen.setdefault(key,[]):
                    if max(start,a)<min(end,b):err('E_OVERLAP',id,'overlap/repeat double count')
                seen[key].append((start,end));total+=end-start
                if d['stage']=='usable':
                    tests=[get(i)['data'] for i in d['delivery_ids'] if get(i)['data']['programme_id']==p['id']]
                    if not tests or any(x['result']!='pass' or get(x['feature_id'])['data']['feature']!=d['feature'] for x in tests):err('E_DELIVERY',id,'usable provision includes missing/failed/wrong feature')
            if d['numerator_unit']=='minutes' and abs(total/60-d['numerator'])>1e-8:err('E_COUNT',id,'minutes do not match qualifying intervals')
            if d['numerator_unit'] in ['titles','episodes'] and len(seen)!=d['numerator']:err('E_COUNT',id,'title/episode count differs from eligible inventory')
        if t=='improvement':
            a,b=get(d['baseline_id'])['data'],get(d['current_id'])['data']
            if not d['reconciliation'].strip() and d['progress']!='cannot_compare':err('E_PROGRESS',id,'missing period/catalogue reconciliation')
            if a['feature']!=b['feature'] or a['numerator_unit']!=b['numerator_unit']:err('E_PROGRESS',id,'incompatible comparison')
            if a['stage']!=b['stage'] and d['progress']!='cannot_compare':err('E_PROGRESS',id,'unlike provision stages cannot establish comparable progress')
        if t=='issue' and d['resolution']=='verified_resolved':
            retest=get(d['retest_id'])
            if retest['data']['result']!='pass' or not d['correction_version']:err('E_RETEST',id,'resolution lacks successful versioned retest')
        if t=='emergency' and d['missing_variants'] and not d['urgent_correction'].strip():err('E_EMERGENCY',id,'missing accessible emergency route without urgent correction')
        if t=='delegation' and r['status']=='active' and (d['expires']<today or d['revoked']):err('E_AUTHORITY',id,'active delegation expired or revoked')
        if t=='approval':
            target=get(d['target_id']);deleg=get(d['delegation_id'])
            if d['target_version']!=target['record_version'] or d['target_digest']!=digest(target):err('E_BINDING',id,'approval artifact version/hash mismatch')
            expected={i:digest(by[i]) for i in dependencies(target,by)}
            if d['dependency_digests']!=expected:err('E_BINDING',id,'approval dependency versions/content changed; review affected decision')
            if not same_scope(r,target) or d['approved_scope']!=target['scope']:err('E_BINDING',id,'approval scope/period differs')
            auth=deleg['data']
            if d['human_name']!=auth['human_name'] or 'approve' not in auth['operations'] or auth['revoked'] or deleg['status']!='active' or not auth['valid_from']<=d['approval_date']<=auth['expires'] or d['valid_until']>auth['expires'] or d['valid_until']<today:err('E_AUTHORITY',id,'approver lacks current matching authority')
            if r['synthetic']!=target['synthetic'] or r['synthetic']!=deleg['synthetic']:err('E_SYNTHETIC',id,'fictional approval mixed with operational decision')
        if r['status']=='approved' and t!='approval':
            approval=get(r['approval_id'])
            if approval['record_type']!='approval' or approval['status']!='approved' or approval['data']['target_id']!=id:err('E_APPROVAL',id,'approval does not approve this exact record')
        if t=='conclusion':
            scope=get(d['classification_id'])['data'];req=get(d['requirement_id'])['data']
            if d['result']=='met':
                if get(d['classification_id'])['status']!='approved':err('E_SCOPE',id,'positive conclusion requires approved classification')
                if scope['mode']=='vsp' and req['clause'].startswith('Article 7'):err('E_VSP',id,'Article 7 not automatically applied to every platform upload')
                if scope['applicability']!='applicable' or req['applicability']!='applicable':err('E_SCOPE',id,'positive conclusion without applicable approved scope')
                if d['unresolved_issues']:err('E_CONCLUSION',id,'unresolved material issue in positive conclusion')
                if not d['quality_ids'] or not d['coverage_ids']:err('E_CONCLUSION',id,'positive accessibility conclusion requires quality and provision evidence')
                for i in d['quality_ids']:
                    if get(i)['data']['result']!='pass':err('E_CONCLUSION',id,'positive conclusion despite quality failure')
                for i in d['coverage_ids']:
                    c=get(i)['data'];target=get(c['target_id'])['data'];value=100*c['numerator']/c['denominator'] if target['unit']=='percent' else c['numerator']
                    if value<target['threshold']:err('E_CONCLUSION',id,'positive conclusion despite missed target')
                if any(get(i)['data']['finding']=='not supported' for i in d['viewer_ids']):err('E_CONCLUSION',id,'severe viewer barrier needs legal investigation; cannot assert met automatically')
        if t=='report':
            if d.get('deadline_source_actor')=='member_state' and d.get('duty_holder')=='provider':err('E_DEADLINE',id,'Member State reporting cycle used for provider deadline')
            for fig in d['figures']:
                c=get(fig['coverage_id'])
                if d['period']!=r['scope']['period'] or not same_scope(r,c) or any(fig[k]!=c['data'][k] for k in ['numerator','denominator']):err('E_REPORT',id,'report period/figures differ from evidence')
        if t=='submission':
            report=get(d['report_id']);approval=get(d['approval_id'])
            if report['status']!='approved' or approval['data']['target_id']!=report['id'] or approval['data']['target_digest']!=digest(report) or d['report_version']!=report['record_version'] or d['report_digest']!=digest(report):err('E_BINDING',id,'submission not exact approved report')
            if d['operation']=='submitted' and (not d['receipt'].strip() or not d['transaction_id'].strip()):err('E_RECEIPT',id,'submission lacks verified receipt/transaction')
        if t=='claim':
            conclusion=get(d['conclusion_id'])
            if d['publication_state'] in ['handoff','published']:
                if conclusion['status']!='approved' or conclusion['data']['result']!='met':err('E_CLAIM',id,'claim lacks approved supporting conclusion')
                if not same_scope(r,conclusion):err('E_CLAIM',id,'claim broadens conclusion scope')
                if d['valid_until']<today:err('E_AUTHORITY',id,'claim expired')
                if d['publication_state']=='published' and not d['receipt'].strip():err('E_RECEIPT',id,'publication not confirmed')
    for run in bundle.get('executions',[]):
        definition=next((w for w in (workflows or []) if w['id']==run['workflow_id']),None)
        if workflows is not None and definition is None:err('E_REF',run['run_id'],'unknown workflow ID')
        defined_steps={s['id']:s for s in definition['steps']} if definition else {}
        completed=set()
        for step in run['steps']:
            if definition and (step['id'] not in defined_steps or step['depends_on']!=defined_steps[step['id']]['depends_on']):err('E_STEP',step['id'],'step/dependencies differ from workflow definition')
            current='pending'
            for transition in step['history']:
                next_state=transition['to'];allowed={'pending':['running','blocked'],'running':['blocked','failed','awaiting_approval','complete'],'blocked':['running'],'failed':['running'],'awaiting_approval':['complete','blocked'],'complete':[]}
                if next_state not in allowed[current]:err('E_TRANSITION',step['id'],current+' to '+next_state)
                if current in ['blocked','failed'] and not transition.get('resume_evidence_ids'):err('E_TRANSITION',step['id'],'retry/resume lacks resolved dependency evidence')
                for i in transition.get('resume_evidence_ids',[]):ref(i,step['id'])
                current=next_state
            if current=='complete':
                if not step['evidence_ids']:err('E_STEP',step['id'],'completed step without evidence')
                if not set(step['depends_on'])<=completed:err('E_STEP',step['id'],'dependency incomplete')
                if step['requires_approval'] and not step.get('approval_id'):err('E_APPROVAL',step['id'],'completed gate lacks approval')
                if step.get('approval_id'):ref(step['approval_id'],step['id'],['approval'])
                completed.add(step['id'])
            for i in step['evidence_ids']:ref(i,step['id'])
    return errors

def package_errors(root):
    errors=[]
    def err(msg):errors.append(('E_PACKAGE',str(root),msg))
    required=['README.md','AGENTS.md','CHANGELOG.md','guides/README.md','control/source-register.yaml','control/source-review.md','control/document-index.yaml','control/legal-status.yaml','control/requirement-register.yaml','control/validation-report.md','workflows/workflows.yaml','workflows/workflow.schema.json','records/README.md','records/record.schema.json','records/templates.yaml','examples/synthetic-programme-and-service-cycle.yaml','validation/README.md','validation/cases.yaml','validation/check_repository.py']
    idxpath=root/'control/document-index.yaml'
    if not idxpath.exists():return [('E_PACKAGE',str(root),'missing document index')]
    try:
        index=load(idxpath);required += [d['path'] for d in index['documents']]
        for p in required:
            if not (root/p).is_file():err('missing '+p)
        structured={str(p.relative_to(root)):load(p) for p in root.rglob('*') if p.suffix in ['.yaml','.json']}
        for p,x in structured.items():
            if p.endswith('.schema.json'):Draft202012Validator.check_schema(x)
        wf=structured['workflows/workflows.yaml'];ws=structured['workflows/workflow.schema.json']
        for e in Draft202012Validator(ws).iter_errors(wf):err('workflow schema: '+e.message)
        ids=[w['id'] for w in wf['workflows']];sources=structured['control/source-register.yaml']['sources'];sids=[s['id'] for s in sources]
        if len(set(ids))!=len(ids) or len(set(sids))!=len(sids):err('duplicate workflow/source ID')
        dids=[d['id'] for d in index['documents']]
        if len(set(dids))!=len(dids) or len(dids)!=7:err('expected seven unique guide IDs')
        types=set(structured['records/record.schema.json']['properties']['record_type']['enum'])
        for w in wf['workflows']:
            if not set(w['depends_on'])<=set(ids) or not set(w['output_types'])<=types:err('unknown workflow/type reference '+w['id'])
            seen=set()
            for step in w['steps']:
                if step['id'] in seen or not set(step['depends_on'])<=seen:err('step ID/dependency '+step['id'])
                seen.add(step['id'])
        def cycle(id,stack):
            if id in stack:err('workflow dependency cycle');return
            for dep in next(w for w in wf['workflows'] if w['id']==id)['depends_on']:cycle(dep,stack+[id])
        for id in ids:cycle(id,[])
        def anchors(p):
            txt=p.read_text();return {re.sub(r'[^\w\- ]','',x.lower()).replace(' ','-') for x in re.findall(r'^#{1,6} (.+)$',txt,re.M)}
        for doc in index['documents']:
            p=root/doc['path'];txt=p.read_text();meta=yaml.safe_load(txt.split('---',2)[1])
            for k in ['document_id','version','status','authority_type','review_date','source_ids','prerequisites','output_record_types']:
                if k not in meta:err('missing guide metadata '+k)
            if meta['document_id']!=doc['id'] or meta['status']!=doc['status']:err('index/metadata inconsistency '+doc['id'])
            for k in ['source_ids','prerequisites','output_record_types','authority_type']:
                if meta[k]!=doc[k]:err('index/metadata mismatch '+k+' '+doc['id'])
            if not set(doc['section_anchors'])<=anchors(p):err('missing indexed anchor '+doc['id'])
            if not set(meta['source_ids'])<=set(sids) or not set(doc['workflow_ids'])<=set(ids) or not set(meta['output_record_types'])<=types:err('unknown guide source/workflow/type '+doc['id'])
            if meta['status']!='draft':err('guide adoption status unsupported by this unapproved package')
        for req in structured['control/requirement-register.yaml']['requirements']:
            if req['source_id'] not in sids or req['workflow_id'] not in ids:err('unknown requirement source/workflow')
        for p in root.rglob('*.md'):
            for link in re.findall(r'\[[^\]]*\]\(([^)]+)\)',p.read_text()):
                if re.match(r'^[a-z]+:',link):continue
                path,_,anchor=link.partition('#');target=(p.parent/path).resolve() if path else p
                if not target.is_relative_to(root.resolve()):err('link escapes repository '+link)
                elif not target.exists():err('broken link '+str(p.relative_to(root))+' '+link)
                elif anchor and target.suffix=='.md' and anchor not in anchors(target):err('broken anchor '+link)
    except Exception as e:err(type(e).__name__+': '+str(e))
    return errors

def apply_mutations(bundle,mutations):
    b=copy.deepcopy(bundle)
    for m in mutations:
        if m['record_id']=='$bundle':target=b
        else:target=next(r for r in b['records'] if r['id']==m['record_id'])
        bits=m['path'].split('.')
        for bit in bits[:-1]:target=target[int(bit)] if isinstance(target,list) else target[bit]
        key=int(bits[-1]) if isinstance(target,list) else bits[-1]
        if m.get('delete'):del target[key]
        else:target[key]=copy.deepcopy(m['value'])
    return b

def main():
    p=argparse.ArgumentParser();p.add_argument('--root',type=Path,default=ROOT);p.add_argument('--records',type=Path);p.add_argument('--as-of',default=TODAY);p.add_argument('--skip-fixtures',action='store_true');args=p.parse_args();root=args.root.resolve()
    errors=package_errors(root)
    if errors:
        for e in errors:print(' | '.join(e))
        return 1
    schema=load(root/'records/record.schema.json');sources={s['id']:s for s in load(root/'control/source-register.yaml')['sources']};bundle=load(root/'examples/synthetic-programme-and-service-cycle.yaml')
    workflows=load(root/'workflows/workflows.yaml')['workflows']
    errors+=records_errors(bundle,schema,sources,args.as_of,workflows)
    if args.records:errors+=records_errors(load(args.records),schema,sources,args.as_of,workflows)
    tested=0
    if not args.skip_fixtures:
        cases=load(root/'validation/cases.yaml')['cases'];case_ids=set()
        for c in cases:
            if c['id'] in case_ids:errors.append(('E_CASE',c['id'],'duplicate case ID'))
            case_ids.add(c['id']);b=apply_mutations(bundle,c['mutations']);found=records_errors(b,schema,sources,args.as_of,workflows);codes={e[0] for e in found};expected=set(c['expected_error_codes'])
            if not expected<=codes or (not expected and found):errors.append(('E_CASE',c['id'],f'expected {expected}; got {codes}'))
            if not c['expected_route'] or not c['expected_status'] or not c['prohibited_conclusions'] or not c['evidence_required']:errors.append(('E_CASE',c['id'],'missing developer reference decision'))
            if c['expected_route'] not in {w['id'] for w in load(root/'workflows/workflows.yaml')['workflows']}:errors.append(('E_CASE',c['id'],'unknown routing reference'))
            tested+=1
    if errors:
        for e in errors:print(' | '.join(e))
        print(f'FAIL: {len(errors)} findings');return 1
    print(f'PASS: seven guides, 12 workflows, {len(sources)} sources, {len(bundle["records"])} linked synthetic records; {tested} developer fixtures.')
    print('Human checks pending: legal truth/currency and national application; editorial judgement; actual evidence, identity/authority, privacy/rights; independent benchmark and operational pilot. Routing labels are developer reference decisions, not measured AI-routing accuracy.')
    return 0
if __name__=='__main__':sys.exit(main())
