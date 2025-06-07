# Write a program to write multiplication of a table using loop

num = int(input("Enter the number you want the multiple of : "))

i = 1
while(i<11):
    multiple = num * i
    print(f"{num} X {i} = {multiple}")
    i +=1