from scipy.integrate import solve_ivp
from tqdm import tqdm

import numpy as np


def integrate_with_progress(
        dynamics,
        initial_state,
        t0,
        tf,
        num_points,
        block_size,
        **solver_options):

    global_t_eval = np.linspace(
        t0,
        tf,
        num_points
    )

    current_state = initial_state
    current_t = t0

    all_t = []
    all_y = []

    n_blocks = int(
        np.ceil((tf - t0) / block_size)
    )

    with tqdm(
        total=n_blocks,
        desc="Simulation"
    ) as pbar:

        for block in range(n_blocks):

            next_t = min(
                current_t + block_size,
                tf
            )

            block_t_eval = global_t_eval[
                (global_t_eval >= current_t)
                &
                (global_t_eval <= next_t)
            ]

            sol = solve_ivp(
                dynamics,
                [current_t, next_t],
                current_state,
                t_eval=block_t_eval,
                **solver_options
            )

            if len(all_t) == 0:

                all_t.extend(sol.t)
                all_y.extend(sol.y.T)

            else:

                all_t.extend(sol.t[1:])
                all_y.extend(sol.y.T[1:])

            current_state = sol.y[:, -1]
            current_t = next_t

            pbar.update(1)

    return (
        np.array(all_t),
        np.array(all_y)
    )