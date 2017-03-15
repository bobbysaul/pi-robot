# control robot by keyboard
# add in sonars and check on time intervals

from my_robot import My_Robot
from my_sonar import My_Sonar
from time import sleep
from time import time
import Tkinter as tk

# wait time constant
delay_time=0.030
check_time=0.75

# set up robot
left_sonar=My_Sonar(15,18)
right_sonar=My_Sonar(17,27)
bob=My_Robot(2,3,4,14,left_sonar,right_sonar)

# start time for when to check distance
start_time=time()
good_to_go=True

# test sonars
def test_sonars():
    if bob.get_left_sonar()<15: 
        print "False - L"
        return False
    if bob.get_right_sonar()<15:
        print "False - R"
    return True

# assign actions on keypress
def key(event):
    global start_time
    global good_to_go

    if event.keysym=='Escape':
        bob.clear_robot()
        root.destroy()

    # see if time to check sonars
    if time()-start_time>check_time:
        good_to_go=test_sonars()
        start_time=time()

    if good_to_go:

        if event.char.lower()=='w':
            bob.forward()
            sleep(delay_time)
            bob.stop()

        elif event.char.lower()=='s':
            bob.reverse()
            sleep(delay_time)
            bob.stop()

        elif event.char.lower()=='a':
            bob.left_turn()
            sleep(delay_time)
            bob.stop()

        elif event.char.lower()=='d':
            bob.right_turn()
            sleep(delay_time)
            bob.stop()

        elif event.char.lower()=='q':
            bob.left_pivot()
            sleep(delay_time)
            bob.stop()

        elif event.char.lower()=='e':
            bob.right_pivot()
            sleep(delay_time)
            bob.stop()

        else:
            print "unknown command"

    else:
        print "too close"

# set up tkinter
root=tk.Tk()
print("Use keyboard to control the robot")
root.bind_all('<Key>',key)
root.mainloop()






        
