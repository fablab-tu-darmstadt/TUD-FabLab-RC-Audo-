import serial
import time
import sys
from signal import signal, SIGINT
from sys import exit


ser = serial.Serial('/dev/ttyACM0', 112500)

gummi_open = 1890
gummi_closed = 920

flyer_open = 1800
flyer_closed = 560


# ============== Handle SIGINT  Begin ========================
def handler(signal_received, frame):
	# Handle any cleanup here
	#sock.close()
	ser.close()
	print('SIGINT or CTRL-C detected. Exiting gracefully')
	exit(0)

signal(SIGINT, handler)
# ============== Handle SIGINT  End ========================


#ser.open()

ser.isOpen()


while True:
	ser.write('Gummi 1890\n'.encode('utf-8'))
	ser.write('Flyer 560\n'.encode('utf-8'))
	time.sleep(1)
	ser.write('Gummi 920\n'.encode('utf-8'))
	ser.write('Flyer 1800\n'.encode('utf-8'))
	time.sleep(1)

ser.close()


