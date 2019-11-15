from PIL import Image
from select import select
from sender import Sender
from v4l2capture import Video_device

sender = Sender()

video = Video_device("/dev/video0")
size_x, size_y = video.set_format(1280, 720, fourcc='MJPG')
video.create_buffers(30)
video.queue_all_buffers()

sender.start()
video.start()

while(True):
    # wait for device to fill buffer
    select((video,), (), ())

    data = video.read_and_queue()
    sender.put(data)