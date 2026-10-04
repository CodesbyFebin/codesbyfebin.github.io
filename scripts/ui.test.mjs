import test from 'node:test';
import assert from 'node:assert/strict';
import vm from 'node:vm';
import fs from 'node:fs';
const source=fs.readFileSync(new URL('../assets/site.js',import.meta.url),'utf8');
function setup(query=''){
 const nodes={};function node(extra={}){return Object.assign({hidden:false,dataset:{},listeners:{},addEventListener(name,fn){this.listeners[name]=fn},setAttribute(name,value){this[name]=value},classList:{toggle(){}}},extra)}
 nodes.theme=node();nodes.search=node({value:''});nodes.results=node({textContent:''});nodes.empty=node();
 const cards=[node({dataset:{silo:'rust'},textContent:'Rust ownership'}),node({dataset:{silo:'ai-infra'},textContent:'Worker leases'})];
 const buttons=[node({dataset:{filter:'all'}}),node({dataset:{filter:'rust'}})];
 const root={dataset:{}};const history={replaceState(a,b,c){this.url=String(c)}};const storage=new Map();
 const document={documentElement:root,getElementById(id){return nodes[id]},querySelectorAll(selector){return selector==='.note-card'?cards:buttons}};
 vm.runInNewContext(source,{document,localStorage:{getItem(k){return storage.get(k)},setItem(k,v){storage.set(k,v)}},URL,URLSearchParams,location:{href:'https://example.test/blog/'+query,search:query},history});
 return {nodes,cards,buttons,root,history,storage};
}
test('search restores URL query and selects a matching note',()=>{const s=setup('?q=leases');assert.equal(s.nodes.search.value,'leases');assert.equal(s.cards[0].hidden,true);assert.equal(s.cards[1].hidden,false);assert.equal(s.nodes.results.textContent,'1 of 2 notes')});
test('silo and text filters combine and report an empty result',()=>{const s=setup('?q=leases');s.buttons[1].listeners.click();assert.equal(s.nodes.empty.hidden,false);assert.equal(s.nodes.results.textContent,'0 of 2 notes');s.nodes.search.value='';s.nodes.search.listeners.input();assert.equal(s.cards[0].hidden,false);assert.equal(s.cards[1].hidden,true)});
test('theme preference persists and can be reversed',()=>{const s=setup();s.nodes.theme.listeners.click();assert.equal(s.root.dataset.theme,'light');assert.equal(s.storage.get('portfolio-theme'),'light');s.nodes.theme.listeners.click();assert.equal(s.root.dataset.theme,'dark')});
test('untrusted URL query is treated as text without HTML insertion',()=>{const s=setup('?q=%3Cscript%3E');assert.equal(s.nodes.results.textContent,'0 of 2 notes');assert.equal(s.nodes.empty.hidden,false);assert.equal(s.history.url.includes('%3Cscript%3E'),true)});
