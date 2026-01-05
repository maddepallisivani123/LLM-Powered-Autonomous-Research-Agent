from agent.agent import AutonomousAgent

if __name__ == "__main__":
    agent = AutonomousAgent()
    goal = "Analyze recent AI agent research trends and summarize key findings"
    output = agent.run(goal)
    print(output)
