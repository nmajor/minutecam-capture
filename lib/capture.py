import time
import re

class Capture(object):
    def __init__(self, camera, config):
        self.capturing = False
        self.camera = camera
        self._unpack_config(config)

    def start(self):
        self.capturing = True
        while(self.capturing):
            self._capture()
            self._wait_interval()

    def stop(self):
        self.capturing = False

    def _capture(self):
        timestamp = self._get_timestamp()
        video_filename = self._get_video_filename(timestamp)
        self._capture_video(video_filename)

    def _capture_video(self, filename):
        print 'capturing ' + filename
        print 'self.capturing ' + str(self.capturing)
        self.camera.start_recording(filename)
        time.sleep(self.duration)
        self.camera.stop_recording()

    def _wait_interval(self):
        time.sleep(self.interval)

    def _unpack_config(self, config):
        self.interval = config['interval']
        self.duration = config['duration']
        self.video_path = config['video_path']
        self.video_file_suffix = config['video_file_suffix']

    def _get_video_filename(self, timestamp):
        path = re.sub(r"/$", '', self.video_path)
        filename = str(timestamp) + '-' + self.video_file_suffix + '.h264'
        return path + '/' + filename

    def _get_timestamp(self):
        return int(time.time())

