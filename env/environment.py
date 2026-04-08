import random
from models import Observation, Action
from tasks import get_tasks
from grader import grade_task

class OpenEnv:
    def __init__(self):
        self.tasks = get_tasks()
        self.index = 0
        self.current_task = None

    def reset(self):
        self.index = 0
        self.current_task = self.tasks[self.index]

        return Observation(
            task=self.current_task["name"],
            content=self.current_task["input"]
        )

    def step(self, action: Action):
        score = grade_task(self.current_task, action.response)

        done = False
        self.index += 1

        if self.index >= len(self.tasks):
            done = True
        else:
            self.current_task = self.tasks[self.index]

        return (
            Observation(
                task=self.current_task["name"] if not done else "done",
                content="next"
            ),
            score,
            done,
            {}
        )

    def state(self):
        return self.current_task
