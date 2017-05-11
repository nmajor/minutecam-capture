class Capture(object):
    def __init__(self, camera, config):
        self.capturing = false
        self.camera = camera
        self.config = config

    def start(self):
        self.capturing = true
        while(self.capturing):
            self.capture_interval

    def stop(self):
        self.capturing = false

    def capture_interval(self):
        camera.start_recording('video.h264')
        sleep(5)
        camera.stop_recording()


