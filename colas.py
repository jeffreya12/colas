lines = []
a = []
s = []
miu = []
p = []
m = int

def leerArchivo(nombreArchivo):
    file = open(nombreArchivo, 'r')
    global lines
    lines = file.readlines()
    
    print(lines)
    
def init():
    m = int(lines[0].split()[0])
    #print(m)
    i = 1
    line = []
    while (i <= m):
        j = 0
        line = lines[i].split()
        while (j < 4):
            if (j == 0):
                a.append(line[j])
            elif (j == 1):
                s.append(line[j])
            elif (j == 2):
                miu.append(line[j])
            else:
                p.append(line[j:])
            j += 1
        i += 1
    
    print(m)
    print(a)
    print(s)
    print(miu)
    print(p)
        
    
leerArchivo("prueba.txt")
init()