import serial
import time

ser = serial.Serial('/dev/ttyACM0', 112500)

#ser.open()

ser.isOpen()

time.sleep(1)

ser.write('Servo 18200\n'.encode('utf-8'))

time.sleep(1)

ser.write('Servo 18800\n'.encode('utf-8'))

time.sleep(1)

ser.write('Servo 18450\n'.encode('utf-8'))

time.sleep(1)

ser.close()


