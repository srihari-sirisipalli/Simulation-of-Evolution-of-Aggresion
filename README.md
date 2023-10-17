# Simulation of the Evolution of Aggression

## Overview
This Python script simulates the evolution of aggression in a population of agents using the concepts of evolutionary game theory. The agents are categorized into two types: "dove" and "hawk." They compete for food, adapt their strategies, reproduce, and experience natural selection over multiple generations. This simulation explores how the relative population of each type evolves in response to varying environmental conditions.

## Description
The simulation consists of two main classes:

#### `Agent` Class:
- Represents an individual agent within the population.
- Key attributes include:
  - `type_history`: A list to record the agent's historical types ('dove' or 'hawk').
  - `food_history`: A list to track the agent's food acquisition history.
  - `current_food`: The agent's current food level, updated based on interactions.
  - `dead`: A boolean indicating whether the agent is alive or dead.

- Methods include:
  - `__init__`: Initializes an agent with an optional historical type. If not provided, the type is randomly selected.
  - `update_details`: Updates an agent's details, including food levels.
  - `current_details`: Retrieves the agent's current type and food level.
  - `print_details`: Prints the agent's key information, including its vital status, historical types, and food history.

#### `Simulation` Class:
- Manages the simulation, handling the population, competition, reproduction, survival, and data collection.

- Methods include:
  - `__init__`: Initializes the simulation with the number of agents and generations. It maintains lists of alive and dead agents, and tracks population counts.
  - `interact`: Simulates interactions between two agents, updating their food levels based on their types.
  - `compete`: Randomly shuffles the list of alive agents, allowing them to compete based on their types.
  - `reproduce`: Agents with sufficient food (2 units) can reproduce by creating new agents of the same type.
  - `survive`: Checks and updates the vital status of agents based on food levels.
  - `inject_new_agents`: Introduces new agents to the simulation, allowing customization of their type and quantity.
  - `print_statistics`: Calculates and displays population statistics.
  - `collect_data`: Gathers data on population dynamics at each generation.
  - `run`: Runs the simulation over the specified number of generations, and generates a plot illustrating population dynamics.

## How to Run
To run the simulation, follow these steps:

1. Open the script in a Python environment.
2. Configure the simulation parameters by modifying the `num_agents` and `num_generations` variables.
3. Execute the script. The simulation will run, and a plot illustrating population dynamics will be displayed at the end.

```python
num_agents = 6  # Adjust the number of agents as needed
num_generations = 100
simulation = Simulation(num_agents, num_generations)
simulation.run()
