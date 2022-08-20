from classes import Ninja,Mascota, Dog
# from classes.Mascota import Mascota, Dog

mascota1 = Dog("bob", "gato", "cat nip", "tan")
print(mascota1)
mascota2 = Mascota("mascota", "gato", "cat nip")
print(mascota2)
Ninja1 = Ninja("Ninja", "One", "black belt", "cat nip", mascota1)
Ninja1.caminar().alimentar().banar()
# Ninja1.alimentar()
# Ninja1.banar()
print(Ninja1)