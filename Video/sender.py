from queue import Queue
from threading import Thread
from sys import stdout
import socket
from sys import getsizeof


class Sender (Thread):
    def __init__(self):
        self.__queue = Queue()
        self.__running = True
        self.__socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.__address = ('chronosynclastic.de', 10001)
        Thread.__init__(self)

    def run(self):
        while(self.__running):
            input = self.__queue.get()
            # stdout.buffer.write(input)
            # send input to golosomie.de
            # print(getsizeof(input), "\n") # 40609 war max
            self.__socket.sendto(input, self.__address)

    def put(self, data):
        self.__queue.put(data)

    def stop(self):
        self.__socket.close()
        self.__running = False
