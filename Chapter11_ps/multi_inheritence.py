class A:
    def method(self):
        print("A method")

class B:
    def method(self):
        print("B method")

class C:
    def method(self):
        print("C method")

# class D(A, B, C):
#     pass



class D(A, B, C):
    def method(self):
        A.method(self)
        B.method(self)
        C.method(self)
d = D()
d.method()