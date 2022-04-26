# example1.py
# This exemple only use OpenCV to get frame source and keyboard response
# Use the command below to install openCV
# pip install opencv-python

#  it's common to rename the cv2 only to cv for compatibility
import cv2 as cv


# On Windows use "cmd" to set the environment
#   SET cam_ip=ip_from_your_camera
# On Linux use "bash" to set the environment
#   export NAME=VALUE
# Or only change the default values, or fix the value

import os
cam_ip = os.getenv("cam_ip", "192.168.0.40")

# Sorces samples
# You need to discover your RTSP url, or use some of this examples
# source = "http://158.58.130.148:80/mjpg/video.mjpg"
# source = "http://46.151.101.158:8081/?action=stream"
# source = "http://pendelcam.kip.uni-heidelberg.de/mjpg/video.mjpg"
source = f'rtsp://{cam_ip}/11'

cap = cv.VideoCapture(source)

while True:

    # Try get frame
    ret, frame = cap.read()

    # frame read?
    if ret:
        # Get current size of frame
        height, width, colors = frame.shape

        # Set new width
        newWidth = 640

        # calculate new Height in the same aspect ratio
        newHeight = int(newWidth * height / width)

        # Creates a new image with the specified size
        image = cv.resize(frame, (newWidth, newHeight))

        cv.imshow("image", image)

    else:
        # problem!
        print("Error on read()")

    # only wait for a key each 30 milliseconds
    key = cv.waitKey(30)
    
    # if ESC, ou leter "Q" quit program
    if key == 27 or key == ord("q") or key == ord("Q"):
        break

cap.release()
