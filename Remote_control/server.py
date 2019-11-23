import socket
import sys
from signal import signal, SIGINT
from sys import exit

#sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ============== Handle SIGINT  Begin ========================
def handler(signal_received, frame):
	# Handle any cleanup here
	sock.close()
	print('SIGINT or CTRL-C detected. Exiting gracefully')
	exit(0)

signal(SIGINT, handler)
# ============== Handle SIGINT  End ========================


# Create a UDP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('golosomie.de', 10001)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

neutral_value = 18450
max_value = 18900
min_value = 18050

gummi_open = 1890
gummi_closed = 920
flyer_open = 1800
flyer_closed = 560

servo_value = neutral_value
motor_value = neutral_value
gummi_value = gummi_closed
flyer_value = flyer_closed


# Receive the data in small chunks and retransmit it
while True:
	data, client_ip = sock.recvfrom(512)
	print >>sys.stderr, 'received "%s"' % data
	if data:
		message = data.split(" ")
		if message[0] == "audo":
			mess = "Servo " + str(servo_value) + " Motor " + str(motor_value) + " Gummi " + str(gummi_value) + " Flyer " + str(flyer_value)
			sock.sendto(mess, client_ip)
		elif message[0] == "control":
			sock.sendto(message[1],client_ip)
			if message[1] == "servo":
				servo_value = int(message[2])
			elif message[1] == "motor":
				motor_value = int(message[2])
			elif message[1] == "gummi":
				gummi_value = int(message[2])
			elif message[1] == "flyer":
				flyer_value = int(message[2])
            	else:
			break


sock.close()

