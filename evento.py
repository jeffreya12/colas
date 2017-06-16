class Evento:
	ID = 0
	tiempo = 0
	tipo = 0
	#Tipos de eventos
	#1. Entrada de un cliente a la cola n*, Empieza a ser atendido.
	

	def __init__(self,ID,tiempo,tipo):
		self.ID = ID
		self.tiempo = tiempo
		self.tipo = tipo

	def toString(self):
		print("\n\nID = " + str(self.ID) + "\n" + "Tiempo = " + str(self.tiempo) + "\n" + "Tipo = " + str(self.tipo))



def main(): 
	evn = Evento(1,30,45)
	evn.toString()
	#evn = Evento(1,30,45)

if __name__ == "__main__":
	main()

