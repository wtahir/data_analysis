# filelist=$(find . -iname 'merged_case.pdf')
# outdir
# for file in $filelist
# do 
# 	echo $file && 

# done
#%%

from glob import glob
from pathlib import Path
import shutil

indir  = Path('./')
li = list(indir.glob('**/merged_case.pdf'))
outdir = Path('merged')
outdir.mkdir(exist_ok=True)

# print(len(li))
for file in li:

    # file = li[0]
    dest = outdir /file.parent.with_suffix('.pdf')
    shutil.copyfile(file, dest)
    

