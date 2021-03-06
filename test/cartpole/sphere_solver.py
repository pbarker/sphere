  
import random

from environment import Env

import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
import matplotlib.pyplot as plt

from scores.score_logger import ScoreLogger

ENV_NAME = "CartPole-v1"

GAMMA = 0.95
LEARNING_RATE = 0.001

MEMORY_SIZE = 1000000
BATCH_SIZE = 20

EXPLORATION_MAX = 1.0
EXPLORATION_MIN = 0.01
EXPLORATION_DECAY = 0.995


class DQNSolver:

    def __init__(self, observation_space, action_space):
        self.exploration_rate = EXPLORATION_MAX

        self.action_space = action_space
        self.memory = deque(maxlen=MEMORY_SIZE)
        self.loss = []

        self.model = Sequential()
        self.model.add(Dense(24, input_shape=(observation_space,), activation="relu"))
        self.model.add(Dense(24, activation="relu"))
        self.model.add(Dense(self.action_space, activation="linear"))
        self.model.compile(loss="mse", optimizer=Adam(lr=LEARNING_RATE), metrics=['mae', 'acc'])

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() < self.exploration_rate:
            return random.randrange(self.action_space)
        q_values = self.model.predict(state)
        # print("qvalues: ", q_values)
        action = np.argmax(q_values[0])
        # print("action: ", action)
        return action

    def experience_replay(self):
        if len(self.memory) < BATCH_SIZE:
            return
        batch = random.sample(self.memory, BATCH_SIZE)
        for state, action, reward, state_next, terminal in batch:
            print("-------")
            print("state", state)
            print("action", action)
            print("reward", reward)
            print("obv", state_next)
            print("done", terminal)
            q_update = reward
            if not terminal:
                next_max = np.amax(self.model.predict(state_next)[0])
                print("next max: ", next_max)
                q_update = (reward + GAMMA * next_max)
            print("qUpdate: ", q_update, " for action: ", action)
            q_values = self.model.predict(state)
            print("current qvalues", q_values)
            q_values[0][action] = q_update
            print("x: ", state)
            print("y: ", q_values)
            history = self.model.fit(state, q_values, verbose=0)
            # print("history keys", history.history.keys())
            self.loss.append(history.history['loss'])
            print("loss: ", history.history['loss'])
            pred = self.model.predict(state)
            print("final qvalues: ", pred)
            print("-------")
        self.exploration_rate *= EXPLORATION_DECAY
        self.exploration_rate = max(EXPLORATION_MIN, self.exploration_rate)


def cartpole():
    env = Env('localhost:32822')
    env.make(ENV_NAME)
    score_logger = ScoreLogger(ENV_NAME)
    observation_space = env.observation_space.box.shape[0]
    action_space = env.action_space.discrete.n
    dqn_solver = DQNSolver(observation_space, action_space)
    run = 0
    while True:
        run += 1
        state = env.reset()
        # print(state)
        state = np.reshape(state, [1, observation_space])
        step = 0
        while True:
            step += 1
            # env.render()
            print("acting on state: ", state)
            action = dqn_solver.act(state)
            state_next, reward, terminal, info = env.step(action)
            reward = reward if not terminal else -reward
            state_next = np.reshape(state_next, [1, observation_space])
            dqn_solver.remember(state, action, reward, state_next, terminal)
            state = state_next
            if terminal:
                print("Run: " + str(run) + ", exploration: " + str(dqn_solver.exploration_rate) + ", score: " + str(step))
                score_logger.add_score(step, run)
                plt.plot(dqn_solver.loss)
                plt.title('Model loss')
                plt.ylabel('Loss')
                plt.xlabel('Episode')
                plt.savefig("loss.png")
                break
            dqn_solver.experience_replay()


if __name__ == "__main__":
    cartpole()