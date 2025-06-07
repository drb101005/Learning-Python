# Write a program to write multiplication of a table using loop

num = int(input("Enter the number you want the multiple of : "))

for i in range(0, 11):
    multiple = num * i
    print(f"{num} * {i} = {multiple}")