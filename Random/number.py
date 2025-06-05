def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def factorial(n):
    if n < 0:
        return None
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def number_sequence(n):
    return list(range(1, n + 1))

def main():
    while True:
        print("\n--- Number Utility Tool ---")
        print("1. Check if number is Prime")
        print("2. Check if number is Even or Odd")
        print("3. Calculate Factorial")
        print("4. Generate Sequence up to N")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == '5':
            print("Goodbye!")
            break

        num_input = input("Enter a number: ")
        if not num_input.isdigit():
            print("Please enter a valid positive integer.")
            continue
        num = int(num_input)
        if choice == '1':
            print(f"{num} is {'a Prime' if is_prime(num) else 'not a Prime'} number.")
        elif choice == '2':
            print(f"{num} is {'Even' if num % 2 == 0 else 'Odd'}.")
        elif choice == '3':
            result = factorial(num)
            print(f"Factorial of {num} is {result}")
        elif choice == '4':
            print(f"Sequence up to {num}: {number_sequence(num)}")
        else:
            print("Invalid choice. Please choose between 1 and 5.")

if __name__ == "__main__":
    main()