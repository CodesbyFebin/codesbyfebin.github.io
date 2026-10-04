"""Import source article fragments; record all editorial removals."""
import json,re,html
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1];SRC=ROOT.parent/'sources/workspace/codesbyfebin.github.io';GROK=ROOT.parent/'sources/grok/.grok/skills';changes=[];articles=[]
def text(s):return html.unescape(re.sub('<[^>]+>',' ',s)).strip()
def clean(s,slug):
 original=s
 # Draft experiential claims are not supported by measurement artifacts.
 evidence=re.compile(r'\bmy\b|\bour\b|\bI\s+(?:diagnose|prefer|recommend|remember|learn|can|will|usually|always|never|see|wrote|am|was|enforce|hand|maintain|cite|quote|give|sequence|hold|value)|\bI\s+(?:built|measured|use|run|teach|review|found|did|have|spent|host|keep|ship|maintain|worked|saw|learned)|\bwe\s+(?:measured|deployed|saved|run|built|host|found|achieved)|every code block runs|every number is measured|survived three years|production repository adds|was measured on|Measured on|in production for|in my benchmarks|These numbers come from',re.I)
 def paragraphs(m):
  s=m.group(0)
  if evidence.search(text(s)):
   changes.append({'slug':slug,'reason':'Unsupported personal experience or measurement','removed':text(s)[:240]});return ''
  return s
 s=re.sub(r'<p\b[^>]*>.*?</p>',paragraphs,s,flags=re.S)
 s=re.sub(r'<li\b[^>]*>.*?</li>',paragraphs,s,flags=re.S)
 s=re.sub(r'//[^\n]*(?:3\.4\s*s|96\s*KB|@65k)[^\n]*','// Illustrative sketch; no measurement reported',s)
 s=re.sub(r'64-bit prime field[^<]*?(?:security|fastest arithmetic)[^<]*', 'Security depends on the complete protocol parameters, not the base field alone. ',s)
 s=re.sub(r'128-bit raises the floor at ~15% prover cost\.', 'Changing fields requires re-evaluating the protocol and measuring implementation cost.',s)
 # Empirical timing/cost comparison tables cannot be represented as observations.
 def tables(m):
  t=text(m.group(0))
  if evidence.search(t) or re.search(r'prover.*(?:time|seconds)|\b(?:p50|p99|latency|measured|peak RSS)\b|cycles.*(?:seconds|\bKB\b)',t,re.I):
   changes.append({'slug':slug,'reason':'Unmeasured empirical table','removed':t[:240]});return '<p>Measure this comparison on your own workload. No timing or memory table from the draft is presented as an observed result.</p>'
  return m.group(0)
 s=re.sub(r'<table\b[^>]*>.*?</table>',tables,s,flags=re.S)
 s=re.sub(r'<script\b.*?</script>','',s,flags=re.S|re.I)
 s=s.replace('Every step compiles against axum 0.7+ and tokio,','The sketches illustrate Axum and Tokio patterns; check the dependency version before adapting them,').replace('cloning the Arc per request is free','cloning the Arc per request increments its shared reference count').replace('let truly unexpected errors panic into your 500 handler','return an internal error for unexpected failures and log the cause').replace('complete runnable Rust snippets','illustrative Rust snippets').replace('complete runnable','illustrative').replace('every code block runs','code sketches require validation').replace('without runtime overhead','without a tracing garbage collector')
 # Fix the identified route-version mismatch in the imported Axum draft.
 if slug in ['axum-web-server-tutorial','axum-rest-api-serde']:s=s.replace('axum 0.7+','Axum 0.8').replace('/proofs/:id','/proofs/{id}')
 # Don't duplicate lede metadata as article text.
 s=re.sub(r'^\s*<p class="lede answer">.*?</p>','',s,count=1,flags=re.S)
 return s
for a in json.loads((SRC/'data/articles.json').read_text())['articles']:
 s=(SRC/'src/pages/blog'/a['cluster']/(a['slug']+'.body.html')).read_text();s=clean(s,a['slug']);date=a['date']
 if date>'2026-10-04':changes.append({'slug':a['slug'],'reason':'Future draft date replaced by actual package publication date','old':date});date='2026-10-04'
 title=a['title'];desc=a['meta'].replace('complete runnable Rust snippets','illustrative Rust snippets').replace('working STARK prover','STARK proving design').replace('in under an hour','through a small example')
 title=title.replace('Your First STARK in Under an Hour','A Small STARK Design Walkthrough')
 articles.append({'slug':a['slug'],'silo':a['cluster'],'path':'/blog/'+a['cluster']+'/'+a['slug']+'/','title':title,'description':desc,'date':date,'type':a['type'],'origin':'Adapted from supplied workspace article draft','body':s,'sections':[],'faq':[],'primaryKeyword':a.get('primary_kw','')})
# Use the bounded tutorial from the Grok site in place of the inflated source.
bounded=next(a for a in json.loads((ROOT/'data/imported-articles.json').read_text()) if a['slug']=='zkp-tutorial-developers')
a=next(a for a in articles if a['slug']==bounded['slug']);parts=[]
for i,p in enumerate(bounded['paragraphs']):
 if '3.4 seconds' in p:p='This note is adapted from a tutorial draft without a reproducible benchmark record. Code blocks are sketches, not a complete crate compiled by this site.'
 if p.startswith('The draft printed a table:'):p='The tutorial draft supplied benchmark figures without a source revision, exact parameters, or a measurement record. Those figures are not published here.'
 p=p.replace('debug columns become part of the public statement once a verifier pins them','unnecessary columns increase the data processed by the prover')
 block='<pre><code>'+html.escape(p[5:])+'</code></pre>' if p.startswith('CODE\n') else '<p>'+html.escape(p)+'</p>'
 if i in [0,2,4,7,9,11,13,15]:parts.append('<h2 id="note-'+str(i)+'">'+['Scope of this walkthrough','Trace, constraints, commitment','A small teaching ISA','Execution and determinism','Constraint boundaries','Benchmark traps','Security parameters','Next reading'][[0,2,4,7,9,11,13,15].index(i)]+'</h2>')
 parts.append(block)
a.update(title=bounded['title'],description='Trace, constraints, commitments, a small teaching ISA, program pinning, and four traps. A bounded walkthrough without unmeasured proof claims.',body='\n'.join(parts),origin='Bounded adaptation of preview-article.html and supplied Grok tutorial note')
# Keep the originating fragments and their revision history in the package.
(ROOT/'content/workspace-articles.json').write_text(json.dumps(articles,indent=2,ensure_ascii=False));(ROOT/'EDITORIAL-CHANGES.json').write_text(json.dumps(changes,indent=2,ensure_ascii=False));print('Imported',len(articles),'full article drafts;',len(changes),'editorial corrections')
