#power function
def power(a,b):
    result=1
    for i in range(b):
        result=result*a
    return result
def differentpower(a,b):
    result=a**b
    return result
x=int(input("Enter thr base: "))
y=int(input("Enter thr exponent: "))
res=power(x,y)
print(f"The value of {x} raised to the power of {y} is {res} using power")
another_res=differentpower(x,y)
print(f"The value of {x} raised to the power of {y} is {another_res} using power")

