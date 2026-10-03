#!/usr/bin/env python3
"""Validate the emitted site: routes, anchors, metadata, schema and size budgets."""
import json,re
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import xml.etree.ElementTree as ET
ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
class Page(HTMLParser):
    def __init__(self,text):
        super().__init__(convert_charrefs=True);self.links=[];self.ids=[];self.h1=0;self.title='';self.desc='';self.canonical='';self.scripts=[];self.ld=False;self.script='';self.in_title=False;self.main=False;self.skip=0;self.words=[];self.imgs=[];self.feed(text)
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.append(a['id'])
        if tag=='h1':self.h1+=1
        if tag=='title' and not self.main:self.in_title=True
        if tag=='main':self.main=True
        if tag=='meta' and a.get('name')=='description':self.desc=a.get('content','')
        if tag=='link' and a.get('rel')=='canonical':self.canonical=a.get('href','')
        if tag=='script':self.ld=a.get('type')=='application/ld+json';self.script='';self.skip+=1
        if tag=='style':self.skip+=1
        if tag=='img':self.imgs.append(a)
        for key in ['href','src']:
            if key in a:self.links.append(a[key])
    def handle_endtag(self,tag):
        if tag=='title':self.in_title=False
        if tag=='main':self.main=False
        if tag=='script':
            if self.ld:self.scripts.append(json.loads(self.script))
            self.ld=False;self.skip-=1
        if tag=='style':self.skip-=1
    def handle_data(self,data):
        if self.in_title:self.title+=data
        if self.ld:self.script+=data
        if self.main and not self.skip:self.words.extend(re.findall(r"\b[\w]+(?:[’-][\w]+)*\b",data))

pages={str(f.relative_to(DIST)):Page(f.read_text()) for f in DIST.rglob('*.html')}
fail=[];titles=set();descriptions=set();primary=[]
sitemap=json.loads((DIST/'sitemap.json').read_text())['pages']
for entry in sitemap:
    path=entry['path'];p=pages[path]
    if p.h1!=1:fail.append(f'{path}: expected one H1, found {p.h1}')
    if p.title in titles:fail.append(f'{path}: duplicate title')
    titles.add(p.title)
    if p.desc in descriptions:fail.append(f'{path}: duplicate description')
    descriptions.add(p.desc)
    if p.canonical!=entry['url']:fail.append(f'{path}: canonical mismatch')
    if not p.scripts:fail.append(f'{path}: missing JSON-LD')
    if len(p.ids)!=len(set(p.ids)):fail.append(f'{path}: duplicate IDs')
    if not 80<=len(p.desc)<=175:fail.append(f'{path}: description length {len(p.desc)}')
    if '/' not in path:primary.append({'path':path,'mainWords':len(p.words),'titleChars':len(p.title),'descriptionChars':len(p.desc)})
for path,p in pages.items():
    for link in p.links:
        u=urlparse(link)
        if u.scheme or u.netloc:continue
        target=(DIST/u.path.lstrip('/')) if u.path.startswith('/') else (DIST/path).parent/u.path
        if not u.path:target=DIST/path
        if target.is_dir():target=target/'index.html'
        target=target.resolve()
        if not target.is_relative_to(DIST.resolve()):fail.append(f'{path}: escaping link {link}');continue
        if not target.exists():fail.append(f'{path}: missing {link}');continue
        relative=str(target.relative_to(DIST))
        if u.fragment and relative in pages and unquote(u.fragment) not in pages[relative].ids:fail.append(f'{path}: missing anchor {link}')
    for image in p.imgs:
        if 'alt' not in image:fail.append(f'{path}: missing image alt')
ET.parse(DIST/'sitemap.xml')
files=list(f for f in DIST.rglob('*') if f.is_file())
size=sum(f.stat().st_size for f in files)
css=sum(f.stat().st_size for f in (DIST/'assets/css').glob('*.css'))
wordcount=sum(p['mainWords'] for p in primary)
if size>=3_000_000:fail.append(f'Footprint {size} exceeds 3 MB')
if css>=50_000:fail.append(f'CSS {css} exceeds 50 KB')
if wordcount<15_000:fail.append(f'Primary content {wordcount} words falls short of 15,000')
if len(json.loads((DIST/'data/projects.json').read_text())['projects'])<20:fail.append('Fewer than 20 repositories')
report={'primaryPages':len(primary),'projectGuides':len(sitemap)-len(primary),'primaryMainWords':wordcount,'deployedBytes':size,'cssBytes':css,'pageMetrics':primary,'failures':fail,'method':'Words in main HTML, excluding scripts and styles. Includes source documentation, code, tables, headings, and visible callouts. Excludes navigation/footer and project-guide pages.'}
(ROOT/'validation-report.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
if fail:raise SystemExit(1)
