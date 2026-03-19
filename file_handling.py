import os

#open("path", "mode")
# r - read
# a - append
# w - write
# x - creat
# r+ - read + write

f = open("test/test.txt", "r")
#print(f.readable()) #true or false
print(f.read()) #read all file

#print(f.readline()) # read first line
#print(f.readline()) #read second line

#list_f = f.readlines()
#print(list)
#print(list[3])


#f = open("test/test.txt","a")
#f.write("\nSQL")
#f.write("\nPascal")
#f.write("\nJava")


#f = open("test/test.txt","w") #when "w" is used at an existing file, all the content is deletedf
#f.write("Ruby")

#f = open("test/test2.txt", "w") #when the path doesn't exist a new file is created
#f.write("HTML\nCSS\nJavaScript\nNode\n")


#f = open("test/test3.txt", "x")
#f.write("Python")

f.close() #if the file is not closed, it may cause errors when we try to handle the file again

#os.remove("test/test3.txt") or
'''if os.path.exists("test/test3.txt"):
    os.remove("test/test3.txt")
else:
    print("File does not exist") '''

#after I created a test directory
#os.rmdir("test/test_directory") # it will just remove this directory if it's empty

#I deleted the txt files to let git/github clean