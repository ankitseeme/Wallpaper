import os
from shutil import copy2
from shutil import move
from time import time

print("INFO: Starting the process ... ")

start = time()

extensions = ['.jpg','.png']

os.chdir("/media/ankit/New Volume")

count=1
not_available=[1]
for i in os.listdir('./Wallpapers'):
	fname, ext = os.path.splitext(i)
	if ext.lower() in extensions:
		not_available.append(fname)

try:
	not_available=list(map(int,not_available))
except:
	print("Error... one of the files in Target directory has non-numeric name")
	exit(1)
else:
	count = max(not_available) + 1

print("INFO: the new files will start from " +str(count))

pass_count=fail_count=0
for i in os.listdir('./temp'):
    fname, ext = os.path.splitext(i)
    if ext.lower() in extensions:
        pass_count+=1
        newfname=str(count)+ext
        move('./temp/'+i,'./Wallpapers/'+newfname)
        count+=1
    else:
        fail_count+=1

print("Copy SUCCESSFUL")

stop = time()
print("Total files : " + str(pass_count+fail_count))
print("Total pictures : " + str(pass_count))
print("Total non-pictures : " + str(fail_count))
print("Operation completed in : " + str(stop-start) + "s")
