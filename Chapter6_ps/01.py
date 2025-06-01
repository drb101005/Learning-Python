'''write a program to find the biggest number out of 4 entered by user'''

a = int(input("Enter the number 1 : "))
b = int(input("Enter the number 2 : "))
c = int(input("Enter the number 3 : "))
d = int(input("Enter the number 4 : "))

if(a > b and a > c and a > d):
    print(f"The greatest number is {a}")
elif(b > a and b > c and b > d):
    print(f"The greatest number is {b}")
elif(c > b and c > d and c > a):
    print(f"The greatest number is {c}")
else:
    print(f"The greatest number is {d}")