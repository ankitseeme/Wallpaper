import os
from shutil import copy2
from shutil import rmtree
from time import time

print("INFO: Starting the process ... ")

start = time()

extensions = ['.jpg','.png']

os.chdir("/media/ankit/New Volume/Wallpapers")

try:
    os.mkdir('./temp')
except:
    print("Error .. temp directory already exists")
    exit(1)


count=1
pass_count=fail_count=0
for i in os.listdir('.'):
    fname, ext = os.path.splitext(i)
    if ext.lower() in extensions:
        pass_count+=1
        newfname=str(count)+ext
        copy2(i,"./temp/"+newfname)
        #print("copied " + str(i) + " to " + str(newfname))
        count+=1
    else:
        fail_count+=1
print("INFO: Copy to TEMP SUCCESSFUL ... ")
print("INFO: Copy from TEMP to orginial SUCCESSFUL")


for i in extensions:
	os.system("rm -f *"+i)
	os.system("rm -f *"+i.upper())
print("INFO: Removal of temp SUCCESSFUL ... ")


os.system('cp ./temp/* .')
rmtree('temp')


stop = time()
print("Total files :".ljust(35) + str(pass_count+fail_count-1))
print("Total pictures :".ljust(35) + str(pass_count))
print("Total non-pictures:".ljust(35) + str(fail_count-1))
print("Operation completed in:".ljust(35) + str(stop-start) + "s")
