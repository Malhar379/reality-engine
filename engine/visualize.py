import matplotlib.pyplot as plt


def plot_time_series(time_series):
    """
    Plot one or more simulation time series.
    """

    for key, value in time_series.items():
        plt.plot(value, label=key)

    plt.xlabel("Time Step")
    plt.ylabel("Value")
    plt.title("Simulation")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
