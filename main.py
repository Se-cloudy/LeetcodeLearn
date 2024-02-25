# This is a sample Python script.

# RL
import gym
import stable_baselines3

stable_baselines3.PPO()
from stable_baselines3 import MlpPolicy
from stable_baselines.common.vec_env import DummyVecEnv
from stable_baselines3 import PPO2

env = gym.make('CartPole-v1')
env = DummyVecEnv([lambda: env])  # The algorithms require a vectorized environment to run

model = PPO2(MlpPolicy, env, verbose=1)
model.learn(total_timesteps=10000)

obs = env.reset()
for i in range(1000):
    action, _states = model.predict(obs)
    obs, rewards, dones, info = env.step(action)
    env.render()
