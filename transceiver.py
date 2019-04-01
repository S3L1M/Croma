 #!/usr/bin/env python3
import socket, threading

class Emitter:
  def __init__(self, ip_from, ip_to, buffer_size):
    self.IP1 = ip_from
    self.IP2 = ip_to
    self.BUFFER_SIZE = buffer_size
    self.snd = self.rec = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    self.rec.bind(('0.0.0.0', 5005))
    self.data = bin(0)

  def eventListener(self):
      while True:
          self.data, addr = self.rec.recvfrom(self.BUFFER_SIZE)
          if addr[0]==self.IP1:
            # Send data to frontend
            self.send(self.getData())

  def listen(self):
    threading.Thread(target=self.eventListener).start()

  def getData(self):
    return self.data.decode()
  
  def getDataBinary(self):
    return self.data

  def send(self, data):
      self.snd.sendto(str.encode(data), (self.IP2, 5005))
