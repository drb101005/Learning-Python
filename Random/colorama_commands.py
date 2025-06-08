from colorama import Fore, Back, Style, init

# Initialize colorama
init(autoreset=True)

def print_fore_colors():
    print("Foreground colors:")
    for color_name in dir(Fore):
        if not color_name.startswith("_"):
            color_value = getattr(Fore, color_name)
            print(f"{color_value}{color_name}")

def print_back_colors():
    print("\nBackground colors:")
    for color_name in dir(Back):
        if not color_name.startswith("_"):
            color_value = getattr(Back, color_name)
            print(f"{color_value}{color_name}")

def print_styles():
    print("\nText styles:")
    for style_name in dir(Style):
        if not style_name.startswith("_"):
            style_value = getattr(Style, style_name)
            print(f"{style_value}{style_name}")

if __name__ == "__main__":
    print_fore_colors()
    print_back_colors()
    print_styles()
