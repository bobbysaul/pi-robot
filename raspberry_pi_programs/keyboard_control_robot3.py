# control robot by keyboard
# add in sonars and check in own thread

from my_robot import My_Robot
from my_sonar import My_Sonar
from time import sleep
from time import time
import Tkinter as tk
import threading

# wait time constant
delay_time=0.030

# set up robot
left_sonar=My_Sonar(15,18)
right_sonar=My_Sonar(17,27)
bob=My_Robot(2,3,4,14,left_sonar,right_sonar)

# check booleans
stop_sonars=False
good_to_go=True

# test sonars
def test_sonars():
    global good_to_go
    global stop_sonars
    
    while not(stop_sonars):
        if bob.get_left_sonar()<15: 
            print "False - L"
            good_to_go=False
        elif bob.get_right_sonar()<15:
            print "False - R"
            good_to_go=False
        else:
            good_to_go=True

        sleep(0.25)

    print "sonars have stopped"

# assign actions on keypress
def key(event):
    global good_to_go
    global stop_sonars

    if event.keysym=='Escape':
        stop_sonars=True
        sleep(1)
        bob.clear_robot()
        root.destroy()

    if event.char.lower()=='s':
        bob.reverse()
        sleep(delay_time)
        bob.stop()

    if good_to_go:

        if event.char.lower()=='w':
            bob.forward()
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
            print 

# start sonar thread
sonar_thread=threading.Thread(target=test_sonars)
sonar_thread.start()

# set up tkinter
root=tk.Tk()
print("Use keyboard to control the robot")
root.bind_all('<Key>',key)
root.mainloop()






        
