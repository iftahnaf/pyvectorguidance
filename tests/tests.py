import numpy as np
import sys
import logging
import rich
from rich.logging import RichHandler

sys.path.append("./pyvectorguidance/")

from VectorGuidance import VectorGuidance

FORMAT = "%(message)s"
logging.basicConfig(
    level="NOTSET", format=FORMAT, datefmt="[%X]", handlers=[RichHandler()]
)
logger = logging.getLogger("rich")

handle = "main"
logger = logging.getLogger(handle)

r = np.random.rand(3) * np.random.uniform(40, 60, size=1)
v = np.random.rand(3) * np.random.uniform(5, 15, size=1)
vm = np.random.rand(3) * np.random.uniform(0, 2, size=1)

k = 0.035
rho_u = 10
gz = 9.81

def test_interception_bounded():
    try:
        tgo = VectorGuidance().interception_tgo_bounded(r, v, vm, k, rho_u)[0]
    except Exception:
        logger.error(" failed - reason: error in tgo calculation!")
        return 1

    if tgo < 0:
        logger.fatal(" fatal - reason: error in tgo calculation!")
        return 1

    try:
        u = VectorGuidance().interception_controller_bounded(r, v, rho_u, tgo, gz)
    except Exception:
        logger.error(" failed - reason: error in controller calculation calculation!")
        return 1

    logger.info(" pass - test_interception_bounded")

    return 0

def main():
    test_interception_bounded()

if __name__ == "__main__":
    main()
