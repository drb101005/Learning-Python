class Human:
    def __init__(self, name, height, weight, age):
        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def display_info(self):
        print(f"Name: {self.name}")
        print(f"Height: {self.height} cm")
        print(f"Weight: {self.weight} kg")
        print(f"Age: {self.age} years")

    def birthday(self):
        self.age += 1
        print(f"Happy Birthday {self.name}! You are now {self.age} years old.")

    def bmi(self):
        height_m = self.height / 100  # Convert height to meters
        bmi_value = self.weight / (height_m ** 2)
        return round(bmi_value, 2)
