import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from particle import Particle
from cloud import Cloud

# ----------
# Simulation Setup

n_particles = 10
n_steps = 100
step_size = 0.1

particle_cloud = Cloud(n_particles,0)

# ----------
# Animation Setup
fig = plt.figure() #creates figure
ax = plt.axes(xlim=(0,1),ylim=(0,1)) #adds single axis to figure OLD
plt.gca().set_aspect('equal',adjustable='box')
dots, = ax.plot([],[],'bo',ms=6) # creates object which will modify with animation

def init():
    global particle_cloud
    dots.set_data(particle_cloud.locations()[:,0],particle_cloud.locations()[:,1])
    return dots,

def animate(i):
    global particle_cloud, step_size
    #  TAKE A STEP
    dots.set_data(particle_cloud.locations()[:,0],particle_cloud.locations()[:,1])
    return dots,

# ----------
# Do It

init()
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=n_steps,interval=20,blit=True)
anim.save('test_animation.mp4', fps=30, extra_args=['-vcodec','libx264'])
plt.show()
