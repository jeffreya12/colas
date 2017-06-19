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
        for e in range(cantServ):
            self.servidores.append([None])

    def pasarCliente(self,cliente):
        indice = 0
        for e in self.servidores:
            if (e == [None]):
                self.servidores[indice] = cliente
                cliente.servidorActual = indice + 1
                print("Empieza a ser atendido.")
                print(self.servidores)
                return
            indice +=1
        print("Servidores llenos espere en la cola.")
        self.colaEspera.append(cliente)

    def sacarCliente(self,IDCliente):
        indice = 0
        print("Servidores{}".format(self.servidores))
        for e in self.servidores:
            print("Cliente en servidor: " + str(e.ID))
            print(IDCliente)
            print(e.ID)
            if (e.ID == IDCliente):
                clnt = self.servidores.pop(indice)
                self.servidores.append([None])
                return clnt
            else:
                print("No hay cliente")
                return -5
            indice += 1

    def generarTiempoLLegada(self):
        x = random.uniform(0,1)
        while (x == 0.0):
            x = random.uniform(0,1)
        self.y += (-math.log(x)/self.pLambda)

    def obtenerTiempoServicio(self):
        yServicio = None
        x = random.uniform(0,1)
        while (x == 0.0):
            x = random.uniform(0,1)
        yServicio = (-math.log(x)/self.pMiu)
        return yServicio

    def agregarCliente(self,cliente):
        self.colaEspera.append(cliente)

    def toString(self):
        print("Cantidad de servidores = " + str(self.cantServ) + "\n" + "Tasa media de atención = " + str(self.pMiu) + "\n" + "Tasa de Llegadas a la cola = " + str(self.pLambda) +"\nServidores de la cola = " + str(self.servidores) )
        '''for e in self.servidores:
            if (e == True):
                print("Servidor Libre")
            else: 
                print("Servidor Ocupado")'''
        print("\n\n")