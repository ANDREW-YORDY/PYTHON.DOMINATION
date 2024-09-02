"""
[POO]
3. PROGRAMACIÓN ORIENTADAD A OBJETOS.
"""
from itertools import count

print( "__POO__ \n" )


#
# CLASES & OBJETCTS
#

#*SIMPLE CLASS:
class TestClass:

    # CONSTRUCTOR
    def __init__(self, nametest):
        self.nametest = nametest

    #METHOD
    def displayTest(self):
        print( "MY NAME IS: " +self.nametest )

dataTest = TestClass("tommy")  #CREATION OF INSTANCE
#print( dataTest.nametest )     #ACCESS ONE OF THE VARIABLES OF THE CLASS.
#dataTest.displayTest()         #METHOD INVOKE

#
#CONSTRUCTOR
#
class ClassTest2:
    count = 0

    def __init__(self):
        ClassTest2.count = ClassTest2.count + 1
Obj1 = ClassTest2()
Obj2 = ClassTest2()
Obj3 = ClassTest2()
#print( "Repetición de la clase: " , ClassTest2.count ) # output: Repetición de la clase: 3

#
#FUNCIONES INTEGRADAS:
#
# getattr()  --> Se utiliza para acceder al atributo del objeto.
# setattr()  --> Se utiliza para establecer un valor particular para el atributo específico de un objeto.
# delattr()  --> Se utiliza para eliminar un atributo específico.
# hasattr()  --> Devuelve true si el objeto contiene algún atributo específico.

class ClassTest3:

    def __init__(self, nombre, ids):
        self.nombre = nombre
        self.ids = ids

obj = ClassTest3( "NametestTst", 1 )

#print( getattr(obj,'nombre') )
setattr(obj, 'nombre', "NameModify")
setattr(obj, 'age', 2)
"""print( getattr( obj,'nombre') )
print( getattr( obj, 'age' ) )
print(hasattr(obj, 'nombre'))
delattr(obj, 'age')
print(obj.age)"""

print("Verificando cambio subidos a mi nueva rama 'adr'")










