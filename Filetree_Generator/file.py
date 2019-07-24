import shutil
import os
import re
dirnum=0
filenum=0
last=''
for f in open('filenames.txt', 'r'):
	filename = re.sub(r'[\\/:*?\"<>|]', '', f).rstrip()
	filename = re.sub(r' ', '_', filename)
	if last=='':
		dirnum+=1
		dirname=str(dirnum).zfill(2)+'-'+filename
		os.mkdir(dirname)
		filenum=0
		last=dirname
		print(last)
		continue
	if(filename != ''):
		filenum+=1
		shutil.copy('default.py', dirname+'/'+str(filenum).zfill(2)+'-'+filename+'.py')
	last=filename