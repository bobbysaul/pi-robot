import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(4,GPIO.OUT)
GPIO.setup(14,GPIO.OUT)

GPIO.setup(2,GPIO.OUT)
GPIO.setup(3,GPIO.OUT)

print "gpio set up"

print "spin one way"

GPIO.output(4,True)
GPIO.output(14,False)

GPIO.output(2,True)
GPIO.output(3,False)

time.sleep(3)

print "other way"

GPIO.output(4,False)
GPIO.output(14,True)

GPIO.output(2,False)
GPIO.output(3,True)

time.sleep(3)

print "stop wheels"

GPIO.output(4,False)
GPIO.output(14,False)

GPIO.output(2,False)
GPIO.output(3,False)


print "ending program"

GPIO.cleanup()

