import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation

r =0
t = 1

fig = plt.figure()
ax = fig.gca(projection = 'polar')
fig.canvas.set_window_title('Doppler')
ax.plot(r, t, color ='b', marker = 'o', markersize = '3')
ax.set_theta_zero_location('N')
ax.set_theta_direction(-1)
ax.set_ylim(0,1.02*t)

line1, = ax.plot([0, 0],[0,t], color = 'r', linewidth = 2)

def update(angle):
    line1.set_data([angle],[0,t])
    return line1,

frames = np.array([ 94.3123  * (np.pi/180),  120  * (np.pi/180),  220  * (np.pi/180),  0  * (np.pi/180)])

fig.canvas.draw()
ani = matplotlib.animation.FuncAnimation(fig, update, frames=frames, blit=True, interval=500)

plt.show()