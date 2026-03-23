with open("test2/example.txt", "r") as f: #It's important to use with (it closes the file automatically)
    content = f.read()
    print(content)

#reading line by line
with open("test2/example.txt", "r") as f:
    for line in f:
        print(line.strip())
        print("-------------")

#read into a list
with open("test2/example.txt", "r") as f:
    lines = f.readlines()
    print(lines)
    print("Line 1: ", lines[0])
    print("Line 2: ", lines[1])

#writing files
with open("test2/example2.txt", "w") as f: #overwrite or create a new file
    f.write("Hello World! I am John.")

with open("test2/example2.txt", "a") as f:
    f.write("\nWriting a new line")