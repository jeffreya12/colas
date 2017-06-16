import sys
import numpy as np
import random
import evento
import math

lines = []
clientes = []                #a:j
servidores = []              #s:i
miu = []                     #u:i
probabilidades = []          #P:ij
lambdas = []                 #lamba de cada col
colas = int                  #m
pSalir = []             	 #probabilidades de salir
colaPrioridad = []			 #Contiene eventos de la simulación.

# Funcion que lee el archivo y lo asigna al la lista lines
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
		Lq+= [calcularLongitudCola(lambdas[i,0], miu[i], servidores[i], p0[i])]

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
	print("------------------------------------------------")
	print("------------------------------------------------")
	print("-Resultados según la teoría de redes de Jackson:-")
	print("------------------------------------------------")
	print("------------------------------------------------")

	for i in range(len(lambdas)):
		print("---------------Resultados de cola ", i + 1, "---------------")
		print("Lambda ", i + 1, ": ", lambdas[i,0])
		print("Lq ", i + 1, ": ", Lq[i])
		print("L ", i + 1, ": ", L[i])
		print("Wq ", i + 1, ": ", Wq[i])
		print("W ", i + 1, ": ", W[i])

	for e in probabilidades:
		for i in e:
			valor += float(i)

	for c in probabilidades:
		pSalir.append(1 - sum(c))

	print("Probabilidad de salir q:i:               ",pSalir)

	# print(random.expovariate(lambdas[0, 0]))

	# print(randomExponencial(clientes[0]))


	# print(random.expovariate(lambdas[0, 0]))

	# print(randomExponencial(clientes[0]))

# Funcion que calcula el numero aleatorio exponencialmente distribuido
def randomExponencial(lambd):
	return -(np.log(random.random())) / lambd


def main():
	print("\r\n\r\n\r\n")
	print("--------------------------\n--------------------------")
	print("-Ordenando Datos:-")
	print("--------------------------\n--------------------------\n")
	leerArchivo(sys.argv[1])
	init()
	calcularSalida()
	print("\r\n\r\n\r\n")


if __name__ == "__main__":
	main()

#Para correr archivo
#python colas.py prueba.txt
