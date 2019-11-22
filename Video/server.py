import socket
from sys import exit, stderr
from signal import signal, SIGINT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def handler(signal_received, frame):
    s.close()
    print("BYE")
    exit(0)


signal(SIGINT, handler)

address = ('chronosynclastic.de', 10001)
print("starting on ", address)
s.bind(address)

# get incoming connections
# get one from audo and one from laptop
# special message from laptop -> send until laptop says stop
