from cmath import pi
from Sensoresv3 import Sensores
from MongoDB import MongoDB
class InterfaceSensor():
    def __init__(self):
        self.Sensorlista=Sensores()
        self.Sensorlista.toObjects()
        self.mongo=MongoDB()
        #self.Sensorlista.append(Sensores(condifuracion))
    def interfaceSensor(self):
        self.opc=''
        while(self.opc!='8'):
            print("1)Agregar sensor")
            print("2)Ver sensores")
            print("3)Buscar sensor")
            print("4)Modificar sensores")
            print("5)Eliminar sensor")
            print("6)Medir")
            print("7)Ver sensores de la BD")
            print("8)Salir")
            self.opc=input("Elige una opciion:\n")
            if(self.opc=="1"):
                nsensor=self.agregarSensor()
                self.Sensorlista.add(nsensor)
                self.Sensorlista.toJson(self.Sensorlista)
                dicc=self.Sensorlista.listaDiccionarios()
                self.mongo.insertar(dicc)
            elif(self.opc=='2'):
                self.verSensor()
            elif(self.opc=='3'):
                res=self.buscarSensor()
                print(res)
            elif(self.opc=='4'):
                self.verSensor()
                self.modificarSensor()
            elif(self.opc=='5'):
                self.verSensor()
                self.eliminarSensor()
            elif(self.opc=='6'):
                self.verSensor()
                id=input("Escribe el id del sensor:")
                res=self.Sensorlista.buscarSensor(id)
                self.Sensorlista.medicion(res)
            elif(self.opc=='7'):
                self.verSensores()
    def agregarSensor(self):
        sen=Sensores()
        sen.id=input("Escriba el id del sensor:")
        pinesnvo=self.addpines()
        sen.pin=pinesnvo
        sen.tipo=input("Escriba el tipo del sensor:")
        sen.clave=input("Escribe la clave del sensor:")
        return sen
    def addpines(self):
        self.pines=[]
        otro=''
        while otro!='NO':
            pin=int(input("Escriba el pin:"))
            self.pines.append(pin)
            otro=input("Desea agregar otro pin?(SI/NO):")
        return self.pines
    def buscarSensor(self):
        id=input("Escribe el id del sensor que quieres buscar:")
        self.Sensorlista.verifCode(id)
        if(self.Sensorlista.busq==True):
            res=self.Sensorlista.buscarSensor(id)
            return res
        else:
            return('No se encontro')
    def modificarSensor(self):
        id=input("Escribe el id del sensor que quieres modificar:")
        self.Sensorlista.verifCode(id)
        if(self.Sensorlista.busq==True):
            sen=Sensores()
            sen.id=input("Escriba el id del sensor:")
            pinesnvo=self.addpines()
            sen.pin=pinesnvo
            sen.tipo=input("Escriba el tipo del sensor:")
            sen.clave=input("Escriba la clave del sensor")
            self.Sensorlista.modificarSensor(id,sen)
        else:
            print("El sensor no existe")
    def eliminarSensor(self):
        id=input("Escribe el id del sensor que quieres eliminar:")
        self.Sensorlista.verifCode(id)
        if(self.Sensorlista.busq==True):
            self.Sensorlista.eliminarSensor(id)
        else:
            print('No se pudo eliminar')
    def verSensor(self,lista=None):
        print("\n\n"+"*"*30+"Datos de Sensores"+"*"*30)
        if(lista==None):
            mylista=self.Sensorlista
        i=0
        for p in mylista:
            print(str(p))
            i+=1
    def verSensores(self):
        res=self.mongo.getSensores()
        for sensor in res:
            print('------------------------------------')
            print("Id del sensor:"+str(sensor['id']))
            print("Tipo:"+str(sensor['Tipo']))
            print("Clave:"+str(sensor['Clave']))
            print("Pines:"+str(sensor['Pines']))
            print('------------------------------------')
menu=InterfaceSensor()
menu.interfaceSensor()