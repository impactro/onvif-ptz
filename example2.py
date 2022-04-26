# FIRST SEE "example1.py"

import os

cam_ip = os.getenv("cam_ip","192.168.0.40")
cam_user = os.getenv("cam_user","admin")
cam_password = os.getenv("cam_password","admin")

# https://www.onvif.org/specs/srv/ptz/ONVIF-PTZ-Service-Spec-v1706.pdf?ccc393&ccc393
# https://www.onvif.org/onvif/ver20/ptz/wsdl/ptz.wsdl
