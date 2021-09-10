class lista:
    def __init__(self,tamanio=3):
        self.lista=[]
        self.longitud=0
        self.size=tamanio
        
    def append(self,dato):
        if self.longitud<self.size:
            self.lsita +=[dato]
            self.longitud+=1
        else:
            print("Lista esta llena")
    
    def obtener(self,pos):
        self.mostrar()
        if pos <0 or pos >=self.longitud:
            return None
        else:
            return self.lista[pos]
        
    def obtenerEliminado(self,pos):
        if pos <0 or pos >=self.longitud:
            return None
        else:
            eliminado=self.lista[pos]
            listaAux=[]
            for ind in range(pos):
                listaAux+=[self.lista[ind]]
            for indice in range(pos+1,self.longitud):
                listaAux+=[self.lista[indice]]
            self.longitud-=1
            self.lista=listaAux
               
            return (self.lista,eliminado)
    
    def mostrar(self):
        print("{:2}{:9} {}".format("","lista","posicion"))
        for pos,ele in enumerate(self.lista):
            print("[{:10}] {:10}".format(ele,pos))
            
lista1=lista()
lista1.append("Daniel")
lista1.append(52)
lista1.append(True)
lista1.mostrar()
posicion=int(input("Ingrese posicion para optner el elemento: "))
resp=lista1.obtener(posicion)
if resp==None:
    print("Posicion no valida, verifique la lista")       
else:
    print("EL ELEMENTO DE LA POSICION: {} es:{}".format(posicion,resp))