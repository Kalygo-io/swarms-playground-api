from typing import Any, Optional


class Agent():
    def __init__(
        self,
        llm: Optional[Any] = None,
        agent_name: Optional[str] = "",
        system_prompt: Optional[str] = ""
    ):
        self.llm = llm
        self.name = agent_name
        self.system_prompt = system_prompt
        
    async def astream_events(
        self, task: str = None, img: str = None, *args, **kwargs
    ):
        """
        Run the Agent with LangChain's astream_events API.
        Only works with LangChain-based models.
        """
        try:
            async for evt in self.llm.astream_events(task, version="v1"):
                yield evt
        except Exception as e:
            print(f"Error streaming events: {e}")