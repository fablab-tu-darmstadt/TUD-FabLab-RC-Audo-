from queue import Queue
from threading import Thread
from sys import stdout


class Sender (Thread):
    def __init__(self):
        self.__queue = Queue()
        Thread.__init__(self)

    def run(self):
        while(True):
            input = self.__queue.get()
            stdout.buffer.write(input)
            # send input to golosomie.de

    def put(self, data):
        self.__queue.put(data)

    def empty(self):
        self.__queue.clear()
