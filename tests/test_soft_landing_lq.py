import numpy as np
import sys
import logging
import rich
from rich.logging import RichHandler
import sys
sys.path.append("/workspaces/pyvectorguidance/pyvectorguidance/")
import pyvectorguidance

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
logger = logging.getLogger("rich")

handle = "main"
logger = logging.getLogger(handle)

r = np.array([100.74149774, 2.33579398, 100.30108823])
v = np.array([-0.56447553, -6.19976263, -5.48968756])


soft_landing_instance = pyvectorguidance.SoftLanding()
soft_landing_instance.um = 20.0

def test_interception_bounded():
    try:
        tgo = soft_landing_instance.soft_landing_tgo_lq(r, v, 0.01)
        logger.info(f"Tgo = {tgo}")
    except Exception as e:
        logger.error(" failed - reason: error in tgo calculation!")
        print(e)
        return 1

    if tgo < 0:
        logger.fatal(" fatal - reason: error in tgo calculation!")
        return 1

    try:
        u = soft_landing_instance.soft_landing_controller_lq(r, v, tgo)
        logger.info(f"u = {u}")
    except Exception as e:
        logger.error(" failed - reason: error in controller calculation calculation!")
        print(e)
        return 1

    logger.info("pass - test_soft_landing_lq")

    return 0

def main():
    result = test_interception_bounded()
    sys.exit(result)

if __name__ == "__main__":
    main()
