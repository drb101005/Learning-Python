'''A program to input 8 numbers from user abd display the unique ones'''

number1 = int(input("Enter the number 1 :"))
number2 = int(input("Enter the number 2 :"))
number3 = int(input("Enter the number 3 :"))
number4 = int(input("Enter the number 4 :"))
number5 = int(input("Enter the number 5 :"))
number6 = int(input("Enter the number 6 :"))
number7 = int(input("Enter the number 7 :"))
number8 = int(input("Enter the number 8 :"))

set = set()
set.add(number1)
set.add(number2)
set.add(number3)
set.add(number4)
set.add(number5)
set.add(number6)
set.add(number7)
set.add(number8)

print(set)