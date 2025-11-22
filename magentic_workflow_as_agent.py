# Copyright (c) Microsoft. All rights reserved.

import logging

from agent_framework import (
    ChatAgent,
    HostedCodeInterpreterTool,
    MagenticBuilder
)
from agent_framework.openai import OpenAIChatClient, OpenAIResponsesClient

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

"""
Sample: Build a Magentic orchestration and wrap it as an agent.

The script configures a Magentic workflow with streaming callbacks, then invokes the
orchestration through `workflow.as_agent(...)` so the entire Magentic loop can be reused
like any other agent while still emitting callback telemetry.

Prerequisites:
- OpenAI credentials configured for `OpenAIChatClient` and `OpenAIResponsesClient`.

I am preparing a report on the energy efficiency of different machine learning model architectures.
Compare the estimated training and inference energy consumption of ResNet-50, BERT-base, and GPT-2
on standard datasets (e.g., ImageNet for ResNet, GLUE for BERT, WebText for GPT-2).
Then, estimate the CO2 emissions associated with each, assuming training on an Azure Standard_NC6s_v3
VM for 24 hours. Provide tables for clarity, and recommend the most energy-efficient model
per task type (image classification, text classification, and text generation).
"""



def get_magentic_workflow():
    # 定義研究員 agent (ResearcherAgent)
    # 專注於資訊檢索，不進行額外的計算或定量分析
    researcher_agent = ChatAgent(
        name="ResearcherAgent",
        description="Specialist in research and information gathering",
        instructions=(
            "You are a Researcher. You find information without additional computation or quantitative analysis."
        ),
        # 這個 agent 需要 gpt-4o-search-preview 模型來執行網路搜尋 (Web Search)
        # Feel free to explore with other agents that support web search, for example,
        # the `OpenAIResponseAgent` or `AzureAgentProtocol` with bing grounding.
        chat_client=OpenAIChatClient(model_id="gpt-4o-search-preview"),
    )

    # 定義程式設計師 agent (CoderAgent)
    # 協助撰寫和執行程式碼來處理和分析數據
    coder_agent = ChatAgent(
        name="CoderAgent",
        description="A helpful assistant that writes and executes code to process and analyze data.",
        instructions="You solve questions using code. Please provide detailed analysis and computation process.",
        chat_client=OpenAIResponsesClient(),
        # 使用 HostedCodeInterpreterTool 進行程式碼執行
        tools=HostedCodeInterpreterTool(),
    )

    print("\nBuilding Magentic Workflow...")

    # 構建 Magentic 工作流
    # 使用 MagenticBuilder 將多個 agent 組合在一起
    workflow = (
        MagenticBuilder()
        .participants(researcher=researcher_agent, coder=coder_agent)
        .with_standard_manager(
            chat_client=OpenAIChatClient(),
            max_round_count=10, # 最大回合數
            max_stall_count=3,  # 最大停滯次數
            max_reset_count=2,  # 最大重置次數
        )
    )

    workflow = workflow.build()
    workflow.name = "MagenticWorkflow"
    workflow.description = "A Magentic workflow."
    return workflow
