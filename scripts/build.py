#!/usr/bin/env python3
"""Build the static portfolio using the Python standard library only."""
import json,re,html,shutil,os,math,hashlib
from pathlib import Path
from datetime import date
from urllib.parse import urlparse
from xml.etree import ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]; OUT=ROOT/'dist'
CONFIG=json.loads((ROOT/'data/site.json').read_text()); BASE=CONFIG['url'].rstrip('/'); TODAY=CONFIG['updated']
H=html.escape
SILOS={'stark':('STARK & verifiable compute','Trace semantics, proof statements, commitments, and meaningful negative controls.','https://github.com/facebook/winterfell'), 'rust':('Rust systems engineering','Ownership, async boundaries, service design, and operational behavior.','https://doc.rust-lang.org/book/'), 'self-hosting':('Sovereign self-hosting','Deployment, networking, backups, and recovery under your own control.','https://kubernetes.io/docs/concepts/'), 'ai-infra':('AI infrastructure & MCP','Tool permissions, retrieval, durable workers, and evidence of execution.','https://modelcontextprotocol.io/specification/')}
def slug(t):return re.sub(r'[^a-z0-9]+','-',t.lower()).strip('-')
def write(p,s):
 q=OUT/p.lstrip('/');q.parent.mkdir(parents=True,exist_ok=True);q.write_text(s,encoding='utf8')
def link(path,title):return f'<a href="{H(path)}">{H(title)}</a>'
def words(s):return len(re.findall(r'\b[\w’\'-]+\b',html.unescape(re.sub('<[^>]*>',' ',s))))
def script(x):return json.dumps(x,ensure_ascii=False).replace('<','\\u003c')
articles=json.loads((ROOT/'content/workspace-articles.json').read_text())
SILOS['grok-build']=('Application build guides','Identity, persistence, multiplayer, games, 3D graphics, LLM clients, and interface design.','https://developer.mozilla.org/en-US/docs/Web')
for g in json.loads((ROOT/'content/grok-guides.json').read_text()):
 g.update(silo='grok-build',path='/blog/grok-build/'+g['slug']+'/',origin='New adaptation of supplied Grok platform documentation: '+g['reference'],date=TODAY,type='guide',faq=[])
 articles.append(g)
def article_path(a):return a['path']
by_source={ '/blog/'+a['silo']+'/'+a['slug']+'/':a['path'] for a in articles }
for a in articles:
 if 'body' not in a:continue
 body=a['body'].replace('{{ROOT}}','/')
 def fix_link(m):
  ref=m.group(1)
  if ref.startswith('http'):
   if 'codesbyfebin.github.io' not in ref:return m.group(0)
   ref=ref.split('codesbyfebin.github.io',1)[1]
  path,sep,frag=ref.partition('#')
  if path.startswith('/blog/'):
   path=by_source.get(path.rstrip('/')+'/',path)
   if path.rstrip('/') in ['/blog/'+k for k in SILOS]:path=path.rstrip('/')+'/'
  elif frag and path.startswith(('/systems','/projects','/specifications','/research','/services','/contributions')):
   path=path.split('.')[0].rstrip('/')+'/'
   if path=='/projects/' and any(p['slug']==frag for p in json.loads((ROOT/'data/projects.json').read_text())):path='/projects/'+frag+'/'
   sep=frag=''
  if path=='/blog/':sep=frag=''
  return 'href="'+H(path+(sep+frag if sep else ''))+'"'
 body=re.sub(r'href="([^"]*)"',fix_link,body)
 # Remove empty FAQ entries after unsupported answers were stripped.
 body=re.sub(r'<details>\s*<summary>.*?</summary>\s*</details>','',body,flags=re.S)
 a['body']=body
 a['faq']=[{'question':html.unescape(re.sub('<[^>]+>',' ',q)).strip(),'answer':html.unescape(re.sub('<[^>]+>',' ',ans)).strip()} for q,ans in re.findall(r'<details>\s*<summary>(.*?)</summary>(.*?)</details>',body,re.S) if re.sub('<[^>]+>',' ',ans).strip()]
projects=json.loads((ROOT/'data/projects.json').read_text())
if OUT.exists():shutil.rmtree(OUT)
OUT.mkdir();shutil.copytree(ROOT/'assets',OUT/'assets')
shutil.copy(ROOT/'assets/site.css',OUT/'assets/site.css');shutil.copy(ROOT/'assets/site.js',OUT/'assets/site.js')
person={'@id':BASE+'/#person','@type':'Person','name':'Febin Francis','alternateName':'CodesbyFebin','url':BASE+'/','jobTitle':'Systems Engineer','homeLocation':{'@type':'Place','name':'Kerala, India'},'knowsAbout':['AI infrastructure','Systems engineering','Verifiable compute','Self-hosting'],'knowsLanguage':['en','ml'],'sameAs':['https://github.com/CodesbyFebin','https://codesbyfebin.github.io/','https://dev.to/codesbyfebin']}
website={'@id':BASE+'/#website','@type':'WebSite','url':BASE+'/','name':'CodesbyFebin','publisher':{'@id':person['@id']},'inLanguage':'en'}
pages=[];graph=[person,website];edges=[]
NAV=[('/projects/','Projects'),('/systems/','Systems'),('/blog/','Field notes'),('/about/','About'),('/contact/','Contact')]
def page(path,title,desc,body,extra=None,crumbs=None,noindex=False):
 url=BASE+path; desc=html.unescape(re.sub('<[^>]+>',' ',desc));desc=(desc[:154].rsplit(' ',1)[0]+'.') if len(desc)>160 else desc
 entity={'@type':'WebPage','@id':url+'#page','url':url,'name':title,'description':desc,'isPartOf':{'@id':website['@id']},'about':{'@id':person['@id']},'inLanguage':'en'}
 nodes=[person,website,entity]+(extra or [])
 trail=''
 if crumbs:
  bc={'@type':'BreadcrumbList','@id':url+'#breadcrumb','itemListElement':[{'@type':'ListItem','position':i+1,'name':n,'item':BASE+p} for i,(p,n) in enumerate(crumbs)]};nodes.append(bc)
  trail='<nav class="breadcrumb" aria-label="Breadcrumb">'+'<span aria-hidden="true"> / </span>'.join(link(p,n) for p,n in crumbs[:-1])+f'<span aria-hidden="true"> / </span><span>{H(crumbs[-1][1])}</span></nav>'
 footer='<div class="footer-grid"><div><strong>CodesbyFebin<span class="accent">_</span></strong><p>Systems that prove what happened.</p><p class="small">Kerala, India · English / Malayalam</p></div><div><p class="eyebrow">FIELD GUIDES</p>'+''.join(link('/blog/'+k+'/',v[0]) for k,v in SILOS.items())+'</div><div><p class="eyebrow">EXPLORE</p>'+''.join(link(p,n) for p,n in [('/research/','Research'),('/specifications/','Specifications'),('/contributions/','Contributions'),('/github/','GitHub'),('/services/','Working together'),('/methodology/','Editorial method'),('/privacy/','Privacy'),('/feed.xml','RSS'),('/llms.txt','AI reading index')])+'</div></div>'
 output=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{H(title)} · CodesbyFebin</title><meta name="description" content="{H(desc)}"><meta name="author" content="Febin Francis"><meta name="robots" content="{'noindex,follow' if noindex else 'index,follow,max-image-preview:large'}"><link rel="canonical" href="{url}"><meta property="og:title" content="{H(title)}"><meta property="og:description" content="{H(desc)}"><meta property="og:url" content="{url}"><meta property="og:type" content="{'article' if '/blog/' in path and len(path.strip('/').split('/'))>2 and path!='/blog/' else 'website'}"><meta property="og:image" content="{BASE}/assets/social.png"><meta name="twitter:card" content="summary_large_image"><link rel="icon" href="/assets/favicon.svg" type="image/svg+xml"><link rel="stylesheet" href="/assets/site.css"><link rel="alternate" type="application/atom+xml" title="CodesbyFebin notes" href="/feed.xml"><link rel="search" type="application/opensearchdescription+xml" title="CodesbyFebin" href="/opensearch.xml"><script type="application/ld+json">{script({'@context':'https://schema.org','@graph':nodes})}</script><script defer src="/assets/site.js"></script></head><body><a class="skip" href="#main">Skip to content</a><header><div class="nav-shell"><a class="brand" href="/">CodesbyFebin<span class="accent">_</span></a><nav aria-label="Main">{''.join(link(p,n) for p,n in NAV)}</nav><button id="theme" type="button" aria-label="Toggle color theme">◐</button></div></header><main id="main" class="shell">{trail}{body}</main><footer class="shell">{footer}<div class="footer-bottom"><span>© 2026 Febin Francis</span><span>Source-linked. Scope stated. Results measured separately.</span></div></footer></body></html>'''
 dest='index.html' if path=='/' else path.strip('/')+'/index.html';write(dest,output)
 if not noindex:pages.append({'path':path,'title':title,'description':desc});graph.extend([entity]+(extra or []))
def heading(kicker,title,lede):return f'<div class="page-heading"><p class="eyebrow">{H(kicker)}</p><h1>{H(title)}</h1><p class="lede">{H(lede)}</p></div>'
def card(a):return f'<a class="card note-card" href="{article_path(a)}" data-silo="{a["silo"]}" data-title="{H(a["title"].lower())}"><span class="eyebrow">{H(SILOS[a["silo"]][0])}</span><h3>{H(a["title"])}</h3><p>{H(a["description"][:190])}</p><span class="card-end">{a["minutes"]} min read <span aria-hidden="true">↗</span></span></a>'
# Resolve related articles by lexical overlap, with explicit cross-silo bridges.
for a in articles:
 tokens=set(re.findall(r'[a-z]{4,}',a['title'].lower()))
 rank=lambda b:len(tokens&set(re.findall(r'[a-z]{4,}',b['title'].lower())))
 same=sorted([b for b in articles if b!=a and b['silo']==a['silo']],key=rank,reverse=True)[:3]
 other=sorted([b for b in articles if b['silo']!=a['silo']],key=rank,reverse=True)[:2]
 a['related']=[b['slug'] for b in same+other];a['wordCount']=words(a['body']) if 'body' in a else sum(words(x[1]) for x in a['sections']);a['minutes']=max(1,math.ceil(a['wordCount']/200));a['url']=BASE+article_path(a)
 a['tags']=sorted(tokens)
 for b in same+other:edges.append({'from':a['slug'],'to':b['slug'],'kind':'related'})
# Add reverse relationships to keep the navigational graph reciprocal.
for a in articles:
 incoming=[e['from'] for e in edges if e['to']==a['slug']]
 for other in incoming:
  if other not in a['related']:a['related'].append(other)
 existing={(e['from'],e['to']) for e in edges}
 for other in a['related']:
  if (a['slug'],other) not in existing:edges.append({'from':a['slug'],'to':other,'kind':'reciprocal'})
for a in articles:
 content=a.get('body','');toc=[link('#'+ident,html.unescape(re.sub('<[^>]+>',' ',name))) for ident,name in re.findall(r'<h2[^>]*id="([^"]+)"[^>]*>(.*?)</h2>',content,re.S)]
 for i,(name,text) in enumerate(a['sections']):
  ident='section-'+str(i+1);toc.append(link('#'+ident,name))
  if text.startswith('CODE\n'):block='<pre><code>'+H(text[5:])+'</code></pre>'
  elif text.startswith(('fn ','//','docker ','version:')):block='<pre><code>'+H(text)+'</code></pre>'
  else:block='<p>'+H(text)+'</p>'
  content+=f'<section id="{ident}"><h2>{H(name)}</h2>{block}</section>'
 source=SILOS[a['silo']][2]
 sourcebox=f'<aside class="callout"><h2>Source and scope</h2><p>{H(a["origin"])}. This is an adapted technical draft. Code examples require version checks and validation before use. No benchmarks, deployment history, or proposed experiments are reported as verified results.</p><p>{link(source,"Primary reference: "+SILOS[a["silo"]][0])} · {link("/methodology/","How these notes are maintained")}</p></aside>'
 faqs=''
 if a['faq'] and 'body' not in a:faqs='<section><h2>Questions to carry into a review</h2>'+''.join(f'<details><summary>{H(q["question"])}</summary><p>{H(q["answer"])}</p></details>' for q in a['faq'])+'</section>'
 related=[next(b for b in articles if b['slug']==s) for s in a['related']]
 learning=[b for b in articles if b['silo']==a['silo']];position=learning.index(a);previous=learning[position-1] if position else None;following=learning[position+1] if position+1<len(learning) else None
 learning_links='<section><h2>Learning path</h2><p>Suggested reading order, not a claim that the previous article is a technical dependency.</p>'+('<p>Previous: '+link(article_path(previous),previous['title'])+'</p>' if previous else '')+('<p>Next: '+link(article_path(following),following['title'])+'</p>' if following else '')+'</section>'
 article={'@type':'TechArticle','@id':a['url']+'#article','headline':a['title'],'description':a['description'],'url':a['url'],'mainEntityOfPage':{'@id':a['url']+'#page'},'author':{'@id':person['@id']},'publisher':{'@id':person['@id']},'datePublished':a['date'],'dateModified':TODAY,'inLanguage':'en','wordCount':a['wordCount'],'articleSection':SILOS[a['silo']][0],'isPartOf':{'@id':BASE+'/blog/'+a['silo']+'/#collection'},'citation':[source],'image':BASE+'/assets/social.png','speakable':{'@type':'SpeakableSpecification','cssSelector':['.page-heading h1','.page-heading .lede']}}
 extra=[article]
 if a['faq']:extra.append({'@type':'FAQPage','@id':a['url']+'#faq','mainEntity':[{'@type':'Question','name':q['question'],'acceptedAnswer':{'@type':'Answer','text':q['answer']}} for q in a['faq']]})
 body=heading(SILOS[a['silo']][0],a['title'],a['description'])+f'<p class="meta">Febin Francis · <time datetime="{a["date"]}">{a["date"]}</time> · {a["minutes"]} min read · {a["wordCount"]} words</p><p class="small">Adapted technical draft · code examples require validation</p><div class="reading-layout"><aside class="toc"><h2>On this page</h2>'+''.join(toc)+link('#related','Related reading')+'</aside><article class="prose">'+content+sourcebox+faqs+learning_links+f'<section id="related"><h2>Related reading</h2><ul>'+''.join('<li>'+link(article_path(b),b['title'])+'</li>' for b in related)+'</ul><p>'+link('/blog/'+a['silo']+'/', 'Return to '+SILOS[a['silo']][0])+'</p></section><section><h2>Discuss a reproducible example</h2><p>Share the source revision, environment, expected outcome, and observed result. Do not paste credentials or private data.</p>'+link('https://github.com/CodesbyFebin','Find the relevant repository on GitHub')+'</section></article></div>'
 page(article_path(a),a['title'],a['description'],body,extra,[('/','Home'),('/blog/','Field notes'),('/blog/'+a['silo']+'/',SILOS[a['silo']][0]),(article_path(a),a['title'])])
for k,(name,desc,ref) in SILOS.items():
 items=[a for a in articles if a['silo']==k];entity={'@type':'CollectionPage','@id':BASE+'/blog/'+k+'/#collection','name':name,'url':BASE+'/blog/'+k+'/','isPartOf':{'@id':BASE+'/blog/#collection'},'hasPart':[{'@id':a['url']+'#article'} for a in items]}
 page('/blog/'+k+'/',name,desc,heading(f'{len(items)} notes · learning path',name,desc)+'<p>Start with definitions, move into implementation boundaries, then use failure experiments to challenge assumptions. These are reading notes of varying depth; each page states its scope.</p><div class="grid">'+''.join(card(a) for a in items)+'</div>',[entity],[('/','Home'),('/blog/','Field notes'),('/blog/'+k+'/',name)])
filters='<label class="search-label" for="search">Find a topic</label><input id="search" type="search" placeholder="Search notes, e.g. worker leases" aria-controls="notes"><div class="filters"><button class="selected" data-filter="all">All notes</button>'+''.join(f'<button data-filter="{k}">{H(v[0])}</button>' for k,v in SILOS.items())+'</div><p id="results" aria-live="polite"></p>'
page('/blog/','Engineering field notes',f'{len(articles)} source-linked notes on STARKs, Rust, self-hosting and AI infrastructure. Search by topic and follow connected learning paths.',heading('Knowledge base', 'Ideas you can put under test.', 'Small explanations, concrete failure modes, and practical checks. Read across five connected engineering paths.')+f'<p class="catalog-stats">{len(articles)} articles · {len(SILOS)} silos · {sum(a["wordCount"] for a in articles):,} body words</p>'+filters+'<div class="grid" id="notes">'+''.join(card(a) for a in articles)+'</div><p id="empty" hidden>No matching notes. Try a broader term.</p>',[{'@type':'CollectionPage','@id':BASE+'/blog/#collection','url':BASE+'/blog/','name':'Engineering field notes','hasPart':[{'@id':BASE+'/blog/'+k+'/#collection'} for k in SILOS]}],[('/','Home'),('/blog/','Field notes')])
def pc(p):return f'<a class="card project-card" href="/projects/{p["slug"]}/"><span class="eyebrow">{H(p["category"])}</span><h3>{H(p["name"])}</h3><p>{H(p["summary"])}</p><span class="card-end">{H(p["language"])} <span>Inspect source ↗</span></span></a>'
page('/projects/','Projects and source records','Explore source-linked projects from the supplied repository snapshot: verifiable compute, AI agents, sovereign infrastructure, and developer tools.',heading('Repository atlas','The work, with its boundaries.', 'Project descriptions come from the supplied 3 October 2026 snapshot. Repository status may have changed; inspect the source before relying on a capability.')+'<div class="grid">'+''.join(pc(p) for p in projects)+'</div>',crumbs=[('/','Home'),('/projects/','Projects')])
for p in projects:
 body=heading(p['category'],p['name'],p['summary'])+'<div class="prose">'+''.join('<p>'+H(t)+'</p>' for t in p['paragraphs'])+'<h2>Inspect the repository</h2><p>'+link(p['url'],'Open '+p['name']+' on GitHub')+'</p><p>Source description retained from the supplied snapshot. This build does not claim to have compiled or qualified this project.</p><h2>Stack recorded in the source</h2><ul>'+''.join('<li>'+H(t)+'</li>' for t in p['stack'])+'</ul><h2>Read alongside</h2><ul>'+''.join('<li>'+link(article_path(a),a['title'])+'</li>' for a in articles if a['slug'] in p.get('articles',[]))+'</ul><p>'+link('/projects/','Browse all project records')+'</p></div>'
 page('/projects/'+p['slug']+'/',p['name'],p['summary'],body,crumbs=[('/','Home'),('/projects/','Projects'),('/projects/'+p['slug']+'/',p['name'])])
featured=[p for p in projects if p['slug'] in ['rust-stark-zkvm','agent-swarm','om-personal-ai']][:3]
if len(featured)<3:featured=projects[:3]
hero='''<section class="hero"><div><p class="eyebrow">FEBIN FRANCIS / KERALA, INDIA</p><h1>Build systems.<br><span class="accent">Prove the work.</span></h1><p class="lede">Systems Engineer · AI Infrastructure · Verifiable Compute</p><p>Building systems that prove what happened instead of asking you to trust what happened.</p><div class="actions"><a class="button" href="/projects/">Explore the work <span>↗</span></a><a class="button secondary" href="/blog/">Read field notes</a></div><p class="small">Open source. Explicit boundaries. Evidence before claims.</p></div><figure class="hero-visual"><img src="/assets/lab.jpg" alt="Dark workspace illustration with code on three monitors" width="1100" height="619"><figcaption>THE SYSTEMS WORKBENCH <span>01 / 04</span></figcaption><div class="terminal" aria-label="Engineering principles"><span class="accent">$ inspect the claim</span><br>source → execution → evidence<br><span class="dim">unknown remains unknown</span></div></figure></section>'''
rail='<section class="section"><div class="section-head"><div><p class="eyebrow">CONNECTED FIELD GUIDES</p><h2>Five paths into the system.</h2></div>'+link('/blog/','Browse all '+str(len(articles))+' notes →')+'</div><div class="silo-grid">'+''.join(f'<a class="silo-card" href="/blog/{k}/"><span class="eyebrow">0{i+1} / {len([a for a in articles if a["silo"]==k])} NOTES</span><h3>{H(v[0])}</h3><p>{H(v[1])}</p><span class="accent">Explore path ↗</span></a>' for i,(k,v) in enumerate(SILOS.items()))+'</div></section>'
page('/','Febin Francis — systems engineer and open-source builder','Febin Francis builds AI infrastructure, verifiable compute, and sovereign systems. Explore source-linked projects and practical engineering field notes.',hero+'<section class="section"><div class="section-head"><div><p class="eyebrow">SELECTED SYSTEMS</p><h2>Architecture meets implementation.</h2></div>'+link('/projects/','All projects →')+'</div><div class="grid">'+''.join(pc(p) for p in featured)+'</div></section>'+rail+'<section class="statement"><p class="eyebrow">THE OPERATING PRINCIPLE</p><h2>A green status needs<br>something behind it.</h2><p>Separate a configured system from an executing one. Preserve blocked states. Bind artifacts to their source. Test whether the verifier can reject a wrong result.</p>'+link('/methodology/','Read the editorial method →')+'</section>')
core={
'about':('About Febin Francis','Systems engineering from Kerala, India.','I build around three questions: what was intended, what actually ran, and what evidence survives. My focus includes AI infrastructure, verifiable computation, and systems people can inspect and operate themselves.','Working principles',['Describe the implemented boundary before the roadmap.','Keep source identity with each measured result.','Treat recovery and refusal paths as part of the product.']),
'systems':('Systems and architecture','Control planes, worker runtimes, and proof boundaries.','A control plane expresses intent and governs permissions. A runtime produces observed effects. An evidence layer records which source, environment, and artifacts support a result. These layers should agree without collapsing desired state into observed state.','Follow the system',['Intent: a mission, configuration, or deployment request.','Admission: identity, resource budget, policy, and approval.','Execution: bounded work with durable ownership.','Evidence: outputs and checks tied to the actual run.']),
'research':('Research notes','Questions that connect verifiable compute and agent infrastructure.','These notes are engineering investigations rather than journal publications. The useful starting point is a falsifiable claim: can a wrong program be rejected, can a stale worker commit, or can a restore recreate application state?','Current reading paths',['Proof statement binding and negative controls.','Agent tool permissions and independent checks.','Data locality and recovery in self-hosted systems.']),
'specifications':('Specifications and contracts','Define what a system is allowed to claim.','A useful contract names inputs, outputs, limits, permissions, and completion criteria. It states what happens on timeout and partial failure. Examples here are design guidance, not claims that a runtime implements every mechanism.','Contract review',['Inputs: typed fields, semantic ranges, ownership.','Outputs: stable identifiers, digests, retention.','Limits: duration, concurrency, resources, retries.','Completion: an observable result and an independent check.']),
'contributions':('Open-source contributions','Inspect repositories rather than invented event histories.','The supplied sources contain project records and technical writing. They do not substantiate the proposed meetup, workshop, or Monsoon Mesh event. This page points to inspectable source contributions without publishing an event schedule.','Ways to contribute',['Report a reproducible issue with version and environment.','Propose a focused change with an observable outcome.','Improve documentation where scope and actual behavior differ.']),
'github':('GitHub and source identity','The source is part of the explanation.','Use the GitHub profile to inspect repositories, histories, and contribution records. Star counts and activity are intentionally not copied as live statistics from a dated snapshot.','Source review checklist',['Read the README against the current tree.','Distinguish an original project from a fork.','Look for tests that reject incorrect behavior.']),
'services':('Working together','Systems architecture, AI infrastructure, and technical review.','My work focuses on clear interfaces, observable execution, and reviewable technical claims. A useful engagement starts with a concrete workflow and a defined result, then establishes the source and environment needed to verify that result.','Possible scopes',['Architecture review for an AI agent or control plane.','Technical documentation grounded in source.','Review of verification, recovery, and deployment boundaries.']),
'contact':('Contact Febin Francis','Start with the system and the outcome you need.','Use my public profiles to start a conversation. Include the repository or system, current behavior, desired result, and relevant constraints. Do not share tokens, personal data, or private production logs in public issues.','Public channels',['GitHub: CodesbyFebin.','DEV Community: codesbyfebin.','LinkedIn: codes-by-febin.']),
'methodology':('Editorial method and evidence scope','Source-linked explanations with explicit limits.','This portfolio merges 100 supplied workspace article drafts with seven new guides adapted from the supplied platform documentation. The STARK tutorial uses the bounded source note. Unsupported first-person measurements and deployment claims were removed. Article lengths are calculated from the final bodies; no universal 2,000-word minimum is claimed. Project descriptions preserve a dated source snapshot rather than fresh qualification results.','Publication rules',['No placeholder posts or fabricated case studies.','No claimed benchmarks without raw measurements and configuration.','No fabricated comments, events, live counters, or proof-success animations.','FAQ markup matches visible questions. No QAPage for editorial FAQs or invented local business entity.','English pages only; Malayalam capability does not imply a translated page.','Crawler access does not guarantee indexing, AI citation, or rankings.']),
'privacy':('Privacy','A static site with browser-local preferences.','The generated site has no analytics, tracking pixels, authentication, comments backend, or contact form. Theme preferences are stored in your browser. Search filters the already-loaded article cards. Following an external link subjects that visit to the destination service policies. Hosting providers may keep their own request logs.','Your choices',['Clear browser storage to reset the theme.','Read the full site without enabling JavaScript.','Use the RSS feed or AI reading index instead of interactive search.'])}
for key,(title,lede,intro,subtitle,items) in core.items():
 body=heading('Portfolio / '+key,title,lede)+'<div class="prose"><p>'+H(intro)+'</p><h2>'+H(subtitle)+'</h2><ul>'+''.join('<li>'+H(x)+'</li>' for x in items)+'</ul><h2>Public source and connected reading</h2><p>'+link('https://github.com/CodesbyFebin','GitHub profile')+' · '+link('https://dev.to/codesbyfebin','DEV Community')+' · '+link('https://www.linkedin.com/in/codes-by-febin/','LinkedIn profile')+'</p><p>'+link('/projects/','Project records')+' · '+link('/blog/','Engineering field notes')+'</p></div>'
 page('/'+key+'/',title,lede+' '+intro,body,crumbs=[('/','Home'),('/'+key+'/',title)])
page('/404/','Page not found','This page does not exist. Browse the project atlas or engineering field notes.',heading('404','That path has no artifact.','Follow a known path back into the site.')+'<p>'+link('/','Home')+' · '+link('/blog/','Field notes')+'</p>',noindex=True)
shutil.copy(OUT/'404/index.html',OUT/'404.html')
def alias(path,target):
 write(path,'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex,follow"><meta name="description" content="This portfolio page has moved to its canonical URL."><meta http-equiv="refresh" content="0;url='+target+'"><link rel="canonical" href="'+BASE+target+'"><meta property="og:image" content="'+BASE+'/assets/social.png"><title>Page moved · CodesbyFebin</title><script type="application/ld+json">'+script({'@context':'https://schema.org','@type':'WebPage','url':BASE+target})+'</script></head><body><h1>Page moved</h1><p>'+link(target,'Continue to the canonical page')+'</p></body></html>')
alias('portfolio.html','/')
for name in ['about','systems','projects','blog','services','research','contributions','contact','specifications','privacy']:alias(name+'.html','/'+name+'/')
alias('blog/zkp-tutorial-developers/index.html','/blog/stark/zkp-tutorial-developers/')
# Machine-readable outputs are generated from the same inventory as visible pages.
write('data/articles.json',json.dumps(articles,indent=2,ensure_ascii=False));write('data/projects.json',json.dumps(projects,indent=2));write('data/taxonomy.json',json.dumps({k:{'name':v[0],'description':v[1],'count':sum(a['silo']==k for a in articles)} for k,v in SILOS.items()},indent=2));write('data/graph.json',json.dumps({'nodes':[a['slug'] for a in articles],'edges':edges},indent=2));write('data/schema-graph.json',script({'@context':'https://schema.org','@graph':graph}));write('data/pages.json',json.dumps(pages,indent=2))
ET.register_namespace('','http://www.sitemaps.org/schemas/sitemap/0.9');ns='{http://www.sitemaps.org/schemas/sitemap/0.9}'
def sitemap(items):
 root=ET.Element(ns+'urlset')
 for p in items:
  el=ET.SubElement(root,ns+'url');ET.SubElement(el,ns+'loc').text=BASE+p['path']
 return ET.tostring(root,encoding='unicode',xml_declaration=True)
write('sitemap.xml',sitemap(pages));write('sitemap.json',json.dumps([BASE+p['path'] for p in pages],indent=2))
for k in SILOS:write('feeds/sitemap-'+k+'.xml',sitemap([p for p in pages if p['path']=='/blog/'+k+'/' or any(p['path']==article_path(a) for a in articles if a['silo']==k)]))
write('feeds/sitemap-core.xml',sitemap([p for p in pages if '/blog/' not in p['path'] or p['path']=='/blog/']))
idx=ET.Element(ns+'sitemapindex')
for k in [*SILOS,'core']:
 el=ET.SubElement(idx,ns+'sitemap');ET.SubElement(el,ns+'loc').text=BASE+'/feeds/sitemap-'+k+'.xml'
write('feeds/sitemap.xml',ET.tostring(idx,encoding='unicode',xml_declaration=True))
atom='{http://www.w3.org/2005/Atom}';feed=ET.Element(atom+'feed');ET.SubElement(feed,atom+'title').text='CodesbyFebin field notes';ET.SubElement(feed,atom+'id').text=BASE+'/feed.xml';ET.SubElement(feed,atom+'updated').text=TODAY+'T00:00:00Z';ET.SubElement(feed,atom+'link',href=BASE+'/feed.xml',rel='self');ET.SubElement(feed,atom+'link',href=BASE+'/blog/');author=ET.SubElement(feed,atom+'author');ET.SubElement(author,atom+'name').text='Febin Francis'
for a in sorted(articles,key=lambda x:x['date'],reverse=True)[:20]:
 e=ET.SubElement(feed,atom+'entry');ET.SubElement(e,atom+'title').text=a['title'];ET.SubElement(e,atom+'id').text=a['url'];ET.SubElement(e,atom+'link',href=a['url']);ET.SubElement(e,atom+'updated').text=TODAY+'T00:00:00Z';ET.SubElement(e,atom+'summary').text=a['description']
write('feed.xml',ET.tostring(feed,encoding='unicode',xml_declaration=True));shutil.copy(OUT/'feed.xml',OUT/'feeds/atom.xml')
rss=ET.Element('rss',version='2.0');channel=ET.SubElement(rss,'channel');ET.SubElement(channel,'title').text='CodesbyFebin engineering articles';ET.SubElement(channel,'link').text=BASE+'/blog/';ET.SubElement(channel,'description').text='Technical drafts and guides on systems engineering, AI infrastructure, and verifiable compute.'
for a in sorted(articles,key=lambda x:x['date'],reverse=True):
 item=ET.SubElement(channel,'item');ET.SubElement(item,'title').text=a['title'];ET.SubElement(item,'link').text=a['url'];ET.SubElement(item,'guid',isPermaLink='true').text=a['url'];ET.SubElement(item,'description').text=a['description']
write('feeds/rss.xml',ET.tostring(rss,encoding='unicode',xml_declaration=True))
write('.well-known/security.txt','Contact: '+BASE+'/contact/\nExpires: 2027-09-30T23:59:59Z\nPreferred-Languages: en\nCanonical: '+BASE+'/.well-known/security.txt\n')
write('robots.txt','User-agent: *\nAllow: /\n\n'+''.join('User-agent: '+bot+'\nAllow: /\n\n' for bot in ['GPTBot','OAI-SearchBot','ChatGPT-User','ClaudeBot','PerplexityBot','CCBot','Googlebot','Bingbot'])+'Sitemap: '+BASE+'/sitemap.xml\n')
write('llms.txt','# CodesbyFebin\n\n> Febin Francis: systems engineering, AI infrastructure, verifiable compute, Kerala, India.\n\nThese are source-linked engineering notes. Proposed checks are not reported test results. Repository descriptions are a 3 October 2026 snapshot.\n\n## Core pages\n'+''.join(f'- [{p["title"]}]({BASE+p["path"]}): {p["description"]}\n' for p in pages if '/blog/' not in p['path'] and '/projects/' not in p['path'])+'\n## Field guides\n'+''.join(f'- [{v[0]}]({BASE}/blog/{k}/)\n' for k,v in SILOS.items())+'\n## All notes\n'+''.join(f'- [{a["title"]}]({a["url"]})\n' for a in articles)+'\n## Machine-readable data\n- [Article inventory]('+BASE+'/data/articles.json)\n- [Entity graph]('+BASE+'/data/schema-graph.json)\n')
write('llms-full.txt','# CodesbyFebin field notes\n\n'+ '\n\n'.join('## '+a['title']+'\n'+a['url']+'\nScope: '+a['origin']+'\n'+(html.unescape(re.sub('<[^>]+>',' ',a['body'])) if 'body' in a else '\n\n'.join(t[0]+'\n'+t[1] for t in a['sections'])) for a in articles))
write('humans.txt','Author: Febin Francis (CodesbyFebin)\nLocation: Kerala, India\nLanguage: English\nBuilt: '+TODAY+'\nSource: supplied Grok workspace and Ultimate Edition content, with bounded editorial revisions.\n')
write('opensearch.xml','<?xml version="1.0"?><OpenSearchDescription xmlns="http://a9.com/-/spec/opensearch/1.1/"><ShortName>CodesbyFebin</ShortName><Description>Search engineering field notes</Description><InputEncoding>UTF-8</InputEncoding><Url type="text/html" template="'+BASE+'/blog/?q={searchTerms}"/></OpenSearchDescription>')
shutil.copy(OUT/'opensearch.xml',OUT/'feeds/opensearch.xml');shutil.copy(OUT/'llms.txt',OUT/'feeds/llms.txt');write('.nojekyll','');(ROOT/'data/articles.json').write_text(json.dumps(articles,indent=2,ensure_ascii=False));(ROOT/'data/taxonomy.json').write_text((OUT/'data/taxonomy.json').read_text());(ROOT/'data/graph.json').write_text((OUT/'data/graph.json').read_text())
print(f'Built {len(articles)} articles, {len(projects)} projects, {len(pages)} indexable pages.')
