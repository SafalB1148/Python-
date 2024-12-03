from datetime import date
class Person:
    def __init__(self, name,age):
        self.name = name
        self.age = age
    #a class method to create a person object by birth year
    @classmethod
    def fromBirthdayYear(cls,name,year):
        return cls(name,date.today().year-year)
    #a static method to check if a person is adult or not.
    @staticmethod
    def isAdult(age):
        return age >= 18
    def getAge(self):
        return self.age
person1=Person('Pitambar',25)
person2=Person.fromBirthdayYear('Pitambar',1996)
print(person1.getAge())
print(person2.getAge())
#print the result
print(Person.isAdult(22))
