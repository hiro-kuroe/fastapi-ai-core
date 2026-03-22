from fastapi import APIRouter, Depends, UploadFile, File
from fastapi.responses import StreamingResponse

from app.services.providers.openai_provider import stream_text, generate_text
from app.services.ai_service import save_usage, search_context
from app.schemas.ai import AIRequest, AIResponse
from app.dependencies.auth import get_current_user
from app.db.session import SessionLocal
from app.models.ai_usage_log import AIUsageLog
from sqlalchemy.orm import Session
from app.db.session import get_db
from app.models.document import Document

router = APIRouter()

@router.post("/ai/test")
async def ai_test(
    request: AIRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    context = search_context(request.prompt, db)

    if not context:
        return AIResponse(result="No relevant information found.")

    full_prompt = f"""
    You are an AI that answers ONLY based on the proveded context.

    Use ONLY the information below.
    Do NOT use prior knowledge.
    Do NOT make assumptions.

    --- context ---
    {context}
    --- end ---

    Question:
    {request.prompt}

    Rules:
    - Answer strictly based on the context
    - If the answer is not in the context, respond with "I don't know"
    """

    result, tokens = await generate_text(full_prompt)

    print("DEBUG result:", result)
    print("DEBUG tokens:", tokens)

    if not result:
        result = "I don't know."

    return AIResponse(result=result)


@router.post("/ai/stream")
async def ai_stream(
    request: AIRequest,
    current_user=Depends(get_current_user),
    db: Session = Depends(get_db)
):

    context = search_context(request.prompt, db)

    prompt = f"""You are an internal company AI assistant.
    You must follow these rules strictly:

    [Rules]
    - Use ONLY the provided context
    - If the answer is not in the context, say "No information available"
    - Do NOT guess

    [Context]
    {context}

    [Question]
    {request.prompt}
    """

    async def generator():
        full_text = ""

        async for chunk in stream_text(prompt):
            full_text += chunk
            yield chunk

        save_usage(
            request.prompt,
            full_text,
            user_id=current_user["id"]
        )

    return StreamingResponse(generator(), media_type="text/event-stream")


@router.get("/ai/logs")
def get_logs(current_user=Depends(get_current_user)):
    db = SessionLocal()

    logs = db.query(AIUsageLog).filter(
        AIUsageLog.user_id == current_user["id"]
    ).all()

    db.close()

    return logs


@router.post("/ai/upload")
async def upload_file(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):

    content = await file.read()
    text = content.decode("utf-8")

    doc = Document(
        content=text,
        source=file.filename
    )

    db.add(doc)
    db.commit()

    return {"message": "uploaded"}