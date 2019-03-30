from urllib import urlopen

while True:
	data = urlopen('http://192.168.1.5/server/test').read()

