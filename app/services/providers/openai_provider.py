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
    stream = await client.responses.create(
        model="gpt-4.1-mini",
        input=prompt,
        stream=True
    )

    async for event in stream:
        if event.type == "response.output_text.delta":
            yield event.delta