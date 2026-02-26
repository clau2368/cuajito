from fastapi import FastAPI
from pydantic import BaseModel
from intents import obtener_respuesta

app = FastAPI()

class ChatRequest(BaseModel):
    mensaje: str

@app.get("/")
def inicio():
    return {"mensaje": "Cuajito está en vivo 🐻"}

@app.post("/chat")
def chat(data: ChatRequest):
    respuesta = obtener_respuesta(data.mensaje)
    return {"respuesta": respuesta}