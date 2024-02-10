import numpy as np
import sys
import logging
import rich
from rich.logging import RichHandler
import sys
sys.path.append("/workspaces/pyvectorguidance/pyvectorguidance/build")
import libpyvectorguidance

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
logger = logging.getLogger("rich")

handle = "main"
logger = logging.getLogger(handle)

r = np.array([11.74149774, 2.33579398, 13.30108823])
v = np.array([0.56447553, 6.19976263, 5.48968756])

rho_w = 9.81
rho_u = 15
gz = 9.81

interception_instance = libpyvectorguidance.BoundedInterception()

def test_interception_bounded():
    try:
        tgo = interception_instance.bounded_interception_tgo(r, v, 0.01)
        logger.info(f"Tgo = {tgo}")
    except Exception as e:
        logger.error(" failed - reason: error in tgo calculation!")
        print(e)
        return 1

    if tgo < 0:
        logger.fatal(" fatal - reason: error in tgo calculation!")
        return 1

    try:
        u = interception_instance.bounded_interception_controller(r, v, rho_u, tgo, gz)
        logger.info(f"u = {u}")
    except Exception:
        logger.error(" failed - reason: error in controller calculation calculation!")
        return 1

    logger.info("pass - test_interception_bounded")

    return 0

def main():
    result = test_interception_bounded()
    sys.exit(result)

if __name__ == "__main__":
    main()
