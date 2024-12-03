def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    if b==0:
        print("Mathematical Error")
    return a/b
def power(a,b):
    return a**b
def main():
    while True:
        print("Menu")
        print("1.Addition")
        print("2.Subtraction")
        print("3.Multiplication")
        print("4.Division")
        print("5.Power")
        print("6.Exit")
        choice=input("Enter your choice: ")
        if choice in ["1","2","3","4"]:
            x=float(input("Enter a number: "))
            y=float(input("Enter another number: "))
        elif choice=="5":
            a=float(input("Enter a base: "))
            b=float(input("Enter the exponent: "))
        elif choice == "6":
            print("Exiting the calculator. Goodbye!")
        else:
            print("Invalid input")
            exit()
        if choice=="1":
            print("The sum of ",x,"and ",y," is is ",add(x,y))
        elif choice=="2":
            print("The difference of ",x,"and ",y," is is ",sub(x,y))
        elif choice=="3":
            print("The product of ",x,"and ",y," is is ",mul(x,y))
        elif choice=="4":
            print("The result of divison of  ",x,"and ",y," is is ",div(x,y))
        elif choice=="5":
            print("The result of ",a,"to the power ",b,"is",power(a,b))
            break
main()