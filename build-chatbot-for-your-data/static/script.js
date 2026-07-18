const chatBox = document.getElementById("chatBox");
const sendBtn = document.getElementById("sendBtn");
const uploadBtn = document.getElementById("uploadBtn");
const userInput = document.getElementById("userInput");
const fileInput = document.getElementById("fileInput");

function appendMessage(sender, message) {
  const msg = document.createElement("p");
  msg.innerHTML = `<strong>${sender}:</strong> ${message}`;
  chatBox.appendChild(msg);
  chatBox.scrollTop = chatBox.scrollHeight;
}

uploadBtn.addEventListener("click", async () => {
  const file = fileInput.files[0];
  if (!file) {
    alert("Selecciona un archivo PDF primero.");
    return;
  }

  const formData = new FormData();
  formData.append("file", file);

  try {
    const response = await fetch("/upload", {
      method: "POST",
      body: formData
    });

    if (!response.ok) {
      throw new Error("Error al cargar el PDF.");
    }

    const result = await response.json();
    alert(result.message);
  } catch (error) {
    alert("Error al cargar el PDF.");
    console.error(error);
  }
});

sendBtn.addEventListener("click", async () => {
  const prompt = userInput.value.trim();
  if (!prompt) return;

  appendMessage("Tú", prompt);
  userInput.value = "";

  try {
    const response = await fetch("/ask", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ prompt })
    });

    const result = await response.json();
    appendMessage("Bot", result.answer);
  } catch (error) {
    appendMessage("Bot", "Error al procesar la pregunta.");
    console.error(error);
  }
});
