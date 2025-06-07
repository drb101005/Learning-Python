#Write a function to convert inches to centimeter..

def inch_to_cms(inch):
    return inch * 2.54

n = int(input("Enter the distance in Inches: "))

print(f"The distance is  {inch_to_cms(n)}")
