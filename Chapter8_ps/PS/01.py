#write a program to find the greatest of 3 numbers

num1 = int(input("Enter the number one : "))
num2 = int(input("Enter the number two : "))
num3 = int(input("Enter the number three : "))

def greatest():
    if(num1>num2 and num1>num3):
        print(f"{num1} is greatest")
        return 0
    elif(num2>num1 and num2>num3):
        print(f"{num2} is greatest")
        return 0
    else:
        print(f"{num3} is greatest")

greatest()