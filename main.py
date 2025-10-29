from agent_framework.devui import serve

from agent import get_agent
from workflow import get_workflow
from magentic_workflow_as_agent import get_magentic_workflow

# Get the entities to serve in the DevUI
agent = get_agent()
workflow = get_workflow()
magentic_workflow = get_magentic_workflow()

# Launch debug UI - that's it!
serve(entities=[agent, workflow, magentic_workflow], auto_open=True)
# → Opens browser to http://localhost:8080
