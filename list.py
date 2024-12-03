thislist=["apple","banana","cherry","orange","kiwi","manago"]
thislist[1:3]=["blackcurrent","watermelon"]
print(thislist)

#to only print the fruits which contains word "a"
newlist=[x for x in thislist if "a" in x]
print(newlist)

#to only print the fruits which contains word "a" and all the word in uppercase
uppercase_newlist=[x.upper() for x in thislist if "a" in x]
print(uppercase_newlist)

#for sorting the list
sort_newlist=sorted(thislist)
print(sort_newlist)




