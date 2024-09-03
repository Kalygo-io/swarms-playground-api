from typing import List
from pydantic import BaseModel
from src.core.local_swarms.swarms.schemas.step import Step


class Plan(BaseModel):
    steps: List[Step]

    class Config:
        orm_mode = True
