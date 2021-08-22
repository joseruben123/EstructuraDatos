import os
 
def menu():
	"""
	Función que limpia la pantalla y muestra nuevamente el menu
	"""
	os.system('clear')
	print ("Selecciona una opción")
	print ("\t1 - Pila")
	print ("\t2 - Cola")
	print ("\t9 - salir")
 



class Pila:
    def __init__(self, tamanio=1):
        self.lista=[]
        self.size=tamanio
        self.top=0
        
    def push(self, dato):
        if self.top < self.size:
            self.lista += self.lista+[dato]
            self.top+=1
        else:
            print("La lista esta llena")
            
    def pop(self):
        if self.empty():
            return None
        else:
            top=self.lista[-1]
            self.lista=self.lista[:self.top]
            self.top-=1
            return top
        
    def show(self):
        for top in range(self.top-1,-1,-1):
            print("[{}]".format(self.lista[top]))
            
    def longitud(self):
        return self.top
    
    def show(self):
        for top in range(self.top-1,-1,-1):
            print("[{}]".format(self.lista[top]))
        
    def empty(self):
        if self.top ==0:
            return True
        else:
            return False
            
pila1=Pila(3)
pila1.push(8)
pila1.push(10)
pila1.push(12)
pila1.push(4)
pila1.show()
print(pila1.longitud())

class Cola:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def agregar(self, item):
        self.items.insert(0,item)

    def avanzar(self):
        return self.items.pop()

    def tamano(self):
        return len(self.items)
c=Cola()

c.agregar(4)
c.agregar(12)
c.agregar(True)
print(c.tamano())

while True:
	
	menu()
 
	
	opcionMenu = input("inserta la opcion >> ")
 
	if opcionMenu=="1":	
        Pila()   
	elif opcionMenu=="2":
		Cola()
	elif opcionMenu=="9":
		break
	else:
		print ("")
		input   ("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")