'''
Created on 22/5/2015

@author: guilledelacruz
'''
from Vehiculo import Vehiculo

class Coche(Vehiculo):
    """Clase Coche"""
    def __init__(self, litrosGasolina, pasajeros, matricula, dueno):
        Vehiculo.__init__(self, matricula, dueno)
        self.litrosGasolina = litrosGasolina
        self.pasajeros = pasajeros
        
    def conductorSolo(self):
        if self.pasajeros > 0:
            print "Conductor acompanado"
            return False
        else:
            print "Conductor solo"
            return True
            
    def gasolinaRestante(self):
        return self.litrosGasolina
    
    def conducir(self, kilometro):
        if self.litrosGasolina > 0:
            self.litrosGasolina = self.litrosGasolina - kilometro
            if self.litrosGasolina <= 0:
                print "Te has quedado sin gasolina"
                self.litrosGasolina = 0
            return True
        else:
            print "No hay gasolina"
            return False
        
    def litrosGasolina(self):
        return self.litrosGasolina
    
    def echaGasolina(self, litros):
        print "Repostando"
        self.litrosGasolina = self.litrosGasolina + litros