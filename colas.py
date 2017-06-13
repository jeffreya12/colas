# Lista con las lineas del archivo
lines = []
# Lista con cantidades de trabajo de cada cola
a = []
# Lista con cantidad de servidores de cada cola
s = []
# Lista con la tasa de atencion de cada cola
miu = []
# Lista con las probabilidades de pasar de una cola a otra
p = []
# Cantidad de colas
m = int

# Funcion que lee el archivo y lo asigna al la lista lines
def leerArchivo(nombreArchivo):
    file = open(nombreArchivo, 'r')
    global lines
    lines = file.readlines()
    
    print(lines)
    
# Funcion que inicializa los valores basicos necesarios
def init():
    global a, s, miu, p, m
    m = int(lines[0].split()[0])
    i = 1
    line = []
    while (i <= m):
        j = 0
        line = lines[i].split()
        while (j < 4):
            if (j == 0):
                a.append(float(line[j]))
            elif (j == 1):
                s.append(int(line[j]))
            elif (j == 2):
                miu.append(float(line[j]))
            else:
                p.append(list(map(float, line[j:])))
            j += 1
        i += 1
    

        
    
leerArchivo("prueba.txt")
init()

print(m)
print(a)
print(s)
print(miu)
print(p)