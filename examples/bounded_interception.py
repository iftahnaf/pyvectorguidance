import pyvectorguidance
import numpy as np
from dynamics import SixDOFDroneDynamics
import matplotlib.pyplot as plt
from utilities import update_frame, plot_controllers, plot_miss_distance, plot_tgo, update_controllers

def main():
    drone = SixDOFDroneDynamics()
    target = SixDOFDroneDynamics()

    vg = pyvectorguidance.VectorGuidance()

    drone.position = np.ones(3,) * np.random.uniform(0, 20, size=1)
    drone.velocity = np.ones(3,) * np.random.uniform(0, 15, size=1)
    drone.drag_coefficient = 1e-3

    target.position = np.ones(3,) * np.random.uniform(100, 200, size=1)
    target.velocity = np.ones(3,) * np.random.uniform(5, 15, size=1)
    target.drag_coefficient = 3e-3

    initial_drone_position = [drone.position[0], drone.position[1], drone.position[2]]

    rho_w = 10.0
    rho_u = 80.0
    gz = 9.81

    tgo = 100.0

    i = 0

    fig = plt.figure(figsize=(10,10))
    ax_frame = fig.add_subplot(111, projection='3d')

    dist = np.linalg.norm(target.position - drone.position)

    controllers = {"drone": {'x': [], 'y': [], 'z': []},
                   "target": {'x': [], 'y': [], 'z': []}}

    miss_distance = []
    miss_distance.append(dist)

    tgo_list = []

    while tgo > 0.01:

        r = target.position - drone.position
        v = target.velocity - drone.velocity

        tgo = vg.interception_tgo_bounded(r, v, rho_u, rho_w)

        u = vg.interception_controller_bounded(r, v, rho_u, tgo, gz)
        w = vg.interception_controller_bounded(r, v, rho_w, tgo, gz)

        controllers = update_controllers(controllers, u, w)

        drone.step(u)
        target.step(w)

        dist = np.linalg.norm(target.position - drone.position)
        miss_distance.append(dist)
        tgo_list.append(tgo)

        update_frame(ax_frame, drone, target, initial_drone_position, dist, tgo, i)

        i += 1

    fig_pp = plt.figure(figsize=(10,10))
    ax_md = fig_pp.add_subplot(221)
    ax_tgo = fig_pp.add_subplot(222)
    ax_ctrl_drone = fig_pp.add_subplot(223)
    ax_ctrl_target = fig_pp.add_subplot(224)

    plot_miss_distance(ax_md, miss_distance, range(i  + 1))

    plot_tgo(ax_tgo, tgo_list, range(i))

    plot_controllers(ax_ctrl_drone, controllers['drone'], range(i))
    plot_controllers(ax_ctrl_target, controllers['target'], range(i), color='red', title='Target')

    plt.close(fig)

    print(f"Final Miss Distance = {dist:.5} [m], Total Scenario Time = {i  * drone.time_step} [sec]")

    plt.show()


if __name__ == "__main__":
    main()
