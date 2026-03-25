from dotenv import load_dotenv
load_dotenv()

from openai import AsyncOpenAI

client = AsyncOpenAI()


async def generate_text(prompt: str) -> tuple[str, int]:
    response = await client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
    )

    text = response.choices[0].message.content
    tokens = response.usage.total_tokens

    return text, tokens

async def stream_text(prompt: str):
    stream = await client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "user", "content": prompt}
        ],
        stream=True,
        stream_options={"include_usage": True},
    )

    total_tokens = None

    async for chunk in stream:
        if chunk.usage:
            total_tokens = chunk.usage.total_tokens

        if chunk.choices and chunk.choices[0].delta.content:
            yield chunk.choices[0].delta.content, None

    yield None, total_tokens