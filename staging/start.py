import numpy
from matplotlib import pyplot as plt

# ----------
# Particle Setup

n_particles = 100
n_steps = 100
step_size = 0.1

x = numpy.random.random((n_particles,2))
# make array of randomized 0-1 particle positions (X,Y)

xp = numpy.zeros((n_particles,2))

xpp = numpy.zeros((n_particles,2))
# just accelerating to upper-right, no box limits yet

# ----------
# Animation Setup

fig = plt.figure()
axes = fig.add_subplot(1,1,1) # one row, one column, first plot

axes.scatter(x[:,0],x[:,1],c='blue')

for i in range(1,n_steps):
    x += xp*step_size
    xp += xpp*step_size
    differences = []
    distances = []
    for j in range(1,n_particles):
        difference = x - x[j,:]
        #differences.append(difference) GENERATE INTERPARTICLE FORCES !!!
    x = x%1 # bring everything back to 1x1 box.

axes.scatter(x[:,0],x[:,1],c='red')
plt.show()
