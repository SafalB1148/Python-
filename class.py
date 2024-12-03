class Vehicle:
    #class attribute
    attr1="4 wheeeler"
    #Instance attribute
    def _init_(self,name):
        self.name=name
#Driver Code
#object instantation
Rav4=Vehicle("Rav4")
Tiago=Vehicle("Tiago")

#Accessing class attribute
print("Rav4 is a (Rav4.attr1")
print("Tiago is also a )

#Accessing instance attributes
print("My name is []".format(Rav4.name))
print("My name is []".format(Tiago.name))


