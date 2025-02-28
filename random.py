#program to read context of a file using python. in the same directory.
with open('testr.txt','r') as f:
    for line in f:
        print (line, end= '')
   
#testr is the name of the file