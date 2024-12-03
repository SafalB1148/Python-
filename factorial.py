#wap to ask a user for a number and use function to calculate factorial of that number
def recursive_factorial(n):
    if n==0:
        return 1
    return n*recursive_factorial(n-1)
numm=int(input("Enter a number: "))
facto=recursive_factorial(numm)
print(f"The factorial of {numm} is {facto}")

def fact(n):
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result
num= int(input("Enter a number: "))
factorial=fact(num)
print(f"The factorial of {num} is {factorial}")
