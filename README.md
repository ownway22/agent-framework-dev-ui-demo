# 🤖 Agent Framework Dev UI Demo

這是一個使用 Microsoft [Agent Framework](https://github.com/microsoft/agent-framework) 構建的範例專案，展示了如何建立 Agents、Workflows 以及更複雜的 Magentic 工作流。

## 📂 專案結構

```text
agent-framework-dev-ui-demo/
├── agent.py
├── magentic_workflow_as_agent.py
├── main.py
├── pyproject.toml
├── README.md
├── uv.lock
├── workflow.py
└── __init__.py
```

本專案包含三個主要範例，分別展示了 Agent Framework 的不同功能：

1. **🌤️ 簡單 agent (Simple Agent)** (`agent.py`):
   * 展示如何建立一個基本的 `WeatherAgent`。
   * 包含自定義工具 (`get_weather`, `get_weather_detail`) 來模擬獲取天氣資訊。

2. **📧 電子郵件分類工作流 (Email Triage Workflow)** (`workflow.py`):
   * 展示了一個複雜的 `EmailTriageWorkflow`。
   * 功能包括：
     * **🛡️ 垃圾郵件檢測**：分析郵件內容並分類為非垃圾郵件 (NotSpam)、垃圾郵件 (Spam) 或不確定 (Uncertain)。
     * **🔀 多路徑路由**：使用多重選擇邊緣群組 (Multi-Selection Edge Group) 根據分析結果將郵件路由到不同的處理器。
     * **✍️ 自動回覆**：協助撰寫專業的郵件回覆。
     * **📝 摘要生成**：針對較長的非垃圾郵件自動生成摘要。
     * **💾 模擬資料庫存儲**：模擬將處理結果存入資料庫。

3. **🧠 Magentic 工作流 (Magentic Workflow)** (`magentic_workflow_as_agent.py`):
   * 展示如何使用 `MagenticBuilder` 構建協作式工作流。
   * 包含兩個角色：
     * **🔍 ResearcherAgent**：專注於資訊檢索 (使用 `gpt-4o-search-preview` 模型)。
     * **💻 CoderAgent**：專注於數據分析和代碼執行 (使用 `HostedCodeInterpreterTool`)。
   * 適用於需要研究和計算的複雜任務，例如比較機器學習模型的能源效率。

## ⚙️ 安裝與設定

### 📋 前置需求

* Python 3.10 或更高版本
* OpenAI API Key (需要配置環境變數)

### 📦 安裝依賴

本專案使用 `pyproject.toml` 管理依賴。請確保您已安裝相關套件：

```bash
pip install .
```

或者直接安裝 `agent-framework` 和 `ruff`：

```bash
pip install agent-framework ruff>=0.13.3
```

### 🔑 環境變數設定

請確保您的環境中已設定 OpenAI 相關的環境變數，以便 Agent Framework 可以調用模型。

您可以複製 `.env_example` 檔案並重新命名為 `.env`，然後填入您的設定：

```bash
cp .env_example .env
```

主要環境變數說明：

* `OPENAI_API_KEY`: 您的 OpenAI API 金鑰
* `OPENAI_CHAT_MODEL_ID`: 聊天模型 ID (例如 `gpt-4o`)
* `OPENAI_RESPONSES_MODEL_ID`: 回應模型 ID (例如 `gpt-4o`)
* `ENABLE_OTEL`: 是否啟用 OpenTelemetry (預設 `true`)

## 🚀 如何執行

本專案使用 `agent_framework.devui` 來啟動一個本地的開發者介面，讓您可以直觀地與 agent 和工作流互動。

執行 `main.py` 啟動服務：

```bash
python main.py
```

啟動後，瀏覽器應會自動打開 `http://localhost:8080`。您可以在介面上選擇並測試以下實體：

* `WeatherAgent`
* `EmailTriageWorkflow`
* `MagenticWorkflow`

## 📚 參考資源

* [Introducing Microsoft Agent Framework | Microsoft Azure Blog](https://azure.microsoft.com/en-us/blog/introducing-microsoft-agent-framework/)
* [Microsoft Agent Framework Quick Start | Microsoft Learn](https://learn.microsoft.com/en-us/agent-framework/tutorials/quick-start?pivots=programming-language-python)
* [Microsoft Agent Framework documentation | Microsoft Learn](https://learn.microsoft.com/en-us/agent-framework/)
* [microsoft/agent-framework: A framework for building, orchestrating and deploying AI agents and multi-agent workflows | GitHub](https://github.com/microsoft/agent-framework)
