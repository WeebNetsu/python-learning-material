import os  # to use the OS module

# print(dir(os)) # will display all attributes and methods the OS module has
# returns the current directory (cwd - current working directory)
print(os.getcwd())

try:
    os.mkdir("new-dir")  # creates a directory
    os.makedirs("newdirs/anotherdir/whatever")  # creates multiple directories
    os.mkdir("folder")
except FileExistsError:
    pass

os.rmdir("new-dir")  # remove 1 dir
# removes a dir within another direcory (directory must be empty)
os.removedirs("newdirs/anotherdir/whatever")


os.rename("folder", "coolfolder")  # renames a file/folder
"""
st_size -> size of file/folder (in bytes)
st_mtime -> modification time

to print out the modification time in a human readible format:
from datetime import datetime
print(datetime.fromtimestamp(os.stat("FolderOrFileName").st_mtime))
"""

print()
print(os.stat("coolfolder"))  # prints out all details about folder
# print(os.stat("coolfoder").st_size) # return specific detail about file/folder

print()
# os.environ -> prints out all enviroment variables
# I specify 1 with get() since I have a lot
home_dir = os.environ.get("HOME")
print(home_dir)

print()
os.chdir(f"{home_dir}/Documents")  # change directory
print(os.getcwd())

print()
print(os.listdir())  # lists all files & folders in directory
# print(os.listdir("/home/netsu/"))  # shows files/folders of specific path

print()
# the below will print out details of the files and folders inside my desktop directory
for dir_path, dir_name, file_name in os.walk("/home/netsu/Desktop"):
    print(
        f"Dir Path: {dir_path}\nFolders: {dir_name}\nFiles: {file_name}\n")

print()
# returns the deepest file/folder in the location (file.txt)
print(os.path.basename("/folder/file.txt"))
print(os.path.dirname("/folder/folder2/file.txt"))  # returns all the folders

print()
# returns whether or not a path exists
print(os.path.exists("/home/netsu/something"))

print(os.path.isdir("/home/netsu"))  # returns true if path is a directory
print(os.path.isfile("/home/netsu"))  # returns true if path is file

print()
# splits filename and extention
print(os.path.splitext("/somefolder/file.txt"))
