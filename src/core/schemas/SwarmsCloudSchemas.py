import time
from typing import List, Any, Dict, Optional, Literal, Union
import uuid
from pydantic import BaseModel, model_validator, Field

from core.local_swarms.swarms.models.cog_vlm import ChatCompletionResponseChoice, ChatCompletionResponseStreamChoice, UsageInfo

class AgentChatCompletionResponse(BaseModel):
    id: str = f"agent-{uuid.uuid4().hex}"
    agent_name: str = Field(
        ...,
        description="The name of the agent that generated the completion response.",
    )
    object: Literal["chat.completion", "chat.completion.chunk"]
    choices: List[
        Union[ChatCompletionResponseChoice, ChatCompletionResponseStreamChoice]
    ]
    created: Optional[int] = Field(default_factory=lambda: int(time.time()))
    usage: Optional[UsageInfo] = None
    completion_time: Optional[float] = Field(default_factory=lambda: 0.0)