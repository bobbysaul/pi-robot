# sonar test

import RPi.GPIO as GPIO
import time

trig=15
echo=18

def get_distace():

    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    
    GPIO.setup(trig,GPIO.OUT)
    GPIO.output(trig,False)
    
    GPIO.setup(echo,GPIO.IN)
    time.sleep(0.1)

    GPIO.output(trig,True)
    time.sleep(0.00001)
    GPIO.output(trig,False)

    while GPIO.input(echo)==0:
        pass
    start=time.time()

    while GPIO.input(echo)==1:
        pass
    stop=time.time()

    GPIO.cleanup()
    
    return (stop-start)*17000


    
