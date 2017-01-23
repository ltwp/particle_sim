import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from particle import Particle
from cloud import Cloud

# ----------
# Simulation Setup

n_particles = 10
n_steps = 150
step_size = 0.01

gravity_force = np.matrix([[0], [-1]])

particle_cloud = Cloud(n_particles,gravity_force,0)

# print particle_cloud.locations()
# print particle_cloud.step(step_size)
# print '\n\n'
# print particle_cloud.locations()
# print particle_cloud.step(step_size)
# print '\n\n'
# print particle_cloud.locations()

# ----------
# Animation Setup
fig = plt.figure() #creates figure
ax = plt.axes(xlim=(0,1),ylim=(0,1)) #adds single axis to figure OLD
plt.gca().set_aspect('equal',adjustable='box')
dots, = ax.plot([],[],'bo',ms=6) # creates object which will modify with animation

def init():
    global particle_cloud
    dots.set_data([],[])
    return dots,

def animate(i):
    global particle_cloud, step_size
    particle_cloud.step(step_size)
    dots.set_data(particle_cloud.locations()[:,0],particle_cloud.locations()[:,1])
    return dots,

# ----------
# Do It

init()
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=n_steps, interval=20, blit=False)
anim.save('test_animation.m4v', fps=25, extra_args=['-vcodec','libx264'])
plt.show()
