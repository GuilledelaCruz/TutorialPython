class Corcho():
	def __init__(self, bodega):
		self.bodega = bodega

class Botella():
	def __init__(self, corcho):
		self.corcho = corcho
		self.descorchada = False

	def descorchar(self):
		self.descorchada = True

class Sacacorchos():
	def __init__(self):
		self.corchos = []
		self.corchado = False

	def descorchar(self, otella):
		if (not self.corchado):
			botella.descorchar()
			self.corchos.append(botella.corcho)
			self.corchado = True
			print "Recuerde quitar el corcho"
		else:
			print "Limpiar sacacorcho"

	def limpiar(self):
		self.corchado = False
		print "Sacacorchos limpio"

if __name__ == '__main__':

	corcho = Corcho("Bodega X")
	botella = Botella(corcho)
	print botella.corcho.bodega, ", ", str(botella.descorchada)

	sacacorchos = Sacacorchos()
	sacacorchos.descorchar(botella)
	sacacorchos.limpiar()

	for corcho in sacacorchos.corchos:
		print str(corcho.bodega)
