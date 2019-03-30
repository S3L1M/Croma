#!/usr/bin/env python3

import socket, threading

x = []
IP = '127.0.0.1'
BUFFER_SIZE = 1024

snd = rec = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rec.bind((IP, 5006))

def listen(data):
    while True:
        x = rec.recvfrom(BUFFER_SIZE)[0].decode()
        data[0] = x

threading.Thread(target=listen, args=x).start()

### OUR PROGRAM
def send(data):
    snd.sendto(str.encode(str(data[0])), (IP, 5005))
    print(data[0])

x[0] = int(x[0]) + 1
send(x)