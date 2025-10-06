import threading
import time
import random

import socket


def client():
    #creates TCP socket if it fails to get created it prints error and exits
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    port = 30047
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    #opens a TCP connection to the server addr(ip, port)
    #triggers 3 way handshake
    server_binding = (localhost_addr, port)
    cs.connect(server_binding) 

    # Receive data from the server
    #reads 100 bytes because
    #using UTF-8 decodes it from bits to string
    data_from_server=cs.recv(100)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    #Open input file and output file
    #for each line in the input,
    # 1. line.strip() removes the newline character from the end of the line
    # 2. encode('utf-8') encodes the string to bits
    # 3. cs.send() sends the bits to the server
    # 4. cs.recv() receives the bits from the server
    # 5. decode('utf-8') decodes the bits to string
    # 6. outfile.write() writes the string to the output file
    with open("in-proj.txt", "r") as infile, open("out-proj.txt", "w") as outfile:
        for line in infile:
            cs.send(line.strip().encode('utf-8'))
            dfs = cs.recv(1024) #recieve back edited message
            response = dfs.decode('utf-8')
            outfile.write(response + '\n')

    # close the client socket
    cs.close()
    exit()

#keep outside function
if __name__ == "__main__":
    client()
