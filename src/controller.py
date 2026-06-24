import numpy as np

from src.system import STATE_NAMES

def synchronization_control(error):

    # constants
    k1 = 15.0
    k2 = 15.0
    k3 = 15.0

    # controller
    control = [
        -k1*error[0],
        -k2*error[1],
        -k3*error[2]
    ]

    if len(STATE_NAMES) != len(control):
        raise ValueError(
            "STATE_NAMES and control must have the same number of dimensions."
        )

    return control