import sys
import os
import random
import hashlib
from shutil import copy2
from shutil import rmtree
import time

drive_loc = ""
copy_from_loc = ""
extensions = ['.jpg', '.png']
valid_args = ['-', 'c', 'd', 'r']
target_files = []


def usage():
    print("The program takes 1 mandatory argument")
    print("python wall.py -c|-d|-r")
    print("-c : copy files from temp")
    print("-d : find duplicate files")
    print("-r : rename files")


def find_rename(drive_loc):
    os.chdir(drive_loc)
    global target_files
    for file in os.listdir('.'):
        fname, ext = os.path.splitext(file)
        if ext.lower() in extensions:
            target_files.append(fname)
    try:
        target_files = [int(i) for i in target_files]
    except:
        print("Found a non numeric wallpaper name in the target directory...")
        new_count = complete_rename()
        return new_count
    else:
        target_files.sort()
        if len(target_files) == 0:
            print("no wallpaper in the directory")
            return 0
        if target_files[-1] == len(target_files):
            print('no need to rename')
            return target_files[-1]
        else:
            new_count = complete_rename()
            return new_count


def complete_rename():
    temp_name = str(random.randint(50000, sys.maxsize))
    print("starting renaming")
    try:
        os.mkdir(temp_name)
    except:
        print("Error during cretion of temp directory")
        exit(2)
    count = 1
    pass_count = fail_count = 0
    for i in os.listdir('.'):
        fname, ext = os.path.splitext(i)
        if ext.lower() in extensions:
            pass_count += 1
            newfname = str(count) + ext
            copy2(i, './' + temp_name + "/" + newfname)
            count += 1
        else:
            fail_count += 1

    for file in os.listdir('.'):
        fname, ext = os.path.splitext(file)
        if ext.lower() in extensions:
            os.remove(file)

    for file in os.listdir('./'+temp_name):
        copy2('./' + temp_name + '/' + file, '.')
    rmtree(temp_name)
    return count


def copy_wallpapers(temp_loc, drive_loc, new_count):
    os.chdir(temp_loc)
    for file in os.listdir('.'):
        fname, ext = os.path.splitext(file)
        if ext.lower() in extensions:
            newfname = str(new_count)+ext
            copy2(file, drive_loc + "/" + newfname)
            new_count += 1


def find_duplicates(drive_loc):
    os.chdir(drive_loc)
    hashes = {}
    count = 0
    for file in os.listdir('.'):
        fname, ext = os.path.splitext(file)
        if ext.lower() in extensions:
            with open(file, "rb") as f:
                bytes = f.read()
                pichash = hashlib.sha256(bytes).hexdigest()
                if pichash in hashes.keys():
                    print(str(file) + " is same as " + hashes[pichash])
                    count += 1
                else:
                    hashes[pichash] = file
    if count == 0:
        print("No duplicate files")
    else:
        print("""Advised to run the script with -r """
              """to rename the files after deleting the duplicates""")
        print("Process Complete")


def take_source_loc():
    global copy_from_loc
    copy_from_loc = input("Provide the source path: ")
    if not os.path.isdir(copy_from_loc):
        print("Not a valid source directory")
        exit(1)


def take_target_loc():
    global drive_loc
    drive_loc = input("Provide the wallpaper path: ")
    if not os.path.isdir(drive_loc):
        print("Not a valid source directory")
        exit(1)


if __name__ == '__main__':
    start = time.time()
    if len(sys.argv) == 1:
        usage()
    elif len(sys.argv) > 2:
        usage()
    else:
        count = 1
        args = list(sys.argv[1])
        for arg in args:
            if arg not in valid_args:
                print("invalid argument: " + arg +
                      " in " + ''.join(sys.argv[1]))
                usage()
                exit(1)
        if 'r' in args:
            print("Starting the renaming process")
            take_target_loc()
            count = find_rename(drive_loc)
            print("Renaming process complete")
            print()
        if 'c' in args and 'r' in args:
            print("starting the copy process to the above given location")
            take_source_loc()
            if drive_loc == copy_from_loc:
                print("Source and Target location is same... Exiting...")
                exit(1)
            copy_wallpapers(copy_from_loc, drive_loc, count+1)
            print("Copy process complete")
            print()
        if 'c' in args and 'r' not in args:
            take_source_loc()
            take_target_loc()
            if drive_loc == copy_from_loc:
                print("Source and Target location is same... Exiting...")
                exit(1)
            print("Starting the renaming process before copying")
            count = find_rename(drive_loc)
            print("Starting the copy process")
            copy_wallpapers(copy_from_loc, drive_loc, count+1)
            print("Copy process complete")
            print()
        if 'd' in args:
            print("Starting to find the duplicates")
            take_target_loc()
            find_duplicates(drive_loc)
            print()
    print("Program run time " + str(time.time() - start) + "s")
