import math

def get_float_input(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a number greater than zero.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a number.")

def print_sin_values():
    print("📐 Sine Value Table Generator")

    max_degree = get_float_input("Enter the maximum angle in degrees (e.g., 180): ")
    interval = get_float_input("Enter the interval step size in degrees (e.g., 15): ")

    print("\n{:<12} {:<12}".format("Angle (°)", "Sin(angle)"))
    print("-" * 25)

    angle = 0.0
    while angle <= max_degree + 1e-6:  # Avoid float rounding issues
        rad = math.radians(angle)
        sin_val = math.sin(rad)
        print("{:<12.2f} {:<12.4f}".format(angle, sin_val))
        angle += interval

# Run the function
if __name__ == "__main__":
    print_sin_values()
