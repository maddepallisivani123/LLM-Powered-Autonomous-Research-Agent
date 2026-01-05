from tools.python_tool import run_python
from tools.search_tool import web_search

class Executor:
    def execute(self, step):
        if "python" in step.lower():
            return run_python(step)
        if "search" in step.lower():
            return web_search(step)
        return f"Executed reasoning step: {step}"
