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

#simulate(rabbit, 20)

#population = [
    #snapshot["population"]
    #for snapshot in rabbit.history
#]

#grass = [
    #snapshot["grass"]
    #for snapshot in rabbit.history
#]

#plot_time_series(
    #{
        #"Population": population,
        #"Grass": grass,
    #}
#)

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
    }
)