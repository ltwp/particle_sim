import numpy as np
from particle import Particle

# ----------
# Cloud Class - a collection of particles.
class Cloud(object):
    def __init__(self, n, exf, ippf):
        self.particles = []
        self.ex_force = exf # expecting a generic vector...?
        self.ipp_force = ippf # expecting a function with argument d(istance)
        for i in range(n):
            particle = Particle()
            self.particles.append(particle)

    def set_ex_force(self, exf):
        self.ex_force = exf # interparticle force law
        return self.particles

    def set_ipp_force(self, ippf):
        self.ipp_force = ippf
        return self.particles

    def step(self,step_size):
        # EXTERNAL FORCE
        for particle in self.particles:
            particle.accelerate(self.ex_force, step_size)
            particle.move(step_size)
            particle.edge_check(1, 1)

        pass
        # something iffy here, recreating particles instead of moving them.

        # INTERNAL FORCE

        # EDGE CONDITIONS

    def locations(self):
        locations = np.zeros((1,2))
        for particle in self.particles:
            locations = np.append(locations, particle.x, axis=0)
        locations = np.delete(locations,(0),axis=0) # remove first line of zeros
        return locations
