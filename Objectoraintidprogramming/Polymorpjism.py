class Dog:
    def __init__(self,name):
        self.name=name
    def talk(self):
       return self.name + ' says woof!'
class Cat:
    def __init__(self,name):
        self.name=name
    def talk(self):
        return self.name + ' says meow!'
mydog=Dog('Sam')
print(mydog.talk())
print(Dog('Sam').talk())
mycat=Cat('john')
print(mycat.talk())
print(Cat('John').talk())
def pet_speak(pet):
    print(pet.talk())
pet_speak(mydog)
pet_speak(mycat)
