from env.environment import OpenEnv
from env.models import Action
import time

def run():
    env = OpenEnv()
    obs = env.reset()

    total_score = 0
    steps = 0

    while True:
        action = Action(response="important bug remove")

        obs, reward, done, _ = env.step(action)

        total_score += reward
        steps += 1

        if done:
            break

    print("Final Score:", total_score / steps)

if __name__ == "__main__":
    run()
    
    # Keep app alive (VERY IMPORTANT)
    while True:
        time.sleep(60)
