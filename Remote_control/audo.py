import socket
import sys
from signal import signal, SIGINT
from sys import exit
import serial
import time

#112500

ser = serial.Serial('/dev/ttyACM0', 112500)
ser.isOpen()
print(ser.readline())

neutral_value = 18450
max_value = 18900
min_value = 18050
timeout_value = 5
keep_alive = time.time()

gummi_open = 1890
gummi_closed = 920

flyer_open = 1800
flyer_closed = 560



servo_value = neutral_value
motor_value = neutral_value
gummi_value = gummi_closed
flyer_value = flyer_closed


ser.write('Servo 18450\n'.encode('utf-8'))
#print(ser.readline())
ser.write('Motor 18450\n'.encode('utf-8'))
#print(ser.readline())
ser.write('Gummi 920\n'.encode('utf-8'))
ser.write('Flyer 560\n'.encode('utf-8'))

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.settimeout(1)
server_address = ('golosomie.de', 10001)
print('connecting to golosomie.de')


send_message = "audo".encode()

# ============== Handle SIGINT  Begin ========================
def handler(signal_received, frame):
    # Handle any cleanup here
	
	sock.close()
	ser.write('Servo 18450\n'.encode('utf-8'))
	ser.write('Motor 18450\n'.encode('utf-8'))
	ser.write('Gummi 920\n'.encode('utf-8'))
	ser.write('Flyer 560\n'.encode('utf-8'))
	#print(ser.readline())
	ser.close()
	print('SIGINT or CTRL-C detected. Exiting gracefully')
	exit(0)

signal(SIGINT, handler)
# ============== Handle SIGINT  End ========================

def get_values():
	global keep_alive
	global servo_value
	global motor_value
	global gummi_value
	global flyer_value
	try:
		# Send data
		#print('sending')
		sock.sendto(send_message, server_address)
		# Look for the response
		#print("receiving")
		data, client_ip = sock.recvfrom(512)
		keep_alive = time.time()
		#print(data)
		message = data.decode().split(" ")
		print(message)
		if len(message) == 8:
			if message[0] == "Servo":
				servo_value = int(message[1])
				send_str = "Servo " + str(servo_value) + "\n" 
				#print(send_str)
				ser.write(send_str.encode('utf-8'))
				#print(ser.readline())
			#time.sleep(0.01)
			if message[2] == "Motor":
				motor_value = int(message[3])
				send_str = "Motor " + str(motor_value) + "\n" 
				ser.write(send_str.encode('utf-8'))
				#print(ser.readline())
			if message[2] == "Gummi":
				gummi_value = int(message[3])
				send_str = "Gummi " + str(gummi_value) + "\n" 
				ser.write(send_str.encode('utf-8'))
				#print(ser.readline())
			if message[2] == "Flyer":
				flyer_value = int(message[3])
				send_str = "Flyer " + str(flyer_value) + "\n" 
				ser.write(send_str.encode('utf-8'))
				#print(ser.readline())
	except socket.timeout:
		ser.write('Servo 18750\n'.encode('utf-8'))
		#print(ser.readline())
		ser.write('Motor 18450\n'.encode('utf-8'))
		#print(ser.readline())
		ser.write('Gummi 920\n'.encode('utf-8'))
		ser.write('Flyer 560\n'.encode('utf-8'))	
		print("Timeout - Stopping AUDO")

	finally:
		#print('Transmission complete')
		done = True
		



while True:
	get_values()
	#print(time.time() - keep_alive)
	if timeout_value < (time.time() - keep_alive):
		ser.write('Servo 18450\n'.encode('utf-8'))
		#print(ser.readline())
		ser.write('Motor 18450\n'.encode('utf-8'))
		#print(ser.readline())
		ser.write('Gummi 920\n'.encode('utf-8'))
		ser.write('Flyer 560\n'.encode('utf-8'))	
		print("Timeout - Stopping AUDO")
	time.sleep(0.1)
	


















