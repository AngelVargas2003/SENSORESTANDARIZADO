from operator import contains
import Adafruit_DHT
from cmath import pi
import imp
import time
from tkinter import Menu
class main():
    def sensorDHT11(self):
        import Adafruit_DHT
        import time
        print('Inicia')
        sensor = Adafruit_DHT.DHT11 #Cambia por DHT22 y si usas dicho sensor
        pin = 18 #Pin en la raspberry donde conectamos el sensor
        print('Leyendo')
        humedad, temperatura = Adafruit_DHT.read_retry(sensor, pin)
        print ('Humedad: ' , humedad)
        print ('Temperatura: ' , temperatura)

        time.sleep(0.25) #Cada segundo se evalúa el sensor

    def sensorULTRASONICO(self):
        import RPi.GPIO as GPIO
        import time
        contador=0
        GPIO.setmode(GPIO.BCM)

        TRIG = 25
        ECHO = 24

        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)

        GPIO.output(TRIG, True)
        time.sleep(1)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == False:
            start = time.time()

        while GPIO.input(ECHO) == True:
            end = time.time()
        sig_time = end-start
         #Centimetros:
        distance = sig_time / 0.000058

        #pulgadas:
        #distance = sig_time / 0.000148

        print('Distance: {} centimetros'.format(distance))

        GPIO.cleanup()
        contador+=1
    def PIR(self):
        from gpiozero import MotionSensor
        #LED
        import RPi.GPIO as GPIO
        import time

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(23, GPIO.OUT)
        #LED

        pir = MotionSensor(21)
        pir.wait_for_motion()
        print("Movimiento detectado")
        GPIO.output(23, True)
        pir.wait_for_no_motion()
        GPIO.output(23, False)
    def SFC22(self):
        import RPi.GPIO as GPIO
        import time

        GPIO.setmode(GPIO.BCM)

        ledOutPin=23
        gasInPin=17
        readValue=1 # default is 1 as Gas sensor deactivated

        GPIO.setup(ledOutPin, GPIO.OUT)
        GPIO.setup(gasInPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        print("Detect changed of Gas sensor to " + str(GPIO.input(gasInPin)))
        readValue = GPIO.input(gasInPin)
        GPIO.output(ledOutPin, readValue)

        GPIO.add_event_detect(gasInPin, GPIO.BOTH)

        try:
            GPIO.output(ledOutPin, readValue)
            print("Detecting....")
            input("Press anykey to finish>")

        except KeyboardInterrupt:
            GPIO.cleanup() # clean up GPIO on CTRL+C exit

        #GPIO.cleanup()

