def fib(n):
    if n==0 or n==1:
        return n
    return fib(n-1)+fib(n-2)
num=int(input("Enter the number of term up to which you want to find your fiboncii series :"))
if num <=0:
    print("please enter a postive number")
else:
    print("The fibonacii series up to ",num,"is: ")
    for i in range(num):
        print(fib(i),end=" ")

