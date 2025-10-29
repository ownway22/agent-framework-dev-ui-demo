# Project Setup

## Description
This project contains a Python application that needs to be configured with environment variables before running.

## Environment Variables
Make sure to set up the following environment variables before running the application:

```bash
# Add your required environment variables here
# Example:
# export OPENAI_API_KEY=your_openai_api_key
# export OPENAI_CHAT_MODEL_ID=gpt-5-nano
# export OPENAI_RESPONSES_MODEL_ID=gpt-5-nano
# export ENABLE_OTEL=true

```

## Setup and Installation
This project uses UV for Python environment management. To set up the project:

1. Install UV if you haven't already:
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. Set up the environment and install dependencies:
    ```bash
    uv sync
    ```

## Running the Application
To run the application, execute:

```bash
uv run --env-file .env python main.py
```

## Prerequisites
- UV (Python package manager)
- Python 3.x (managed by UV)
