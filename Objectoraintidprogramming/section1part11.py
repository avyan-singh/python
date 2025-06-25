class Dog:
    def __init__(self,breed,name,color,spots):
        self.breed=breed
        self.name=name
        self.color=color
        self.spots=spots
my_dog=Dog('Huskie','Sam','Black',True)
print(my_dog.breed)