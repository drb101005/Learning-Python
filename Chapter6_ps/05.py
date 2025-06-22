#write a program if a name is present in a list or not

list = ["dhruv","yati","rahul","hiya","riya","tiya"]

name = input("Enter your name: ")

if(name.lower() in list):
    print("Your name is in the list!!")
else:
    print("Your name is not in the list")