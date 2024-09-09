from fastapi import APIRouter
from .completion import router as completion
from .healthcheck import router as healthcheck
from .designSwarm import router as designSwarm

# Create the main users router
router = APIRouter()

# Include the individual routers from each endpoint file
router.include_router(completion)
router.include_router(healthcheck)
router.include_router(designSwarm)