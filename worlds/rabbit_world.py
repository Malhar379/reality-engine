from engine.world import World


class RabbitWorld(World):
    def __init__(
        self,
        initial_population,
        birth_rate,
        death_rate,
        initial_grass,
        grass_consumption,
        grass_regrowth_rate,
    ):
        super().__init__()

        self.state = {
            "population": initial_population,
            "grass": initial_grass,
        }

        self.parameters = {
            "birth_rate": birth_rate,
            "death_rate": death_rate,
            "grass_consumption": grass_consumption,
            "initial_grass": initial_grass,
            "grass_regrowth_rate": grass_regrowth_rate,
        }

    def calculate_births(self):
        population = self.state["population"]
        grass = self.state["grass"]

        birth_rate = self.parameters["birth_rate"]
        initial_grass = self.parameters["initial_grass"]

        availability_factor = grass / initial_grass
        births = population * birth_rate * availability_factor

        return births

    def calculate_deaths(self):
        population = self.state["population"]
        death_rate = self.parameters["death_rate"]

        deaths = population * death_rate

        return deaths

    def consume_grass(self):
        population = self.state["population"]
        grass = self.state["grass"]

        grass_consumption = self.parameters["grass_consumption"]

        grass -= population * grass_consumption

        if grass < 0:
            grass = 0

        self.state["grass"] = grass

    def regrow_grass(self):
        grass = self.state["grass"]

        grass_regrowth_rate = self.parameters["grass_regrowth_rate"]
        initial_grass = self.parameters["initial_grass"]

        grass += grass_regrowth_rate

        if grass > initial_grass:
            grass = initial_grass

        self.state["grass"] = grass

    def update_population(self, births, deaths):
        population = self.state["population"]

        population += births - deaths

        self.state["population"] = population

    def save_history(self):
        self.history.append(self.state.copy())

    def step(self):
        births = self.calculate_births()
        deaths = self.calculate_deaths()

        self.consume_grass()
        self.regrow_grass()

        self.update_population(births, deaths)
        self.save_history()