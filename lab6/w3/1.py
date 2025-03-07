# file modes: 
            # 'r' - reads the content of the file and returns an error if it doesn't exist
            # 'a' - appends some content to the end of the file and creates a new file if it doesn't exist 
            # 'w' - overwrites the content of the file and creates a new file if it doesn't exist 
            # 'x' - creates a new file and returns an error if it already exists

# read() - reads the content of the file
# write() - inserts content to the file
#           (if it's used with 'w' it overwrites the initial content)
#           (if it's used with 'a' it adds a content to the end of the file)
# readline() - reads a whole line. If it's used two times, it reads first two lines of the file
# 




# deleting a file

import os

path = "/Users/tomiriszarylkasyn/Documents/labpp2/labs/lab6/no.txt"

if os.path.exists(path):
    os.remove(path)
else:
    print("The file doesn't exist")


# os.rmdir() - removes an entire folder,
# if you’re using os.rmdir() from the standard os module, the directory must be completely empty — no files or subfolders can remain