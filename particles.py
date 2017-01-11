import numpy
from matplotlib import pyplot as plt

# ----------
# Particle Deets
class Particle(object):
    def __init__(self):
        self.x = numpy.random.random((1,2))
        self.xp = numpy.zeros((1,2))
        self.xpp = numpy.zeros((1,2))

    def set_velocity(self,velocity):
        self.xp = velocity

    def set_acceleration(self,acceleration):
        self.xpp = acceleration

    def step(self,step_size):
        self.x += self.xp*step_size
        self.xp += self.xpp*step_size
        self.x = self.x%1 # bring everything back to 1x1 box.

# ----------
# Simulation Setup

n_particles = 100
n_steps = 100
step_size = 0.1

test = Particle

particles = []
for i in range(1,n_particles):
    particles.append(Particle)


# ----------
# Animation Setup

fig = plt.figure()
axes = fig.add_subplot(1,1,1) # one row, one column, first plot

#axes.scatter(x[:,0],x[:,1],c='blue')

#for i in range(1,n_steps):

#axes.scatter(x[:,0],x[:,1],c='red')
plt.show()
