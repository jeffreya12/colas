import sys
import numpy as np
import random
import evento

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
				servidores.append(float(line[j]))
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
	

def calcularSalida():
	
	global lambdas, pSalir
	
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
	for i in range(len(lambdas)):
		print("Lambda ", i + 1, ": ", lambdas[i,0])

	for e in probabilidades:
		for i in e:
			valor += float(i)

	for c in probabilidades:
		pSalir.append(1 - sum(c))
		
	print("Probabilidad de salir q:i:               ",pSalir)
	
	# print(random.expovariate(lambdas[0, 0]))
	
	# print(randomExponencial(clientes[0]))

# Funcion que calcula el numero aleatorio exponencialmente distribuido
def randomExponencial(lambd):
	return -(np.log(random.random())) / lambd

def initSimulacion(int eventos):
	
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
