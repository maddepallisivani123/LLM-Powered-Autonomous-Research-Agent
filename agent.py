from agent.planner import Planner
from agent.executor import Executor
from agent.memory import Memory
from config import MAX_STEPS

class AutonomousAgent:
    def __init__(self):
        self.planner = Planner()
        self.executor = Executor()
        self.memory = Memory()

    def run(self, goal):
        for step_num in range(MAX_STEPS):
            plan = self.planner.create_plan(goal, self.memory.get_context())
            self.memory.add(f"Plan:\n{plan}")

            steps = plan.split("\n")
            for step in steps:
                result = self.executor.execute(step)
                self.memory.add(f"Step result: {result}")

        return self.memory.get_context()
