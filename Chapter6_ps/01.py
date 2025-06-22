#write a program to find the greatest of four number entered by the user 

a = int(input("Enter the numbers (1) : "))

b = int(input("Enter the numbers (2) : "))

c = int(input("Enter the numbers (3) : "))

d = int(input("Enter the numbers (4) : "))

if(a>b and a>c and a>d):
    print(f"{a} Is the greatest number")
elif(b>a and b>c and b>d):
    print(f"{b} Is the greatest number")
elif(c>a and c>b and c>d):
    print(f"{c} Is the greatest number")

else:
    print(f"{d} Is the greatest number")