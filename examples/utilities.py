import numpy as np
import matplotlib.pyplot as plt

def update_frame(ax, drone, target, initial_drone_position, dist, tgo,  i):
    ax.scatter(drone.position[0], drone.position[1], drone.position[2], label='Drone', c='b')
    ax.scatter(target.position[0], target.position[1], target.position[2], label='Drone', c='r')

    ax.set_title(f"Miss Distance = {dist:.5} [m]\nTgo = {tgo:.6} [sec]\nTotal Scenario Time = {(i  * drone.time_step):.4} [sec]")

    if i % 2 == 1:
        ax.text(drone.position[0] - 15, drone.position[1] - 15, drone.position[2] - 10, "Drone")
        ax.text(target.position[0] + 5, target.position[1] + 5, target.position[2] + 5, "Target")
    
    ax.set_xlim(initial_drone_position[0], target.position[0]+ 30)
    ax.set_ylim(initial_drone_position[1], target.position[1]+ 30)
    ax.set_zlim(initial_drone_position[2], target.position[2]+ 30)

    if i % 2 == 0:
        ax.cla()

    plt.pause(0.0001)

def plot_miss_distance(ax, dist, i):
    ax.plot([t * 0.01 for t in i], dist, label='Drone', c='k')
    ax.set_title(f"Final Miss Distance = {dist[-1]:.5} [m]")
    ax.scatter(i[-1]* 0.01, dist[-1], c='red', s=1)
    ax.set_xlabel(f"Time [s]")
    ax.set_ylabel(f"Miss Distance [m]")
    ax.grid()

def plot_controllers(ax, controller, i, color='b', title='Drone'):
    ax.scatter([t * 0.01 for t in i], controller['x'], label=title + ' - x', c=color, linestyle='--')
    ax.scatter([t * 0.01 for t in i], controller['y'], label=title + ' - y', c=color, marker='o')
    ax.scatter([t * 0.01 for t in i], controller['z'], label=title + ' - z', c=color, marker='*')

    ax.set_title(title + f" - Control Signals vs. Time")
    ax.set_xlabel(f"Time [s]")
    ax.set_ylabel(f"Control Signals [m/s^2]")
    ax.legend()
    ax.grid()

def plot_tgo(ax, tgo, i):
    ax.plot([t * 0.01 for t in i], tgo, c='k')
    ax.set_title(f"Tgo vs Time")
    ax.set_xlabel(f"Time [s]")
    ax.set_ylabel(f"Tgo [s]")
    ax.grid()

def update_controllers(controllers, u, w):
    controllers['drone']['x'].append(u[0])
    controllers['drone']['y'].append(u[1])
    controllers['drone']['z'].append(u[2])

    controllers['target']['x'].append(w[0])
    controllers['target']['y'].append(w[1])
    controllers['target']['z'].append(w[2])
    return controllers

