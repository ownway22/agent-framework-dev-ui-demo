from agent_framework.devui import serve

from agent import get_agent
from workflow import get_workflow
from magentic_workflow_as_agent import get_magentic_workflow

# 獲取要在 DevUI 中服務的實體 (Entities)
agent = get_agent()
workflow = get_workflow()
magentic_workflow = get_magentic_workflow()

# 啟動除錯 UI (Debug UI)
# serve 函數會啟動一個本地伺服器，並自動打開瀏覽器
serve(entities=[agent, workflow, magentic_workflow], auto_open=True)
# → Opens browser to http://localhost:8080
