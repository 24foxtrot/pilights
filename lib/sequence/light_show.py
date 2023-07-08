import time

class LightShow:
    def __init__(self, pca):
        self.pca = pca
        self.off = 0x0000
        self.low = 0x3FFF
        self.med = 0x7FFF
        self.hi = 0xFFFF

    def run(self):
        self._set_sequence()
        for step in self.sequence:
            self._set_lights(step)
            time.sleep(step['duration'])

    def _set_sequence(self):
        print("no sequence has been set")

    def _set_lights(self, step):
        for channel, brightness in step['brightness'].items():
            self.pca.duty_cycle(channel, brightness)
