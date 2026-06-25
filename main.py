import numpy as np

from scipy.integrate import solve_ivp

from src.synchronization import master_slave_system
from src.disturbances import (WhiteNoise, Sinusoidal, NoDisturbance)
from src.integrator import integrate_with_progress
from src.plots import plot_states
from src.plots import plot_error
from src.plots import plot_attractor

from src.config import SIMULATION_CONFIG
from src.system import STATE_NAMES

# number of states
n_states = len(STATE_NAMES)

# initial conditions
master0 = np.array([
    1.0,
    1.0,
    1.0
])

slave0 = np.array([
    -8.0,
    6.0,
    15.0
])

# disturbances. Defined in disturbances.py
disturbance = WhiteNoise(std=0.1)
#disturbance = Sinusoidal()
#disturbance = NoDisturbance()

if (len(master0) != n_states) or (len(slave0) != n_states):
    raise ValueError(
        "The master and the slave must have the same number of states as the system."
    )

initial_state = np.concatenate([
    master0,
    slave0
])

# simulation
t, states = integrate_with_progress(
    lambda t, state:
        master_slave_system(
            t,
            state,
            n_states,
            disturbance
        ),

    initial_state,

    t0=SIMULATION_CONFIG["t0"],
    tf=SIMULATION_CONFIG["tf"],

    num_points=SIMULATION_CONFIG["num_points"],

    block_size=SIMULATION_CONFIG["block_size"],

    method=SIMULATION_CONFIG["solver"],

    rtol=SIMULATION_CONFIG["rtol"],
    atol=SIMULATION_CONFIG["atol"],

    max_step=SIMULATION_CONFIG["max_step"]
)

# results
xm = states[:, :n_states]
xs = states[:, n_states:]

error = xs - xm

# plots
plot_states(t, xm, xs)

plot_error(t, error)

plot_attractor(xm, xs)