"""
Implementation of Fisher Yates shuffle algorithm also known as Knuth shuffle

"""
import random
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def fisher_yates_shuffle(A: list) -> None:
      for i in range(len(A)-1, 0, -1):
            j = random.randint(0, i)
            A[j], A[i] = A[i], A[j]
            yield A


def draw(save=False):
      plt.style.use('dark_background')
      fig, ax = plt.subplots()
      scatter_points = ax.bar(A, range(len(A)))
      text = ax.text(0.02, 0.95, "", transform=ax.transAxes)


      iteration = [0]
      def update(A, points, iteration):
            for points, val in zip(points, A):
                  points.set_height(val)
            iteration[0] += 1
            text.set_text(f"Number of operations: {iteration[0]}")


      ani = FuncAnimation(fig, 
                          func=update, 
                          fargs=(scatter_points, iteration), 
                          frames=fisher_yates_shuffle(A), 
                          interval=3,
                          repeat=False)
      plt.show()


if __name__ == '__main__':
      A = list(range(80))
      draw()
