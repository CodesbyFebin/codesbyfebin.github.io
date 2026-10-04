#!/usr/bin/env python3
"""Check generated HTML, local links, metadata, graph, XML, and transfer budget."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlsplit,unquote
from xml.etree import ElementTree as ET
import json,gzip,re,hashlib,sys
ROOT=Path(__file__).resolve().parents[1];DIST=ROOT/'dist';BASE=json.loads((ROOT/'data/site.json').read_text())['url'].rstrip('/');errors=[];links=0;ids={};parsed={}
class Page(HTMLParser):
 def __init__(self):super().__init__();self.links=[];self.ids=[];self.meta={};self.canon=[];self.h1=0;self.json=[];self.capture=False;self.buffer='';self.title=False;self.titletext='';self.lang=None
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='html':self.lang=a.get('lang')
  if 'id' in a:self.ids.append(a['id'])
  if t in ['a','link'] and 'href' in a:self.links.append(a['href'])
  if t in ['img','script'] and 'src' in a:self.links.append(a['src'])
  if t=='img' and 'alt' not in a:errors.append('Missing image alt')
  if t=='h1':self.h1+=1
  if t=='title':self.title=True
  if t=='meta':self.meta[a.get('name',a.get('property',''))]=a.get('content','')
  if t=='link' and a.get('rel')=='canonical':self.canon.append(a.get('href'))
  if t=='script' and a.get('type')=='application/ld+json':self.capture=True;self.buffer=''
 def handle_data(self,d):
  if self.capture:self.buffer+=d
  if self.title:self.titletext+=d
 def handle_endtag(self,t):
  if t=='title':self.title=False
  if t=='script' and self.capture:
   try:self.json.append(json.loads(self.buffer))
   except Exception as e:errors.append('Invalid JSON-LD '+str(e))
   self.capture=False
for p in DIST.rglob('*.html'):
 q=Page();q.feed(p.read_text());parsed[p]=q;ids[p]=set(q.ids)
 if len(q.ids)!=len(set(q.ids)):errors.append(f'Duplicate IDs: {p.relative_to(DIST)}')
 if q.h1!=1:errors.append(f'H1 count {q.h1}: {p.relative_to(DIST)}')
 if q.lang!='en':errors.append(f'Language missing: {p}')
 if len(q.canon)!=1 or not q.canon[0].startswith(BASE+'/'):errors.append(f'Canonical mismatch: {p}')
 if not q.meta.get('description'):errors.append(f'Description missing: {p}')
 if not q.meta.get('og:image','').startswith(BASE+'/'):errors.append(f'Non-absolute OG: {p}')
 if not q.json:errors.append(f'Schema missing: {p}')
for p,q in parsed.items():
 for ref in q.links+[q.meta.get('og:image','')]:
  u=urlsplit(ref)
  if u.scheme and not ref.startswith(BASE+'/'):continue
  if u.scheme:target=u.path
  else:target=u.path
  if not target:dest=p
  elif target.startswith('/'):dest=DIST/unquote(target.lstrip('/'))
  else:dest=p.parent/unquote(target)
  if dest.is_dir():dest=dest/'index.html'
  if not dest.exists():errors.append(f'Broken link {p.relative_to(DIST)} → {ref}')
  elif u.fragment and dest in ids and unquote(u.fragment) not in ids[dest]:errors.append(f'Broken fragment {p.relative_to(DIST)} → {ref}')
  links+=1
for p in DIST.rglob('*.xml'):
 try:ET.parse(p)
 except Exception as e:errors.append(f'Invalid XML {p}: {e}')
articles=json.loads((DIST/'data/articles.json').read_text());graph=json.loads((DIST/'data/graph.json').read_text());slugs={a['slug'] for a in articles}
if len(slugs)!=len(articles):errors.append('Duplicate article slugs')
if len(articles)<100:errors.append('Fewer than 100 articles')
for e in graph['edges']:
 if e['from'] not in slugs or e['to'] not in slugs:errors.append('Unresolved graph edge')
for a in articles:
 p=DIST/a['path'].strip('/')/'index.html';q=parsed.get(p)
 if not q:errors.append('Missing article '+a['slug']);continue
 if q.canon!=[a['url']]:errors.append('Article canonical mismatch '+a['slug'])
 if len(a['related'])<5:errors.append('Related mesh too small '+a['slug'])
 if a['wordCount']<65:errors.append('Empty or underdeveloped note '+a['slug'])
 if any(x in a['title'] for x in ['Advanced Development Technique','UGC Post']):errors.append('Placeholder title')
 nodes=[n for g in q.json for n in g.get('@graph',[])]
 if not any(n.get('@type')=='TechArticle' for n in nodes):errors.append('Missing TechArticle '+a['slug'])
# Inventory counts, reciprocal graph, dates, and visible FAQ/schema parity.
edgepairs={(e['from'],e['to']) for e in graph['edges']}
for source,target in edgepairs:
 if (target,source) not in edgepairs:errors.append('Nonreciprocal graph edge '+source+' → '+target)
for a in articles:
 if a['date']>json.loads((ROOT/'data/site.json').read_text())['updated']:errors.append('Future publication date '+a['slug'])
 q=parsed[DIST/a['path'].strip('/')/'index.html']
 nodes=[n for g in q.json for n in g.get('@graph',[])]
 faq=[n for n in nodes if n.get('@type')=='FAQPage']
 if bool(faq)!=bool(a['faq']):errors.append('FAQ presence mismatch '+a['slug'])
 if faq and len(faq[0]['mainEntity'])!=len(a['faq']):errors.append('FAQ count mismatch '+a['slug'])
 for f in a['faq']:
  if not f['question'] or not f['answer']:errors.append('Empty FAQ '+a['slug'])
ns={'s':'http://www.sitemaps.org/schemas/sitemap/0.9'}
locs=[n.text for n in ET.parse(DIST/'sitemap.xml').findall('s:url/s:loc',ns)]
expected=[BASE+p['path'] for p in json.loads((DIST/'data/pages.json').read_text())]
if len(locs)!=len(set(locs)) or set(locs)!=set(expected):errors.append('Sitemap inventory mismatch')
if len(ET.parse(DIST/'feeds/rss.xml').findall('channel/item'))!=len(articles):errors.append('RSS article count mismatch')
for p in DIST.rglob('*'):
 if p.is_file() and p.suffix in ['.html','.json','.txt','.js','.css']:
  if re.search(r'proof verified:\s*true|10K\+ GitHub Stars|alexrivera\.dev|codesbyfebin\.com',p.read_text(),re.I):errors.append('Unsupported copied claim/domain '+str(p))
size=sum(len(gzip.compress(p.read_bytes(),mtime=0)) for p in DIST.rglob('*') if p.is_file())
if size>3_000_000:errors.append('Compressed deploy footprint exceeds 3 MB')
report={'status':'PASS' if not errors else 'FAIL','articles':len(articles),'projects':len(json.loads((DIST/'data/projects.json').read_text())),'indexablePages':len(json.loads((DIST/'data/pages.json').read_text())),'internalReferencesChecked':links,'relatedEdges':len(graph['edges']),'compressedDeployBytes':size,'articleBodyWords':sum(a['wordCount'] for a in articles),'minimumBodyWords':min(a['wordCount'] for a in articles),'maximumBodyWords':max(a['wordCount'] for a in articles),'errors':errors,'verificationLimits':['No browser visual or accessibility certification performed.','External links and current repository state not qualified.','No example code or proposed experiments executed.','No production deployment, Search Console submission, indexing, or ranking verified.','Adapted drafts and new guides; no universal 2000-word minimum claimed.']}
(ROOT/'AUDIT.json').write_text(json.dumps(report,indent=2));print(json.dumps(report,indent=2));sys.exit(bool(errors))
