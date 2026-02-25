import re
import random

# ===============================
# MEMORIA SIMPLE
# ===============================

ULTIMA_INTENCION = None


def limpiar_texto(texto):
    texto = texto.lower()
    texto = re.sub(r'[^\w\s]', '', texto)
    return texto


# ===============================
# INTENCIONES
# ===============================

INTENCIONES = {
    "saludo": {
        "palabras_clave": ["hola", "buenas", "hey", "que tal"],
        "respuestas": [
            "Hola 👋 Soy Cuajito 🐻 ¿En qué puedo ayudarte?",
            "¡Hola! 😊 Estoy aquí para orientarte sobre UAM-C.",
            "Qué gusto saludarte 👋 ¿Qué información necesitas?"
        ]
    },

    "becas": {
        "palabras_clave": ["beca", "becas", "apoyo", "apoyos", "economico"],
        "respuestas": [
            "Las becas vigentes pueden consultarse en el portal oficial de UAM-C Conecta.",
            "Puedes revisar las convocatorias de becas en la sección de apoyos estudiantiles.",
            "Existen diferentes apoyos económicos disponibles según convocatoria vigente."
        ]
    },

    "inscripciones": {
        "palabras_clave": ["inscripcion", "inscripciones", "reinscripcion", "reinscripciones"],
        "respuestas": [
            "Las inscripciones y reinscripciones se realizan según el calendario académico vigente.",
            "Revisa el calendario escolar para conocer fechas oficiales de inscripción.",
            "Las fechas de reinscripción aparecen en la página oficial de la UAM-C."
        ]
    },

    "agradecimiento": {
        "palabras_clave": ["gracias", "muchas gracias"],
        "respuestas": [
            "De nada 😊 Estoy para ayudarte.",
            "Con gusto 👋 Si necesitas algo más, dime.",
            "Siempre es un placer ayudarte 🐻"
        ]
    }
}


# ===============================
# DETECTOR
# ===============================

def detectar_intencion(pregunta):
    for nombre_intencion, datos in INTENCIONES.items():
        for palabra in datos["palabras_clave"]:
            if palabra in pregunta:
                return nombre_intencion
    return None


def obtener_respuesta(pregunta):
    global ULTIMA_INTENCION

    if not pregunta.strip():
        return "Por favor escribe una pregunta 😊"

    pregunta = limpiar_texto(pregunta)

    intencion = detectar_intencion(pregunta)

    # Si detecta intención nueva
    if intencion:
        ULTIMA_INTENCION = intencion
        return random.choice(INTENCIONES[intencion]["respuestas"])

    # Palabras que indican continuación
    continuacion = ["y", "eso", "tambien", "mas", "informacion"]

    palabras_usuario = pregunta.split()

    if any(palabra in palabras_usuario for palabra in continuacion) and ULTIMA_INTENCION:
        return f"Claro 😊 Sobre {ULTIMA_INTENCION}, puedo decirte que puedes consultar la información oficial en la página de UAM-C."

    # Si no entiende nada
    ULTIMA_INTENCION = None
    return "Lo siento 🤖 no entendí tu pregunta. ¿Podrías reformularla?"