#!/usr/bin/env python3
import socket, threading

class transceiver:
  def __init__(self, ip, buffer_size):
    self.IP = ip
    self.BUFFER_SIZE = buffer_size
    self.init()
  
  def init(self):
    self.snd = self.rec = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.rec.bind((self.IP, 5005))

  def eventListener(self):
    while True:
      self.data, addr = self.rec.recvfrom(self.BUFFER_SIZE)

  def listen(self):
    threading.Thread(target=self.eventListener).start()

  def getData(self):
    return self.data.decode()
  
  def getDataBinary(self):
    return self.data.decode()

  def send(self, data):
      self.snd.sendto(str.encode(data), (self.IP, 5005))
      
      
class stream (transceiver):
  def __init__(self, ip_a, ip_b, buffer_size):
    self.IP = ip_a
    self.IP2 = ip_b
    self.BUFFER_SIZE = buffer_size
    self.init()
  
  def eventListener(self):
    while True:
      self.data, addr = self.rec.recvfrom(self.BUFFER_SIZE)