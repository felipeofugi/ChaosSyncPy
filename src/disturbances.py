import numpy as np

from src.system import STATE_NAMES
from src.config import SIMULATION_CONFIG

n_states = len(STATE_NAMES)

t0 = SIMULATION_CONFIG["t0"]
tf = SIMULATION_CONFIG["tf"]
num_points = SIMULATION_CONFIG["num_points"]

class WhiteNoise:

    def __init__(self, std=0.1):

        self.noise_time = np.linspace(
            t0,
            tf,
            num_points
        )

        self.master_noise = std*np.random.randn(
            num_points,
            n_states
        )

        self.slave_noise = std*np.random.randn(
            num_points,
            n_states
        )

    def master(self, t, state):

        return np.array([
            np.interp(
                t,
                self.noise_time,
                self.master_noise[:,i]
            )
            for i in range(len(state))
        ])

    def slave(self, t, state):

        return np.array([
            np.interp(
                t,
                self.noise_time,
                self.slave_noise[:,i]
            )
            for i in range(len(state))
        ])

class Sinusoidal:

    def master(self, t, state):

        disturbances = [
            0.5*np.sin(t),
            0.5*np.cos(t),
            0.7*np.sin(t)+0.2*np.cos(t)
        ]

        if len(disturbances) != len(state):
            raise ValueError(
                "disturbances must have the same number of dimensions as the system."
            )

        return np.array(disturbances)
    
    def slave(self, t, state):

        disturbances = [
            5*np.sin(t),
            5*np.cos(t),
            7*np.sin(t)+0.2*np.cos(t)
        ]

        if len(disturbances) != len(state):
            raise ValueError(
                "disturbances must have the same number of dimensions as the system."
            )

        return np.array(disturbances)
    
class NoDisturbance:

    def master(self, t, state):

        return np.zeros_like(state)
    
    def slave(self, t, state):

        return np.zeros_like(state)
    
