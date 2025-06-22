#Write a program to find out wether a student has passed or failed if it requires a total of 44 % and at least 33% in each
#  subject to pass.Assume 3 subjects and take marks from user

sub_1 = int(input("Enter the Marks in subject 1 : "))
sub_2 = int(input("Enter the Marks in subject 2 : "))
sub_3 = int(input("Enter the Marks in subject 3 : "))

sub_total = (100*(sub_1 + sub_2 + sub_3))/300
sub_total2 = float(sub_total)

if(sub_1>33 and sub_2>33 and sub_3>33 and sub_total >44):
    print(f"You have passed indiviually And in Total :{sub_total2} !!! ")
else:
    print("App Pass nahi ho paye")

# print("The Job is done")
