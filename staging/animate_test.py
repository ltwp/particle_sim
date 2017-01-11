import numpy
from matplotlib import pyplot as plt
from matplotlib import animation

# ----------
# Particle Setup

n_particles = 50
n_steps = 100
step_size = 0.1

x = numpy.random.random((n_particles,2))
# make array of randomized 0-1 particle positions (X,Y)

xp = numpy.zeros((n_particles,2))

xpp = (numpy.ones((n_particles,2))*(-1)).dot(numpy.array([[0,1],[0,0]]))
# accelerating down.

def step(step_size):
    global x, xp, xpp
    x += xp*step_size
    xp += xpp*step_size
    return x

# ----------
# Animation Setup

fig = plt.figure() #creates figure
ax = plt.axes(xlim=(0,1),ylim=(0,1)) #adds single axis to figure OLD
plt.gca().set_aspect('equal',adjustable='box')
particles, = ax.plot([],[],'bo',ms=6) # creates object which will modify with animation

def init():
    global x # bring in global x.
    particles.set_data(x[:,0],x[:,1])
    return particles,

def animate(i):
    global step_size
    x = step(step_size)
    particles.set_data(x[:,0],x[:,1])
    return particles,

# ----------
# Do It

init()
anim = animation.FuncAnimation(fig, animate, init_func=init, frames=n_steps,interval=20,blit=True)
anim.save('test_animation.mp4', fps=30, extra_args=['-vcodec','libx264'])
plt.show()
