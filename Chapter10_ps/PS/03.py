class Trying:
    a = 4

o = Trying()
print(o.a) # Prints the class attribute because instance attribute is not present
o.a = 0 # Instance attribute is set
print(o.a) # Prints the instance attribute because instance attribute is present
print(Trying.a) # Prints the class attribute