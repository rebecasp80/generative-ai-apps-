from flask import Flask, render_template, request, jsonify
from worker import translate_text
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/translate", methods=["POST"])
def translate():
    data = request.get_json()

    text = data.get("text")
    source_lang = data.get("source_lang")
    target_lang = data.get("target_lang")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    translation = translate_text(text, source_lang, target_lang)

    return jsonify({"translation": translation})

if __name__ == "__main__":
    app.run(debug=True)
