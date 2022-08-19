class Ninja:
    def __init__(self,nombre, apellido, premios, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota
        self.mascota = mascota
    # caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
    def caminar(self):
        print("Camindo la mascota...")
        self.mascota.jugar()
        return self

    # alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
    def alimentar(self):
        print("Alimentar")
        self.mascota.comer()
        return self
    # bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
    def banar(self):
        print('Banando ')
        self.mascota.sonido()
        return self

    def __repr__(self):
        return f'*****\nName: {self.nombre}\nMascota:{self.mascota}\n*****'