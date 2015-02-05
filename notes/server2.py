import socket, time
import os

def serve(host, port, handler):
    s = socket.socket()
    s.bind((host, port))
    s.listen(5)
    print 'Server up, running, and waiting for call'
    try:
        while True:
            c, a = s.accept()
            pid = os.fork()
            if pid:
                # We are parent
                c.close()
            else:
                handler(c, a)
                os._exit(0)
    finally:
        s.close()

def time_handler(c, a):
    print "Received connection from", a
    c.send("Hello %s\r\n" % a[0])
    c.send("The time is %s\r\n" % time.ctime())
    c.close()

def slow_time_handler(c, a):
    print "Received connection from", a
    c.send("Hello %s\r\n" % a[0])
    c.send("The time is %s\r\n" % time.ctime())
    for i in range(15):
        time.sleep(1)
        c.send("The count is %d\r\n" % i)
    c.close()

if __name__ == '__main__':
    serve('localhost', 9605, slow_time_handler)
