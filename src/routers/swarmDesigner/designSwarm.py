from fastapi import APIRouter, Request, Response

import os

from slowapi.util import get_remote_address
from slowapi import Limiter
from core.classes.SwarmDesigner.openai_function_caller import OpenAIFunctionCaller
from core.prompts.BOSS_SYS_PROMPT import BOSS_SYS_PROMPT
from core.schemas.SwarmDesigner.SwarmLevel import SwarmLevel
from core.schemas.SwarmDesigner.DesignSwarmPrompt import DesignSwarmPrompt

from src.deps import jwt_dependency

limiter = Limiter(key_func=get_remote_address)

router = APIRouter()

@router.post("/design-swarm")
@limiter.limit("5/minute")  # 5 requests per minute
def designSwarm(payload: DesignSwarmPrompt, request: Request, response: Response, jwt: jwt_dependency):
    
    model = OpenAIFunctionCaller(
        system_prompt=BOSS_SYS_PROMPT,
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        base_model=SwarmLevel,
        max_tokens=5000,
    )

    swarmConfig: dict = model.run(payload.prompt)

    return {
        "swarmConfig": swarmConfig
    }