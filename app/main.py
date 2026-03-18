from fastapi import FastAPI
from app.api.routes.ai import router as ai_router

from app.db.base import Base
from app.db.session import engine
from app.models.ai_usage_log import AIUsageLog

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(ai_router)