'''
Created on 22/5/2015

@author: guilledelacruz
'''

class Persona(object):
    "Clase que representa una persona."
    def __init__(self, identificacion, nombre, apellido):
        "Constructor de Persona"
        self.identificacion = identificacion
        self.nombre = nombre
        self.apellido = apellido
    def __str__(self):
        return " %s: %s, %s" % (str(self.identificacion), self.apellido, self.nombre)
    
    def __cmp__(self, persona):
        if isinstance(persona, Persona):
            if self.nombre == persona.nombre and self.apellido == persona.apellido:
                return True
            else:
                return False
        else: 
            return False

