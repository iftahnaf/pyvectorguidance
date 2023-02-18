import pyvectorguidance
import numpy as np

def main():
    vg = pyvectorguidance.VectorGuidance()
    r = np.random.rand(3) * np.random.uniform(40, 60, size=1)
    v = np.random.rand(3) * np.random.uniform(5, 15, size=1)
    vm = np.random.rand(3) * np.random.uniform(0, 2, size=1)

    k = 0.035
    rho_u = 10
    gz = 9.81

    tgo = vg.interception_tgo_bounded(r, v, vm, k, rho_u)[0]
    u = vg.interception_controller_bounded(r, v, rho_u, tgo, gz)

    print(tgo, u)


if __name__ == "__main__":
    main()
