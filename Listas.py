
class ReLista():
    def __init__(self,lista1 = ["Lady", 27, 97.3, True, "Mario", 57.3]):
        self.lista=lista1
        
    def mostrarLis(self):
        return self.lista
        
    def Mostrar1(self,num):
        print(self.lista[num])
        
    def agregar(self,ele):
        self.lista.append(ele)

    def viewlist(self): 
        print("::::::::Posicion [-1] ::::::::")  
        print(self.lista[-1])
        print("::::::::Posicion [0:3] ::::::::")
        print(self.lista[0:3])
        print("::::::::Posicion [:2] ::::::::")
        print(self.lista[:2])
        print("::::::::Posicion [3:] ::::::::")
        print(self.lista[3:])

    def insertar(self,pos,nom):
        self.lista.insert(pos, nom)
        

    def extender(self):
        self.lista.extend(["Alexa", 110, False])
        
    def indiceElem(self):
        return self.lista.index("Mario")

    def remover(self,ele):
        self.lista.remove(ele)

    def sacar(self):
        self.lista.pop()

        
   
        
        


