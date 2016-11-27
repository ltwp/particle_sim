import numpy as np
import matplotlib.pyplot as plt

n_particles = 100
n_steps = 10
step_size = 0.1

x = np.random.random((n_particles,2))
# make array of randomized 0-1 particle positions (X,Y)

xp = np.zeros((n_particles,2))

xpp = np.ones((n_particles,2))
# just accelerating to upper-right, no box limits yet

for i in range(1,n_steps):
    x += xp*step_size
    xp += xpp*step_size
    print(x)
    plt.scatter(x[:,0],x[:,1])

plt.show()