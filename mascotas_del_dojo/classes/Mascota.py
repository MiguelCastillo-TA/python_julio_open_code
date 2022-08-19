class Mascota:
    def __init__(self, name, tipo, golosinas):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.salud = 100
        self.energia = 100
  
    # dormir() - incrementa la energía de la mascota en 25
    def dormir(self):
        self.energia = self.energia + 25
        
     # comer() - incrementa la energía de la mascota en 5 y la salud en 10
    def comer(self):
        print('Comiendo')
        self.energia = self.energia + 5
        self.salud = self.salud + 10
    # jugar() - incrementa la salud de la mascota en 5
    def jugar(self):
        print('Mascota jugando')
        self.salud = self.salud + 5
    # ruido() - imprime el sonido que produce la mascota
    def sonido(self):
        print('meow')
    
    def __repr__(self):
        return f'***** \nName: {self.name}\nSalud:{self.salud}\nEnergia:{self.energia} \n*****'

class Dog(Mascota):
    def __init__(self, name, tipo, golosinas):
        super().__init__(name, tipo, golosinas)

    def sonido(self):
        print('BARK')


if __name__ == "__main__":
    print('MASCOTA MAIN')
    dog1 = Dog("dog", "dog", "dog treats")
    dog1.sonido()

