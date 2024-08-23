
# 2. Manejo de Datos y Estructuras

#GPT

"""

1. Iteración sobre Estructuras:

¿Cómo iteras sobre los elementos de una lista y un diccionario en Python?
Mediante un loop for.

Ejercicio: Dada una lista numeros = [1, 2, 3, 4, 5], escribe un código que itere sobre esta
lista e imprima cada número multiplicado por 2. Luego, dado un
diccionario edades = {'Ana': 28, 'Luis': 34, 'María': 25}, escribe un código que itere sobre este
diccionario e imprima cada nombre junto con la edad.

numeros = [1, 2, 3, 4, 5]
for num in numeros:
    mult = num * 2
    print( mult )

edades = {
    'Ana': 28,
    'Luis': 34,
    'María': 25
}
for nombre,edad in edades.items():
    print( f'{nombre}:{edad}' )


2. Combinación de Diferentes Estructuras
Pregunta: ¿Cómo combinarías una lista de claves y una lista de valores en un solo diccionario?

Ejercicio: Dadas las listas claves = ['nombre', 'edad', 'ciudad'] y valores = ['Ana', 28, 'Bogotá'],
escribe un código que combine ambas listas en un diccionario.





"""
"""
claves = ['nombre', 'edad', 'ciudad']
valores = ['Ana', 28, 'Bogotá']
combi = list( zip(claves,valores) )
print( combi )





"""
dicc_de_listas = {
    'claves': ['nombre', 'edad', 'ciudad'],
    'valores': ['Ana', 28, 'Bogotá']
}
for cla,val in dicc_de_listas.items():
    print(f" ")






















