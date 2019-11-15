from queue import Queue
from threading import Thread

class Sender (Thread):
    def __init__(self):
        self.__queue = Queue()
        Thread.__init__(self)

    def run(self):
        while(True):
            input = self.__queue.get()
            # send input to golosomie.de

    def push(self, data):
        self.__queue.push(data)
