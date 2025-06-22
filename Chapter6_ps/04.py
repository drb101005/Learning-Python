#write a program to see if the entered name contains 10 or not

username = input("Enter your name: ")


if(len(username)<10):
    print("Your user name has less then 10 char..")
else:
    print("Your username has more then 10 char")