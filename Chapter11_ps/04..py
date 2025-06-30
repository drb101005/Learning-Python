# Write a class 'Complex' to represent complex numbers, along with overloaded operators '+'  which adds them


class complex:
    def __init__(self, r, i, x):
        self.r = r
        self.i = i
        self.x = x

        
    # def __add__(self, c2):
    #     return complex(self.r + c2.r , self.i + c2.i)
    

    # def __str__(self):
    #     return f"{self.r} + {self.i} i"

    def __add__(self, c3):
        return complex(self.r + c3.r , self.i + c3.i , self.x+c3.x)
    
    def __str__(self):
        return f"{self.r}r + {self.i}i + {self.x}x"
    
c1 = complex(1, 2, 1)
c2 = complex(3, 8, 7)
c3 = complex(1, 4, 2)
print(c1 + c2 + c3)
