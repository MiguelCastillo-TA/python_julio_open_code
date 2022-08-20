from Animals import Elephant
class Zoo:
    def __init__(self, zoo_name):
        self.animals = []
        self.name = zoo_name

    def addElephant(self):
        newElephant = Elephant("ele", 40, 1200)
        self.animals.append(newElephant)
        print('Elephant added to zoo')

    # def imprimir_toda_info(self):
    #     print("-"*30, self.name, "-"*30)
    #     for animal in self.animals:
    #         animal.display_info()

zoo1 = Zoo("El zoo de John")
zoo1.addElephant()
