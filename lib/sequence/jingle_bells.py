from lib.sequence.light_show import LightShow

class jingle_bells(LightShow):
    def _set_sequence(self):
        self.sequence = [
            {'brightness': {0: self.off, 1: self.med, 2: self.off}, 'duration': 2},
            {'brightness': {3: self.med, 4: self.off, 5: self.off}, 'duration': 2},
            {'brightness': {6: self.off, 7: self.med, 12: self.off}, 'duration': 2},
            {'brightness': {13: self.med, 14: self.off, 15: self.off}, 'duration': 2},
            {'brightness': {8: self.off, 9: self.off, 10: self.off, 11: self.off}, 'duration': 2},
        ]
