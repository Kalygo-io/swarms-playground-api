from pydantic import BaseModel

class SwarmDesignerPrompt(BaseModel):
    content: str
    sessionId: str
    agentsConfig: list
    flow: str