# Agent

# File: tests/test_agent.py

import pytest
from unittest.mock import AsyncMock, Mock, patch
from src.core.classes.agent import Agent

@pytest.fixture
def mock_llm():
    """Fixture to create a mock LLM"""
    return AsyncMock()

@pytest.fixture
def agent(mock_llm):
    """Fixture to create an Agent instance"""
    return Agent(llm=mock_llm, agent_name="TestAgent", system_prompt="Test Prompt")

def test_agent_initialization(agent, mock_llm):
    """Test the initialization of the Agent object"""
    assert agent.llm == mock_llm
    assert agent.name == "TestAgent"
    assert agent.system_prompt == "Test Prompt"

def test_agent_initialization_defaults():
    """Test the default initialization of the Agent object"""
    agent = Agent()
    assert agent.llm is None
    assert agent.name == ""
    assert agent.system_prompt == ""

@pytest.mark.asyncio
async def test_astream_events_monkeypatch(agent, monkeypatch):
    """Test the astream_events method using monkeypatch"""
    async def mock_astream_events(*args, **kwargs):
        for event in ["event1", "event2"]:
            yield event

    monkeypatch.setattr(agent.llm, "astream_events", mock_astream_events)

    events = []
    async for event in agent.astream_events(task="test_task"):
        events.append(event)

    assert events == ["event1", "event2"]