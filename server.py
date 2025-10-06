import threading
import time
import random

import socket

def server():
   
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()
  
    server_binding = ('', 30047)
    ss.bind(server_binding)
   
    ss.listen(1)
    
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    msg = "Welcome to CS 352!"
    csockid.send(msg.encode('utf-8'))

    while True:
        data = csockid.recv(1024)
        if not data:
            break
        line = data.decode('utf-8')
        processed = line[::-1].swapcase()
        csockid.send(processed.encode('utf-8'))

   
    ss.close()
    exit()

#keep outside function
if __name__ == "__main__":
    server()
  