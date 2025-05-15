# Box class definition
class Box:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def surface_area(self):
        lw = self.length * self.width
        lh = self.length * self.height
        wh = self.width * self.height
        return 2 * (lw + lh + wh)

# Example usage
if __name__ == "__main__":
    # Create a box with length=5, width=3, height=2
    my_box = Box(5, 3, 2)

    print("Box dimensions:")
    print(f"Length: {my_box.length}")
    print(f"Width: {my_box.width}")
    print(f"Height: {my_box.height}")
    print("\nCalculations:")
    print(f"Volume: {my_box.volume()}")
    print(f"Surface Area: {my_box.surface_area()}")

