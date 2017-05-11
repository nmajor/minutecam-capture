import yaml
from time import sleep
from lib.camera import CameraFactory
from lib.capture import Capture

config = yaml.safe_load(open('config.yml'))
print config
camera = CameraFactory(config).get_camera()
capture = Capture(camera, config)

capture.start()
sleep(20)
capture.stop()
