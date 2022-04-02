import sys
import time

import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

angles = [100 * (np.pi / 180)]
radii = [1]
fig, ax = plt.subplots(subplot_kw=dict(polar=True))

kw = dict(arrowstyle="->", color='r')
[ax.annotate("", xy=(angle, radius), xytext=(0, 0),
             arrowprops=kw) for
 angle, radius in zip(angles, radii)]

ax.set_ylim(0, np.max(radii))
ax.set_theta_zero_location("N")
ax.set_theta_direction(-1)

l, = ax.plot([], [])

def update(i):
    global angles
    angles += (np.random.rand(50) + np.cos(i * 2. * np.pi / 50.)) * 2
    angles[-1] = angles[0]
    l.set_data(1, angles)
    return l,


anim = animation.FuncAnimation(fig, update, frames=50, interval=500, blit=True)
plt.show()




