def armstrong(n):
    str_n=str(n)
    length=len(str_n)
    sum_of_powers=0
    for digit in str_n:
        sum_of_powers=sum_of_powers+int(digit)**length
    if sum_of_powers==n:
        return("Tnumber is an armstrong number")
    return("The number is not an armstrong number")
number=int(input("Enter a number: "))
print(armstrong(number))



