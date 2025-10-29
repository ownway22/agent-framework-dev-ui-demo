from agent_framework import ai_function
from typing import Annotated
from agent_framework.openai import OpenAIResponsesClient

from random import randrange


conditions = ["sunny", "cloudy", "raining", "snowing", "clear"]


def get_weather(
    location: Annotated[str, "The city and state, e.g. San Francisco, CA"],
) -> str:
    """Get the current weather for a given location."""
    # Simulate weather data
    return f"The weather in {location} is {conditions[randrange(0, len(conditions))]} and {randrange(-10, 30)}°C."


def get_weather_detail(
    location: Annotated[str, "The city and state, e.g. San Francisco, CA"],
) -> str:
    """Get the detailed weather for a given location, this includes a forecast."""
    # Simulate weather data
    return (
        f"The weather in {location} is {conditions[randrange(0, len(conditions))]} and {randrange(-10, 30)}°C, "
        "with a humidity of 88%. "
        f"Tomorrow will be {conditions[randrange(0, len(conditions))]} with a high of {randrange(-10, 30)}°C."
    )


def get_agent():
    """Create and return a ChatAgent instance."""
    # Create your agent
    return OpenAIResponsesClient().create_agent(
        name='WeatherAgent',
        tools=[get_weather, get_weather_detail],
    )
