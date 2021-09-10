class Pila:
    def __init__(self,listas):
        self._lista=listas
        
    @property
    def lista(self):
        return self._lista

    def busquedaLineal(self,buscado):
        pos=0
        enc=False
        lon=len(self.__lista)
        
        while pos<lon and enc==False:
            if self._lista[pos]["nombre"]==buscado:
                enc=True
            else:
                pos=pos+1
                
        if enc: return pos
        else: return -1
                
    def ordenar(self):
        for pos in range(0,len(self.__lista)):
            for sig in range(pos+1,len(self.__lista)):
                if self.__lista[pos]["nombre"]>self.__lista[sig]["nombre"]:
                    aux=self.lista[pos]
                    self.__lista[pos]=self.lista[sig]
                    self.__lista[sig]=aux
                    
    def busquedaBinaria(self,buscado):
        listaNotas.ordenar("asc")
        fin=len(self.lista) -1
        inicio=0
        enc=False
        
        while inicio <= fin and enc==False:
            medio=(inicio+fin)//2
            if self.lista[medio]["nombre"]==buscado:enc=True
            elif self.lista[medio]["nombre"]>buscado: fin=medio-1
            else: inicio=medio+1
        if enc: return medio
        else: return -1
    
notas=[
    {"nommbre":"Daniel","n1":20,"n2":40},
    {"nommbre":"Danny","n1":30,"n2":50},
    {"nommbre":"Dayana","n1":40,"n2":50},
    {"nommbre":"Romina","n1":50,"n2":40},
    {"nommbre":"Erick","n1":55,"n2":40},
    {"nommbre":"Yady","n1":60,"n2":40}
       
]

bus= Lista(notas)
posicion=bus.busquedaBinaria("Daniel")
if posicion !=-1:
    print(bus.lista[posicion])
else:
    print("Nombre no se encuentra en la lista")
bus.ordenar("asc")
print(bus.lista)
