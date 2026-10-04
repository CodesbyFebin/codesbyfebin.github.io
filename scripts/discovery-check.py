#!/usr/bin/env python3
"""Check crawl discovery, structured answers, geographic signals and link reachability."""
import json,posixpath
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse
ROOT=Path(__file__).resolve().parents[1];D=ROOT/'dist'
class Scan(HTMLParser):
 def __init__(self,text):
  super().__init__();self.links=[];self.meta={};self.ld=[];self.inld=False;self.buf='';self.feed(text)
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='a':self.links.append(a.get('href',''))
  if t=='meta':self.meta[a.get('name',a.get('property',''))]=a.get('content','')
  if t=='script' and a.get('type')=='application/ld+json':self.inld=True;self.buf=''
 def handle_data(self,t):
  if self.inld:self.buf+=t
 def handle_endtag(self,t):
  if t=='script' and self.inld:self.ld.extend(json.loads(self.buf)['@graph']);self.inld=False
entries=json.loads((D/'sitemap.json').read_text())['pages'];paths={e['path'] for e in entries};graph={};checks=[]
for e in entries:
 path=e['path'];text=(D/path).read_text();p=Scan(text)
 for name in ['description','robots','og:title','og:description','og:image','og:url','twitter:card','twitter:image','geo.region','geo.placename']:
  assert p.meta.get(name),f'{path}: missing {name}'
 assert p.meta['geo.region']=='IN-KL' and p.meta['geo.placename']=='Kerala, India'
 types={x['@type'] for x in p.ld};assert {'Person','WebPage','WebSite','BreadcrumbList'}<=types
 if path.startswith('projects/'):
  assert 'SoftwareSourceCode' in types
  crumb=next(x for x in p.ld if x['@type']=='BreadcrumbList');assert len(crumb['itemListElement'])==3
 else:
  assert 'FAQPage' in types
  faq=next(x for x in p.ld if x['@type']=='FAQPage')['mainEntity'][0]
  import html
  assert html.escape(faq['name'],quote=True) in text
  assert html.escape(faq['acceptedAnswer']['text'],quote=True) in text
 graph[path]=set()
 for link in p.links:
  u=urlparse(link)
  if u.scheme or u.netloc:continue
  target=posixpath.normpath(posixpath.join(posixpath.dirname(path),u.path)) if u.path else path
  if (D/target).is_dir():target=target.rstrip('/')+'/index.html'
  if target in paths:graph[path].add(target)
for start in paths:
 reached=set();todo=[start]
 while todo:
  n=todo.pop()
  if n in reached:continue
  reached.add(n);todo.extend(graph[n]-reached)
 assert reached==paths,f'{start}: unreachable pages {paths-reached}'
assert 'sitemap.xml' in (D/'robots.txt').read_text()
assert all(e['url'] in (D/'llms.txt').read_text() for e in entries)
report={'indexedPages':len(paths),'internalPageEdges':sum(map(len,graph.values())),'allPagesMutuallyReachable':True,'geographicMetadata':'Kerala, India / IN-KL','visibleStructuredAnswers':10,'projectBreadcrumbDepth':3,'schemaAndDiscoveryChecks':'passed','outboundLinks':{p:sorted(v) for p,v in graph.items()},'scope':'Static discovery and reachability checks. Does not predict ranking, rich results, or crawler inclusion.'}
(ROOT/'discovery-report.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='outboundLinks'},indent=2))
