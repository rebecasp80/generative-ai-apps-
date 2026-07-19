const chatBox = document.getElementById("chat-box");
const textInput = document.getElementById("text-input");
const sendBtn = document.getElementById("send-btn");
const recordBtn = document.getElementById("record-btn");

let recognition;
let isRecording = false;

// STT
if ("webkitSpeechRecognition" in window) {
    recognition = new webkitSpeechRecognition();
    recognition.lang = "es-ES";
    recognition.interimResults = false;

    recognition.onresult = (event) => {
        const text = event.results[0][0].transcript;
        textInput.value = text;
    };

    recognition.onerror = () => {
        alert("Error en reconocimiento de voz.");
    };
}

recordBtn.addEventListener("click", () => {
    if (!recognition) return alert("Tu navegador no soporta STT.");

    if (!isRecording) {
        recognition.start();
        recordBtn.textContent = "🔴";
        isRecording = true;
    } else {
        recognition.stop();
        recordBtn.textContent = "🎤";
        isRecording = false;
    }
});

// Enviar texto
sendBtn.addEventListener("click", async () => {
    const text = textInput.value.trim();
    if (!text) return;

    const sourceLang = document.getElementById("source-lang").value;
    const targetLang = document.getElementById("target-lang").value;

    addMessage(text, "user");

    const response = await fetch("/translate", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            text,
            source_lang: sourceLang,
            target_lang: targetLang
        })
    });

    const data = await response.json();

    addMessage(data.translation, "ai");
    speakText(data.translation, targetLang);

    textInput.value = "";
});

function addMessage(text, sender) {
    const div = document.createElement("div");
    div.classList.add("message", sender);
    div.textContent = text;
    chatBox.appendChild(div);
    chatBox.scrollTop = chatBox.scrollHeight;
}

function speakText(text, lang) {
    const utter = new SpeechSynthesisUtterance(text);
    utter.lang = lang;
    speechSynthesis.speak(utter);
}
