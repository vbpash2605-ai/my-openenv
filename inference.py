import os
from openai import OpenAI
from env.environment import OpenEnv
from models import Action

client = OpenAI(api_key=os.getenv("HF_TOKEN"))

env = OpenEnv()
obs = env.reset()

total_score = 0
steps = 0

while True:
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": obs.content}]
    )

    action = Action(response=response.choices[0].message.content)

    obs, reward, done, _ = env.step(action)

    total_score += reward
    steps += 1

    if done:
        break

print("Final Score:", total_score / steps)
