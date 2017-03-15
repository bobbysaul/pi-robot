import socket

host=''
port=8000
storedValue="hey "

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

def GET():
    reply=storedValue
    return reply

def REPEAT(datamessage):
    reply=datamessage[1]
    return reply

def dataTransfer(conn):
    while True:
        data=conn.recv(1024)
        dataMessage=data.split(' ',1)
        command=dataMessage[0]
        if command=="GET":
            reply=GET()
        elif command=="REPEAT":
            reply=REPEAT(dataMessage)
        elif command=="EXIT":
            print "client is gone"
            break
        elif command=="KILL":
            print "server is shutting down"
            s.close()
            break
        else:
            reply="unknown command"
        conn.sendall(str(reply))
        print "data is sent"
    conn.close()

s =setupServer()

while True:
    try:
        conn=setupConnection()
        dataTransfer(conn)

    except:
        break
