import picamera

class CameraFactory(object):
    def __init__(self, config):
        self.config = config
        self.camera = picamera.PiCamera()
        self.configure()

    def configure(self):
        self.camera.brightness = self.config['brightness']
    
    def get_camera(self):
        return self.camera
