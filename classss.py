class person:
    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
    def details(self):
        print(f"my name is {self.name}")
        print(f"my idnumber is {self.idnumber}")
#child clas
class Employee(person):
    def __init__(self, name, idnumber, salary,post):
        self.salary = salary
        self.post = post
        person.__init__(self, name, idnumber)
    def details(self):
        print(f"my name is {self.name}")
        print(f"my idnumber is {self.idnumber}")
        print(f"my salary is {self.salary}")
        print(f"my post is {self.post}")

p=Employee("safal",22070503,50000,"Manager")
p.display()
p.details()
