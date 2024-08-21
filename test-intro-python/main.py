### ########
#  1. SINTAXIS Y ESTRUCTURA BÁSICA   ***********
### ########

nombre = "Haris"
#print(nombre)

#function
"""
def mi_funcion(e):
    print("Esta es una función." +e)
mi_funcion("tst param")
"""

"""def sumando():
    res = 5 + 2
    return res * 2
print(sumando())"""


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
print(z[0][2],z[1][1])


print("---")


#CONDICIONALES

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
print( "HORAS:",diccAnidado["diccMateria2"]["HORASSEMANA"] )

#Acceder a un valor específico.
print( diccAnidado["diccMateria"]["NOMBREMT"] )                # Imprime MATEMATICAS.
print( diccAnidado["diccMateria"]["GRADOS"] )                  # Imprime {'JORNADA': 'DIURNA', 'NUMALUMNOS': 200}
print( diccAnidado["diccMateria2"]["GRADOS"]["NUMALUMNOS"] )   # Imprime 200


# TUPLA #
# Colecciones ordenadas e inmutables. Definición ( ).

#creación
coordenadasTupla = ( 10, 4, 7 )

#Desempaquetado
#Desempaqueta los elementos de la tupla en variables
#Las tuplas no pueden ser modificadas después de su creación, a diferencia de las listas.
#Se pueden acceder a las tuplas, no solo por posición si no también por nombres.
x, y, z = coordenadasTupla

# Tuplas nombradas (namedtuples)
from collections import namedtuple
nuevaTupla = namedtuple('nuevatupla',['a','b'])
tp  = nuevaTupla(7,4)
print(tp.a,tp.b)