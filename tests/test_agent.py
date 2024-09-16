import pytest
from unittest.mock import AsyncMock, patch, create_autospec
from src.core.classes.agent import Agent

# Fixture to create an Agent instance
@pytest.fixture
def agent():
    mock_llm = create_autospec(AsyncMock)
    return Agent(llm=mock_llm, agent_name="TestAgent", system_prompt="TestPrompt")

# Test __init__ method
def test_agent_initialization(agent):
    assert agent.llm is not None
    assert agent.name == "TestAgent"
    assert agent.system_prompt == "TestPrompt"

# Test astream_events method with successful event streaming
@pytest.mark.asyncio
async def test_astream_events_success(agent):
    mock_event = {"event": "test_event"}
    agent.llm.astream_events = AsyncMock(return_value=mock_event)
    
    events = [event async for event in agent.astream_events(task="test_task")]
    
    assert events == mock_event

# Test astream_events method when an exception is raised
@pytest.mark.asyncio
async def test_astream_events_exception(agent, capsys):
    agent.llm.astream_events.side_effect = Exception("Streaming Error")
    
    events = [event async for event in agent.astream_events(task="test_task")]
    
    assert len(events) == 0
    captured = capsys.readouterr()
    assert "Error streaming events: Streaming Error" in captured.out

# Test astream_events with various parameterizations
@pytest.mark.asyncio
@pytest.mark.parametrize("task, img, expected", [
    ("task1", None, {"event": "test_event_1"}),
    ("task2", "image_data", {"event": "test_event_2"}),
])
async def test_astream_events_parameters(agent, task, img, expected):
    agent.llm.astream_events = AsyncMock(return_value=expected)
    
    events = [event async for event in agent.astream_events(task=task, img=img)]
    
    assert events == expected

# Test for proper handling of missing task parameter
@pytest.mark.asyncio
async def test_astream_events_no_task(agent):
    mock_event = {"event": "test_event_no_task"}
    agent.llm.astream_events = AsyncMock(return_value=mock_event)
    
    events = [event async for event in agent.astream_events()]
    
    assert events == mock_event

# Test for proper handling of additional arguments
@pytest.mark.asyncio
async def test_astream_events_with_additional_args(agent):
    mock_event = {"event": "test_event_with_additional_args"}
    agent.llm.astream_events = AsyncMock(return_value=mock_event)
    
    events = [event async for event in agent.astream_events(task="test_task", additional_arg="value")]
    
    assert events == mock_event

# Test for proper handling of keyword arguments
@pytest.mark.asyncio
async def test_astream_events_with_kwargs(agent):
    mock_event = {"event": "test_event_with_kwargs"}
    agent.llm.astream_events = AsyncMock(return_value=mock_event)
    
    events = [event async for event in agent.astream_events(task="test_task", kwarg_key="kwarg_value")]
    
    assert events == mock_event