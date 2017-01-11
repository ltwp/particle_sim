import numpy as np
from particle import Particle

# ----------
# Cloud Class - a collection of particles.
class Cloud(object):
    def __init__(self,n,force_law):
        self.particles = []
        self.ip_force = force_law
        for i in range(n):
            particle = Particle()
            self.particles.append(particle)

    def set_force(self,force_law):
        self.ip_force = force_law # interparticle force law
        return self.particles

    def step(self,step_size):
        # go through particle cloud and increment positions, apply forces to increment velocities
        pass

    def locations(self):
        locations = np.zeros((1,2))
        for particle in self.particles:
            #print particle.x
            locations = np.append(locations,particle.x, axis=0)
        locations = np.delete(locations,(0),axis=0) # remove first line of zeros
        return locations
