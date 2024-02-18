import pyvectorguidance
import numpy as np

def main():
    r = np.array([11.74149774, 2.33579398, 13.30108823])
    v = np.array([0.56447553, 6.19976263, 5.48968756])

    print(pyvectorguidance.__spec__)
    interception_instance = pyvectorguidance.BoundedInterception()

    tgo = interception_instance.interception_tgo_bounded(r, v)
    u = interception_instance.interception_controller_bounded(r, v, tgo)

    print(tgo, u)


if __name__ == "__main__":
    main()
