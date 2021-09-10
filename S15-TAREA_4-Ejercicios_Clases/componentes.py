from typing import Collection
from helpers import gotoxy
import time
class Menu:
    def __init__(self,titulo=",opciones=[],col=6,fil=1"):
        self.titulo=titulo
        self.opciones=opciones
        self.col=col
        self.fil=fil
        
    def menu(self):
        gotoxy(self.col,self.fil);print(self.titulo)
        self.col-=5
        for opcion in self.opciones:
            self.fil+=1
            gotoxy(self.col,self.fil);print(opcion)
        gotoxy(self.col,self.fil)
        opc=input("Elija opcion[1..{}]:".format(len(self.opciones)))
        
class Valida:
    def solo_numeros(self,mensajeError,col,fil):
        while True:
            gotoxy(col,fil)
            valor=input()
            try:
                if int(valor)>0:
                    break
            except:
                gotoxy(col+10,fil);print(mensajeError)
                time.sleep(1)
                gotoxy(col+10,fil);print(" "*len(mensajeError))
        return valor
    
    def solo_letras(self,mensaje,mensajeError):
        pass
    
    def solo_decimales(self,mensajeError):
        pass
    
    def cedula():
        pass
    
class otra:
    pass

val
    
        
                
                