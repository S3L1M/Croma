 #!/usr/bin/env python3
import socket, threading

CROMA_PORT = 5005
CROMA_BUFFER_SIZE = 1024


class UDP:
  def __init__(self):
    self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

class Sender (UDP):
  def __init__(self, ip, port):
    self.IP = ip
    self.PORT = port
    UDP.__init__(self)
  
  def send(self, data):
    self.sock.sendto(str.encode(data), (self.IP, self.PORT))


class Receiver (UDP):
  def __init__(self, port, buffer_size):
    UDP.__init__(self)
    self.rPORT = port
    self.BUFFER_SIZE = buffer_size
    self.sock.bind(('0.0.0.0', self.rPORT))
    self.data = 'undefined'
  
  def eventListener(self):
    while True:
      self.data, addr = self.sock.recvfrom(self.BUFFER_SIZE)
  
  def listen(self):
    threading.Thread(target=self.eventListener).start()
  
  def getData(self):
    return self.data.decode()
  
  def getDataBinary(self):
    return self.data


class Transceiver (Sender, Receiver):
  def __init__(self, target_ip, target_port, port, buffer_size):
    Sender.__init__(self, target_ip, target_port)
    Receiver.__init__(self, port, buffer_size)


class Emitter (Transceiver):
  def __init__(self, ip_from, ip_to, port, port_to, buffer_size, onReceive=None):
    Transceiver.__init__(self, ip_to, port_to, port, buffer_size)
    self.rIP = ip_from
    self.onReceive = onReceive
  
  def eventListener(self):
    while True:
      self.data, addr = self.sock.recvfrom(self.BUFFER_SIZE)
      if addr[0]==self.rIP:
        if self.onReceive: self.onReceive()
        self.send(self.getData())  


class Duplex:
  def __init__(self, target_ip, target_port, port, buffer_size):
    self.outgoing = Sender(target_ip, target_port)
    self.incoming = Receiver(port, buffer_size)

class Connection (Transceiver):
  def __init__(self, ip):
    Transceiver.__init__(self, ip, CROMA_PORT, CROMA_PORT, CROMA_BUFFER_SIZE)


class Stream (Emitter):
  def __init__(self, source, sPort, destination, event):
    Emitter.__init__(self, source, destination[0], sPort, destination[1], CROMA_BUFFER_SIZE, onReceive=event)
    self.listen()