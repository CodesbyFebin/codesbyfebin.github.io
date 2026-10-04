#!/usr/bin/env python3
from pathlib import Path
import zipfile,subprocess,sys
root=Path(__file__).resolve().parents[1]
subprocess.run([sys.executable,str(root/'scripts/build.py')],check=True)
subprocess.run([sys.executable,str(root/'scripts/audit.py')],check=True)
subprocess.run(['node','--test',str(root/'scripts/ui.test.mjs')],check=True)
target=root.parent/'CodesbyFebin-Master-Portfolio.zip'
with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(root.rglob('*')):
  if p.is_file() and '__pycache__' not in p.parts:z.write(p,Path('CodesbyFebin-Master-Portfolio')/p.relative_to(root))
print(target)
