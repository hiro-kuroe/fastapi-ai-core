from app.models.ai_usage_log import AIUsageLog
from app.db.session import SessionLocal

def save_usage(prompt: str, response: str, total_tokens: int = None, user_id: int = None):
    db = SessionLocal()

    log = AIUsageLog(
        prompt=prompt,
        response=response,
        total_tokens=total_tokens,
        user_id=user_id
    )

    db.add(log)
    db.commit()
    db.close