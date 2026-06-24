import matplotlib.pyplot as plt

from src.system import STATE_NAMES

n_states = len(STATE_NAMES)

def plot_states(t, xm, xs):

    for i in range(n_states):

        plt.figure(figsize=(10,5))
        plt.plot(t, xm[:, i], label='Master')
        plt.plot(t, xs[:, i], '--', label='Slave')

        plt.grid()
        plt.legend()

        plt.xlabel('Time [s]')
        plt.ylabel(STATE_NAMES[i])
        
        plt.savefig(
            "figures/fig_" + str(i) + "_state_" + STATE_NAMES[i] + ".pdf",
            bbox_inches="tight"
        )
        plt.savefig(
            "figures/fig_" + str(i) + "_state_" + STATE_NAMES[i] + ".png",
            bbox_inches="tight"
        )


def plot_error(t, error):

    plt.figure(figsize=(10,5))

    for i in range(n_states):

        plt.plot(t, error[:,i], label='e_' + STATE_NAMES[i])

    plt.grid()
    plt.legend()

    plt.xlabel('Time')
    plt.ylabel('Error')

    plt.title('Synchronization Errors')

    plt.savefig(
        "figures/fig_" + str(n_states+1) + "_errors.pdf",
        bbox_inches="tight"
    )
    plt.savefig(
        "figures/fig_" + str(n_states+1) + "_errors.png",
        bbox_inches="tight"
    )

def plot_attractor(master, slave):

    fig = plt.figure(figsize=(8,6))

    ax = fig.add_subplot(
        111,
        projection='3d'
    )

    ax.plot(
        master[:,0],
        master[:,1],
        master[:,2],
        label='Master'
    )

    ax.plot(
        slave[:,0],
        slave[:,1],
        slave[:,2],
        '--',
        label='Slave'
    )

    ax.legend()

    plt.savefig(
        "figures/attractor.pdf",
        bbox_inches="tight"
    )
    plt.savefig(
        "figures/attractor.png",
        bbox_inches="tight"
    )