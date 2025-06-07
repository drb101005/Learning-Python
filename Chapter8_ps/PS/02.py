#write a program to convert Celsius to Fahrenheit

cel = int(input("Enter the degree is Celsius : "))
far = 0

def converter():
    far = (cel * 1.8) + 32
    print(far)
    return 0

converter()