# turkey-map-quiz

An interactive Python `turtle` game where the player clicks cities on a Turkey map and tries to guess their names.

## Overview

This project is a simple geography quiz built with Python's standard `turtle` module. Each clickable region on the map represents a city. When the player clicks a supported city, the game asks for its name and marks the correct answer on the map.

## Features

- Interactive Turkey map interface
- Click-to-guess gameplay
- Correct answers are marked directly on the map
- Progress tracking in the window title
- No external dependencies required

## Current Coverage

The current version includes these cities:

- Ankara
- Istanbul
- Izmir

## Requirements

- Python 3
- Standard library `turtle` module

## How To Run

```bash
python turkey_map_quiz.py
```

## How To Play

1. Run the script.
2. Click one of the supported cities on the map.
3. Enter the city name in the prompt window.
4. Correct answers are marked with a check sign.
5. The game ends after all available cities are found.

## Project Files

- `turkey_map_quiz.py`: Main game script
- `turkey_map.png`: Background map image

## Possible Improvements

- Add all 81 cities
- Add a score panel or timer
- Support Turkish character input more flexibly
- Show missed cities at the end of the game
