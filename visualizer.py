"""
For reference please go to 
https://stackoverflow.com/questions/9401658/how-to-animate-a-scatter-plot]
"""
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np


class Animation:
    def __init__(self, numpoints=10):
        self.numpoints = numpoints
        self.stream = self.data_stream()
        self.fig, self.ax = plt.subplots()
        self.ani = animation.FuncAnimation(self.fig, 
                                           self.update, 
                                           interval=100, 
                                           init_func=self.setup_plot, 
                                           blit=True)


    def setup_plot(self):
        x, y, s, c = next(self.stream).T
        self.scat = self.ax.scatter(x, y, c=c,
                                    vmin=0, 
                                    vmax=1,
                                    alpha=0.8,
                                    cmap="jet", 
                                    edgecolor="k")

        self.ax.axis([-5, self.numpoints+5, -5, self.numpoints+5])
        return self.scat,

    def data_stream(self):
        xy = np.c_[np.arange(self.numpoints), np.arange(self.numpoints)]
        x, y = xy[:, 0], xy[:, 1]
        s, c = np.random.random((self.numpoints, 2)).T
        for i in range(self.numpoints-1, 0, -1):
            j = np.random.randint(0, i)
            x[j], x[i] = x[i], x[j]
            yield np.c_[x, y, s, c]


    def update(self, frame):
        try:
            data = next(self.stream)
        except StopIteration:
            plt.close()

        self.scat.set_offsets(data[:, :2])
        self.scat.set_sizes(300 * abs(data[:, 2])**1.5 + 100)
        self.scat.set_array(data[:, 3])
        return self.scat,


if __name__ == '__main__':
    a = Animation(100)
    plt.show()
