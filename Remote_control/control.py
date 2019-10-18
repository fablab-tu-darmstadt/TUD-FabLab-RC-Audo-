import socket
import sys
from signal import signal, SIGINT
from sys import exit
import time

neutral_value = 18450
max_value = 18900
min_value = 18050

servo_value = neutral_value
motor_value = neutral_value


# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)
# Connect the socket to the port where the server is listening
server_address = ('golosomie.de', 10001)
print('connecting to golosomie.de')

# ============== Handle SIGINT  Begin ========================
def handler(signal_received, frame):
    # Handle any cleanup here
	sock.close()
	print('SIGINT or CTRL-C detected. Exiting gracefully')
	exit(0)

signal(SIGINT, handler)
# ============== Handle SIGINT  End ========================


def set_servo():
	try:
		# Send data
		send_message = 'control servo ' + str(servo_value)
		#print('sending')
		sock.sendto(send_message.encode(), server_address)
		# Look for the response
		#print("receiving")
		data, client_ip = sock.recvfrom(512)		
		print(data.decode())
	except socket.timeout:
		print("timeout")
	finally:
		#print('Transmission complete')
		done = True
	
def set_motor():
	try:
		# Send data
		send_message = 'control motor ' + str(motor_value)
		#print('sending')
		sock.sendto(send_message.encode(), server_address)
		# Look for the response
		#print("receiving")
		data, client_ip = sock.recvfrom(512)		
		print(data.decode())
	except socket.timeout:
		print("timeout")
	finally:
		#print('Transmission complete')
		done = True



while True:
	set_servo()
	set_motor()
	#if motor_value == max_value:
	#	motor_value = min_value
	#else:
	#	motor_value += 1
	if servo_value == max_value:
		servo_value = min_value
	else:
		servo_value += 10
	time.sleep(0.01)




















