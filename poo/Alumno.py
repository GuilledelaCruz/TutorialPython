'''
Created on 22/5/2015

@author: guilledelacruz
'''
from Persona import Persona

class Alumno(Persona):
    "Clase que representa a un alumno de FIUBA."
    def __init__(self, identificacion, nombre, apellido, padron):
        "Constructor de AlumnoFIUBA"
        # llamamos al constructor de Persona
        Persona.__init__(self, identificacion, nombre, apellido)
        # agregamos el nuevo atributo
        self.padron = padron
        self.__variableprivada = True
        
    def __metodoprivado(self):
        return self.__variableprivada