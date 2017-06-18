class Evento:
    ID = 0
    tiempo = 0
    tipo = None
    procesado = None
    colaMadre = None
    IDCliente = None
    
    #Tipos de eventos----
    #1. Entrada de un cliente a la cola n. (1)
        #1.1. Espera en la cola.*          (-)
        #1.2. Empieza a ser atendido.*     (-)
        #1.3  Termina de ser atendido.     (2)
            #1.3.1  Pasa a la cola n.      (3)
        #1.4 Sale del sistema.             (4)

    #* : Puede empezar de primero.

    def __init__(self,ID,colaMadre,tiempo,tipo):
        self.ID = ID
        self.colaMadre = colaMadre
        self.tiempo = tiempo
        self.tipo = tipo
        self.procesado = False
        self.IDCliente = 0

    def toString(self):
        return("\n\nID = " + str(self.ID) + "\n" + "Pertenece a la cola = " + str(self.colaMadre) + "\n" + "Tiempo = " + str(self.tiempo) + "\n" + "Tipo = " + str(self.tipo) + "\nProcesado = " + str(self.procesado))

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

