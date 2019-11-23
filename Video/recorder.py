from PIL import Image
from select import select
from sender import Sender
import v4l2capture
from sys import exit
from signal import signal, SIGINT

sender = Sender()


def handler(signal_received, frame):
    sender.stop()
    sender.join()
    print("BYE")
    exit(0)


signal(SIGINT, handler)

video = v4l2capture.Video_device("/dev/video0")
size_x, size_y = video.set_format(480, 272, fourcc='MJPG')
fps = video.set_fps(15)
video.create_buffers(30)
video.queue_all_buffers()

sender.start()
video.start()

while(True):
    # wait for device to fill buffer
    select((video,), (), ())

    data = video.read_and_queue()
    sender.put(data)
