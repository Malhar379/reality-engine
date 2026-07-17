import matplotlib.pyplot as plt


def plot_time_series(time_series, title="Simulation", save_path=None):
    """
    Plot one or more simulation time series.
    """

    for key, value in time_series.items():
        plt.plot(value, label=key)

    plt.xlabel("Time Step")
    plt.ylabel("Value")
    plt.title(title)

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    if save_path is not None:
        plt.savefig(save_path, dpi=300)

    plt.show()