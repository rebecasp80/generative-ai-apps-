# 🤖 Babel Voice Assistant — Traductor de Voz Multilingüe con Flask + Groq + LangChain

Este proyecto implementa un asistente de voz capaz de escuchar, transcribir, traducir y hablar en múltiples idiomas utilizando Groq, LangChain 1.x y un servidor Flask.

Incluye una interfaz web moderna estilo AI Purple, con diseño tecnológico, efectos brillantes y experiencia fluida para traducción automática.

Forma parte del repositorio Generative AI Apps, donde se desarrollan aplicaciones de IA generativa para portafolios profesionales.

---

## 🚀 Características principales

🎤 Reconocimiento de voz (STT)

Convierte voz a texto usando la Web Speech API del navegador.

🔊 Síntesis de voz (TTS)

El asistente pronuncia la traducción en el idioma destino seleccionado.

🌐 Traducción automática con Groq + LangChain

Traducción rápida y precisa utilizando:

Groq (modelo llama-3.1-8b-instant)

LangChain 1.x

Arquitectura moderna basada en Runnables

🧠 Detección automática del idioma origen

El usuario puede hablar en cualquier idioma y el sistema lo detecta automáticamente.

🌍 Selector de idioma destino

Traducción disponible a:

Español

Inglés

Francés

Alemán

Italiano

Portugués

Japonés

Chino

Ruso

Árabe

---

## 🎨 Interfaz AI Purple

Diseño moderno con:

Fondo degradado púrpura

Efectos brillantes

Contenedores con blur

Botones luminosos

Chat estilizado

Scroll automático

---

## ⚡ Servidor Flask

Rutas:

/ → interfaz web

/translate → procesamiento de traducción

---

## 📁 Estructura del proyecto

Código

babel-voice-assistant/

│

├── app.py                 # Servidor Flask

├── worker.py              # Traducción con Groq + LangChain

│

├── templates/

│   └── index.html         # Interfaz AI Purple

│

├── static/

│   ├── style.css          # Estilos modernos

│   └── script.js          # Lógica del frontend (STT, TTS, fetch)

│

└── .env                   # API Key de Groq

---

## 🔧 Requisitos

Instala las dependencias dentro de tu entorno virtual:

bash

pip install flask langchain langchain-core langchain-community langchain-groq faiss-cpu sentence-transformers python-dotenv

---

## 🔑 Configuración de la API de Groq

En tu archivo .env:

Código

GROQ_API_KEY=tu_clave_aquí

Modelo utilizado:

Código

llama-3.1-8b-instant

▶️ Ejecutar el asistente de voz

Desde la carpeta del proyecto:

bash

python app.py

Luego abre en tu navegador:

Código

http://127.0.0.1:5000

---

## 🧠 Rutas del servidor

GET /

Renderiza la interfaz web.

POST /translate

Recibe texto, detecta idioma origen, traduce al idioma destino y devuelve la respuesta.

---

## 🎨 Interfaz web (AI Purple)

Incluye:

Fondo púrpura con degradado radial

Contenedores con blur

Botones luminosos

Selector de idiomas

Chat estilizado

Scroll automático

Micrófono integrado

TTS automático

Diseñada para transmitir una estética moderna, tecnológica y profesional.

---

## 📌 Objetivo del proyecto

Este módulo forma parte del repositorio Generative AI Apps, demostrando habilidades en:

IA generativa

Traducción automática

Flask

Groq

LangChain 1.x

Diseño web moderno

Integración STT + TTS

Aplicaciones interactivas

---

## 👩‍💻 Autora

Proyecto desarrollado por Rebeca Soto como parte de su portafolio profesional de Ingeniería de IA generativa.

Repositorio: Generative AI Apps  

Tecnologías: Python, Flask, Groq, LangChain, HTML/CSS, JavaScript

---

## 📄 Licencia

Este proyecto está bajo la licencia incluida en el repositorio principal.
