import sys
from rich import print
from time import sleep

def printsong():
    lines = [
        ("I wanna da-", 0.6),
        ("I wanna dance in the lights", 0.05),
        ("I wanna ro-", 0.7),
        ("I wanna rock your body", 0.08),
        ("I wanna go-", 0.068),
        ("I wanna go for a ride", 1.0),
        ("You don't have to admit you wanna play", 1.3),
        ("Just let me rock you", 1.0),
        ("Till the break of day", 1.2),
        # Add more lines as needed
    ]

    for line, delay in lines:
        print(f"[bold cyan]{line}[/bold cyan]")
        sleep(delay)

if __name__ == "__main__":
    printsong()
