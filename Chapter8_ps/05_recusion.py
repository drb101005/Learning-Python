def factiorial(n):
    if(n ==1 or n ==0):
        return 1
    return n * factiorial(n-1)

n = int(input("Enter a number: "))

f = factiorial(n)

print(f)

