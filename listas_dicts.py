x = [ [5,2,3], [10,8,9] ] 

estudiantes = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'}
]

directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'fútbol' : ['Messi', 'Ronaldo', 'Rooney']
}

z = [ {'x': 10, 'y': 20} ]

# 1.
# for index, lista in enumerate(x):
#     for i, a in enumerate(lista):
#         x[index][i] = 10
# print(x)

# 2.
# estudiantes[0]['last_name'] = 'Bryant'
# print(estudiantes)
# 3.
# directorio_deportes['fútbol'][0] = 'Andres'
# 4.
# z[0]['y'] = 30



# Iterar a través de una lista de diccionarios
# Crea una función iterateDictionary(some_list)para que, dada una lista de diccionarios,
# la función recorra cada diccionarios de la lista e imprima cada llave y el valor asociado.
# Por ejemplo, dada la siguiente lista:
def iterateDictionary(lista):
    for estudiante in estudiantes:
        # print(estudiante)
        for index, x in enumerate(estudiante):
            if index + 1 == len(estudiante):
                print(f'{x} - {estudiante[x]}', end=' ')
            else:
                print(f'{x} - {estudiante[x]}', end=', ')
        print('')

estudiantes = [
         {'first_name':  'Michael', 'last_name' : 'Jordan'},
         {'first_name' : 'John', 'last_name' : 'Rosales'},
         {'first_name' : 'Mark', 'last_name' : 'Guillen'},
         {'first_name' : 'KB', 'last_name' : 'Tonel'}
]
# iterateDictionary(estudiantes) 

# Obtener valores de una lista de diccionarios
# Crea una función iterateDictionary2(key_name, some_list)que, dada una lista de diccionarios y un nombre de clave, 
# la función imprima el valor almacenado en esa clave para cada diccionario. 
# Por ejemplo, iterateDictionary2('name', estudiantes) debería generar:

def iterateDictionary2(llave, lista):
    for x in lista:
        print(x[llave])

iterateDictionary2('last_name', estudiantes) 