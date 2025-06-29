#Create a class 'Employee' and add salary and increment properties to it
#Write a method "Salary after increment " with a @property decorator with a setter which changes the value after increment


class employee():
    pass
    salary = 45
    increment = 20
    @property 
    def salaryafterincrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @salaryafterincrement.setter
    #This is to find the value of increment
    def salaryafterincrement(self, salary):
        self.increment = ((salary/self.salary) - 1)*100
    

e = employee()
#print(f"{e.salary} and {e.salaryafterincrement}")

e.salaryafterincrement = 54.1
print(e.increment)



