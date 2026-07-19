"""
worker.py — Traducción inteligente con detección automática de idioma
Proyecto: Generative AI Voice Assistant
Autor: Rebeca Soto
"""

import os
from typing import Optional
from langdetect import detect
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# --- Configuración del entorno ---
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# --- Inicialización del modelo ---
model = ChatGroq(
    groq_api_key=GROQ_API_KEY,
    model_name="llama-3.1-8b-instant"
)

# --- Plantilla de prompt ---
prompt_template = ChatPromptTemplate.from_messages([
    ("system",
     "Eres un traductor profesional y preciso. "
     "Tu tarea es traducir el texto al idioma destino, manteniendo el tono y contexto original."),
    ("user",
     "Texto: {text}\nIdioma origen: {source}\nIdioma destino: {target}")
])

# --- Función principal de traducción ---
def translate_text(text: str, source_lang: Optional[str], target_lang: str) -> str:
    """
    Traduce texto entre idiomas utilizando Groq + LangChain.
    Si el idioma origen es 'auto', se detecta automáticamente.
    """

    try:
        # Detección automática del idioma
        if not source_lang or source_lang.lower() == "auto":
            source_lang = detect(text)

        # Construcción del pipeline
        chain = prompt_template | model
        response = chain.invoke({
            "text": text,
            "source": source_lang,
            "target": target_lang
        })

        return response.content.strip()

    except Exception as e:
        # Manejo elegante de errores
        return (
            f"⚠️ Error al traducir el texto: {str(e)}. "
            "Verifica tu conexión o la clave de API de Groq."
        )

# --- Ejemplo de uso local ---
if __name__ == "__main__":
    ejemplo = translate_text("Hola mundo", "auto", "fr")
    print(f"Traducción: {ejemplo}")
