# control robot through socket 
# add in sonars and check in own thread

from my_robot import My_Robot
from my_sonar import My_Sonar
from time import sleep
from time import time
import threading
import socket

# set up socket
host=''
port=8000

def setupServer():
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print "socket creaded"
    try:
        s.bind((host,port))
    except socket.error as msg:
        print msg
    print "socket bind complete"
    return s

def setupConnection():
    s.listen(1)
    conn, address = s.accept()
    print "connected to : "+address[0]+ ":"+str(address[1])
    return conn

#######################################


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

# start sonar thread
sonar_thread=threading.Thread(target=test_sonars)
sonar_thread.start()

# receive data and move
def dataTransfer(conn):
    
    global good_to_go
    global stop_sonars
    
    while True:
        data=conn.recv(1024)

        print str(data)

        if str(data).lower()=='exit':
            stop_sonars=True
            s.close()
            print "end of server"
            sleep(1)
            bob.clear_robot()
            print "end of program"
            break

        if str(data).lower()=='s':
            bob.reverse()
            sleep(delay_time)
            bob.stop()

        if good_to_go:

            if str(data).lower()=='w':
                bob.forward()
                sleep(delay_time)
                bob.stop()

            elif str(data).lower()=='a':
                bob.left_turn()
                sleep(delay_time)
                bob.stop()

            elif str(data).lower()=='d':
                bob.right_turn()
                sleep(delay_time)
                bob.stop()

            elif str(data).lower()=='q':
                bob.left_pivot()
                sleep(delay_time)
                bob.stop()

            elif str(data).lower()=='e':
                bob.right_pivot()
                sleep(delay_time)
                bob.stop()

            else:
                print "not a movement comand"
        
    conn.close()

s =setupServer()

while True:
    try:
        conn=setupConnection()
        dataTransfer(conn)

    except:
        break






        
