from flask import Flask, render_template, request, jsonify
from groq import Groq

app = Flask(__name__)

client = Groq(api_key="grok_api_key")

# Memoria de conversación
conversation_history = []

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    global conversation_history

    user_message = request.json["message"]

    # Añadir mensaje del usuario a la memoria
    conversation_history.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Eres un asistente amable, claro y útil."},
            *conversation_history
        ]
    )

    bot_reply = response.choices[0].message.content

    # Añadir respuesta del bot a la memoria
    conversation_history.append({"role": "assistant", "content": bot_reply})

    return jsonify({"reply": bot_reply})

@app.route("/clear", methods=["POST"])
def clear():
    global conversation_history
    conversation_history = []
    return jsonify({"status": "memoria borrada"})

if __name__ == "__main__":
    app.run(debug=True)
