# Imprimir y devolver: crea una función que reciba una lista con dos números. 
# Imprime el primer valor y devuelve el segundo.
# Ejemplo: imprimir_y_devolver([1,2]) debe imprimir 1 y devolver 2

def imprimir_y_devolver(listaNums):
    print(listaNums[0])
    return listaNums[1]


# result = imprimir_y_devolver([1,2])
# print('*'*20)
# print(result)



# Esta longitud, ese valor: escribe una función que acepte dos enteros como parámetros: tamaño y valor. 
# La función debe crear y devolver una lista cuya longitud sea igual al tamaño dado, 
# y cuyos valores sean todos el valor dado.
# Ejemplo: length_and_value(4,7) debe devolver [7,7,7,7]
# Ejemplo: length_and_value(6,2) debe devolver [2,2,2,2,2,2]

def length_and_value(num1, num2):
    results = []
    for x in range(0, num1):
        results.append(num2)

    return results

# print(length_and_value(21,8))
# arr = length_and_value(6,2)
# print(arr)

x = [ [5,2,3], [10,8,9] ] 
# Cambia el valor 10 en x a 15. Una vez que hayas terminado, x ahora debería ser [ [5,2,3], [15,8,9] ].
x[1][0] = 15
print(x[1])


estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]
# Cambia el "apellido” del primer alumno de 'Jordan' a 'Bryant'.
estudiantes[0]['last_name'] = 'Bryant'
print(estudiantes[0]['last_name'])

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}
# En el directorio_deportes, cambia "Messi" por "Andrés".
directorio_deportes['fútbol'][0] = "Andrés"
print(directorio_deportes)

# En el directorio_deportes, cambia "Messi" por "Andrés".


z = [ {'x': 10, 'y': 20} ]
z[0]['y'] = 3
print(z)
# Cambia el valor 20 en z a 3


# Iterar a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios,
# la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado. 
# Por ejemplo, dada la siguiente lista:
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
def iterateDictionary(some_list):
    for x in some_list:
        print(f"first name: {x['first_name']} - last name: {x['last_name']} ")

iterateDictionary(estudiantes)
# debería devolver: (está bien si cada par clave-valor termina en 2 líneas separadas;
# un bonus para que aparezcan exactamente como se muestra a continuación)

# first_name - Michael, last_name - Jordan
# first_name - John, last_name - Rosales
# first_name - Mark, last_name - Guillen
# first_name - KB, last_name - Tonel