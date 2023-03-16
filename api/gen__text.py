from fastapi import FastAPI
from pydantic import BaseModel
import openai
import os

app = FastAPI()

openai.api_key = os.environ["OPENAI_API_KEY"]
model_engine = "davinci"

class TextRequest(BaseModel):
    text: str
    max_tokens: int = 50
    temperature: float = 0.5
    top_p: float = 1
    frequency_penalty: float = 0
    presence_penalty: float = 0

@app.post("/generate_text")
async def generate_text(request: TextRequest):
    prompt = request.text
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=request.max_tokens,
        temperature=request.temperature,
        top_p=request.top_p,
        frequency_penalty=request.frequency_penalty,
        presence_penalty=request.presence_penalty,
    )
    return {"text": response.choices[0].text}
