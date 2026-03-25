from sqlalchemy import Column, Integer, Text, DateTime, Float, String
from datetime import datetime
from app.db.base import Base


class AIUsageLog(Base):
    __tablename__ = "ai_usage_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, nullable=True)
    prompt = Column(Text)
    response = Column(Text)
    total_tokens = Column(Integer, nullable=True)
    estimated_cost = Column(Float, nullable=True)
    response_time_ms = Column(Integer, nullable=True)
    endpoint = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)