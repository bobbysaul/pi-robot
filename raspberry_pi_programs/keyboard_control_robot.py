# control robot by keyboard

from my_robot import My_Robot
from time import sleep
import Tkinter as tk

# wait time constant
delay_time=0.030

# set up robot
bob=My_Robot(2,3,4,14)

# assign actions on keypress
def key(event):

    if event.keysym=='Escape':
        root.destroy()

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

# set up tkinter
root=tk.Tk()
print("Use keyboard to control the robot")
root.bind_all('<Key>',key)
root.mainloop()






        
