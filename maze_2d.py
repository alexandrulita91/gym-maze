import gym
import gym_maze
import time

DIRECTIONS = ["N", "S", "E", "W"]

if __name__ == "__main__":
    env = gym.make("maze-sample-5x5-v0")
    env.reset()
    while True:
        env.render()
        action = DIRECTIONS[env.action_space.sample()]
        env.step(action)





