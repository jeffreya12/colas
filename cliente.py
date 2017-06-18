class Cliente:
    ID      = None
    eventos = None #contiene los eventos relacionados. 

    def __init__(self,ID):
        self.ID = ID
        self.eventos = []

    #Los clientes tienen varios eventos relacionados.
    def agregarEvento(self,evento):
        evento.IDCliente = self.ID
        self.eventos.append(evento)

