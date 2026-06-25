# Solver equivalencies for MATLAB and Python
#
#     MATLAB      Python - SciPy    
#     ode45       RK45
#     ode23       RK23
#     ode113      DOP853
#     ode15s      BDF
#     ode23s      Radau   
#     ode23tb     LSODA (approx.)

SIMULATION_CONFIG = {

    # solver
    "solver": "RK45",

    # relative and absolute tolerances
    "rtol": 1e-8,
    "atol": 1e-8,

    # maximum step size
    "max_step": 0.01,

    # start and stop times
    "t0": 0.0,
    "tf": 30.0,

    # number of samples returned for plotting and analysis
    "num_points": 10000,

    # simulation interval processed between progress updates
    "block_size": 1.0

}