# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 16:43:00 2013

Demo multi-threaded server to demonstrate accepting of incoming socket
requests and responding to them with interesting stuff.


@author: rammanur
"""


import socket, sys, time
import threading


def standard_handler(conn, addr_info):
    conn.send("You are connected.\n\n")
    conn.close()
    

def slowpoke_handler(conn, addr_info):
    conn.send("Hello there.  I see you are from %s.\n" % (addr_info[0],))
    conn.send("Current time here is: %s\n" % (time.ctime(),))
    for i in range(10):
        time.sleep(2)
        conn.send("%d\n" % (i,))
    conn.close()


if __name__ == '__main__':
    s = socket.socket()
    s.bind( ( '0.0.0.0', 7003 ) )
    s.listen(5)
    exit_status = 0
    try:
        while True:
            conn, addr_info = s.accept()
            print "Got:", conn, addr_info
            threading.Thread(target=slowpoke_handler, args=(conn, addr_info)).start()
    except KeyboardInterrupt:
        exit_status = 1
    finally:
        conn.close()

    s.close()
    if exit_status:
        sys.exit(exit_status)
