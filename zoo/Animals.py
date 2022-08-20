# Start by creating an Animal class and then at least 3 specific 
#animal classes that inherit from Animal. (Perhaps lions and tigers and bears, oh!).
# Each animal must have at least a name, an age, a health level and a happiness level. 
# The Animal class must have a display_info method that displays the animal's name, 
# health, and happiness. You must also have an eating method 
# that increases health and happiness by 10.

# In at least one of the Animal child classes you've created, add at least one unique attribute. 
# Give each animal different predetermined levels of health and happiness.
# The animals should also respond to the feeding method with different 
# levels of changes in health and happiness.

class Animal:
    def __init__(self, name, age, health, happiness):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness
    #animal's name, health, and happiness
    def display_info(self):
        print(f'{self.name}: health - {self.health} , happiness: {self.happiness}')

    def eat(self):
        self.health = self.health + 10
        self.happiness = self.happiness + 10

class Bear(Animal):
    def __init__(self,name, age, color):
        health = 60
        happiness = 50
        super().__init__(name, age, health, happiness)
        self.color = color

    def eat(self):
        self.health = self.health + 15
        self.happiness = self.happiness + 5

class Lion(Animal):
    def __init__(self,name, age, species):
        health = 70
        happiness = 80
        super().__init__(name, age, health, happiness)
        self.species = species

    def eat(self):
        self.health = self.health + 20
        self.happiness = self.happiness + 15

class Elephant(Animal):
    def __init__(self, name, age, weight):
        super().__init__(name, age, health=99, happiness=99)
        self.weight = weight

    def eat(self):
        self.health = self.health + 30
        self.happiness = self.happiness + 40
    
