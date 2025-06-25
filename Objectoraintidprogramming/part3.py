class Animal:
    def __init__(self):
        print('animal Created!')
    def who_am_I(self):
        print('I am an animal!')
    def Eat(self):
        print('I am eating!')
myanimal=Animal()
print(myanimal)
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        print('Dog created')
    def bark(self):
        print('Woof!')
mydog=Dog()
print(mydog.Eat())
print(mydog.who_am_I())
print(mydog.bark())
        