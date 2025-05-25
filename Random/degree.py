import math

def print_sin_values():
    # Ask user for the maximum degree to calculate sine for
    try:
        max_degree = int(input("Enter the maximum angle in degrees (e.g., 180): "))
        interval = float(input("Enter the interval step size in degrees (e.g., 15): "))

        if max_degree < 0 or interval <= 0:
            print("Please enter positive values for degrees and interval.")
            return

        print("\nAngle (°)\tSin(angle)")
        print("-" * 25)

        for angle in range(0, max_degree + 1, interval):
            rad = math.radians(angle)  # Convert degrees to radians
            sin_val = math.sin(rad)
            print(f"{angle:>8}°\t{sin_val:.4f}")
    except ValueError:
        print("Please enter valid integers for degrees and interval.")

# Run the function
print_sin_values()
