class World:
    """
    Base class for all simulation worlds.

    Every world contains:
    - state: current variables of the simulation
    - parameters: fixed configuration values
    - history: snapshots of previous states
    """

    def __init__(self):
        self.state = {}
        self.parameters = {}
        self.history = []
