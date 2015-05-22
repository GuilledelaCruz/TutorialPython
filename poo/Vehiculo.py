'''
Created on 22/5/2015

@author: guilledelacruz
'''

class Vehiculo:
    def __init__(self, matricula, dueno):
        self.matricula = matricula
        self.dueno = dueno
        
    def __str__(self):
        return "Matricula %s, Dueno %s" % (self.matricula, self.dueno)
    
    def matricula(self):
        print self.matricula