 #!/usr/bin/env python3
from flask import Flask, render_template, request, redirect
from flask_socketio import SocketIO
import transceiver as Lib

app = Flask(__name__)
socketio = SocketIO(app)
lst = []

@app.route('/')
def main():
  return render_template('index.html')

#@app.route('/states')
#def getState():
#  return x.getData()

@app.route('/add', methods=['POST'])
def addStream():
  req = dict(request.args)
  ip, sp = req['ip'], int(req['sp'])
  dest = req['dip'], int(req['dp'])
  lst.append(Lib.Stream(ip, sp, dest, socketio.emit('pushStates', {'data':map(Lib.Stream.getData, lst)})))
  return redirect('/')

if __name__=='__main__':
  app.run(debug=False, host='0.0.0.0', port=80)
