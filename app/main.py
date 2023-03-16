from connections.openia_conn import get_openai_api_key 
from connections.redis_conn import redis_client 
from fastapi import FastAPI, Form
import openai

app = FastAPI()  
openai.api_key = get_openai_api_key()

@app.get("/generate_text")
async def get_text(prompt: str):
    completions = openai.Completion.create(
        engine="davinci",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = completions.choices[0].text
    return message.strip()

@app.post('/inputText')
async def ruta(formulario: str = Form(...)):
    return {'formulario': formulario}




