from typing import List
from pydantic import BaseModel, Field

from core.schemas.SwarmDesigner.AgentInfo import AgentInfo

class SwarmLevel(BaseModel):
    swarm_name: str = Field(
        ...,
        description="The name of the swarm.",
    )
    rules: str = Field(
        ...,
        description="Define the rules of engagement for the agents in the swarm.",
    )
    plan: str = Field(
        ...,
        description="Create a plan for the swarm, define the goal and then create a list of agents that are needed to accomplish the goal.",
    )
    # goal: str = Field(
    #     ...,
    #     description="The goal of the swarm. Extract the goal from the user's request.",
    # )
    task: str = Field(
        ...,
        description="The task that the user wants the swarm to complete. This is the task that the user wants the agents to complete. Make it very specific and clear.",
    )
    agents: List[AgentInfo] = Field(
        ...,
        description="The list of agents participating in the swarm.",
    )
    flow: str = Field(
        ...,
        description="""
        Define the communication flow between the agents in the swarm.
        Only output the names of the agents you have created, only output the flow of the agents followed by the name.
        Use the arrow sign for sequential processing and or a comma for parallel processing.
        Ensure that the names of the agents you pass are the same as the ones you have created,
        if there are agents you have not created, do not include them in the flow. Maximum 7 agents can be in the flow at a time.

        Example A: Agent Name 1 -> Agent Name 2 -> Agent Name 3
        Example B: Agent Name 1 -> Agent Name 2, Agent Name 3
        Example C: Agent Name 1, Agent Name 2 -> Agent Name 3, Agent Name 4
        """,
    )