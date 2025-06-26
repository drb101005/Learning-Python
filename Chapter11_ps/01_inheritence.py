class Employee:
    company = "G-CORP"
    def show(self):
        print(f"The name of the Employee is {self.name} and the salary is {self.salary}")


# class Programmer:
#     company = "Cal-T"
#     def show(self):
#         print(f"The name is {self.name} and the salary is {self.salary}")

#     def showLanguage(self):
#         print(f"The name is {self.name} and he is good with {self.language} language")
#so intead of writing the whole above part again you can just inherit from a parent/base class...

class Programmer(Employee):
    company = "CAL-T"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")



a = Employee()
b = Programmer()

print(a.company, b.company)