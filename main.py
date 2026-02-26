from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from intents import obtener_respuesta

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/")
def inicio():
    return {"mensaje": "Cuajito está en vivo 🐻"}

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/chat")
def chat(pregunta: str):
    respuesta = obtener_respuesta(pregunta)
    return {"respuesta": respuesta}