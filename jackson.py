import sys
import numpy as np
import random
import math
from evento import Evento
from cola import Cola
from cliente import Cliente
from operator import itemgetter, attrgetter

lines             = []
clientes          = []     #a:j
servidores        = []     #s:i
miu               = []     #u:i
probabilidades    = []     #P:ij
lambdas           = []     #lamba de cada col ; se obtienen con sistema de ecuaciones
colas             = int    #m
pSalir            = []     #probabilidades de salir
eventoCount       = 0      #Contador de la cantidad de eventos.
clienteCount      = 0      #Contador de clientes.
instalaciones     = []     #Contiene las colas reales (clase Cola).
colaPrioridad     = []     #Contiene eventos de la simulación.
eventosProcesados = []     #Datos de los eventos.
clntsSistema      = []     #Clientes que se van generando y entran al sistema.
clientesViejos    = []


# Funcion que lee el archivo y lo asigna a la lista lines
def leerArchivo(nombreArchivo):
    file = open(nombreArchivo, 'r')
    global lines
    lines = file.readlines()
    print("\n\r\n")
    #print(lines)

# Funcion que inicializa los valores basicos necesarios
def init():
    random.seed()
    global clientes, servidores, miu, probabilidades, colas
    colas = int(lines[0].split()[0])

    i = 1
    line = []
    while (i <= colas):
        j = 0
        line = lines[i].split()
        while (j < 4):
            if (j == 0):
                servidores.append(int(line[j]))
            elif (j == 1):
                miu.append(float(line[j]))
            elif (j == 2):
                clientes.append(int(line[j]))
            else:
                probabilidades.append([float(item) for item in line[j:]])
            j += 1
        i += 1

    print("Cantidad de colas:                       ",colas)
    print("Servidores s:j:                          ",servidores)
    print("Ts.. atencion por unidad de tiempo u:j   ",miu)
    print("Trabajos/Clientes a:j:                   ",clientes)
    print("Probabilidades P:ij:                     ",probabilidades)


def calcularP0(lambd, miu, cantServidores):
    sumatoria = 0
    for i in range(0, cantServidores):
        sumatoria+= (((lambd/miu) ** i)/math.factorial(i))
    deno = ((lambd/miu) ** cantServidores)/math.factorial(cantServidores)
    deno = deno*1/(1-lambd/(cantServidores*miu))
    deno = sumatoria + deno
    p0 = 1/deno
    return p0

def calcularLongitudCola(lambd, miu, cantServidores, p0):
    p = (lambd/(cantServidores*miu))
    num = p0*(lambd/miu)**cantServidores*p
    deno = math.factorial(cantServidores)*(1-p)**2
    return num/deno

def calcularLongitudSistema(lambd, miu, Lq):
    L = Lq + (lambd/miu)
    return L

def calcularTiempoEnCola(lamd, Lq):
    Wq = Lq/lamd
    return Wq

def calcularTiempoEnSistema(miu, Wq):
    W = Wq + 1/miu
    return W

def calcularSalida():

    global lambdas, pSalir, miu, servidores

    valor = 0

    b = np.matrix(clientes)
    b = b.transpose()
    b = -b
    a = np.matrix(probabilidades)

    #Coloca en diagonal -1 en la matriz de a
    for i in range(len(a)):
        a[i,i] = -1

    #Resuelve la ecuacion lineal para obtener valores de lambda
    lambdas = np.linalg.solve(a,b)


    #Obtiene los p0
    p0 = []
    for i in range(len(lambdas)):
        p0+= [calcularP0(lambdas[i,0], miu[i], servidores[i])]

    #Calcula los Lq de cada servicio
    Lq = []
    for i in range(len(lambdas)):
        Lq += [calcularLongitudCola(lambdas[i,0], miu[i], servidores[i], p0[i])]

    #Calcula los L de cada servicio
    L = []
    for i in range(len(Lq)):
        L+= [calcularLongitudSistema(lambdas[i,0], miu[i], Lq[i])]

    #Calcula los Wq de cada servicio
    Wq = []
    for i in range(len(Lq)):
        Wq+= [calcularTiempoEnCola(lambdas[i,0], Lq[i])]

    #Calcula los Wq de cada servicio
    W = []
    for i in range(len(Wq)):
        W+= [calcularTiempoEnSistema(miu[i], Wq[i])]

    #Prints de los datos obtenidos segun teoria

    print("\r\n\r\n\r\n")
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    print("-Resultados según la teoría de redes de Jackson:-")
    print("-------------------------------------------------")
    print("-------------------------------------------------\r\n")

    for i in range(len(lambdas)):
        print("---------------Resultados de cola ", i + 1, "---------------")
        print("Lambda ", i + 1, ": ", lambdas[i,0])
        #print("Lq     ", i + 1, ": ", Lq[i])
        print("Lq      ", i + 1, ": ", L[i])
        print("Wq     ", i + 1, ": ", Wq[i])
        #print("W      ", i + 1, ": ", W[i])

    for e in probabilidades:
        for i in e:
            valor += float(i)

    for c in probabilidades:
        pSalir.append(1 - sum(c))

    print("\nW:                                       ", sum(L)/sum(clientes))
    print("L:                                       ", sum(L))
    print("\nProbabilidad de salir q:i:               ",pSalir)
    
    print("\r\n\r\n\r\n")
    print("-------------------------------------------------")
    print("-------------------------------------------------")
    print("-Resultados según la simulación:-")
    print("-------------------------------------------------")
    print("-------------------------------------------------\r\n")

    for i in range(len(lambdas)):
        print("---------------Resultados de cola ", i + 1, "---------------")
        print("Lambda ", i + 1, ": ", lambdas[i,0])
        #print("Lq     ", i + 1, ": ", Lq[i])
        print("Lq      ", i + 1, ": ", L[i])
        print("Wq     ", i + 1, ": ", Wq[i])
        #print("W      ", i + 1, ": ", W[i])

    for e in probabilidades:
        for i in e:
            valor += float(i)

    for c in probabilidades:
        pSalir.append(1 - sum(c))

    print("\nW:                                       ", sum(L)/sum(clientes))
    print("L:                                       ", sum(L))
    print("\nProbabilidad de salir q:i:               ",pSalir)

# Funcion que calcula el numero aleatorio exponencialmente distribuido
def randomExponencial(lambd):
    return -(np.log(random.random())) / lambd

def initSimulacion(tiempo): #tiempo en unidades.
    global eventoCount 
    global clienteCount
    global clntsSistema
    global instalaciones
    global servidores
    global clientes
    global miu
    colaCount = 0

    print("\nTiempo que va a correr la simulación: " + str(tiempo) + "\n")
    #Creamos las instalaciones del sistema
    for e in range(colas):
        ins = Cola(servidores[e],miu[e],clientes[e])
        instalaciones.append(ins)

    #Generar Eventos
    #    Para el  tiempo t = 0 deben generar el evento de 
    #    "entrada de una persona desde el exterior a la cola"
    for c in instalaciones:
        colaCount +=1
        eventoCount += 1
        #ID del evento,Cola del evento, tiempo = 0, tipo Evento 1-3
        evn = Evento(eventoCount,colaCount,0,1)
        colaPrioridad.append(evn)
        ordernarColaPrioridad()
        #generar tiempos de llegadas totales del exterior del sistema para cada cola.
    ordernarColaPrioridad()
    cFin = 0
    while( len(colaPrioridad) > 0 and (cFin < tiempo*40)):
        event = colaPrioridad[0]
        largoCola = len(instalaciones[event.colaMadre-1].colaEspera)
        event.procesar() #Cambia el estado de procesado de False a True del evento.
        #1: Llegada a la cola
        if(event.tipo == 1):
            #print("Caso 1:")
            #Verificar que el evento pertenezca a un cliente, sino se crea un cliente nuevo y se le asigna el evento.
            clnt = Cliente(clienteCount)
            clienteCount += 1
            clnt.agregarEvento(event)
            clntsSistema.append(clnt)
            #print(clntsSistema)
            #Verificar si hay personas en la cola.
            if(largoCola > 0):
                #Debe de esperar en la cola.
                instalaciones[event.colaMadre-1].agregarCliente(clntsSistema[0])
                del clntsSistema[0]
                print("{} : Entra cliente en la cola {}, espera en la cola".format(event.tiempo,event.colaMadre) )
            else:
                #Pasar cliente a servidor para ser atendido.
                eventoCount += 1
                tiempoServicio = instalaciones[event.colaMadre-1].obtenerTiempoServicio()
                #ID del evento,Cola del evento, tiempo = 0, tipo Evento 1-4
                eve = Evento(eventoCount,event.colaMadre,tiempoServicio,2)
                clntsSistema[0].agregarEvento(eve) #Asigna el evento con el cliente.
                colaPrioridad.append(eve)
                ordernarColaPrioridad()
                print( "{} : Entra cliente en la cola {}, empieza a ser atendido".format(event.tiempo,event.colaMadre) )
                #Pasamos el cliente al servidor y lo sacamos de la lista de clientes del sistema.
                instalaciones[event.colaMadre-1].pasarCliente(clntsSistema[0])
                del clntsSistema[0]
            #Generar siguiente llamada desde el exterior.
            cola = instalaciones[event.colaMadre-1]
            cola.generarTiempoLLegada()
            #Generar evento de nueva llegada, si no supera el límite de tiempo.
            if(cola.y <= tiempo):
                #print("Crea llegada nueva")
                eventoCount += 1
                nEvn = Evento(eventoCount,event.colaMadre,cola.y,1)
                #print(nEvn.IDCliente)
                colaPrioridad.append(nEvn)
                ordernarColaPrioridad()

        #2: Termina de ser atendido.
        #Aquí se puede procesar (generar bitácora) los eventos del cliente una vez que sale de la cola.
        elif(event.tipo == 2):
            #print("Caso 2:")
            #Sacar Cliente del servidor.
            clnt = instalaciones[event.colaMadre-1].sacarCliente(event.IDCliente)
            clientesViejos.append(clnt)
            if(clnt==-5):
                for c in instalaciones:
                    for cliente in c.servidores:
                        if (cliente.ID == event.IDCliente):
                            clnt = cliente
            #Decidir cola a nueva a la que se debe ir.
            colaSig = colaSiguiente(event.colaMadre)
            #Averiguar si sale del sistema o pasa a cola nueva.
            if (colaSig == 0):
                print( "{} : El Cliente termina de ser atendido en la cola {}, sale del sistema.".format(clnt.obtenerTiempoSalida(),event.colaMadre) )
            else: 
                print("{} : Cliente termina de ser atendido en la cola {}, pasa a la cola {}".format(clnt.obtenerTiempoSalida(),event.colaMadre,colaSig))
                eventoCount += 1
                #ID del evento,Cola del evento, tiempo = 0, tipo Evento 1-4
                eve = Evento(eventoCount,colaSig,clnt.obtenerTiempoSalida(),3)
                colaPrioridad.append(eve)
                ordernarColaPrioridad()
                clnt.agregarEvento(eve)
                instalaciones[colaSig-1].agregarCliente(clnt)
                if(largoCola > 0):
                    #Pasar siguiente cliente de la cola al servidor.Generar Evento de atención.
                    eventoCount += 1
                    tiempoServicio = instalaciones[event.colaMadre-1].obtenerTiempoServicio()
                    #ID del evento,Cola del evento, tiempo = 0, tipo Evento 1-4
                    eve = Evento(eventoCount,event.colaMadre,tiempoServicio,2)
                    colaPrioridad.append(eve)
                    ordernarColaPrioridad()
                    instalaciones[event.colaMadre-1].colaEspera[0].agregarEvento(eve)#Asignar evento con cliente.
                    nClnt = instalaciones[event.colaMadre-1].colaEspera[0]
                    instalaciones[event.colaMadre-1].pasarCliente(nClnt)        
        #3: Termina de ser atendido y pasa a la cola n.
        elif(event.tipo == 3):
            #print("Caso 3:")
            if(largoCola > 0):
                #Debe de esperar en la cola.
                print("{} : Entra cliente en la cola {}, espera en la cola".format(event.tiempo,event.colaMadre) )
            else:
                #Pasar cliente a servidor para ser atendido.
                eventoCount += 1
                tiempoServicio = instalaciones[event.colaMadre-1].obtenerTiempoServicio()
                #ID del evento,Cola del evento, tiempo = 0, tipo Evento 1-4
                eve = Evento(eventoCount,event.colaMadre,tiempoServicio,2)
                cln = instalaciones[colaSig-1].colaEspera[0]
                instalaciones[colaSig-1].colaEspera[0].agregarEvento(eve) #Asigna el evento con el cliente.
                colaPrioridad.append(eve)
                ordernarColaPrioridad()
                print( "{} : Entra cliente en la cola {}, empieza a ser atendido".format(event.tiempo,event.colaMadre) )
                #Pasamos el cliente al servidor y lo sacamos de la lista de clientes del sistema.
                instalaciones[event.colaMadre-1].pasarCliente(cln)
            #Generar siguiente llamada desde el exterior.
            cola = instalaciones[event.colaMadre-1]
            cola.generarTiempoLLegada()
            #Generar evento de nueva llegada, si no supera el límite de tiempo.
            if(cola.y <= tiempo):
                #print("Crea llegada nueva")
                eventoCount += 1
                nEvn = Evento(eventoCount,event.colaMadre,cola.y,1)
                #print(nEvn.IDCliente)
                colaPrioridad.append(nEvn)
                ordernarColaPrioridad()
        else:
            print("Caso X: Inexistente")

        #print("Borra de cola de prioridad")
        event = None
        eventosProcesados.append(colaPrioridad.pop(0))
        cFin+=1

     
def colaSiguiente(numCola):
    global probabilidades
    x = random.uniform(0,1)
    dif = []
    for e in probabilidades[numCola-1]:
        dif.append(abs(e-x))
    indexMin = dif.index(min(dif))
    if(probabilidades[indexMin] == 0.0):
        return 0
    nCola = indexMin + 1
    return nCola 

def calcularStrTiempo(tiempo):
    sttr = ""
    return sttr  

def ordernarColaPrioridad():
    global colaPrioridad
    colaPrioridad = sorted(colaPrioridad, key=attrgetter('tiempo', 'ID'))




def main(): 
    print("\r\n\r\n\r\n")
    print("--------------------------\n--------------------------")
    print("-Ordenando Datos:-")
    print("--------------------------\n--------------------------\n")   
    leerArchivo(sys.argv[1])
    init()
    calcularSalida()
    tiempoLimite = int(sys.argv[2])
    initSimulacion(tiempoLimite)
    print("\r\n")

if __name__ == "__main__":
    main()

#Para correr archivo
#python jackson.py prueba.txt 300
