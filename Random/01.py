
Name = input("Enter your name : ")
day = int(input("Enter the day : "))
month = input("Enter the month: ")
year = int(input("Enter the year(in 2005,2008,etc) : "))


string_day = str(day)
string_month = month
string_year = str(year)

letter = '''          Dear name
	You are selected
	on date x-y-z'''



print(letter.replace("name",Name).replace("x",string_day).replace("y",string_month).replace("z",string_year))
