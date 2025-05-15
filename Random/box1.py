class Box:
    def __init__(self, length, width, height):
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("All dimensions must be positive numbers.")
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

    def is_cube(self):
        return self.length == self.width == self.height

    def __str__(self):
        box_type = "Cube" if_
