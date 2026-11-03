# Robotic Vacuum Navigation

A Python-based robotic vacuum navigation project developed as part of COMP10001 Foundations of Computing at the University of Melbourne (2024).

## Project Overview

The project explores grid-based navigation, state representation, obstacle avoidance, and rule-based decision-making in a simulated environment.

The environment is represented as a two-dimensional Python list, with four possible cell types:

- `X`: Current vacuum position
- `D`: Dirt requiring cleaning
- `W`: Wall or obstacle
- `E`: Empty traversable space

## My Implementation

### 1. Distance to Wall — `distance_to_wall(world)`

Implemented a function to locate the vacuum and surrounding walls within a two-dimensional grid and calculate the minimum distance using coordinate-based calculations.

### 2. Directional Movement — `make_move(world, direction)`

Implemented movement logic supporting four directions (up, down, left, and right), including:

- Identifying the vacuum's current coordinates
- Calculating the target position
- Checking grid boundaries and obstacles
- Updating the environment after valid movements
- Preserving the current state when a movement is invalid

### 3. Dirt Detection and Path Planning — `path_to_next(world)`

Developed an initial implementation to identify dirt along horizontal and vertical directions and generate movement sequences toward a detected target.

This component requires further debugging and validation.

## Technical Concepts

Python, two-dimensional lists, iteration, conditional logic, coordinate calculations, state transitions, obstacle detection, and rule-based decision-making.

## Project Status

The distance-calculation and directional-movement tasks have completion indicators in the original coursework environment. The dirt-detection component is not yet confirmed as passing.

This is an introductory rule-based navigation project rather than a fully implemented autonomous AI agent.

## Future Improvements

- Strengthen handling of empty grids and missing obstacles
- Improve dirt detection and movement prioritization
- Add automated tests covering normal and edge cases
- Integrate the individual functions into a complete navigation workflow

