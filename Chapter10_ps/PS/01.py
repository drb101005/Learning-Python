#Create a class "programmer" for storing info of programmers working in microsoft

class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin


p = programmer("Dhruv ",9000000, 401202)
print(p.name, p.salary, p.pin, p.company)

r = programmer("Rohan ",9000000, 401202)
print(r.name, r.salary, r.pin, r.company)
