import numpy
from matplotlib import pyplot as plt
from matplotlib import animation

# ----------
# Particle Setup

n_particles = 100
n_steps = 10
step_size = 0.1

x = numpy.random.random((n_particles,2))
# make array of randomized 0-1 particle positions (X,Y)

xp = numpy.zeros((n_particles,2))

xpp = numpy.ones((n_particles,2))
# just accelerating to upper-right, no box limits yet

# ----------
# Animation Setup

fig = plt.figure()
ax = fig.add_subplot(1,1,1) # one row, one column, first plot

def init():
    global x
    ax.scatter(x[:,0],x[:,1])
    return ax,

def animate(i):
    canvas.restore_region(background)
    global x
    global xp
    global xpp
    global step_size
    x += xp*step_size
    xp += xpp*step_size
    ax.scatter(x[:,0],x[:,1])
    return ax,


"""
for i in range(1,n_steps):
    x += xp*step_size
    xp += xpp*step_size
    print(x)
    ax.scatter(x[:,0],x[:,1])
"""

# ----------
# Do It

# anim = animation.FuncAnimation(fig,animate,init_func=init,frames=n_steps,interval=20,blit=True)

anim = animation.FuncAnimation(fig,animate,init_func=init,frames=n_steps,interval=20,blit=True)
plt.show()