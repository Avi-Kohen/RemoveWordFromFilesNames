import os
file_ending = input("Enter file extension name\n")
files = set()
base_path = input("Enter full file location\n")
name_to_remove = input("Enter the word you want to remove from the file name\n")
for x in os.listdir(base_path):
    name = x.split('.')
    if len(name) == 2 and name[1] == file_ending:
        files.add(name[0])
for filename in files:
    if name_to_remove in filename:
        print(filename.replace(name_to_remove,""))
        os.rename(os.path.join(base_path,filename+'.' +  file_ending),os.path.join(base_path,filename.replace(name_to_remove,"")+'.' +  file_ending))
