import socket
from sys import exit
from signal import signal, SIGINT

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def handler(signal_received, frame):
    s.close()
    print("BYE")
    exit(0)


signal(SIGINT, handler)
