# Reality Engine

A modular simulation framework built in Python for modeling state-based systems that evolve over time.

The project separates the simulation engine from the worlds it simulates, allowing different systems to share the same execution pipeline.

## Features

- Modular simulation engine
- Object-oriented world abstraction
- Multiple interchangeable simulation worlds
- History recording for every timestep
- Generic visualization for any time series
- Easy extension with new worlds

## Project Structure

```text
reality-engine/
│
├── engine/
│   ├── world.py
│   ├── simulate.py
│   └── visualize.py
│
├── worlds/
│   ├── rabbit_world.py
│   └── disease_world.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Implemented Worlds

### Rabbit Ecosystem

Models an ecosystem where:

- Rabbits reproduce
- Rabbits die naturally
- Rabbits consume grass
- Grass regrows over time

State variables:

- Population
- Grass

---

### Disease Spread

Models disease propagation using three interacting groups:

- Susceptible
- Infected
- Recovered

State variables evolve according to configurable spread and recovery rates.

---

## Running

```bash
python main.py
```

Select the desired simulation by uncommenting the corresponding example in `main.py`.

## Requirements

- Python 3.14
- matplotlib

## Future Extensions

The engine is designed to support additional worlds such as:

- Predator–Prey ecosystems
- Financial markets
- Resource allocation systems
- Cellular automata
- Custom user-defined simulations