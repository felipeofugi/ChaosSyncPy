import numpy as np

# put the names of the states (ex: x, y, z, w, etc. or x1, x2, x3, x4, etc.)
STATE_NAMES = [
    "x",
    "y",
    "z"
]

def system(t, state):

    # constants
    sigma=10.0
    rho=28.0
    beta=8.0/3.0

    #states of the system
    x, y, z = state

    # dynamic system equations
    dynamic_system = [
        sigma * (y - x),
        x * (rho - z) - y,
        x * y - beta * z
    ]

    if len(STATE_NAMES) != len(dynamic_system):
        raise ValueError(
            "STATE_NAMES and dynamic_system must have the same number of dimensions"
        )

    return np.array(dynamic_system)