# my wheels class

import RPi.GPIO as GPIO
class My_Wheel:

    _in_pin=0
    _out_pin=0

    # initialize the wheel with 2 pins
    def __init__(self,gpio_in,gpio_out):

        self._in_pin=gpio_in
        self._out_pin=gpio_out

        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._in_pin,GPIO.OUT)
        GPIO.setup(self._out_pin,GPIO.OUT)

    # forward
    def forward(self):
        GPIO.output(self._in_pin,False)
        GPIO.output(self._out_pin,True)

    # reverse
    def reverse(self):
        GPIO.output(self._in_pin,True)
        GPIO.output(self._out_pin,False)

    # stop
    def stop(self):
        GPIO.output(self._in_pin,False)
        GPIO.output(self._out_pin,False)

    # end wheel
    def clear_pins(self):
        GPIO.cleanup()

    # reset pins
    def reset_pins(self,gpio_in,gpio_out):
        self._in_pin=gpio_in
        self._out_pin=gpio_out

        #GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self._in_pin,GPIO.OUT)
        GPIO.setup(self._out_pin,GPIO.OUT)
