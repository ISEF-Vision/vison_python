import matplotlib.pyplot as plt
import numpy


class Plot:
    def __init__(self, patter_recognition):
        self.pr = patter_recognition
        self.fig = plt.figure(figsize=(15,6))
        self.fig.patch.set_facecolor('w')
        plt.ion()

        self.avg_plot = self.fig.add_subplot(212)
        self.avg_max = 15

        self.line_plot = self.fig.add_subplot(211)
        self.line_max = 15

        self.avg_plot.set_xlim([0, 3])
        self.avg_plot.set_ylim([0, self.avg_max])
        self.line_plot.set_xlim([0, 3])
        self.line_plot.set_ylim([0, self.line_max])

        self.plots = {
            "left_border": {
                "line": self.line_plot.plot([], [], color='blue', label='left_border')[0],
                "avg_line": self.avg_plot.plot([], [], color='blue', label='left_border')[0]
            },
            "right_vector": {
                "line": self.line_plot.plot([], [], color='pink', label='right_vector')[0],
                "avg_line": self.avg_plot.plot([], [], color='pink', label='right_vector')[0]
            },
            "horizon": {
                "line": self.line_plot.plot([], [], color='green', label='horizon')[0],
                "avg_line": self.avg_plot.plot([], [], color='green', label='horizon')[0]
            },
            "right_border": {
                "line": self.line_plot.plot([], [], color='red', label='right_border')[0],
                "avg_line": self.avg_plot.plot([], [], color='red', label='right_border')[0]
            },
            "left_vector": {
                "line": self.line_plot.plot([], [], color='gray', label='left_vector')[0],
                "avg_line": self.avg_plot.plot([], [], color='gray', label='left_vector')[0]
            },
        }

        self.avg_plot.legend()
        self.line_plot.legend()

    def update(self):
        for key, value in self.pr.lines.items():
            index = len(self.pr.lines[key]["avg_array"])

            self.plots[key]["avg_line"].set_xdata(numpy.arange(index))
            self.plots[key]["avg_line"].set_ydata(self.pr.lines[key]["avg_array"])

            self.plots[key]["line"].set_xdata(numpy.arange(index))
            self.plots[key]["line"].set_ydata(self.pr.lines[key]["array"])

            if self.avg_max < self.pr.lines[key]["avg_array"][-1]:
                self.avg_max = self.pr.lines[key]["avg_array"][-1] + 10
                self.avg_plot.set_ylim([0, self.avg_max])

            if self.line_max < self.pr.lines[key]["array"][-1]:
                self.line_max = self.pr.lines[key]["array"][-1] + 10
                self.line_plot.set_ylim([0, self.line_max])

        plt.draw()
        plt.pause(0.01)
        self.avg_plot.set_xlim([0, self.pr.index + 10])
        self.line_plot.set_xlim([0, self.pr.index + 10])

    def save(self, name ="figure.png"):
        self.fig.savefig("./chart/"+name+".png")
