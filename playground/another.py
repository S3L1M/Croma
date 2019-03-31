#!/usr/bin/env python3

import socket, threading

IP = '127.0.0.1'
BUFFER_SIZE = 1024

snd = rec = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
rec.bind((IP, 5006))

def listen():
    while True:
        data, addr = rec.recvfrom(BUFFER_SIZE)
        print("received message:", data.decode())

threading.Thread(target=listen).start()

### OUR PROGRAM
while True:
    snd.sendto(str.encode(input()), (IP, 5005))