import socket
import sys
from signal import signal, SIGINT
from sys import exit
import time
import tkinter
from tkinter.ttk import Progressbar

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
job_value = 0

window = tkinter.Tk()
window.title("AUDO Control")
window.geometry('360x300')

motor_label = tkinter.Label(window, text="Motor: 0")
motor_label.grid(column=0, row=2)

servo_label = tkinter.Label(window, text="Servo: 0")
servo_label.grid(column=0, row=3)

min_label = tkinter.Label(window, text="Min: " + str(min_value - neutral_value) )
min_label.grid(column=0, row=4)

max_label = tkinter.Label(window, text="Max: " + str(max_value - neutral_value) )
max_label.grid(column=0, row=5)


def forward():
	global motor_value
	global bar_forward
	global bar_backward
	if motor_value >= min_value + 25:
		motor_value -= 25
	set_motor()
	motor_label.configure(text="Motor: " + str(motor_value - neutral_value))

btn_forward = tkinter.Button(window, text=" V+ ", bg="orange", fg="red", command=forward, padx=20, pady=8)
btn_forward.grid(column=5, row=3)

def backward():
	global motor_value
	global bar_forward
	global bar_backward
	if motor_value <= max_value - 25:
		motor_value += 25
	set_motor()
	motor_label.configure(text="Motor: " + str(motor_value - neutral_value))

btn_backward = tkinter.Button(window, text=" V- ", bg="orange", fg="red", command=backward, padx=20, pady=8)
btn_backward.grid(column=5, row=5)

def left():
	global servo_value
	if servo_value >= min_value + 25:
		servo_value -= 25
	set_servo()
	servo_label.configure(text="Servo: " + str(servo_value - neutral_value))

btn_left = tkinter.Button(window, text="Left", bg="orange", fg="red", command=left, padx=20, pady=8)
btn_left.grid(column=4, row=4)

def right():
	global servo_value
	if servo_value <= max_value - 25:
		servo_value += 25
	set_servo()
	servo_label.configure(text="Servo: " + str(servo_value - neutral_value))

btn_right = tkinter.Button(window, text="Right", bg="orange", fg="red", command=right, padx=20, pady=8)
btn_right.grid(column=6, row=4)

def stop():
	global motor_value
	global servo_value
	global bar_forward
	global bar_backward
	motor_value = neutral_value
	servo_value = neutral_value
	set_servo()
	set_motor()
	motor_label.configure(text="Motor: 0")
	servo_label.configure(text="Servo: 0")

btn_stop = tkinter.Button(window, text="Stop", bg="orange", fg="red", command=stop, padx=20, pady=8)
btn_stop.grid(column=5, row=4)

def gummi_opening():
	global gummi_value
	gummi_value = gummi_open
	set_gummi()

btn_gummi_open = tkinter.Button(window, text="GOPEN", bg="orange", fg="red", command=gummi_opening, padx=20, pady=8)
btn_gummi_open.grid(column=4, row=6)

def gummi_close():
	global gummi_value
	gummi_value = gummi_closed
	set_gummi()

btn_gummi_close = tkinter.Button(window, text="GCLOSE", bg="orange", fg="red", command=gummi_close, padx=20, pady=8)
btn_gummi_close.grid(column=6, row=6)

def flyer_opening():
	global flyer_value
	flyer_value = flyer_open
	set_flyer()

btn_flyer_open = tkinter.Button(window, text="FOPEN", bg="orange", fg="red", command=flyer_opening, padx=20, pady=8)
btn_flyer_open.grid(column=4, row=7)

def flyer_close():
	global flyer_value
	flyer_value = flyer_closed
	set_flyer()

btn_flyer_close = tkinter.Button(window, text="FCLOSE", bg="orange", fg="red", command=flyer_close, padx=20, pady=8)
btn_flyer_close.grid(column=6, row=7)

def job_forward():
	global job_value
	job_value = 1
	set_job()

btn_job_forward = tkinter.Button(window, text="Forward", bg="orange", fg="red", command=job_forward, padx=20, pady=8)
btn_job_forward.grid(column=4, row=8)

def job_backward():
	global job_value
	job_value = 2
	set_job()

btn_job_backward = tkinter.Button(window, text="Backward", bg="orange", fg="red", command=job_backward, padx=20, pady=8)
btn_job_backward.grid(column=4, row=9)

def job_right():
	global job_value
	job_value = 3
	set_job()

btn_job_right = tkinter.Button(window, text="Right 90", bg="orange", fg="red", command=job_right, padx=20, pady=8)
btn_job_right.grid(column=6, row=8)

def job_left():
	global job_value
	job_value = 4
	set_job()

btn_job_left = tkinter.Button(window, text="Left 90", bg="orange", fg="red", command=job_left, padx=20, pady=8)
btn_job_left.grid(column=6, row=9)

def job_circle():
	global job_value
	job_value = 5
	set_job()

btn_job_circle = tkinter.Button(window, text="Circle", bg="orange", fg="red", command=job_circle, padx=20, pady=8)
btn_job_circle.grid(column=5, row=8)


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

def set_gummi():
	try:
		# Send data
		send_message = 'control gummi ' + str(gummi_value)
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

def set_flyer():
	try:
		# Send data
		send_message = 'control flyer ' + str(flyer_value)
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

def set_job():
	try:
		# Send data
		send_message = 'control job ' + str(job_value)
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


window.mainloop()
sock.close()


#while True:
#	set_servo()
#	set_motor()
#	#if motor_value == max_value:
#	#	motor_value = min_value
#	#else:
#	#	motor_value += 1
#	if servo_value == max_value:
#		servo_value = min_value
#	else:
#		servo_value += 10
#	time.sleep(0.01)




















