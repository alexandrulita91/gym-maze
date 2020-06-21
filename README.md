# gym-maze

A simple 2d maze environment for Open AI Gym, where the agent needs to finds its way from the top left corner to the bottom right corner.

### Action space
The agent may only choose to go up, down, left, or right ("N", "S", "W", "E"). If the way is blocked, it will remain at the same the location.

### Observation space
The observation space is the (x, y) coordinate of the agent. The top left cell is (0, 0).

### Reward
A reward of 1 is given when the agent reaches the goal. For every step in the maze, the agent recieves a reward of -0.1/(number of cells).

### End condition
The maze is reset when the agent reaches the goal. 

## Maze Versions

### Pre-generated mazes
* 5 cells x 5 cells: _MazeEnvSample5x5_
* 10 cells x 10 cells: _MazeEnvSample10x10_
* 25 cells x 25 cells: _MazeEnvSample25x25_
* 50 cells x 50 cells: _MazeEnvSample50x50_
* 100 cells x 100 cells: _MazeEnvSample100x100_

### Randomly generated mazes
* 5 cells x 5 cells: _MazeEnvRandom5x5_
* 10 cells x 10 cells: _MazeEnvRandom10x10_
* 25 cells x 25 cells: _MazeEnvRandom25x25_
* 50 cells x 50 cells: _MazeEnvRandom50x50_
* 100 cells x 100 cells: _MazeEnvRandom100x100_

## Requirements
You need Python **3.6** or **3.7** to run the script. After this, install the required packages. 
- `python setup.py install`

Another way to install the package is by using test.pypi.org.
- `pip install -i https://test.pypi.org/simple/ gym-maze-trustycoder83`


