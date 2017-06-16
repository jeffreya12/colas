class Evento:
	ID = 0
	tiempo = 0
	tipo = 0
	procesado = None
	
	#Tipos de eventos----
	#1. Entrada de un cliente a la cola n.
		#1.1. Espera en la cola.*
		#1.2. Empieza a ser atendido.*
		#1.3  Termina de ser atendido.
			#1.3.1  Pasa a la cola n.
		#1.4 Sale del sistema.

	#* : Puede empezar de primero.

	def __init__(self,ID,tiempo,tipo):
		self.ID = ID
		self.tiempo = tiempo
		self.tipo = tipo
		self.procesado = False

	def toString(self):
		print("\n\nID = " + str(self.ID) + "\n" + "Tiempo = " + str(self.tiempo) + "\n" + "Tipo = " + str(self.tipo))

	def procesar(self):
		self.procesado = True

''' 
def main(): 
	evn = Evento(1,30,45)
	evn.toString()
	#evn = Evento(1,30,45)

if __name__ == "__main__":
	main()
'''

