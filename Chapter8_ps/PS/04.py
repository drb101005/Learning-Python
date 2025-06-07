#write a funtion to calculate the sum of n natural numbers 
b = int(input("Enter the number till which you want the sum : "))
def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n

print(sum(b))