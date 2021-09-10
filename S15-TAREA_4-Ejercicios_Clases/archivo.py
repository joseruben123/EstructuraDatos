class Texto:
    
    def __init__(self, nombreArchivo):
        self.archivo=nombreArchivo
    
    def leer(self):
        with open("datos.txt", 'r', encoding="UTF-8") as file:
            for linea in file:
                print(linea[:-1])
                
    def escribir(self):
        nombres=['Fernanda', 'lola', 'esperanza', 'esther', 'lucas']
        with open(self.archivo, modo, encodinf="UTF-8") as file:
            for dato in datos:
                file.write(dato+"\n")
                
arch1=Texto("estudiantes.txt")
arch1.escribir(["Marco vera", "Ana Bohorquez", "Miguel Vera"],"a")
arch1.leer()