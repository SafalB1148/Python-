numlist=[]
while(True):
    x=int(input("Enter a number: "))
    if x==0:
        break
    numlist.append(x)
def findmax(listofnumbers):
    max=0
    for num in listofnumbers:
        if num>max:
            max=num
    return max
maxnum=findmax(numlist)
print(f"The maximum number in the list is {maxnum}")
