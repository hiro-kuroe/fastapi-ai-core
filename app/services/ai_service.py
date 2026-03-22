from app.models.ai_usage_log import AIUsageLog
from app.db.session import SessionLocal
from sqlalchemy.orm import Session
from app.models.document import Document
import re
from sqlalchemy import or_


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
    db.close()

def search_context(prompt: str, db: Session):
    STOP_WORDS = ["とは", "なんで", "原因", "について", "教えて", "何", "の", "は"]

    clean_prompt = re.sub(r"[^\w\s]", "", prompt)

    clean_prompt = clean_prompt.replace("の", " ")

    clean_words = []
    for word in clean_prompt.split():
        for stop in STOP_WORDS:
            word = word.replace(stop, "")
        if word:
            clean_words.append(word.lower())

    if not clean_words:
        return ""

    query = db.query(Document)

    for word in clean_words[:3]:
        query = query.filter(Document.content.contains(word))

    docs = query.all()

    if not docs:
        query = db.query(Document)
        conditions = [
            Document.content.contains(word)
            for word in clean_words
        ]
        query = query.filter(or_(*conditions))
        docs = query.all()

    context = "\n---\n".join([doc.content for doc in docs])
    
    return context