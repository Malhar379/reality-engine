def simulate(world, steps):
    """
    Advance a simulation world for a given number of time steps.
    """

    for _ in range(steps):
        world.step()