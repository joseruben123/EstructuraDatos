class Calculadora:
    def __init__(self,numero1, numero2):
        self.num1=numero1
        self.num2=numero2
        
    def suma(self):
        return self.num1+self.num2
    
    def resta(self):
        pass
    
    def multiplicacion(self):
        multi=self.num1*self.num2
        print("{}*{}={}".format(self.num1,self.num2,multi))
        
    def division(self):
        pass

class CalEstandar(Calculadora):
    def __init__(self,numero1,numero2):
        super().__init__(numero1,numero2)
        
    def multiplicacion(self):
        return self.num1*self.num2
    
    def exponente(self):
        pass
    
    def ValorAbsoluto(self,numero):
        if numero<0:
            numero=numero*-1
        return numero
    
class CalCientifica(Calculadora):
    def __init__(self,numero1, numero2):
        super().__init__(numero1,numero2)
        
    def circunferencia(radio):
        print("circunferencia")
        
def mensaje(men):
    print(men)
             
""" cal=CalEstandar(4,8)
print(cal.suma())
print(cal.multiplicacion())
print(cal.ValorAbsoluto(-5))
centi=CalCientifica(3,2)
centi.circunferencia()
print(centi.suma()) """