import socket
import threading
from queue import Queue

print_lock = threading.Lock()

target = 'IP/DOMAIN OF CHOICE'

def portscan(port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        con = s.connect((target,port))
        with print_lock:
            print('port {} is open!'.format(port))
        con.close()
    except:
        pass

def threader():
    while True:
        worker = q.get()
        portscan(worker)
        q.task_done()

q = Queue()

for x in range(100):
    t = threading.Thread(target=threader)
    t.daemon = True
    t.start()

for worker in range(1,10000):
    q.put(worker)

q.join()
