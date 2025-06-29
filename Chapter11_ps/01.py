#Create a class (2-D vector) and use it to create another class representing a 3 D vector

class TwoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    
    def show(self):
        print(f"The Vectors are {self.i}i and {self.j}j ")


class ThreeDvector(TwoDvector):
    def __init__(self, i, j, k):
        super().__init__(i, j)
        self.k = k 
    
    def show(self):
        print(f"The Vectors are {self.i}i and {self.j}j and {self.k}k")

a = TwoDvector(1, 3)
a.show()
b = ThreeDvector(1, 89, 8)
b.show()