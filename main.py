import gymnasium as gym
'''
pip install gymnasium[classic-control]
'''
# Create the Breakout environment
env = gym.make("ALE/Breakout-v5", render_mode='human')

state = env.reset()

for _ in range(1000):
    print(f"Iter: {_}")
    env.render()
    action = env.action_space.sample()  # This is a random action
    state, reward, done, info = env.step(action)[:4]
    if done:
        state = env.reset()
env.close()




