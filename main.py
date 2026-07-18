from worlds.rabbit_world import RabbitWorld
from worlds.disease_world import DiseaseWorld

from engine.simulate import simulate
from engine.visualize import plot_time_series


# =====================================================
# Example 1: Rabbit Ecosystem
# =====================================================

rabbit = RabbitWorld(
    initial_population=100,
    birth_rate=0.2,
    death_rate=0.1,
    initial_grass=1000,
    grass_consumption=2,
    grass_regrowth_rate=50,
)

# Uncomment this block to run the Rabbit Ecosystem simulation.

simulate(rabbit, 100)

population = [
    snapshot["population"]
    for snapshot in rabbit.history
]

grass = [
    snapshot["grass"]
    for snapshot in rabbit.history
]

plot_time_series(
    {
        "Population": population,
        "Grass": grass,
    },
    title="Rabbit Ecosystem Simulation",
    save_path="images/rabbit_world.png",
)

peak_population = max(population)
peak_step = population.index(peak_population)
min_population = min(population)
min_step = population.index(min_population)
print(f"Rabbit peak population: {peak_population:.2f} at step {peak_step}")
print(f"Rabbit minimum population: {min_population:.2f} at step {min_step}")
print(f"Population decline from peak: {(1 - min_population/peak_population)*100:.1f}%")

# =====================================================
#Example 2: Disease Spread
#This example is enabled by default.
# =====================================================

disease_world = DiseaseWorld(
    susceptible=100,
    infected=10,
    recovered=5,
    spread_rate=0.4,
    recovery_rate=0.2,
)

simulate(disease_world, 20)

susceptible = [
    snapshot["susceptible"]
    for snapshot in disease_world.history
]

infected = [
    snapshot["infected"]
    for snapshot in disease_world.history
]

recovered = [
    snapshot["recovered"]
    for snapshot in disease_world.history
]

plot_time_series(
    {
        "Susceptible": susceptible,
        "Infected": infected,
        "Recovered": recovered,
    },
    title="Disease Spread Simulation",
    save_path="images/disease_world.png",
)

peak_infected = max(infected)
peak_step = infected.index(peak_infected)
r0 = disease_world.parameters["spread_rate"] / disease_world.parameters["recovery_rate"]
print(f"Disease peak infected: {peak_infected:.2f} at step {peak_step}")
print(f"Basic reproduction number (R0): {r0:.2f}")
print(f"Final susceptible: {susceptible[-1]:.2f}, Final recovered: {recovered[-1]:.2f}")