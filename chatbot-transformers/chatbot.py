from groq import Groq

# Inicializar cliente con tu API Key
client = Groq(api_key="grok_api_key")

print("Chatbot listo 🤖. Escribe 'salir' para terminar.\n")

while True:
    user_input = input("Tú: ")
    if user_input.lower() == "salir":
        print("Chatbot: ¡Hasta luego!")
        break

    # Llamada al modelo de Groq
    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "system", "content": "Eres un asistente amable, claro y útil."},
            {"role": "user", "content": user_input}
        ]
    )

    bot_output = response.choices[0].message.content
    print(f"Chatbot: {bot_output}")
