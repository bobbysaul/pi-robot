# my robot class

from wheel_class import My_Wheel
from my_sonar import My_Sonar

class My_Robot:

    _left_wheel=None
    _right_wheel=None
    _left_sonar=None
    _right_sonar=None

    # initialize robot with two wheels
    def __init__(self,left_pin1,left_pin2, right_pin1, right_pin2,left_sonar=None,right_sonar=None):

        self._left_wheel=My_Wheel(left_pin1,left_pin2)
        self._right_wheel=My_Wheel(right_pin1,right_pin2)

        if not(left_sonar==None):
            self._left_sonar=left_sonar
        if not(right_sonar==None):
            self._right_sonar=right_sonar

    # clean robot
    def clear_robot(self):
        if not(self._left_sonar==None):
            self._left_sonar.clear_sonar()
        if not(self._right_sonar==None):
            self._right_sonar.clear_sonar()
        self._left_wheel.clear_pins()
        self._right_wheel.clear_pins()
    
    # get left sonar
    def get_left_sonar(self):
        if self._left_sonar==None:
            return None
        return self._left_sonar.get_distance()

    # get right sonar
    def get_right_sonar(self):
        if self._right_sonar==None:
            return None
        return self._right_sonar.get_distance()

    # forward
    def forward(self):
        self._left_wheel.forward()
        self._right_wheel.forward()

    # reverse
    def reverse(self):
        self._left_wheel.reverse()
        self._right_wheel.reverse()

    # right pivot
    def right_pivot(self):
        self._left_wheel.forward()
        self._right_wheel.reverse()

    # left pivot
    def left_pivot(self):
        self._left_wheel.reverse()
        self._right_wheel.forward()

    # right turn
    def right_turn(self):
        self._left_wheel.forward()
        self._right_wheel.stop()

    # left turn
    def left_turn(self):
        self._left_wheel.stop()
        self._right_wheel.forward()

    # stop
    def stop(self):
        self._left_wheel.stop()
        self._right_wheel.stop()
