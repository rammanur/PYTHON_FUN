# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 14:34:03 2013

Demo server to demonstrate accepting of incoming socket requests
and responding to them with interesting stuff.


@author: rammanur
"""

import socket, sys, time, os

def standard_handler(pid, conn, addr_info):
    conn.send("%d: STD: You are connected from %s\n\n" % (pid, addr_info[0],))
    conn.close()

def slower_handler(pid, conn, addr_info):
    conn.send("%d: SLOW: You are connected from %s\n\n" % (pid, addr_info[0],))
    conn.send("%d: Current time here is: %s\n" % (pid, time.ctime(), ))
    conn.send("%d: " % (pid,))
    for i in range(10):
        time.sleep(1)
        conn.send("%d" % (i,))
    conn.send("\n\n")
    conn.close()


def socket_program(bind_address, port):    
    s = socket.socket()
    s.bind( ( bind_address, port) )
    s.listen(5)
    exit_status = 0
    count = 1
    
    try: 
        while True:
            count += 1
            conn = 0
            conn, addr_info = s.accept()
            pid = os.fork()
            if pid: 
                # I am the parent. free the useless connection
                print "%d: Started Child=%d. Closing my connection\n" % \
                    (os.getpid(), pid,)
                conn.close()
            else:
                # I am the child. do my thing
                if ((count % 2) == 0):  
                    standard_handler(os.getpid(), conn, addr_info)
                else:
                    slower_handler(os.getpid(), conn, addr_info)
                os._exit(0)
                
    except KeyboardInterrupt:
        exit_status = 1
    finally:
        if (conn != 0):
            conn.close()

    s.close()
    if exit_status:
        sys.exit(exit_status)
        
#if __name__ == 'socket_test':
#    socket_program()
#else:
#    print "%s: Hmm, how didwe end up here ?\n" % (__name__,)