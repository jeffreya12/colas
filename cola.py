import math
import random

class Cola:
	cantServ = 0
	pMiu = 0        #Ui :Tasa de atención de cada servidor por unidad de tiempo.
	pLambda = 0		#Ai :Tasa de llegadas por unidad de tiempo.
	servidores = [] #[estaLibre:bool]
	colaEspera = []
	y = 0

	def __init__(self,cantServ,pMiu,pLambda):
		self.cantServ = cantServ
		self.pMiu = pMiu
		self.pLambda = pLambda
		for e in range(cantServ):
			servidores.append()

	def generarLLegada():
		x = random.randrange(2)
		self.y = (log(x, 10)/pLambda)

	def getY()
		return self.y

	def toString(self):
		print("\n\nCantidad de servidores = " + str(self.cantServ) + "\n" + "Tasa media de atención = " + str(self.pMiu) + "\n" + "Tasa de Llegadas a la cola = " + str(self.pLambda))