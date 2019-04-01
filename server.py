 #!/usr/bin/env python3
from flask import Flask, render_template
from transceiver import Emitter

app = Flask(__name__)
x = Emitter('192.168.43.1', '192.168.43.5', 1024)
x.listen()

@app.route('/')
def main():
  return render_template('index.html')

@app.route('/state')
def getState():
  return x.getData()

#@app.route('/set', methods=['POST'])
#def setEmitter():

if __name__=='__main__':
  app.run(debug=False, host='0.0.0.0', port=80)