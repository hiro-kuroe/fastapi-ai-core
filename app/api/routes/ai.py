from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse

from app.services.providers.openai_provider import stream_text, generate_text
from app.services.ai_service import save_usage
from app.schemas.ai import AIRequest, AIResponse
from app.dependencies.auth import get_current_user


router = APIRouter()

@router.post("/ai/test")
async def ai_test(
    request: AIRequest,
    current_user=Depends(get_current_user)
):

    result, tokens = await generate_text(request.prompt)

    save_usage(
        request.prompt, 
        result, 
        tokens,
        user_id=current_user["id"]
    )
    
    return AIResponse(result=result)

@router.post("/ai/stream")
async def ai_stream(request: AIRequest):

    prompt = request.prompt

    async def generator():
        full_text = ""

        async for chunk in stream_text(prompt):
            full_text += chunk
            yield chunk

        save_usage(prompt, full_text)

    return StreamingResponse(generator(), media_type="text/plain")