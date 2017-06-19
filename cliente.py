class Cliente:
    ID      = None
    eventos = None #contiene los eventos relacionados.
    servidorActual = None

    def __init__(self,ID):
        self.ID = ID
        self.eventos = []
        self.servidorActual = 0

    #Los clientes tienen varios eventos relacionados.
    def agregarEvento(self,evento):
        evento.IDCliente = self.ID
        self.eventos.append(evento)

    def obtenerTiempoSalida(self):
        tiempo = 0
        for e in self.eventos:
            tiempo += e.tiempo
        return tiempo

    def __repr__(self):
        return("ID: "+ str(self.ID))
