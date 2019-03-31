#!usr/bin/env python3
from transceiver import transceiver as tr

class stream:
  def __init__(self, IP_a, IP_b, buffer_size):
    self.a = tr(IP_a, buffer_size)
    self.b = tr(IP_b, buffer_size)

  def aaa(self):

  def activate():
    