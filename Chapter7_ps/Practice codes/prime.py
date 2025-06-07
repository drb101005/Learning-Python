#write a program to find all prime numbers from 0 to 100

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

for i in range(0, 101):
    if is_prime(i):
        print(i)

