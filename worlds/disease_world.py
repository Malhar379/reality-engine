from engine.world import World


class DiseaseWorld(World):
    def __init__(self, susceptible, infected, recovered, spread_rate, recovery_rate):
        super().__init__()

        self.state = {
            "susceptible": susceptible,
            "infected": infected,
            "recovered": recovered,
        }

        self.parameters = {
            "spread_rate": spread_rate,
            "recovery_rate": recovery_rate,
        }

    def calculate_new_infections(self):
        susceptible = self.state["susceptible"]
        infected = self.state["infected"]
        recovered = self.state["recovered"]

        spread_rate = self.parameters["spread_rate"]

        total_population = susceptible + infected + recovered
        susceptible_fraction = susceptible / total_population

        new_infections = infected * spread_rate * susceptible_fraction

        return new_infections

    def calculate_recoveries(self):
        infected = self.state["infected"]
        recovery_rate = self.parameters["recovery_rate"]

        recoveries = infected * recovery_rate

        return recoveries

    def update_population(self, new_infections, recoveries):
        susceptible = self.state["susceptible"]
        infected = self.state["infected"]
        recovered = self.state["recovered"]

        susceptible -= new_infections
        infected += new_infections - recoveries
        recovered += recoveries

        self.state["susceptible"] = susceptible
        self.state["infected"] = infected
        self.state["recovered"] = recovered

    def save_history(self):
        self.history.append(self.state.copy())

    def step(self):
        new_infections = self.calculate_new_infections()
        recoveries = self.calculate_recoveries()

        self.update_population(new_infections, recoveries)
        self.save_history()
    


