'''
Created on 22/5/2015

@author: guilledelacruz
'''
from Coche import Coche
from Persona import Persona
global str

coche = Coche(10, 2, "matricula", "dueno")

coche.conductorSolo()
coche.conducir(9)
coche.conducir(2)
coche.echaGasolina(100)
print coche.gasolinaRestante()
print coche.__str__()

persona = Persona("identificacion", "nombre", "apellido")
print persona.identificacion
print persona.nombre
print persona.apellido
print persona.__cmp__(persona)