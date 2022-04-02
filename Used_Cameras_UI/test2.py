import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

fig = plt.figure(figsize=(4, 4))
ax = fig.add_subplot(111, projection='polar')
ax.set_ylim(0, 100)

data = np.random.rand(50) * 6 + 2
theta = np.linspace(0, 2. * np.pi, num=50)
l, = ax.plot([], [])


def update(i):
    global data
    data += (np.random.rand(50) + np.cos(i * 2. * np.pi / 50.)) * 2
    data[-1] = data[0]
    l.set_data(theta, data)
    return l,


ani = animation.FuncAnimation(fig, update, frames=50, interval=1000, blit=True)
plt.show()
