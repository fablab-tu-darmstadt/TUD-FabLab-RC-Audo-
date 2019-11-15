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

servo_value = neutral_value
motor_value = neutral_value


window = tkinter.Tk()
window.title("AUDO Control")
window.geometry('320x160')

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

window.mainloop()
sock.close()
