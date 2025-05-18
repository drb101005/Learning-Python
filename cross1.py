def print_fancy_cross(size=11, char='✝', border_char='█'):
    """
    Prints a more artistic cross using customizable characters.

    Parameters:
    - size: Odd integer >= 5
    - char: Character used to draw the cross (e.g., ✝, +, *, etc.)
    - border_char: Optional border character to frame the cross
    """
    if size < 5 or size % 2 == 0:
        raise ValueError("Size must be an odd integer >= 5.")

    middle = size // 2

    # Top border
    print(border_char * (size + 2))
    
    for i in range(size):
        row = border_char
        for j in range(size):
            if i == middle or j == middle:
                row += char
            else:
                row += ' '
        row += border_char
        print(row)
    
    # Bottom border
    print(border_char * (size + 2))

# Example usage
if __name__ == "__main__":
    try:
        size = int(input("Enter an odd number >= 5 for cross size: "))
        print_fancy_cross(size=size)
    except ValueError as ve:
        print("Error:", ve)
