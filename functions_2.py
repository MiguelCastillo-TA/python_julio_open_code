# Imprimir y devolver: crea una función que reciba una lista con dos números. 
# Imprime el primer valor y devuelve el segundo.
# Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

def imprimir_y_devolver(listaNums):
    print(listaNums[0])
    return listaNums[1]


result = imprimir_y_devolver([1,2])
print('*'*20)
print(result)

