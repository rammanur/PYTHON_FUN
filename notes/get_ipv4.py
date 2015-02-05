'Simple parsing demo'

with open('notes/ipv4_int_bri.txt') as f:
    for line in f:
        interface, ipaddr, status, protocol = line.split()
        if status == 'Up':
            print interface, ipaddr
        
