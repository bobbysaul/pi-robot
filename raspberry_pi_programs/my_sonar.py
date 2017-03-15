# my sonar class

import RPi.GPIO as GPIO
import time

class My_Sonar:

    _trig=0
    _echo=0

    def __init__(self,trig,echo):

        self._trig=trig
        self._echo=echo

    def get_distance(self):

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        
        GPIO.setup(self._trig,GPIO.OUT)
        GPIO.output(self._trig,False)
    
        GPIO.setup(self._echo,GPIO.IN)
        time.sleep(0.1)
    
        GPIO.output(self._trig,True)
        time.sleep(0.00001)
        GPIO.output(self._trig,False)
    
        while GPIO.input(self._echo)==0:
            pass
        start=time.time()

        while GPIO.input(self._echo)==1:
            pass
        stop=time.time()

        return (stop-start)*17000

    def clear_sonar(self):
        GPIO.cleanup()
