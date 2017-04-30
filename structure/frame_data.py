class FrameData:

    def __init__(self, lines):
        self.lines = lines
        self.counts = {
            "vertical": 0,
            "left_border": 0,
            "right_vector": 0,
            "horizon": 0,
            "right_border": 0,
            "left_vector": 0,
            "undefined": 0
        }

        for line in self.lines:
            self.counts[line.type] += 1

    def __str__(self):
        return "<FrameData> self.counts ="+str(self.counts)


