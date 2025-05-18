def print_cross(size):
    """
    Prints a cross pattern of the specified size.
    The size must be an odd integer >= 3.
    """
    if size < 3 or size % 2 == 0:
        raise ValueError("Size must be an odd integer greater than or equal to 3.")
    
    middle = size // 2

    for i in range(size):
        for j in range(size):
            if i == middle or j == middle:
                print('+', end='')
            else:
                print(' ', end='')
        print()
        

# Example usage
try:
    user_size = int(input("Enter an odd number (>=3) for the cross size: "))
    print_cross(user_size)
except ValueError as e:
    print(f"Error: {e}")
