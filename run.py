from lib.capture import Capture
from time import sleep
import picamera

camera = picamera.PiCamera()
camera.start_recording('video.h264')
sleep(5)
camera.stop_recording()


