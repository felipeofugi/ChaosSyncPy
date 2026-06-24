import numpy as np

from src.system import system
from src.controller import synchronization_control

def master_slave_system(t, state, n_states, disturbance):

    master = state[:n_states]
    slave = state[n_states:]

    # disturbances
    dm = disturbance.master(t, master)
    ds = disturbance.slave(t, slave)

    master_dot = system(t, master) + dm

    error = slave - master

    control = synchronization_control(error)

    slave_dot = system(t, slave) + control + ds

    return np.concatenate([master_dot, slave_dot])