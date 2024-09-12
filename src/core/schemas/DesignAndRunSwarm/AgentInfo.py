from pydantic import BaseModel, Field


class AgentInfo(BaseModel):
    name: str = Field(
        ...,
        title="Agent name",
        description="The name of the agent.",
    )
    # agent_description: str = Field(
    #     ...,
    #     description = "A financial agent that provides information on financial topics.",
    # )
    system_prompt: str = Field(
        ...,
        description="A custom system prompt for the agent that is very direct and provides instructions and multi-examples on how to complete it's task!",
    )
    # Max loops to run the agent
    # max_loops: int = Field(
    #     1,
    #     description="The maximum number of loops the agent will run for",
    # )
    # task: str = Field(
    #     ...,
    #     description="The very specific task that the agent is supposed to complete. This is the task that the user wants the agent to complete. Make it very specific and clear.",
    # )