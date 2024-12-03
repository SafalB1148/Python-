# write a recursive function to print the fibonacii sequence up to nth term n should be ask to ehe user
def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
num=int(input("Enter the number of terms up to which you want the fibonacci series: "))
if num<=0:
    print("please enter a positive number")
else:
    print("Fibonacci sequence upto",num,"is:")
    for i in range(num):
        print(fib(i),end=" ")
