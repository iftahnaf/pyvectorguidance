import pyvectorguidance
import numpy as np
from dynamics import SixDOFDroneDynamics
import matplotlib.pyplot as plt

def main():
    drone = SixDOFDroneDynamics()
    target = SixDOFDroneDynamics()

    vg = pyvectorguidance.VectorGuidance()

    drone.position = np.ones(3,) * np.random.uniform(0, 20, size=1)
    drone.velocity = np.ones(3,) * np.random.uniform(0, 15, size=1)

    target.position = np.ones(3,) * np.random.uniform(100, 200, size=1)
    target.velocity = np.ones(3,) * np.random.uniform(5, 15, size=1)

    initial_drone_position = drone.position.copy() - [50, 50, 50]
    initial_target_position = target.position.copy() + [100, 100, 100]

    rho_w = 9.81
    rho_u = 15.0
    gz = 9.81
    w = np.array([0.0, 0.0, 9.81]) # non maneuvering target

    tgo = 100.0

    i = 0

    fig = plt.figure(figsize=(6,6))
    ax = fig.add_subplot(111, projection='3d')

    tmp_dist = 1000.0
    dist = np.linalg.norm(target.position - drone.position)
    
    while tgo > 0.01:

        tmp_dist = dist

        r = target.position - drone.position
        v = target.velocity - drone.velocity

        tgo = vg.interception_tgo_bounded(r, v, rho_u, rho_w)
        u = vg.interception_controller_bounded(r, v, rho_u, tgo, gz)

        drone.step(u)
        target.step(w)

        dist = np.linalg.norm(target.position - drone.position)

        if i > 1000 and tmp_dist > dist:
            break

        ax.scatter(drone.position[0], drone.position[1], drone.position[2], label='Drone', c='b')
        ax.scatter(target.position[0], target.position[1], target.position[2], label='Drone', c='r')

        ax.set_title(f"Miss Distance = {dist:.5} [m]\nTgo = {tgo:.6} [sec]\nTotal Scenario Time = {(i  * drone.time_step):.4} [sec]")

        if i % 2 == 1:
            ax.text(drone.position[0] - 50, drone.position[1] - 50, drone.position[2] - 10, "Drone")
            ax.text(target.position[0] + 25, target.position[1] + 25, target.position[2] + 10, "Target")
        
        ax.set_xlim(initial_drone_position[0], initial_target_position[0])
        ax.set_ylim(initial_drone_position[1], initial_target_position[1])
        ax.set_zlim(initial_drone_position[2], initial_target_position[2])

        plt.pause(0.0001)

        if i % 2 == 0:
            ax.cla()
            
        i += 1
    print(f"Final Miss Distance = {dist:.5} [m], Total Scenario Time = {i  * drone.time_step} [sec]")

    plt.show()

if __name__ == "__main__":
    main()
