class Box:
    def __init__(self, length, width, height):
        if not all(x > 0 for x in (length, width, height)):
            raise ValueError("Dimensions must be positive numbers.")
        self.length = length
        self.width = width
        self.height = height

    def volume(self):
        return self.length * self.width * self.height

    def surface_area(self):
        l, w, h = self.length, self.width, self.height
        return 2 * (l * w + l * h + w * h)

    def is_cube(self):
        return self.length == self.width == self.height

    def __str__(self):
        title = "Cube" if self.is_cube() else "Box"
        return (
            f"{title}\n"
            f"Dimensions : {self.length} × {self.width} × {self.height}\n"
            f"Volume     : {self.volume()}\n"
            f"Surface    : {self.surface_area()}"
        )


def get_dimension(name):
    while True:
        try:
            value = float(input(f"{name}: "))
            if value <= 0:
                raise ValueError
            return value
        except ValueError:
            print("Enter a valid positive number.")



def main():
    print("Enter box dimensions:")
    length = get_dimension("Length")
    w = get_dimension("Width")
    h = get_dimension("Height")
    box = Box(length, w, h)
    print("\nResult:")
    print(box)


if __name__ == "__main__":
    main()
