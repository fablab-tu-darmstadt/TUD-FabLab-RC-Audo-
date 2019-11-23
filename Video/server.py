import socket
from sys import exit, stderr
from signal import signal, SIGINT

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


def handler(signal_received, frame):
    s.close()
    print("BYE")
    exit(0)


signal(SIGINT, handler)

address = ('chronosynclastic.de', 10001)
print("starting on ", address)
s.bind(address)

laptop_request = "data please".encode()

invalid = "invalid".encode()
frame = "".encode()
valid = False

while True:
    data, ip = s.recvfrom(2048)
    if data:
        if laptop_request in data:
            if valid:
                s.sendto(frame, ip)
                valid = False
            else:
                s.sendto(invalid, ip)
        else:
            frame = data
            valid = True
