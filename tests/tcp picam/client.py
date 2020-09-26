##!/usr/bin/env python
"""
"""
from vidgear.gears import NetGear
import cv2

if __name__ == "__main__":
    # define netgear client with `receive_mode = True` and default settings
    client = NetGear(address="192.168.50.76", receive_mode=True)

    # infinite loop
    while True:
        # receive frames from network
        frame = client.recv()

        # check if frame is None
        if frame is None:
            # if True break the infinite loop
            break

        # do something with frame here

        # Show output window
        cv2.imshow("Output Frame", frame)

        key = cv2.waitKey(1) & 0xFF
        # check for 'q' key-press
        if key == ord("q"):
            # if 'q' key-pressed break out
            break

    # close output window
    cv2.destroyAllWindows()
    # safely close client
    client.close()

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

    vs = VideoStream(usePiCamera=True).start()

    time.sleep(2.0)

    while True:
        frame = vs.read()
        sender.send_image(rpiName, frame)
"""