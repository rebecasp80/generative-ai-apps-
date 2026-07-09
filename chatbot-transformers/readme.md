# 🤖 Chatbot Transformers — Flask + Groq + Interfaz Web

Este proyecto implementa un chatbot moderno utilizando **Groq** como motor de IA, **Flask** como servidor backend y una **interfaz web personalizada** con modo oscuro, memoria de conversación y avatar profesional.

Es parte del proyecto *Generative AI Apps*, donde se integran diferentes aplicaciones de IA generativa.

---

## 🚀 Características principales

- **Modelo Groq (llama-3.1-8b-instant)**

Respuestas rápidas, coherentes y con razonamiento real.

- **Servidor Flask**  

Maneja las rutas `/`, `/chatbot` y `/clear`.

- **Interfaz web estilo ChatGPT**  

  - Modo oscuro  

  - Avatar personalizado  

  - Burbujas de chat  

  - Scroll automático  

  - Botón para borrar memoria  

- **Memoria de conversación**  

El chatbot recuerda el contexto hasta que el usuario decide borrarlo.

---

## 📁 Estructura del proyecto

chatbot-transformers/

│

├── app.py                 # Backend Flask + Groq

│

├── templates/

│   └── index.html         # Interfaz web del chatbot

│

└── static/

├── style.css          # Estilos (modo oscuro + diseño moderno)

└── avatar.png         # Avatar del chatbot

---

## 🔧 Requisitos

Instala las dependencias dentro de tu entorno virtual:

pip install flask groq

---

## 🔑 Configuración de la API de Groq

Edita app.py y coloca tu API Key:

client = Groq("grok_api_key")

---

## ▶️ Ejecutar el chatbot

Desde la carpeta chatbot-transformers

python app.py

Luego abre en tu navegador:

http://127.0.0.1:5000

---

## 🧠 Rutas del servidor

GET /

Renderiza la interfaz web.

POST /chatbot

Envía el mensaje del usuario y devuelve la respuesta del modelo.

POST /clear

Borra la memoria de conversación.

---

## 🎨 Interfaz web

La interfaz incluye:

Modo oscuro

Avatar del chatbot

Burbujas de conversación

Botón para borrar memoria

Envío automático de mensajes

Scroll automático

---

## 📌 Objetivo del proyecto

Este módulo forma parte del repositorio Generative AI Apps, donde se construyen aplicaciones de IA generativa para tu portafolio profesional.

---

## 👩‍💻 Autora

Proyecto desarrollado por Rebeca Soto como parte de su portafolio profesional de Ingeniería de IA generativa.

Proyecto: Generative AI Apps  

Tecnologías: Python, Flask, Groq, HTML/CSS, JavaScript

---

## 📄 Licencia
Este proyecto está bajo la licencia incluida en el repositorio principal.
