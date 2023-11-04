![OS](https://img.shields.io/badge/OS-Linux-red?style=flat&logo=linux)
[![Python Version](https://img.shields.io/badge/Made%20with-Python%203.10-1f425f.svg?logo=python)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-available-green.svg?style=flat&logo=docker)](https://github.com/emalderson/ThePhish/tree/master/docker)
[![Maintenance](https://img.shields.io/badge/Maintained-yes-green.svg)](https://github.com/iftahnaf/pyvectorguidance)
[![GitHub](https://img.shields.io/github/license/iftahnaf/pyvectorguidance)](https://github.com/iftahnaf/pyvectorguidance/blob/main/LICENSE)


# General Info
This repository implemented Vector Guidance methods for autonomous systems.

# Table of Contents

1. [About Vector Guidance](#about-vector-guidance)
2. [Install](#install)
3. [Usage](#usage)
4. [References](#references)

# About Vector Guidance
Vector Guidance are 3D optimal control methods for aerial systems.

The guidance laws based on a controller that minimized an finite LQ cost function with form of:

$$ J = \|\mathbf{y(t_f)}\| + k \int_{t_0}^{t_f} \|\mathbf{u(t)}\|^2 dt $$

Where:
- $y$ is the Zero-Effort-Miss (ZEM) / Zero-Effort-Velocity (ZEV) variable.
- $k$ is weight on the integration part of the cost.
- $u$ is the controller.
- $t_0$ is the initial time and $t_f$ is the final time.

Because the controller that minimized the LQ cost function is unbound, we define the maximum acceleration of the system as $u_m$, such that:

$\|\mathbf{u}\| \leq u_m$ while $t_0 \leq t \leq t_f$

**Note**: The value of $u_m$ is determine by the physical properties of the system (eg. thrusters saturations, aerodynamical constants)

# Install:

        pip install pyvectorguidance

# Usage

```python

import pyvectorguidance
import numpy as np
from dynamics import SixDOFDroneDynamics

def main():
    drone = SixDOFDroneDynamics()
    target = SixDOFDroneDynamics()

    vg = pyvectorguidance.VectorGuidance()

    drone.position = np.ones(3,) * np.random.uniform(0, 20, size=1)
    drone.velocity = np.ones(3,) * np.random.uniform(0, 15, size=1)

    target.position = np.ones(3,) * np.random.uniform(100, 200, size=1)
    target.velocity = np.ones(3,) * np.random.uniform(0, 5, size=1)

    rho_w = 9.81
    rho_u = 15.0
    gz = 9.81
    w = np.array([0.0, 0.0, 9.81]) # non maneuvering target

    tgo = 100.0
    i = 0

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
        i += 1
    print(f"Final Miss Distance = {dist:.5} [m], Total Scenario Time = {i  * drone.time_step} [sec]")

    plt.show()

if __name__ == "__main__":
    main()

```

![gif](doc/example.gif)


# References

1. S. Gutman and S. Rubinsky, "3D-nonlinear vector guidance and exo-atmospheric interception," in IEEE Transactions on Aerospace and Electronic Systems, vol. 51, no. 4, pp. 3014-3022, Oct. 2015, doi: 10.1109/TAES.2015.140204.

2. Gutman, S. (2019). Exoatmospheric Interception via Linear Quadratic Optimization. Journal of Guidance, Control, and Dynamics.

3. S. Gutman, "Rendezvous and Soft Landing in Closed Form via LQ Optimization," 2019 27th Mediterranean Conference on Control and Automation (MED), Akko, Israel, 2019, pp. 536-540, doi: 10.1109/MED.2019.8798572.