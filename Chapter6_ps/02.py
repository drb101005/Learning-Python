'''The check if a student is passing or not
conditions : 40 % all avg 
 33 % in each subject for 3 subjects
 '''

mark1 = int(input("Enter the marks of subject 1: "))
mark2 = int(input("Enter the marks of subject 2: "))
mark3 = int(input("Enter the marks of subject 3: "))

average = (mark1 + mark2 + mark3) / 3

if average >= 40 and mark1 >= 33 and mark2 >= 33 and mark3 >= 33:
    print("You passed!!!!")
else:
    print("You failed")
