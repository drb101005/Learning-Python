import os
#specify the directory you want to list
directory_path = '/'
#Lists of all directory
contents = os.listdir(directory_path)
#print each file and directory name
for item in contents:
    print(item)