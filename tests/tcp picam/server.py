##!/usr/bin/env python
"""
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
