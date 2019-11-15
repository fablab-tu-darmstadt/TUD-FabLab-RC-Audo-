import socket
import sys
from signal import signal, SIGINT
from sys import exit

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# ============== Handle SIGINT  Begin ========================
def handler(signal_received, frame):
        # Handle any cleanup here
        sock.close()
        print('SIGINT or CTRL-C detected. Exiting gracefully')
        exit(0)

signal(SIGINT, handler)
# ============== Handle SIGINT  End ========================


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('golosomie.de', 10001)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
#sock.listen(1)

neutral_value = 18450
max_value = 18900
min_value = 18050

servo_value = neutral_value
motor_value = neutral_value

while True:
	# Wait for a connection
        print >>sys.stderr, 'waiting for a connection'
        #connection, client_address = sock.accept()
        try:
            	#print >>sys.stderr, 'connection from', client_address
                # Receive the data in small chunks and retransmit it
                while True:
                        #data = connection.recv(512)
                        data, client_ip = sock.recvfrom(512)
                        print >>sys.stderr, 'received "%s"' % data
                        if data:
                               #print >>sys.stderr, 'sending data back to the client'
                                #connection.sendall(data)
                                message = data.split(" ")
                                if message[0] == "audo":
                                        mess = "Servo " + str(servo_value) + " Motor " + str($
                                        #connection.sendall(mess)
                                        sock.sendto(mess, client_ip)
                                elif message[0] == "control":
                                        #connection.sendall(message[1])
                                        sock.sendto(message[1],client_ip)
                                        if message[1] == "servo":
                                                servo_value = int(message[2])
                                        elif message[1] == "motor":
                                                motor_value = int(message[2])                $
                        else:
                             	#print >>sys.stderr, 'no more data from', client_address
                                break
        #except:
        #	print("dop")
        finally:
                # Clean up the connection
                #connection.close()
                print("done")

