import numpy as np

# ----------
# Particle Class
class Particle(object):
    def __init__(self):
        self.x = np.random.random((1,2)) # [[x,y]] coordinates
        self.xp = np.zeros((1,2))
        self.radius = 0.1

    def set_velocity(self,velocity):
        self.xp = velocity
        return self
