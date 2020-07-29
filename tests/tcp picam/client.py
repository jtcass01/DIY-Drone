##!/usr/bin/env python
"""
"""
from imutils.video import VideoStream
import imagezmq
import argparse
import socket
import time

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-s", "--server-ip", required=True,
                        help="ip address of the server to which the client will connect")

    args = vars(parser.parse_args())

    sender = imagezmq.ImageSender(connect_to="tcp://{}:5555".format(args["server_ip"]))

    rpiName = socket.gethostname()

    vs = VideoStream(usePiCamera=True)

    time.sleep(2.0)

    while True:
        frame = vs.read()
        sender.send_image(rpiName, frame)
