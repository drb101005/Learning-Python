# write a program to find the grade of a student from his marks 
# 90 - 100 = Ex
# 80 - 90 = A 
# 70 - 80 = B 
# 60 - 70 = C 
# 50 - 60 = D 
# <50 = F

marks = int(input("Enter Your Marks: "))

if(marks>=90 and marks<=100):
    print("Your grade is Ex")
elif(marks>=80 and marks<=90):
    print("Your grade is A")
elif(marks>=70 and marks<=80):
    print("Your grade is B")
elif(marks>=60 and marks<=70):
    print("Your grade is C")
elif(marks>=50 and marks<=60):
    print("Your grade is D")
elif(marks<=50):
    print("Your grade is F")
else:
    print("Invalid marks")