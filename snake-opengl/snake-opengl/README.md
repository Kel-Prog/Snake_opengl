# Snake Game in OpenGL

This project implements a classic Snake game using OpenGL for rendering and Pygame for handling user input and window management.

## Project Structure

```
snake-opengl
├── src
│   ├── main.py          # Entry point of the game
│   ├── game
│   │   ├── __init__.py  # Initializes game package
│   │   ├── snake.py     # Manages snake properties and behaviors
│   │   ├── food.py      # Represents food items in the game
│   │   └── board.py     # Manages the game board
│   └── utils
│       └── __init__.py  # Initializes utils package
├── requirements.txt      # Lists project dependencies
└── README.md             # Project documentation
```

## Requirements

To run this project, you need to install the following dependencies:

- PyOpenGL
- Pygame

You can install the required packages using pip:

```
pip install -r requirements.txt
```

## Running the Game

To start the game, run the following command in your terminal:

```
python src/main.py
```

## Controls

- Use the arrow keys to control the direction of the snake.
- The objective is to eat the food and grow the snake without colliding with the walls or itself.

## Additional Information

Feel free to modify the code to add new features or improve the game mechanics. Enjoy coding and playing!