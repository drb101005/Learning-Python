HSBC = {"Amit", "Priya", "Raj", "KK", "Anjali"}
CapG = {"Karan", "Shivank", "Dhruv", "Durva", "Yati"}



common_project = HSBC.intersection(CapG)
print("Employees working on common project:", common_project)


all_employees = HSBC.union(CapG)
print("\nAll employees from both HSBC and CapG:", all_employees)

only_working_in_hsbc = HSBC.difference(CapG)
only_working_in_capG = CapG.difference(HSBC)

print("\nEmployees only in HSBC:", only_working_in_hsbc)
print("Employees only in CapG:", only_working_in_capG)
