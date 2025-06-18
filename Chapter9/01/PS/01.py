#write a program to read the text from a given file (poems.txt) and find out where is the word twinkle
f = open("Chapter9/01/PS/poems.txt")
content = f.read()
if("twinkle" in content):
    print("twinkle is present")
else:
    print("Its not present")
f.close()

