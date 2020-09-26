##!/usr/bin/env python
"""
example taken from: https://abhitronix.github.io/vidgear/gears/netgear/usage/
"""
from vidgear.gears import VideoGear
from vidgear.gears import NetGear

if __name__ == "__main__":
    # open any valid video stream(for e.g `test.mp4` file)
    stream = VideoGear(enablePiCamera=True, source='test.mp4').start()

    # Define Netgear Server with default parameters
    server = NetGear()

    # loop over until KeyBoard Interrupted
    while True:

        try:

            # read frames from stream
            frame = stream.read()

            # check for frame if Nonetype
            if frame is None:
                break

            # {do something with the frame here}

            # send frame to server
            server.send(frame)

        except KeyboardInterrupt:
            break

    # safely close video stream
    stream.stop()

    # safely close server
    server.close()

"""
from imutils import build_montages
from datetime import datetime
import numpy as np
import imagezmq
import argparse
import imutils
import cv2

if __name__ == "__main__":
    image_hub = imagezmq.ImageHub()

    last_active = {}
    last_active_check = datetime.now()

    while True:
        (rpiName, frame) = image_hub.recv_image()
        image_hub.send_reply(b'OK')

        if rpiName not in last_active.keys():
            print("[INFO] receiving data from {}...".format(rpiName))

        last_active[rpiName] = datetime.now()

        # draw the sending device name on the frame
        cv2.putText(frame, rpiName, (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

        cv2.imshow("Frame", frame)
"""