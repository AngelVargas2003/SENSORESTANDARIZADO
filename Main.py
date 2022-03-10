from Sensores import Sensores
class Principal():
    def __init__(self):
        self.Sensoresras=Sensores()

    def Menu(self):
            opc=''

            while(opc!='6'):
                print('1)DHT11')
                print('2)Ultrasonico')
                print('3)PIR')
                print('4)FC-22')
                print('5)Todos')
                print('6)Salir')
                opc=input("Escribe una opcion:")
                if(opc=='1'):
                    self.Sensoresras.sensorDHT11()
                elif(opc=='2'):
                    self.Sensores.sensorULTRASONICO()
                elif(opc=='3'):
                    self.Sensores.PIR()
                elif(opc=='4'):
                    self.Sensores.SFC22()
                elif(opc=='5'):
                    print('Sensor DHT11')
                    self.Sensores.sensorDHT11()
                    print('---------------------------')
                    print('Sensor Ultrasonico')
                    self.Sensores.sensorULTRASONICO()
                    print('----------------------------')
                    print('Sensor PIR')
                    self.Sensores.PIR()
                    print('-----------------------------')
                else:
                    print('Escribe una opcion valida\n')

main=Principal()
main.Menu()