import numpy as np

# ----------
# Particle Class
class Particle(object):
    def __init__(self):
        self.x = np.random.random((1,2)) # [[x,y]] coordinates
        self.xp = np.zeros((1,2))
        self.radius = 0.1
        self.mass = 1

    def accelerate(self, force_vector, step_size):
        acceleration = np.multiply((1/self.mass), force_vector)
        self.xp = np.add(self.xp, np.multiply(step_size, acceleration))
        return self

    def move(self, step_size):
        self.x = np.add(self.x, np.multiply(step_size, self.xp))
        return self

    def edge_check(self, xmax, ymax):
        self.x = self.x % 1

    def set_velocity(self, velocity):
        self.xp = velocity
        return self

    def set_position(self, position):
        self.x = position
        return self
