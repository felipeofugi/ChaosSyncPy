import numpy as np

from scipy.integrate import solve_ivp

from src.synchronization import master_slave_system
from src.disturbances import (WhiteNoise, Sinusoidal, NoDisturbance)
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
sol = solve_ivp(
    lambda t, state:
        master_slave_system(t, state, n_states, disturbance),
    [SIMULATION_CONFIG["t0"],
     SIMULATION_CONFIG["tf"]],
    initial_state,

    method=SIMULATION_CONFIG["solver"],

    rtol=SIMULATION_CONFIG["rtol"],
    atol=SIMULATION_CONFIG["atol"],

    max_step=SIMULATION_CONFIG["max_step"],

    t_eval=np.linspace(
        SIMULATION_CONFIG["t0"],
        SIMULATION_CONFIG["tf"],
        SIMULATION_CONFIG["num_points"]
    )
)

# results
xm = sol.y[:n_states].T
xs = sol.y[n_states:].T

error = xs - xm

# plots
plot_states(sol.t, xm, xs)

plot_error(sol.t, error)

plot_attractor(xm, xs)