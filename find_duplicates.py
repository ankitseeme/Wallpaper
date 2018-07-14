import hashlib
import os
from time import time

start=time()

os.chdir("/media/ankit/New Volume/Wallpapers")

hashes={}
count=0
for i in os.listdir('.'):
    with open(i,"rb") as f:
        bytes = f.read()
        pichash = hashlib.sha256(bytes).hexdigest()
        if pichash in hashes.keys():
            print(str(i) + " is same as " + hashes[pichash])
            count+=1
        else:
            hashes[pichash] = i

if count == 0:
    print("No duplicate files")
else:
    print("Process Complete")

stop=time()

print("Complete in " + str(stop-start) + "s")