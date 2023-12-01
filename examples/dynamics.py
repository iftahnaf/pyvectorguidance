import numpy as np

class SixDOFDroneDynamics:
    def __init__(self, time_step: float=0.01):
        self.time_step = time_step

        self.gravity = np.array([0.0, 0.0, 9.81])
        self.position = np.array([0.0, 0.0, 100.0])
        self.velocity = np.array([0.0, 0.0, 0.0])
        self.drag_coefficient = 1e-2

    def step(self, u):
        a = u - self.gravity - self.velocity**2 * self.drag_coefficient
        self.velocity += a * self.time_step
        self.position += self.velocity * self.time_step

    


def main():
    drone = SixDOFDroneDynamics()
    for i in range(1000):
        drone.step(np.array([0, 0, 0]))
        print(drone.position)

if "__main__" == __name__:
    main()