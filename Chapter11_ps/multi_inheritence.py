class A:
    def method(self):
        print("A method")

class B:
    def method(self):
        print("B method")

class C:
    def method(self):
        print("C method")

class D(A, B, C):
    pass

d = D()
d.method()
