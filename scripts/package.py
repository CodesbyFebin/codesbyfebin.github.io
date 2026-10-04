#!/usr/bin/env python3
"""Create a reproducible master archive with deployable root and editable sources."""
import json,hashlib,zipfile,subprocess
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
for script in ['build.py','verify.py','discovery-check.py']:
 subprocess.run(['python',str(ROOT/'scripts'/script)],check=True,cwd=ROOT)
files={str(p.relative_to(ROOT/'dist')):p for p in (ROOT/'dist').rglob('*') if p.is_file()}
for folder in ['content','scripts','.github','data']:
 for p in (ROOT/folder).rglob('*'):
  if p.is_file() and '__pycache__' not in p.parts:files[str(p.relative_to(ROOT))]=p
for name in ['BUILD.md','MASTER-README.md','validation-report.json','discovery-report.json','browser-report.json','assets/js/main.ts']:
 files[name]=ROOT/name
manifest={name:{'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for name,p in sorted(files.items())}
output=ROOT/'CodesbyFebin-Master-Portfolio.zip'
with zipfile.ZipFile(output,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for name,p in sorted(files.items()):z.write(p,name)
 z.writestr('PACKAGE-MANIFEST.json',json.dumps({'files':manifest},indent=2)+'\n')
with zipfile.ZipFile(output) as z:
 assert z.testzip() is None
 assert all(hashlib.sha256(z.read(name)).hexdigest()==row['sha256'] for name,row in manifest.items())
print(json.dumps({'archive':str(output),'compressedBytes':output.stat().st_size,'uncompressedBytes':sum(x['bytes'] for x in manifest.values()),'files':len(manifest)+1,'integrity':'passed'},indent=2))
