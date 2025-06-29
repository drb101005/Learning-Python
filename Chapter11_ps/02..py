#Create a class 'pet' from a class 'Animals' and further create a class'dog' from 'pets'. 
#Add a method 'bark' to class 'Dog' 

class animal:
    def __init__(self):
        pass

class pets(animal):
    pass


class dog(pets):
    @staticmethod
    def bark():
        print("Bark Bark")


d = dog()

d.bark()