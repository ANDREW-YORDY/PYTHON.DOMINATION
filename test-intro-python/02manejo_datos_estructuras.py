### ########
#  1.    ***********
### ########
from ast import increment_lineno
from operator import length_hint
from tkinter.font import names

from fontTools.svgLib.path.parser import UPPERCASE

# SINTAXIS Y ESTRUCTURA BÁSICA
### ########


# VARIABLES #

nombre = "Haris"
#print(nombre)

# TIPOS DE DATOS
# Lista, Tupla, Diccionario, Conjunto

#Lista
_lista  = [ 1, 2, 3, 4, 5 ]

#Tupla
_tupla = ( 6, 7, 8, 9 )

#Diccionario
_diccionario = { "Nombre": "Haris", "Edad": 21 }

#Conjunto
_conjunto = { "AUTOMÓVIL", "AVIÓN", "CRUSERO" }

#Anidar listas
x = [ 1, 2, 3, 4 ]
y = [ 'a', 'b', 'c' ]
z = [ x, y ]
#print(z[0][2],z[1][1])

#print("---")

#CONDICIONALES
# if, else, elif

"""x = 189

if x < 18:
    print("Eres menor de edad.")
elif x == 18:
    print("Acabas de pasar, a la mayoría de edad.")
elif x > 18 :
    print("Bienvenido a la adultez.")
else:
    print("Eres raro.")"""


#BUCLES
# for, while

"""for lista in _lista :
    print( lista )
for tupla in _tupla :
    print( tupla )
for diccionario in _diccionario :
    print( diccionario )
for conjunto in _conjunto :
    print( conjunto )"""

"""y = 0
while y <= 10:
    print(y)
    y += 1"""

"""#Fibonacci
a, b = 0, 1
while a < 10 :
    print(a)
    a, b = b, a+b"""


#  FUNCIONES
### ########

"""
def mi_funcion(e):
    print("Esta es una función." +e)
mi_funcion("tst param")
"""

"""def sumando():
    res = 5 + 2
    return res * 2
print(sumando())"""

"""def simplefuntion(name):
    print( f"NOMBRE FN: {name}" )
simplefuntion("CAROLINA")

def simplefuntion2(name = "CARO"):
    print( f"NOMBRE2 FN: {name}" )
simplefuntion2()"""

# FUNCIÓN LAMBDA

"""variab = lambda argu: print(f"Función Lambda. {argu}")
variab("ARGUMENTO LBD")"""

numeros = lambda arg : arg + 15
#print(numeros(5))

#NOTA: Las funciones lambda se usan comúnmente con funciones como map(), filter(), y reduce().

#-----TEST EVALUACIÓN-------:
"""def multiplicar( a, b ):
    return a * b
print(multiplicar( 6, 4 ))

def  saludar_con_edad (nomb, edad) :
    print( f" HOLA {nomb}, tienes {edad} años ")
saludar_con_edad( "HARIS CAROLINA", 21 )

saludo = lambda arg : print( f"HOLA {arg}" )
saludo( "HARICITA" )

suma = lambda arg1, arg2 :  arg1 + arg2
#print(suma(3,7))"""


### ########
# 2. MANEJO DE DATOS Y ESTRUCTURAS   ***********
### ########


#listas
#Estructuras de datos mutables y ordenadas.

#Creación
autos =  [ "MERCEDEZ","MCLAREN", "LAMBORGINI", "CH.CORVETE", "BUGATTI" ]
motos =  [ "DUCATI","YAMAHA","H.DAVINSON", "HONDA" ]

#Modificación:
#autos.append("TOYOTA")          # Añade al final
#autos.insert(1,"FERRARI")       # Inserta en posición específica
#autos.remove("LAMBORGINI")      # Elimina un elemento
#ultimo = autos.pop()            # Elimina y retorna el último elemento
#autos.extend(motos)             # Agrega los elementos de una lista al final de otra.
#autos[ 1 ] = "MODIFICANDO AUTO" # Modifica el elemento.

testslicinglist = autos[ :3 ]    # slicing --> imprime los 3 primeros elementos.
#print(testslicinglist)
#print(autos)
#print(len(autos))               # obtiene la longitud de una lista

#SLICING
#format -->  secuencia[ inicio:fin:paso ]
lista2 = "Dominando Python"

testslicing1 = lista2[ :: ]    # imprime todo
testslicing2 = lista2[ : ]     # imprime todo
testslicing3 = lista2[ 2:: ]   # imprime desde la posición 2 '/minando python'
testslicing4 = lista2[ :5: ]   # imprime hasta la posición 5 '/Domin'
testslicing5 = lista2[ ::2 ]   # imprime cada dos posiciones 'DmnnoPto
testslicing6 = lista2[ 2:7:1 ] # imprime desde la posición 2, hasta la 7, cada posición.
testslicing7 = lista2[ 2::2 ]  # imprime desde la posición 2, hasta la última, cada 2 posiciones 'mnnoPto'.
#print( testslicing7 )


#Ordenamiento#
#autos.sort()    # Ordena la lista in-place
#print( autos )
#listaordenada = sorted(autos)  # Retorna una nueva lista ordenada.
#print(listaordenada)

#reverse
#autos.reverse()        # invierte el orden de los elmentos.

#reversed
#reversed_autos = list(reversed(autos))
#print(reversed_autos)   # Crea una nueva lista invertida.
#print(autos)            # La lista original no se modifica.


# Diccionarios #
#Colección desordenada mutable, clase:valor. Definición { }
#Methods = get, update, del, pop, keys, values, items

#CREACIÓN:
usuario = {
    "NOMBRE":"Sasha",
    "EDAD": 1,
    "CIUDAD":"Medellin",
    "COLOR":"BLANCA"
}

#MODIFICACIÓN:
diccUser = {
    "NOMBRE":"SASHA",
    "EDAD":2,
    "COLOR":"BLANCA",
    "CIUDAD":"MEDELLÍN"
}

diccUser.update({"COLOR":"ACTUALIZANDO"})  # update
#del diccUser["CIUDAD"]                    # del
Get     = diccUser.get("EDAD")             # get
Keys    = diccUser.keys()                  # keys
Values  = diccUser.values()                # values
Items   = diccUser.items()                 # items
Pop     = diccUser.pop("CIUDAD")           # pop

#AMPLIACIÓN DE MÉTODOS:

# get()
# No devuelve error, aunque no exista la clave a obtener.

"""usuario["HOBBY"] = "Comer"            # Agrega un nuevo par clave-valor al final.
usuario["EDAD"] =  1.5                   # Modifica el valor de la clave EDAD.
getnombre  = usuario.get("NOMBRE")       # Obtiene el valor de la clave NOMBRE.
getdefault = usuario.get("CLIMA","Frío") # Usando get(), con valor por default.
getnone    = usuario.get("VEHICULO")     # Obtener el valor de una clave inexistente.
"""
#update()
usuario.update({ "COLOR":"MANCHAS" })

#del()
#Elimina la clave
del usuario["EDAD"]

#pop()
#Elimina la clave y obtiene su valor.
valorusupop = usuario.pop("CIUDAD")

#keys()
#Obtiene todas las claves del diccionario.
keyss = usuario.keys()

#values()
#Obtiene todos los valores del diccionario.
valuess = usuario.values()

#items
#Obtiene todos los pares clave-valor del diccionario.
itemss = usuario.items()


#Anidación de diccionarios.
diccAnidado = {
    "diccMateria": {
        "NOMBREMT":"MATEMATICAS",
        "HORASSEMANA":14,
        "GRADOS":{
            "JORNADA":"DIURNA",
            "NUMALUMNOS":120
        }
    },
    "diccMateria2": {
        "NOMBREMT": "MATEMATICAS",
        "HORASSEMANA": 14,
        "GRADOS": {
            "JORNADA": "DIURNA",
            "NUMALUMNOS": 200
        }
    }
}

diccAnidado["diccMateria2"]["HORASSEMANA"] = 10                # Modificar un valor.
#print( "HORAS:",diccAnidado["diccMateria2"]["HORASSEMANA"] )

#Acceder a un valor específico.
#print( diccAnidado["diccMateria"]["NOMBREMT"] )                # Imprime MATEMATICAS.
#print( diccAnidado["diccMateria"]["GRADOS"] )                  # Imprime {'JORNADA': 'DIURNA', 'NUMALUMNOS': 200}
#print( diccAnidado["diccMateria2"]["GRADOS"]["NUMALUMNOS"] )   # Imprime 200


# TUPLA #
# Colecciones ordenadas e inmutables. Definición ( ).

#creación
coordenadasTupla = ( 10, 4, 7 )

#Desempaquetado
#Desempaqueta los elementos de la tupla en variables
#Las tuplas no pueden ser modificadas después de su creación, a diferencia de las listas.
#x, y, z = coordenadasTupla

# Tuplas nombradas (namedtuples)
#Se pueden acceder a las tuplas, no solo por posición si no también por nombres.
from collections import namedtuple
nuevaTupla = namedtuple('nuevatupla',['a','b'])
tp  = nuevaTupla(7,4)
#print(tp.a,tp.b)


#
# MANIPULACIÓN DE ESTRUCTURAS DE DATOS
#

# ITERACIÓN SOBRE ESTRUCTURAS (lista, diccionario, tupla, conjunto, ...)

# Bucle for

#ITERANDO LISTA
"""listaIterar = [ 1, 2, 3, 4, 5 ]
for elemento in  listaIterar:
    print(elemento)"""

#ITERANDO DICCIONARIO
dicciIterar = {
    "NOMBRE":"CAROLINA",
    "NUMCARAS":3,
    "EMAIL":"correo@correo.com"
}
#Iterando Diccionario
#Iterar sobre las claves  *
"""for elemento2 in dicciIterar:
    print(elemento2)"""
#Iterando Diccionario
#Iterar sobre los valores  *
"""for elemento3 in dicciIterar.values():
    print( elemento3 )"""
# Iterando Diccionario
# Iterar sobre clave,valor en formato normal de diccionario.  *
"""for elemclave,elemvalor in dicciIterar.items():
    print( f"{elemclave}:{elemvalor}" )"""
#Iterando Diccionario
#Iterar sobre clave,valor, en forma de dupla  *
"""for elementox in dicciIterar.items():
    print( elementox )"""

#ITERANDO TUPLA
"""tuplaIterar = ( 15, 4, 7, 26 )
for elemento in tuplaIterar:
    print( elemento )"""


#COMBINACIÓN DE DIFERENTES ESTRUCTURAS

#LISTA DE TUPLAS
lista_tuplas = [
    (1,'a'),
    (2,'b'),
    (3,'c')
]
"""print( lista_tuplas )  # Impresion normal, de la lista de tuplas, y su formato
for elemtupl in lista_tuplas:
    print( elemtupl )  # Imprime cada dupla separada.
for num, letra in lista_tuplas:
    print( f'NUMERO: {num}, LETRA: {letra}' )  #Imprime con sin formato de tupla. Lo esperado.
"""
#DICCIONARIO DE TUPLAS
"""dicc_listas = {
    'robots': ['Curiosity','Walle','Chapie'],
    'Animes': ['Inuyasha','Damon Slayer','Jujutsu Kaisen']
}
print( dicc_listas )
for claveelm, valelm in dicc_listas.items():
    print( f' {claveelm}, {valelm} ' )"""

#LISTA DE DICCIONARIOS
lista_dicc = [
    { "NOMBRE":"FirstName","EDAD":100 },
    { "NOMBRE":"SecondName","EDAD":250 },
    { "NOMBRE":"Third","EDAD":300 }
]
"""#print( lista_dicc )
for elemdicc in lista_dicc:
    print( elemdicc )   #Imprime cada par por separado, en formato diccionario"""
"""for elementslist in lista_dicc:
    print( f" NAME: {elementslist['NOMBRE']}, EDAD: {elementslist['EDAD']} " )"""


# CONVERSIÓN ENTRE TIPOS DE ESTRUCTURAS

# TRANSFORMAR DATOS DE UNA ESTRUCTURA A OTRA

#LISTA A TUPLA
Lista = [ 2, 4, 6, 8 ]
Tupla = tuple(Lista)
#print( Tupla )

#TUPLA A LISTA
Tupla2 = ( 10, 12, 14, 16 )
Lista2 = list( Tupla2 )
#print( Lista2 )

#LISTA A CONJUNTO
Lista3 = [ 18, 20, 22 ]
Conjunto = set( Lista3 )
#print( Conjunto )

#DICCIONARIO A LISTA DE CLAVES Y VALORES
"""Diccionario = { 'A':1, 'B':2, 'C':3 }
CLAVES  = list( Diccionario.keys() )
VALORES = list( Diccionario.values() )
#print( CLAVES, VALORES )"""

#LISTA DE TUPLAS A DICCIONARIO
"""Lista_de_Tuplas  = [ ('UNO',1),('DOS',2),('TRES',3) ]
DICCIONARIO = dict(Lista_de_Tuplas)
print( DICCIONARIO )"""


#
# COMPRENSIONES
#

# LAS COMPRENSIONES SON UNA HERRAMIENTA PODEROSA PARA CREAR Y MANIPULAR COLECCIONES EN PYTHON.

#COMPRENSIONES DE LISTAS
#SINTAXIS
#[ new_item for item in iterable if condition ]

#LISTA DE NÚMEROS AL CUADRADO
LNumeros = [ 1,2,3,4,5 ]
#COMPRENSIÓN
SQUARES = [ n ** 2 for n in LNumeros ]
#print( SQUARES )

#FILTRAR Y CONVERTIR A MAYÚSCULAS
LNombres = [ "adolf", "socrates", "jacobo" ]
#COMPRENSIÓN
# CONVIERTES TODAS EN MAYÚSCULAS.
UPPERCASE_LNAMES  = [ UPNAM.upper() for UPNAM in LNombres ]
#print( UPPERCASE_LNAMES )
# CONVIERTES EN MAYÚSCULAS SOLO LOS ELEMNTOS QUE INICIEN EN LA LETRA 'a'.
UPPERCASE_LNAMES2 = [ UPNAM.upper() for UPNAM in LNombres if UPNAM.startswith('a') ]
#print( UPPERCASE_LNAMES2 )

#COMPRENSIONES DE DICCIONARIOS
#SINTAXIS
#{key_expression: value_expression for item in iterable if condition}
SQUARES_DICT = { elm: elm ** 2 for elm in range(6) }
#print( SQUARES_DICT )

#COMPRENSION DE CONJUNTOS
#SINTAXIS
# {expression for item in iterable if condición}
vocales_set = { letra for letra in 'piramides' }
#print( vocales_set )
#CONJUNTO CON LONGITUDES DE PALABRAS
words = [ "ATLÁNTICCO","ANTIOQUIA","CUNDINAMARCA" ]
length_set = { len(word) for word in words }
#print( length_set )  # Número de longitudes únicas.




print("--MÓDULO #1#2 SUPERADO--")
















