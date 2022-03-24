import json
import os.path
#import RPi.GPIO as GPIO
#import Adafruit_DHT
#import time
#import time
class Sensores:
    def __init__(self,id='',pin='',tipo='',clave=''):
        self.id=id
        self.pin=pin
        self.tipo=tipo
        self.clave=clave
        self.__idx__=0

    #def initSensor(self):
      #  if(self.tipo=='US'):
            


    def add(self,sensor):
        self.lista.append(sensor)

    def len(self):
        return len(self.lista)

    def getList(self):
        return self.lista

    def tojson(self,listajson):
        file=open("sensores.json","w")
        file=json.dump(listajson, file)

    def medicion(self,sensor):
        if(sensor.tipo=='US'):
            self.sensorULTRASONICO(sensor)
        elif(sensor.tipo=='TH'):
            self.sensorDHT11(sensor)
    
    def getDiccionario(self):
        return{
            "id":self.id,
            "Tipo":self.tipo,
            "Pines":self.pin,
            "Clave":self.clave
        }
    def toJson(self,listaSensores):		
        file = open("sensores.json", "w")
        file = json.dump([ob.__dict__ for ob in listaSensores], file,indent=4)
    
    def toObjects(self):
        lista=list()
        data=self.getDataJson()
        for x in data:
            lista.append(Sensores(id=x['id'],tipo=x['tipo'],pin=x["pin"],clave=x["clave"]))
        self.lista=lista
    def getDataJson(self):		
        data=[]
        if(os.path.isfile('sensores.json')):
            file = open('sensores.json', "r")
            data=json.loads(file.read())
        return data 
    
    def listaDiccionarios(self):
        for x in self.lista:
            diccionario=x.getDiccionario()
        return diccionario

    def addDicc(self):
        listaDiccionario=list()
        for i in self.lista:
            listaDiccionario.append(i.getDiccionario())
            print(i.getDiccionario())
           
        return listaDiccionario

    def getSensor(self):
        sensores=Sensores()
        for x in sensores.getList():
            print(x)

    def __str__(self):
        return "id: "+str(self.id)+ ' \t\t'+'Tipo: '+str(self.tipo)+' \t\t'+"Pines:"+str(self.pin)+'\t\t'+"Clave:"+str(self.clave)

    def verifCode(self,code):
        self.busq=False
        for index,sensor in enumerate(self.lista):
            if sensor.id==code:
                self.busq=True
        
    def modificarSensor(self,id,sensor):
        for index,producto in enumerate(self.lista):
            if producto.id==id:
                self.lista.pop(index)
                self.lista.insert(index,sensor)
                break
            else:
                index=-1 

    def eliminarSensor(self,id):
        for index,sensor in enumerate(self.lista):
            if sensor.id==id:
                self.lista.pop(index)
                print('Se ha eliminado de manera correcta el sensor')

    def buscarSensor(self,id):
        for index,sensor in enumerate(self.lista):
            if(sensor.id==id):
                return self.lista[index]
    def __next__(self):
        if self.__idx__<len(self.lista):
            x =self.lista[self.__idx__]
            self.__idx__+=1 
            return x
        else:
            raise StopIteration 
    def __iter__(self):
        self.__idx__ = 0
        return self
    
    def sensorULTRASONICO(self,sensor):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensor.pin[0],GPIO.OUT)
        GPIO.setup(sensor.pin[1],GPIO.IN)
        GPIO.output(sensor.pin[0], True)
        time.sleep(1)
        GPIO.output(sensor.pin[0], False)
        while GPIO.input(self.pin[1]) == False:
            start = time.time()
        while GPIO.input(self.pin[1]) == True:
            end = time.time()
        sig_time = end-start
         #Centimetros:
        distance = sig_time / 0.000058
        #pulgadas:
        #distance = sig_time / 0.000148
        print('Distance: {} centimetros'.format(distance))
        GPIO.cleanup()
        return distance

    def sensorDHT11(self,sensores):
        print('Inicia')
        sensor = Adafruit_DHT.DHT11 #Cambia por DHT22 y si usas dicho sensor
        pin = sensores.pin[0] #Pin en la raspberry donde conectamos el sensor
        print('Leyendo')
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        print ('Humedad: ' , humedad)
        print ('Temperatura: ' , temperatura)

        time.sleep(0.25) #Cada segundo se evalúa el sensor
        
    