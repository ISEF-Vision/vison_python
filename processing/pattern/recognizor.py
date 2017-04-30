from structure.frame_data import FrameData


class PatternRecognizor:
    def __init__(self):
        self.index = 2
        self.lines = {
            "left_border": {
                "array": [0],
                "avg_array": [0],
            },
            "right_vector": {
                "array": [0],
                "avg_array": [0],
            },
            "horizon": {
                "array": [0],
                "avg_array": [0],
            },
            "right_border": {
                "array": [0],
                "avg_array": [0]
            },
            "left_vector": {
                "array": [0],
                "avg_array": [0],
            }
        }

    def update(self, lines):
        frame_data = FrameData(lines)
        for key, value in frame_data.counts.items():
            if key == 'undefined' or key == 'vertical':
                continue

            self.lines[key]["array"].append(self.lines[key]["array"][-1] + value)

            if self.index > 21:
                array_range = self.lines[key]["array"][self.index - 21:self.index - 11]
                self.lines[key]["avg_array"].append((array_range[9] - array_range[0]) / 10)

            else:
                array_range = self.lines[key]["array"]
                self.lines[key]["avg_array"].append((array_range[self.index - 2] - array_range[0]) / (self.index - 1))

        self.index += 1

    def clear(self):
        self.__init__()

    def get_lines(self):
        return self.lines