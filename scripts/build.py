#!/usr/bin/env python3
"""Build a standalone portfolio with Python's standard library only."""
import json, re, html, shutil, os, posixpath
from discovery import ANSWERS, RELATED, LABELS
from pathlib import Path
from urllib.parse import urljoin, urlparse

ROOT = Path(__file__).resolve().parents[1]
BASE = 'https://codesbyfebin.github.io'
DATE = '2026-10-03'
PAGES = [
 ('home','Home','index.html','Systems that prove what happened.','AI Infrastructure & Verifiable Compute | CodesbyFebin','Explore Febin Francis’s source-backed portfolio of AI infrastructure, verifiable compute, and self-hosted systems, built from Kerala, India.'),
 ('about','About','about.html','The engineer behind the systems.','About Febin Francis · Systems Engineer | CodesbyFebin','Meet Febin Francis, CodesbyFebin: a systems engineer in Kerala, India focused on AI infrastructure, verifiable compute, and sovereign systems.'),
 ('systems','Systems','systems.html','Intent. Execution. Evidence.','AI, STARK & Self-Hosted Systems Guide | CodesbyFebin','Inspect the architecture and boundaries of CodesbyFebin’s STARK VM, hosting systems, AgentSwarm, OM workspace, and browser developer tooling.'),
 ('projects','Projects','projects.html','Source code. Real boundaries.','Open-Source Projects & Repository Guide | CodesbyFebin','Browse 23 source-linked repositories across AI, self-hosting, cryptography, and developer tools, with dated metadata and explicit review status.'),
 ('blog','Writing','blog.html','Notes from the build.','AI Infrastructure & Systems Engineering | CodesbyFebin','Read original engineering notes on agent execution, STARK proofs, self-hosting, and evidence-backed discovery, with links to project sources.'),
 ('services','Services','services.html','Build something inspectable.','AI Infrastructure Consulting & Collaboration | Febin','Explore collaboration on AI infrastructure, systems architecture, self-hosting, and verifiable compute with Febin Francis in Kerala, India.'),
 ('research','Research','research.html','Questions worth testing.','Verifiable Compute & AI Research Interests | Febin','Explore Febin Francis’s research interests in execution integrity, small proof systems, sovereign control planes, and governed AI infrastructure.'),
 ('contributions','Open source','contributions.html','Make the next check reproducible.','Open-Source Contributions & Review Guide | Febin','Find practical contribution paths for CodesbyFebin projects: reproducible issues, focused patches, honest documentation, and source-backed review.'),
 ('contact','Contact','contact.html','Start with a concrete problem.','Contact Febin Francis · Kerala, India | CodesbyFebin','Connect with Febin Francis on GitHub or LinkedIn and prepare a local collaboration brief for AI infrastructure, research, or open-source work.'),
 ('specifications','Specs','specifications.html','A contract you can check.','Protocols, Evidence & Technical Specifications | Febin','Explore execution state, evidence contracts, negative controls, and source-linked STARK and conformance references from CodesbyFebin projects.')]

CURATED = {
 'rust-stark-zkvm': ('rust-stark-zkvm','Verifiable compute','Source documented','Rust','Small STARK VM with arithmetic, forward branches, a fixed register file, Winterfell proving, and HTTP/MCP interfaces. The current verifier re-executes public programs; private witnesses and general-purpose execution are outside the documented scope.','Review instruction semantics, AIR constraints, proof binding, and tamper tests together. A useful first experiment changes the claimed result or program and confirms rejection. Keep the attested on-chain demo distinct from a fully on-chain STARK verifier.'),
 'Decentralized-': ('Decentralized.Host','Infrastructure','Scope review needed','Go','Go control-plane work centered on signed intent, local admission, explicit state, and sovereign hosts. The current README mixes foundation descriptions and provider-discovery roadmap scope; production qualification is not inferred here.','Start with local policy and source-bound evidence. Check how desired placement differs from host admission and fresh workload observations. Read the conformance vectors before assuming compatibility, and examine the relevant runtime evidence before relying on a qualification claim.'),
 'decentralized.hosting': ('Deployment mesh','Infrastructure','Source documented','Python','FastAPI, PostgreSQL, Docker, Traefik, and the dhost CLI form a documented local deployment mesh. Source snapshots can be uploaded for a server-side build. Optional operator credits are devnet-only and disabled by default.','Follow one source snapshot through upload, build, scheduling, container startup, and edge routing. Exercise update, history, and rollback as separate operations. Inspect Docker host access and the documented trust boundary before admitting workloads from other people.'),
 'xfree.in': ('XFree website','Developer tools','Source documented','TypeScript','The current XFree marketing repository documents a Next.js discovery website. It explicitly replaces the older xfree repository for that site. XFree Studio is a separate application and should be evaluated through its own source.','Review real tools and routes rather than inferred cryptographic features. Check the relationship between canonical pages, translations, sitemap eligibility, and the application. A marketing page describing a capability is not evidence that its runtime operation succeeded.'),
 'xfree-app': ('XFree Studio','Developer tools','Source documented','TypeScript','Separate XFree application repository. The README is brief, so feature and stack claims should be checked in the implementation. This card identifies the application source without importing the marketing website’s claims as runtime evidence.','Inspect the dependency manifest, route structure, and client/server boundary. Follow a representative tool from input to output and determine whether data stays in the browser or reaches a backend. Record the behavior of the tool actually tested.'),
 'Agent-Swarm': ('AgentSwarm','AI infrastructure','Source documented','TypeScript','Mission/API/model/event/artifact MVP with persisted state, workers, organization boundaries, and Redis/PostgreSQL dispatch. The documented completion gate checks artifact existence; richer verification and production hardening remain separate work.','Review database claims, worker leases, bounded retries, approval handling, and event replay. Run provider-unavailable and queue-outage paths alongside the happy path. An artifact-existence gate should not be described as proof that the generated work is correct.'),
 '-Om-Personal-Ai': ('OM · Personal AI','AI infrastructure','Source documented','TypeScript','Personal AI workspace with project, note, prompt, finding, mission, and service-configuration surfaces. The README distinguishes persisted workspace features from models, memory, storage, and execution services requiring external setup.','Inspect durable workspace behavior first, then service readiness. A configured Ollama endpoint is different from a measured inference. An owned sandbox worker is required for autonomous execution; its existence cannot be inferred from mission and approval interfaces.'),
 'bestaiagent.in': ('BestAIAgent directory','Discovery','Fork','TypeScript','Fork repository describing an evidence-first catalog for agents, models, frameworks, providers, and MCP infrastructure. GitHub identifies this repository as a fork; upstream implementation authorship and specific local changes should be reviewed separately.','Inspect the catalog/evidence publication model and compare the fork with its parent. Do not infer benchmark validity, review counts, or original authorship from a directory listing. Source snapshots and eligibility rules are more useful than a synthetic popularity score.'),
 'MCP-SERVER': ('MCPserver.in','Discovery','Source documented','JavaScript / Python','Public MCP directory and separate registry-ingestion surface. The README documents a shared publication gate, evidence records, sitemap eligibility, and dry-run ingestion by default. Database writes require an explicit live mode.','Follow one record through the shared indexability function, detail page, sitemap, and machine-readable feeds. Confirm unverified records stay out of public discovery where required. Review ingestion separately from the static site deployment.'),
 'Android-Flashing-Tool': ('Android Flashing Tool','Developer tools','Scope review needed','Python','Android firmware toolkit repository with documentation for device operations and verification workflows. This portfolio confirms the source exists; it does not reproduce hardware qualification or guarantee support for a particular device.','Inspect the actual operation path and device prerequisites before changing firmware. Distinguish browser interface controls from the local backend that accesses a device. A source review is not evidence that a particular flashing procedure was tested on your hardware.'),
 'Indian-MCP-Server': ('MCPServer OS','AI infrastructure','Scope review needed','TypeScript / Python','Repository describing an evidence-first MCP control plane, tenant boundaries, deployment state, and India-oriented technical-control profiles. Documentation claims about regulatory mapping are not certifications or verified production integrations.','Read the project tracker alongside the architecture planes. Distinguish design, implementation, testing, runtime, and production status. Test a specific gateway or evidence operation before treating the complete diagram as delivered capability.'),
 'github-mcpserver--ci-cd-engine': ('MCP CI/CD engine','Discovery','Scope review needed','Repository review','Repository describing synchronization, evidence collection, and discovery routes for MCP metadata. The README includes broad feature and marketing claims, so the implementation must be inspected before treating those as operational results.','Look for the concrete synchronization entry point, configuration, record schema, and invalidation behavior. Verify a small operation against real input. Avoid importing unsupported conversion, ranking, or search-performance numbers from promotional documentation.'),
 'Open-Swarm-ai': ('Open Swarm AI','AI infrastructure','Scope review needed','Repository review','Multi-agent repository with a README describing its intended structure. It is included as an inspectable source surface, without assuming a fully qualified runtime, a production customer base, or measured autonomous execution.','Map the worker entry point, tool permissions, and task persistence. Determine which behavior is implemented and which is an example. A review should include an unavailable-provider path and a concrete artifact, rather than relying on an animated dashboard.'),
 'Worker-Agent': ('Worker Agent.Cloud','AI infrastructure','Fork','TypeScript','Fork describing a content-agent control-plane direction. The README makes broad automation claims and references upstream surfaces. This card preserves fork attribution and avoids treating every claimed publishing integration as independently tested.','Compare the fork with its upstream parent and inspect specific tool adapters. For a publishing workflow, verify configured permissions, human approval, and the final operation on the intended platform. A planned connector does not establish a live integration.'),
 'awesome-zkvm': ('awesome-zkvm reference','Verifiable compute','Fork','Reference list','Fork of an upstream zkVM resource list. It is a research/discovery reference rather than an original proof-system implementation. Upstream authorship and resource maintenance should be attributed to the parent project.','Use the list to find primary project documentation and papers, then check those sources directly. Capability tables can become stale as implementations change. Compare proof systems using a specified workload, hardware, security parameters, and measurement method.'),
 'evidence-cookbook': ('Evidence cookbook','Documentation','Documentation scaffold','Markdown','Documentation scaffold for evidence-driven development. Its current README contains generic examples, placeholder metrics, and placeholder resource links. It is not represented as a completed collection of runnable evidence recipes.','A useful contribution replaces one placeholder with a real source-bound manifest and an independent verification command. Include a tampered-artifact rejection test and explain the expected output. Preserve unknown values rather than filling them with example performance numbers.'),
 'mcp-cookbook': ('MCP cookbook','Documentation','Documentation scaffold','Markdown','Documentation scaffold for MCP learning material. The current README uses generic tutorial and code placeholders. Repository existence is verified, but complete runnable examples and platform integrations are not established by that template.','Begin with one minimal real tool, its schema, and its permission boundary. Document how a client connects and what happens for invalid input. Validate the example against the applicable protocol implementation before publishing it as a working recipe.'),
 'agent-skills-cookbook': ('Agent skills cookbook','Documentation','Documentation scaffold','Markdown','Scaffold for reusable agent-workflow documentation. Current template content is not evidence of tested skills, production automation, or verified tool access. The repository is included as a visible area for future focused contributions.','Replace a broad template with a single scoped workflow. Name prerequisites, allowed operations, and expected artifacts. Test a missing-context case and a failure path, and ensure the instructions preserve the operator’s authority over external actions.'),
 'kubernetes-ai-cookbook': ('Kubernetes AI cookbook','Documentation','Documentation scaffold','Markdown','Documentation scaffold about Kubernetes and AI workloads. Generic setup and benchmark placeholders in the current README should not be interpreted as a tested cluster deployment or measured inference performance.','A concrete recipe should name the manifests, image digests, resource limits, model service, and readiness criteria. Explain where credentials are stored and how the workload is removed. Record real cluster behavior instead of an illustrative throughput target.'),
 'self-hosted-cloud-cookbook': ('Self-hosted cloud cookbook','Documentation','Documentation scaffold','Markdown','Documentation scaffold for self-hosting guidance. Its current generic README does not establish a completed operator runbook or a qualified deployment stack. It is labeled separately from the runnable deployment mesh.','Start with a bounded installation that another operator can reproduce. Include backup and restore, identity handling, and a clear failure path. Explain the hardware and network assumptions before suggesting that the same runbook supports other environments.'),
 'ai-security-cookbook': ('AI security cookbook','Documentation','Documentation scaffold','Markdown','Scaffold for AI security learning material. Generic code and resource placeholders remain in the README. The portfolio does not describe it as an audited defense framework or a tested collection of security controls.','Develop one adversarial fixture with a stated threat and observable expected rejection. Trace the policy enforcement boundary and preserve the failed input safely. A passing positive example alone does not show that a control rejects the attack it targets.'),
 'ai-observability-cookbook': ('AI observability cookbook','Documentation','Documentation scaffold','Markdown','Documentation scaffold for AI observability topics. Current placeholder metrics and examples do not establish real telemetry integrations, measured costs, or production latency. This status remains visible in the directory and machine-readable data.','Add one source-backed observation flow from provider response to persisted event and user interface. Make missing usage explicitly unknown. Define timestamps and correlation identifiers, and show how an operator distinguishes a replayed event from new execution.'),
 'verifiable-ai-cookbook': ('Verifiable AI cookbook','Documentation','Documentation scaffold','Markdown','Scaffold for verifiable-AI explanations and examples. The current generic README does not establish private model inference, proof-backed AI outputs, or benchmarked verification. It remains a documentation contribution opportunity.','A first recipe should state exactly what the check proves, which inputs are public, and what remains trusted. Include the verifier procedure and a negative control. Keep an authenticated assertion distinct from a cryptographic proof of computation.')}

def esc(s): return html.escape(str(s), quote=True)
def slug(s): return re.sub(r'[^a-z0-9]+','-', re.sub(r'[`*_]','',s).lower()).strip('-') or 'section'
def inline(s, source=None):
    s = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', s)
    tokens=[]
    def token(v): tokens.append(v); return f'ZZTOKEN{len(tokens)-1}ZZ'
    s=re.sub(r'`([^`]+)`',lambda m:token('<code>'+esc(m[1])+'</code>'),s)
    def link(m):
        text,url=m[1],m[2].strip().split(' ')[0]
        if source and not url.startswith(('https://','http://','mailto:')):
            url=urljoin(source,url)
        if url.startswith(('javascript:','data:')) or 'example.com' in url:
            return text
        return token(f'<a href="{esc(url)}">{esc(text)}</a>')
    s=re.sub(r'\[([^\]]+)\]\(([^)]+)\)',link,s)
    s=esc(s)
    s=re.sub(r'\*\*([^*]+)\*\*',r'<strong>\1</strong>',s)
    for i,v in enumerate(tokens):s=s.replace(f'ZZTOKEN{i}ZZ',v)
    return s

def markdown(text,prefix='',source=None):
    # Ignore source HTML/images/badges; never execute markup from repository snapshots.
    text=re.sub(r'</?(?:div|img|h[1-6]|p|a|br|span|picture|source)\b[^>]*>','',text,flags=re.I)
    text=re.sub(r'^.*\[!\[.*$', '',text,flags=re.M)
    lines=text.splitlines(); out=[]; toc=[]; para=[]; list_kind=None; i=0; seen={}
    def flush():
        nonlocal list_kind
        if para:out.append('<p>'+inline(' '.join(para),source)+'</p>');para.clear()
        if list_kind:out.append('</'+list_kind+'>');list_kind=None
    while i<len(lines):
        line=lines[i].strip()
        if line.startswith('```'):
            flush();lang=line[3:].strip();code=[];i+=1
            while i<len(lines) and not lines[i].strip().startswith('```'):code.append(lines[i]);i+=1
            out.append('<pre><code class="language-'+esc(lang)+'">'+esc('\n'.join(code))+'</code></pre>')
        elif re.match(r'^#{1,6}\s',line):
            flush();m=re.match(r'^(#{1,6})\s+(.*)',line); level=len(m[1]);title=m[2];key=prefix+slug(title);seen[key]=seen.get(key,0)+1
            if seen[key]>1:key+='-'+str(seen[key])
            if source:level=min(6,level+2)
            else:level=max(2,level)
            out.append(f'<h{level} id="{esc(key)}">{inline(title,source)}</h{level}>')
            if level==2:toc.append((key,re.sub(r'[`*_]','',title)))
        elif line.startswith('|') and i+1<len(lines) and re.match(r'^\|?\s*:?-',lines[i+1].strip()):
            flush();headers=[x.strip() for x in line.strip('|').split('|')];i+=2;rows=[]
            while i<len(lines) and lines[i].strip().startswith('|'):
                rows.append([x.strip() for x in lines[i].strip().strip('|').split('|')]);i+=1
            out.append('<div class="table-wrap"><table><thead><tr>'+''.join('<th scope="col">'+inline(x,source)+'</th>' for x in headers)+'</tr></thead><tbody>'+''.join('<tr>'+''.join('<td>'+inline(x,source)+'</td>' for x in row)+'</tr>' for row in rows)+'</tbody></table></div>');i-=1
        elif re.match(r'^[-*+]\s|^\d+\.\s',line):
            if para:out.append('<p>'+inline(' '.join(para),source)+'</p>');para.clear()
            kind='ol' if re.match(r'^\d+\.',line) else 'ul'
            if kind!=list_kind:
                if list_kind:out.append('</'+list_kind+'>')
                out.append('<'+kind+'>');list_kind=kind
            out.append('<li>'+inline(re.sub(r'^([-*+]|\d+\.)\s+','',line),source)+'</li>')
        elif line.startswith('>'):
            flush();out.append('<blockquote><p>'+inline(line.lstrip('> ').strip(),source)+'</p></blockquote>')
        elif line in ('---','***'):flush();out.append('<hr>')
        elif not line:flush()
        else:
            if list_kind:out.append('</'+list_kind+'>');list_kind=None
            para.append(line)
        i+=1
    flush();return '\n'.join(out),toc

snap=json.loads((ROOT/'data/repository-snapshots.json').read_text())
projects=[]
for raw in snap['records']:
    name,category,status,language,description,review=CURATED[raw['repo']]
    projects.append({k:raw[k] for k in ('id','repo','url','fork','upstream','stars','forks','updated','readmeSha') if k in raw}|dict(name=name,category=category,status=status,language=language,description=description,review=review,detail=f'projects/{raw["id"]}/index.html',checkedAt=DATE))
(ROOT/'data/projects.json').write_text(json.dumps({'checkedAt':DATE,'projects':projects},indent=2,ensure_ascii=False)+'\n')

def card(p,index=0,heading='h3'):
    status=p['status'];klass='good' if status=='Source documented' else 'reference'
    art={'Verifiable compute':'circuit','Infrastructure':'server','AI infrastructure':'swarm','Developer tools':'lock','Discovery':'map','Documentation':'datacenter'}[p['category']]
    return f'''<article class="card" data-project data-name="{esc(p['name'])}" data-category="{esc(p['category'])}" data-status="{esc(status)}" data-stars="{p['stars']}" data-updated="{esc(p['updated'])}" data-search="{esc((p['name']+' '+p['repo']+' '+p['description']+' '+p['category']+' '+p['language']).lower())}">
<img class="card-art" src="/assets/images/{art}.jpg" alt="" width="600" height="337" loading="lazy" decoding="async">
<span class="number">{index+1:02d} / {esc(p['category'])}</span><{heading}><a href="/{p['detail']}">{esc(p['name'])}</a></{heading}><span class="badge {klass}">{esc(status)}</span><p>{esc(p['description'])}</p><span class="badge">{esc(p['language'])}</span><div class="card-stats">{p['stars']} stars · {p['forks']} forks · updated {esc(p['updated'][:10])}</div><div class="links"><a href="/{p['detail']}">Project guide</a><a href="{esc(p['url'])}">Source on GitHub</a></div></article>'''

def header(active):
    return '<a class="skip" href="#main">Skip to content</a><header class="header"><div class="wrap header-inner"><a class="brand" href="/index.html"><span aria-hidden="true">&gt;_</span>CodesbyFebin</a><button class="icon-button menu-button" data-menu aria-controls="navigation" aria-expanded="false">Menu</button><nav class="navigation" id="navigation" aria-label="Main navigation">'+''.join(f'<a href="/{file}"'+(' aria-current="page"' if key==active else '')+'>'+label+'</a>' for key,label,file,*_ in PAGES)+'</nav><button class="icon-button" data-theme-toggle aria-label="Switch to light theme">Light</button></div></header>'

def footer():
    return '''<footer class="footer"><div class="wrap"><div class="footer-grid"><div><a class="brand" href="/index.html">&gt;_ CodesbyFebin</a><p>Systems Engineer · AI Infrastructure · Verifiable Compute<br>Kerala, India · IST UTC+5:30</p><p>Building systems that prove what happened instead of asking you to trust what happened.</p></div><nav aria-label="Explore"><a href="/systems.html">Selected systems</a><a href="/projects.html">Repository directory</a><a href="/blog.html">Engineering notes</a><a href="/research.html">Research interests</a><a href="/specifications.html">Technical references</a></nav><nav aria-label="Connect"><a href="/contact.html">Contact</a><a href="/services.html">Collaboration</a><a href="/contributions.html">Open-source workflow</a><a href="https://github.com/CodesbyFebin">GitHub</a><a href="https://www.linkedin.com/in/codes-by-febin/">LinkedIn</a><a href="https://orcid.org/0009-0002-8123-1531">ORCID</a></nav></div><div class="footer-bottom"><span>© 2026 Febin Francis · Proof over promises</span><span><a href="/sitemap.xml">Sitemap</a> · <a href="/llms.txt">AI discovery</a> · No third-party analytics</span></div></div></footer>'''

def terminal():
    return '''<div class="terminal hero-visual" aria-label="Engineering model"><div class="terminal-top"><i aria-hidden="true"></i><i aria-hidden="true"></i><i aria-hidden="true"></i><span>~/codesbyfebin / system-profile</span></div><div class="terminal-body"><p><span class="prompt">$</span> whoami<br><span class="dim">Febin Francis · Systems Engineer</span></p><p><span class="prompt">$</span> cat principles.conf<br><span class="dim">local_authority = retained<br>unmeasured_state = UNKNOWN<br>evidence_required = true</span></p><svg viewBox="0 0 430 240" role="img" aria-labelledby="model-title model-desc"><title id="model-title">Intent passes through policy to execution and verification</title><desc id="model-desc">Policy can refuse the request and record the refusal. Admitted execution creates observations and evidence for verification.</desc><g fill="none" stroke="#326557"><path d="M130 52h10m120 0h50M200 76v24H70v30M365 76v31H200v23M260 153h50M365 178v25H310"/></g><g fill="#081910" stroke="#26644d"><rect x="10" y="28" width="120" height="48" rx="3"/><rect x="140" y="28" width="120" height="48" rx="3"/><rect x="310" y="28" width="110" height="48" rx="3"/><rect x="10" y="130" width="120" height="48" rx="3"/><rect x="140" y="130" width="120" height="48" rx="3"/><rect x="310" y="130" width="110" height="48" rx="3"/></g><g fill="#aaf3cf" font-family="monospace" font-size="13" text-anchor="middle"><text x="70" y="57">INTENT</text><text x="200" y="57">POLICY</text><text x="365" y="57">EXECUTION</text><text x="70" y="159" fill="#ffcb72">REFUSE</text><text x="200" y="159">OBSERVATION</text><text x="365" y="159">VERIFICATION</text><text x="240" y="209">EVIDENCE</text></g></svg></div></div>'''

def source_section(id,title,repo,path,content,sha):
    source=f'https://github.com/CodesbyFebin/{repo}/blob/main/{path}'
    directory=f'https://github.com/CodesbyFebin/{repo}/blob/main/'+posixpath.dirname(path)+'/'
    rendered,_=markdown(content,prefix=id+'-',source=source)
    return f'<section class="source-doc" id="{esc(id)}"><h2>{esc(title)}</h2><div class="source-note"><strong>Repository documentation snapshot</strong><br>Reviewed {DATE}. <a href="{esc(source)}">Read the current source file</a><br>GitHub blob: <code>{esc(sha)}</code><br>This is source documentation, not a new runtime test report.</div>{rendered}</section>'

def brief():
    return '''<section class="brief-builder" aria-labelledby="brief-title"><h2 id="brief-title">Prepare your brief</h2><p class="notice">Runs on your device. Nothing is submitted or stored by this website.</p><form data-brief-form><div class="form-row"><label for="brief-name">Your name</label><input id="brief-name" name="name" required autocomplete="name" maxlength="120"></div><div class="form-row"><label for="brief-topic">Topic</label><select id="brief-topic" name="topic"><option>AI infrastructure</option><option>Self-hosted systems</option><option>Verifiable compute</option><option>Open-source contribution</option><option>Research or writing</option></select></div><div class="form-row"><label for="brief-source">Project or source URL (optional)</label><input id="brief-source" name="source" type="url" placeholder="https://github.com/owner/project" maxlength="1000"></div><div class="form-row"><label for="brief-message">Current situation and desired result</label><textarea id="brief-message" name="message" required maxlength="5000"></textarea></div><div class="form-row"><label for="brief-constraints">Constraints and acceptance evidence (optional)</label><textarea id="brief-constraints" name="constraints" maxlength="3000"></textarea></div><button class="button" type="submit">Create local brief</button></form><p class="notice" data-brief-status aria-live="polite">Use the public profile links above to start a conversation.</p><div class="brief-output" data-brief-output role="region" aria-label="Prepared brief" tabindex="0">Your brief will appear here.</div><button class="button secondary" type="button" data-copy-brief disabled>Copy brief</button><noscript><p>JavaScript is disabled. Write your brief directly in GitHub or LinkedIn; no website submission is required.</p></noscript></section>'''

urls=[]
def render(key,label,file,headline,title,description,body,toc=None,project=None):
    url=BASE+('/' if file=='index.html' else '/'+file.replace('/index.html','/'))
    schema=[{'@type':'Person','@id':BASE+'/#person','name':'Febin Francis','alternateName':'CodesbyFebin','url':BASE+'/','jobTitle':'Systems Engineer','homeLocation':{'@type':'Place','name':'Kerala, India'},'sameAs':['https://github.com/CodesbyFebin','https://www.linkedin.com/in/codes-by-febin/','https://orcid.org/0009-0002-8123-1531'],'knowsAbout':['AI infrastructure','Verifiable compute','Sovereign systems','Distributed systems']},{'@type':'WebSite','@id':BASE+'/#website','name':'CodesbyFebin','url':BASE+'/','inLanguage':'en','author':{'@id':BASE+'/#person'}},{'@type':'WebPage','@id':url+'#webpage','url':url,'name':title,'description':description,'inLanguage':'en','isPartOf':{'@id':BASE+'/#website'},'about':{'@id':BASE+'/#person'}},{'@type':'BreadcrumbList','itemListElement':[{'@type':'ListItem','position':1,'name':'Home','item':BASE+'/'}]+([] if key=='home' else [{'@type':'ListItem','position':2,'name':label,'item':url}])}]
    if project:
        schema[3]['itemListElement']=[{'@type':'ListItem','position':1,'name':'Home','item':BASE+'/'},{'@type':'ListItem','position':2,'name':'Projects','item':BASE+'/projects.html'},{'@type':'ListItem','position':3,'name':project['name'],'item':url}]
    if not project:
        question,answer=ANSWERS[key]
        schema.append({'@type':'FAQPage','@id':url+'#answers','mainEntity':[{'@type':'Question','name':question,'acceptedAnswer':{'@type':'Answer','text':answer}}]})
        body+='<section id="answers"><h2>Direct answer</h2><h3>'+esc(question)+'</h3><p>'+esc(answer)+'</p></section>'
        if toc:toc.append(('answers','Direct answer'))
    related=RELATED[key]
    if project:
        peers=[p for p in projects if p['category']==project['category'] and p['id']!=project['id']][:3]
        body+='<section><h2>Related repositories</h2><ul>'+''.join('<li><a href="/'+p['detail']+'">'+esc(p['name'])+'</a> — '+esc(p['status'])+'</li>' for p in peers)+'</ul></section>' if peers else ''
    body+='<section class="related-reading"><h2>Continue exploring</h2><ul>'+''.join('<li><a href="/'+next(p[2] for p in PAGES if p[0]==k)+'">'+esc(LABELS[k])+'</a></li>' for k in related)+'</ul></section>'
    if project:schema.append({'@type':'SoftwareSourceCode','name':project['name'],'codeRepository':project['url'],'programmingLanguage':project['language'],'description':project['description'],'url':url})
    if key=='projects':schema.append({'@type':'ItemList','name':'Repository directory','numberOfItems':len(projects),'itemListElement':[{'@type':'ListItem','position':i+1,'name':p['name'],'url':BASE+'/'+p['detail'].replace('/index.html','/')} for i,p in enumerate(projects)]})
    hero=(f'<section class="hero"><div class="wrap hero-inner"><div><div class="eyebrow">// Febin Francis · Systems Engineer</div><h1>Systems that <em>prove what happened.</em></h1><p class="lede">AI infrastructure. Verifiable compute. Sovereign systems.<br>Open-source work you can inspect, from Kerala, India.</p><div class="actions"><a class="button" href="/systems.html">Explore systems</a><a class="button secondary" href="/projects.html">Inspect source code</a></div><div class="meta"><span>Rust · Go · TypeScript · Python</span><span>IST / UTC+5:30</span></div></div>{terminal()}</div></section>' if key=='home' else f'<section class="hero hero-small"><div class="wrap"><div class="breadcrumbs"><a href="/index.html">Home</a> / {('<a href="/projects.html">Projects</a> / ' if project else '')}{esc(label)}</div><div class="eyebrow">// {esc(label)}</div><h1>{esc(headline)}</h1><p class="lede">{esc(description)}</p></div></section>')
    if key=='home':
        featured=[next(p for p in projects if p['repo']==r) for r in ['rust-stark-zkvm','Decentralized-','Agent-Swarm']]
        hero+='<div class="wrap"><div class="signal-strip"><div class="signal"><b>23</b><span>Source-linked repositories</span></div><div class="signal"><b>10</b><span>Connected portfolio pages</span></div><div class="signal"><b>Kerala, IN</b><span>Open-source builder</span></div><div class="signal"><b>UNKNOWN</b><span>When data is unmeasured</span></div></div><div class="section-head"><div><div class="kicker">// Selected systems</div><h2>Different layers. One principle.</h2></div><a href="/systems.html">Inspect the architecture</a></div><div class="grid">'+''.join(card(p,i) for i,p in enumerate(featured))+'</div></div>'
    toc_html='<aside class="toc" aria-label="On this page"><p>ON THIS PAGE</p>'+''.join(f'<a href="#{esc(id)}">{esc(text)}</a>' for id,text in (toc or []))+'</aside>' if toc else ''
    if key in ('blog','about'):
        illustration='lab' if key=='blog' else 'kerala'
        caption='Illustrated engineering workspace' if key=='blog' else 'Illustrated Kerala waterfront'
        body=f'<figure class="editorial-art"><img src="/assets/images/{illustration}.jpg" alt="{caption}" width="1000" height="562" loading="lazy" decoding="async"><figcaption>{caption} · supplied concept artwork</figcaption></figure>'+body
    content=f'<div class="wrap content-layout">{toc_html}<article class="prose">{body}</article></div>' if toc else '<div class="wrap project-area">'+body+'</div>'
    output=f'''<!doctype html><html lang="en" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(title)}</title><meta name="description" content="{esc(description)}"><meta name="author" content="Febin Francis"><meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large"><meta name="theme-color" content="#050c10"><meta name="geo.region" content="IN-KL"><meta name="geo.placename" content="Kerala, India"><link rel="canonical" href="{url}"><meta property="og:title" content="{esc(title)}"><meta property="og:description" content="{esc(description)}"><meta property="og:type" content="website"><meta property="og:url" content="{url}"><meta property="og:image" content="{BASE}/assets/images/og-image-1200x630.png"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630"><meta property="og:image:alt" content="CodesbyFebin — AI Infrastructure, Verifiable Compute, Sovereign Systems"><meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}"><meta name="twitter:description" content="{esc(description)}"><meta name="twitter:image" content="{BASE}/assets/images/twitter-1200x675.png"><link rel="icon" href="/assets/images/logo.svg" type="image/svg+xml"><link rel="manifest" href="/manifest.json"><link rel="stylesheet" href="/assets/css/styles.css"><script defer src="/assets/js/main.js"></script><script type="application/ld+json">{json.dumps({'@context':'https://schema.org','@graph':schema},ensure_ascii=False).replace('<','\\u003c')}</script></head><body>{header(key)}<main id="main">{hero}{content}<div class="wrap"><section class="callout"><div><h2>Build. Measure. Verify. Improve.</h2><p>Have a concrete system, question, or contribution in mind? Start with source, scope, and the result you want to inspect.</p></div><a class="button" href="/contact.html">Start a conversation</a></section></div></main>{footer()}</body></html>'''
    # Relative URLs also make the downloadable site usable from disk.
    depth=len(Path(file).parts)-1; prefix='../'*depth
    output=re.sub(r'(href|src)="/([^"#]*)"',lambda m:m[1]+'="'+prefix+m[2]+'"',output)
    target=ROOT/file;target.parent.mkdir(parents=True,exist_ok=True);target.write_text(output)
    urls.append({'url':url,'path':file,'title':title,'description':description,'lastModified':DATE})

for key,label,file,headline,title,description in PAGES:
    body,toc=markdown((ROOT/'content'/f'{key}.md').read_text())
    if key=='systems':
        for id,title2,repo in [('source-rust-vm','Rust VM · repository guide','rust-stark-zkvm'),('source-deployment-mesh','Python mesh · repository guide','decentralized.hosting'),('source-agentswarm','AgentSwarm · repository guide','Agent-Swarm'),('source-om','OM · repository guide','-Om-Personal-Ai')]:
            r=next(x for x in snap['records'] if x['repo']==repo);body+=source_section(id,title2,repo,'README.md',r['readme'],r['readmeSha']);toc.append((id,title2))
    if key=='specifications':
        for doc in json.loads((ROOT/'data/technical-sources.json').read_text()):
            title2={'zkvm-host-service':'zkVM host service','zkvm-roadmap':'zkVM scope and roadmap','zkvm-threat-model':'zkVM threat model','dh-conformance':'dh/v1 conformance'}[doc['id']]
            body+=source_section(doc['id'],title2,doc['repo'],doc['path'],doc['content'],doc['sha']);toc.append((doc['id'],title2))
    if key=='contact':body+=brief();toc.append(('brief-title','Prepare your brief'))
    if key=='projects':
        controls='<div class="controls"><div class="control"><label for="project-search">Search repositories</label><input type="search" id="project-search" placeholder="Name, topic, or language"></div>'
        for id,label2,values in [('category','Category',sorted({p['category'] for p in projects})),('status','Review status',sorted({p['status'] for p in projects}))]:
            controls+=f'<div class="control"><label for="project-{id}">{label2}</label><select id="project-{id}"><option value="all">All {id} options</option>'+''.join(f'<option>{esc(v)}</option>' for v in values)+'</select></div>'
        controls+='<div class="control"><label for="project-sort">Sort by</label><select id="project-sort"><option value="name">Name</option><option value="stars">Stars (dated snapshot)</option><option value="updated">Last source update</option></select></div><button class="button secondary" type="button" data-reset>Reset</button></div>'
        cards='<section aria-label="Repository directory">'+controls+'<p class="results" data-result-count aria-live="polite">23 repositories · snapshot 3 October 2026</p><div class="grid" data-project-grid>'+''.join(card(p,i,'h2') for i,p in enumerate(projects))+'</div><p class="no-results" data-no-results hidden>No repositories match. Clear search or reset the filters.</p></section>'
        body=cards+'<div class="content-layout"><aside class="toc"><p>DIRECTORY GUIDE</p>'+''.join(f'<a href="#{id}">{esc(text)}</a>' for id,text in toc)+'</aside><article class="prose">'+body+'</article></div>';toc=[]
    render(key,label,file,headline,title,description,body,toc)

for p in projects:
    text=f'''## {p['name']}\n\n{p['description']}\n\n## What to inspect\n\n{p['review']}\n\n## Source and review status\n\n[Inspect the repository]({p['url']}). This project is listed as **{p['status']}**. Metadata was reviewed on 3 October 2026. The GitHub record shows {p['stars']} stars and {p['forks']} forks in this dated snapshot. Those counts are not a quality score or a guarantee of future activity.\n\nThe portfolio does not execute this repository's runtime during its website build. Use the current source, test suite, configuration, and deployment evidence to assess the capability that matters for your environment.\n\n## Related reading\n\n[Selected systems](/systems.html) explains architecture boundaries. [Technical specifications](/specifications.html) covers state, evidence, and negative controls. [Contribution workflow](/contributions.html) explains how to propose a focused correction. Return to [the project directory](/projects.html) to compare source surfaces.\n'''
    if p['upstream']:text+='\n## Upstream attribution\n\nGitHub identifies this as a fork. [Inspect the upstream parent]('+p['upstream']+'). Ownership of this fork does not establish authorship of the upstream project.\n'
    body,toc=markdown(text);render('projects',p['name'],p['detail'],p['name'],p['name']+' · Project Guide | CodesbyFebin',p['description'][:157],body,toc,p)

def redirect(file,target):
    path=ROOT/file;path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="robots" content="noindex, follow"><meta http-equiv="refresh" content="0;url={target}"><link rel="canonical" href="{BASE}/projects.html"><title>Portfolio moved · CodesbyFebin</title></head><body><p>The portfolio is now the <a href="{target}">source-backed project directory</a>.</p></body></html>')
redirect('portfolio.html','projects.html');redirect('docs/index.html','../index.html');redirect('docs/portfolio.html','../projects.html')
(ROOT/'404.html').write_text('<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex, follow"><title>Page not found | CodesbyFebin</title><link rel="stylesheet" href="/assets/css/styles.css"></head><body><main class="wrap hero"><div class="eyebrow">// HTTP 404</div><h1>This route has no result.</h1><p>The page may have moved. Start from the portfolio or inspect the repository directory.</p><div class="actions"><a class="button" href="/">Portfolio home</a><a class="button secondary" href="/projects.html">Projects</a></div></main></body></html>')
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'+''.join('<url><loc>'+esc(x['url'])+'</loc><lastmod>'+DATE+'</lastmod></url>' for x in urls)+'</urlset>\n')
(ROOT/'sitemap.json').write_text(json.dumps({'pages':urls},indent=2)+'\n')
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\n\nSitemap: '+BASE+'/sitemap.xml\n')
(ROOT/'manifest.json').write_text(json.dumps({'name':'CodesbyFebin · Systems Engineer','short_name':'CodesbyFebin','start_url':'/','display':'browser','background_color':'#050c10','theme_color':'#050c10','icons':[{'src':'assets/images/logo.svg','sizes':'any','type':'image/svg+xml'}]},indent=2)+'\n')
(ROOT/'llms.txt').write_text('# CodesbyFebin\n\n> Febin Francis · Systems Engineer · Kerala, India. AI infrastructure, verifiable compute, sovereign systems.\n\n'+ '\n'.join('- ['+x['title']+']('+x['url']+'): '+x['description'].rstrip() for x in urls)+'\n\n## Claim boundaries\nMetadata reviewed 2026-10-03. Source documentation is not independent runtime qualification. Forks are attributed. Documentation scaffolds are not completed examples. Missing telemetry stays UNKNOWN. No unsupported employment, education, publication, customer, or impact counts.\n')
(ROOT/'agents.json').write_text(json.dumps({'name':'Febin Francis','handle':'CodesbyFebin','role':'Systems Engineer','location':'Kerala, India','checkedAt':DATE,'discovery':{'website':BASE+'/','llms':BASE+'/llms.txt','projects':BASE+'/data/projects.json','sitemap':BASE+'/sitemap.xml'},'projects':[{'name':p['name'],'repository':p['url'],'reviewStatus':p['status'],'fork':p['fork']} for p in projects],'claimPolicy':{'simulated':'must remain explicitly simulated','unknown':'must remain unknown','roadmap':'must not be represented as implemented','verification':'source documentation is not independent runtime qualification'}},indent=2)+'\n')
(ROOT/'agents.txt').write_text('# CodesbyFebin discovery\nWebsite: '+BASE+'/\nLLM discovery: '+BASE+'/llms.txt\nRepository dataset: '+BASE+'/data/projects.json\nStructured discovery: '+BASE+'/agents.json\n\nDiscovery metadata only. No executable agent capabilities or MCP endpoints are implied.\n')
(ROOT/'assets/js/main.ts').write_text((ROOT/'assets/js/main.js').read_text())
(ROOT/'.nojekyll').write_text('')
dist=ROOT/'dist'
if dist.exists():shutil.rmtree(dist)
dist.mkdir()
for item in ['assets','projects','data','docs']:
    shutil.copytree(ROOT/item,dist/item,ignore=shutil.ignore_patterns('*.ts','_config.yml','repository-snapshots.json','technical-sources.json'))
for file in [x['path'] for x in urls if '/' not in x['path']]+['404.html','portfolio.html','sitemap.xml','sitemap.json','robots.txt','manifest.json','llms.txt','agents.json','agents.txt','.nojekyll']:
    shutil.copy2(ROOT/file,dist/file)
print(f'Built {len(PAGES)} portfolio pages + {len(projects)} project guides. Static output: {dist}')
