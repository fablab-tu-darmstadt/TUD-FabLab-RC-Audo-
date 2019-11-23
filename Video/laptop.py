import socket
from signal import signal, SIGINT

start_message = "data please"

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def handler(signal_received, frame):
    s.close()
    print("BYE")
    exit(0)


signal(SIGINT, handler)

address = ('chronosynclastic.de', 10001)

s.sendto(start_message.encode(), address)
