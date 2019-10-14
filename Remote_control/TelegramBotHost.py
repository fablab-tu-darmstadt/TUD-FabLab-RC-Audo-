
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters
from signal import signal, SIGINT
from sys import exit
import serial
import time

# TODO
# Make Serial com more reliable
# Another thread for serial????
# Send reset to stm32 over serial??
#
#
# Write Client
# Client reads keyboard 
# Sends commands to host
#


ser = serial.Serial('/dev/ttyACM0', 112500)
ser.isOpen()

neutral_value = 18450
max_value = 18900
min_value = 18050

servo_value = neutral_value
motor_value = neutral_value

ser.write('Servo 18450\n'.encode('utf-8'))
ser.write('Motor 18450\n'.encode('utf-8'))

fablabAUDOHost_bot_Token = '915913122:AAF3_jWXFti-udfqtnPqmKmj2ejW9AwGl9M'

updater = Updater(token=fablabAUDOHost_bot_Token, use_context=True)

dispatcher = updater.dispatcher

#import logging
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)


# ============== Handle SIGINT  Begin ========================
def handler(signal_received, frame):
    # Handle any cleanup here
	updater.stop()
	ser.close()
	print('SIGINT or CTRL-C detected. Exiting gracefully')
	exit(0)

signal(SIGINT, handler)
# ============== Handle SIGINT  End ========================


# ============== Start Command  Begin ========================
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Moin!\nI am the FablabAUDOHost_bot!\nI control things!\n")

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)
# ============== start Command  End ========================


# ============== ECHO  Begin ========================
def echo(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message.text)

echo_handler = MessageHandler(Filters.text, echo)
dispatcher.add_handler(echo_handler)
# ============== ECHO  End ========================




# ============== Servo Command  Begin ========================
def servo(update, context):
	servo_value = int(context.args[0])
	send_str = "Servo " + str(servo_value) + "\n" 
	ser.write(send_str.encode('utf-8'))
	context.bot.send_message(chat_id=update.effective_chat.id, text="Set Servo to " + str(servo_value))
	#context.bot.send_message(chat_id=update.effective_chat.id, text="args[0]: " + context.args[0])

servo_handler = CommandHandler('servo', servo, pass_args=True)
dispatcher.add_handler(servo_handler)
# ============== Servo Command  End ========================


# ============== Motor Command  Begin ========================
def motor(update, context):
	motor_value = int(context.args[0])
	send_str = "Motor " + str(motor_value) + "\n" 
	ser.write(send_str.encode('utf-8'))
	context.bot.send_message(chat_id=update.effective_chat.id, text="Set Motor to " + str(motor_value))
	#context.bot.send_message(chat_id=update.effective_chat.id, text="arg[0]: " + context.args[0])

motor_handler = CommandHandler('motor', motor, pass_args=True)
dispatcher.add_handler(motor_handler)
# ============== Motor Command  End ========================




# ============== Unknown Command  Begin ========================
# ============== Must be last Command Hander =========================
def unknown(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, I didn't understand that command.")

unknown_handler = MessageHandler(Filters.command, unknown)
dispatcher.add_handler(unknown_handler)
# ============== Unknown Command  Begin ========================


updater.start_polling()












