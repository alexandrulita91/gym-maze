from gym.envs.registration import register

register(
    id='maze-v0',
    entry_point='gym_maze.envs.maze_env:MazeEnvSample5x5',
    max_episode_steps=1000,
)

register(
    id='maze-sample-5x5-v0',
    entry_point='gym_maze.envs.maze_env:MazeEnvSample5x5',
    max_episode_steps=1000,
)

register(
    id='maze-random-5x5-v0',
    entry_point='gym_maze.envs.maze_env:MazeEnvRandom5x5',
    max_episode_steps=1000
)

register(
    id='maze-sample-10x10-v0',
    entry_point='gym_maze.envs.maze_env:MazeEnvSample10x10',
    max_episode_steps=2000,
)

register(
    id='maze-random-10x10-v0',
    entry_point='gym_maze.envs.maze_env:MazeEnvRandom10x10',
    max_episode_steps=2000
)

register(
    id='maze-sample-25x25-v0',
    entry_point='gym_maze.envs.maze_env:MazeEnvSample25x25',
    max_episode_steps=5000,
)

register(
    id='maze-random-25x25-v0',
    entry_point='gym_maze.envs.maze_env:MazeEnvRandom25x25',
    max_episode_steps=5000
)

register(
    id='maze-sample-50x50-v0',
    entry_point='gym_maze.envs.maze_env:MazeEnvSample50x50',
    max_episode_steps=10000,
)

register(
    id='maze-random-50x50-v0',
    entry_point='gym_maze.envs.maze_env:MazeEnvRandom50x50',
    max_episode_steps=10000
)

register(
    id='maze-sample-100x100-v0',
    entry_point='gym_maze.envs.maze_env:MazeEnvSample100x100',
    max_episode_steps=20000,
)

register(
    id='maze-random-100x100-v0',
    entry_point='gym_maze.envs.maze_env:MazeEnvRandom100x100',
    max_episode_steps=20000
)
