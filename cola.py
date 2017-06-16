import math
import random

class Cola:
    cantServ = 0
    pMiu = 0        #Ui :Tasa de atención de cada servidor por unidad de tiempo.
    pLambda = 0     #Ai :Tasa de llegadas por unidad de tiempo.
    servidores = None #[estaLibre:bool]
    colaEspera = None #La cola de espera con los clientes.
    y = 0

    def __init__(self,cantServ,pMiu,pLambda):
        self.cantServ = cantServ
        self.pMiu = pMiu
        self.pLambda = pLambda
        self.servidores = []
        self.colaEspera = []
        ite = 0
        while(ite < self.cantServ):
            self.servidores.append(True)
            ite+=1

    def generarLLegada():
        x = random.randrange(2)
        self.y = (log(x, 10)/self.pLambda)

    def toString(self):
        print("Cantidad de servidores = " + str(self.cantServ) + "\n" + "Tasa media de atención = " + str(self.pMiu) + "\n" + "Tasa de Llegadas a la cola = " + str(self.pLambda) +"\nServidores de la cola = " + str(self.servidores) )
        '''for e in self.servidores:
            if (e == True):
                print("Servidor Libre")
            else: 
                print("Servidor Ocupado")'''
        print("\n\n")