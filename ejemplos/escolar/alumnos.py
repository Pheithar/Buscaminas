#importamos todo el módulo con TODAS sus clases.
import basedatos
db = basedatos.DataBase()

#importar solo una clase from móduloName import ClassName
from basedatos import DataBase
db2 = DataBase()

#importar solo una clase from móduloName import ClassName as newName
#Sirve para importar la clase cambiando el nombre
from basedatos import DataBase as DB
db2 = DB()

#importar solo varias clases from móduloName import ClassName, ClassName2
from basedatos import DataBase, Tabla
db2 = DataBase()

class Student(object):

    def __init__(self, name, age):
        '''Creamos el constructor de la clase Student.'''
        self.name = name
        self.age = age
