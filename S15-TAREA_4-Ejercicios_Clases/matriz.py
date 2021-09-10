import os

class Matriz:
    def __init__(self,matriz,fila,col):
        self.matriz=matriz
        self.fila=fila
        self.col=col
        
    def ingresar(self,dato):
        self.matriz=[]
        for fila in range(self.fila):
            columnas=[]
            os.system("cls")
            for col in range(self.col):
                valor=input("Fila[{}] Col[{}]: ".format(fila))
                columnas.append(valor)
            self.matriz.append(columnas)
    
    def presentar(self):
        print("_______")
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                print("[{}]".format(self.matriz[fila][col]),end="")
            print()
        print("_______")
            
    def buscar(self,valor):
        enc={}
        for fila in range(len(self.matriz)):
            for col in range(len(self.matriz[fila])):
                if self.matriz[fila][col]==valor:
                    enc["fila"]=fila
                    enc["col"]=col
                    break
            if enc: break
        return enc
            
    def buscarw(self,valor):
        enc={}
        fila=0
        band=True
        while fila<len(self.matriz) and band:
            col=0
            for fila in range(len(self.matriz)):
                for col in range(len(self.matriz[fila])):
                    if self.matriz[fila][col]==valor:
                        enc["fila"]=fila
                        enc["col"]=col
                        band=False
                    else: col+=1
                fila+=1
            return enc

    def sumar(self,matriz2):
        self.matrizSuma=[]
        for fila in range(self.fila):
            columnas=[]
            os.system("cls")
            for col in range(self.col):
                valor=self.matriz[fila][col]+matriz2[fila][col]
                columnas.append(valor)
            self.matrizSuma.append(columnas)
        return matrizSuma
            
#numeros=[[10,20,30],[60,80,40],[25,35,55]]
numeros=[]
#filas
#col=numeros[0]
#print(numero[0],numero[0][1])
mat1=Matriz([],3,3)
mat2=Matriz(numeros,3,3)
mat1.ingresar()
mat1.presentar()
mat2.ingresar()
mat2.presentar()
mat1.matriz=mat1.sumar(mat2.matriz)

mat1.presentar()

# if resp: print("El valor se encuentra en las siguientes coordenadas", resp)
# else: print("no existe el valor de la matriz")