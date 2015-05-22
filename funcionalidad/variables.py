'''
Created on 22/5/2015

@author: guilledelacruz
'''
#prints
print 1 + 1
print "Hola mundo"

#variables
i = 1
d = 0.123123
h = "hola"
m = " mundo"
print h + m
print type(d)

#listas
lista = [1, 2, 3, "hola", "mundo", 0.1, 0.2, True, False]
l1 = lista[0]
l2 = lista[0:2]
l3 = lista[0:5:2]
l4 = lista[3:]
l5 = lista[:3]
l6 = lista[:]
lista[0:1] = [0, 1]

#tuplas
t = (1, 2, "cadena", True)
t2 = "cadena", False, 0.123

#diccionarios
diccionario1 = {"key1":"clave1",
                1:2}
print diccionario1[1]