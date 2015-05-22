'''
Created on 22/5/2015

@author: guilledelacruz
'''
var1 = "guille"
var2 = 2
var3 = True

#if elif else
if var3 == True:
    var3 = False
else:
    var3 = True
    
if var2 == 1 :
    print 1
elif var2 == 2 :
    print 2
else:
    print 3

var4 = "de la Cruz" if (var1 == "guille") else "Dorado"
print var4

#while
while var2 < 10:
    var2+=1
    if var2 % 3:
        continue
    print "No modulo de 3"
print var2

#for

secuencia = [1, 2, 3, 4, 5]
for elemento in secuencia:
    print elemento
    