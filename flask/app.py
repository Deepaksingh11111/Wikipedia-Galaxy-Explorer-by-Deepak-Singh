from flask import Flask, render_template_string, request, jsonify
import wikipediaapi
import google.generativeai as genai
import os

app = Flask(__name__)

USER_AGENT = "Wikipedia2025ExplorerPRO/6.0 (Deepak Singh)"
wiki = wikipediaapi.Wikipedia(language='en', user_agent=USER_AGENT)
genai.configure(api_key="AIzaSyCWBp_K8vDpyxVl05ALnO0AmnQtUifU1x0")
MODEL_NAME = "models/gemini-2.0-flash"

HTML = """
<!DOCTYPE html>
<html lang="hi">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>🌌 Wikipedia Galaxy Explorer by Deepak Singh</title>
<style>
body {
  margin: 0;
  background: radial-gradient(circle, #000000, #020e1e, #041a33);
  color: #fff;
  font-family: "Poppins", sans-serif;
  overflow: hidden;
}
.container { text-align: center; padding-top: 80px; }
input {
  width: 300px; padding: 10px; border-radius: 12px;
  border: none; outline: none;
  background: rgba(255,255,255,0.1); color: white;
}
button {
  background: linear-gradient(45deg, #00bcd4, #03fc98);
  border: none; margin: 5px; padding: 10px 18px;
  border-radius: 10px; cursor: pointer; color: white;
  font-weight: bold; transition: 0.2s;
}
button:hover { transform: scale(1.1); }
.card {
  background: rgba(255, 255, 255, 0.1);
  margin: 40px auto; padding: 20px; border-radius: 16px; width: 70%;
  box-shadow: 0 0 20px rgba(0, 255, 255, 0.3);
}
#starCanvas {
  position: fixed; top: 0; left: 0; z-index: -1;
  width: 100%; height: 100%;
  background: radial-gradient(circle, #000010, #020a20, #000);
}
</style>
</head>
<body>
<canvas id="starCanvas"></canvas>
<div class="container">
  <h1>🌌 Wikipedia Galaxy Explorer by Deepak Singh</h1>
  <input id="query" placeholder="Type or Speak a topic..." />
  <button onclick="searchWiki()">🔍 Search</button>
  <button onclick="voiceSearch()">🎙️ Speak</button>
  <button onclick="aiExplain()">🤖 AI Explain</button>
  <div id="output" class="card"></div>
</div>
<script>
async function searchWiki() {
  const query = document.getElementById("query").value;
  const output = document.getElementById("output");
  output.innerHTML = "🔍 Searching Wikipedia...";
  const res = await fetch("/search", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({query}),
  });
  const data = await res.json();
  if (data.error) return output.innerHTML = "❌ " + data.error;
  output.innerHTML = `<h2>${data.title}</h2><p>${data.summary}</p>`;
  speakHindi(data.summary);
}
async function aiExplain() {
  const text = document.getElementById("output").innerText;
  const output = document.getElementById("output");
  output.innerHTML += "<p>🤖 Thinking...</p>";
  const res = await fetch("/ai_explain", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({summary: text}),
  });
  const data = await res.json();
  if (data.result) {
    output.innerHTML = `<h3>🤖 आशी का जवाब:</h3><p>${data.result}</p>`;
    speakHindi(data.result);
  } else output.innerHTML = "❌ " + data.error;
}
function voiceSearch() {
  const rec = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
  rec.lang = "en-IN";
  rec.start();
  rec.onresult = (e) => {
    const text = e.results[0][0].transcript;
    document.getElementById("query").value = text;
    searchWiki();
  };
}
function speakHindi(text) {
  const u = new SpeechSynthesisUtterance(text);
  u.lang = "hi-IN"; u.pitch = 1; u.rate = 1; u.volume = 1;
  speechSynthesis.speak(u);
}
const canvas = document.getElementById("starCanvas");
const ctx = canvas.getContext("2d");
let stars = [];
function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
window.addEventListener("resize", resizeCanvas);
resizeCanvas();
for (let i = 0; i < 150; i++) {
  stars.push({
    x: Math.random() * canvas.width,
    y: Math.random() * canvas.height,
    size: Math.random() * 2,
    speed: Math.random() * 1 + 0.5,
  });
}
function animateStars() {
  ctx.fillStyle = "rgba(0, 0, 20, 0.3)";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "#00ffff";
  stars.forEach(s => {
    ctx.beginPath();
    ctx.arc(s.x, s.y, s.size, 0, Math.PI * 2);
    ctx.fill();
    s.y += s.speed;
    if (s.y > canvas.height) {
      s.y = 0;
      s.x = Math.random() * canvas.width;
    }
  });
  if (Math.random() < 0.02) {
    const sx = Math.random() * canvas.width;
    const sy = Math.random() * 100;
    for (let i = 0; i < 20; i++) {
      ctx.beginPath();
      ctx.arc(sx - i * 5, sy + i * 2, 2, 0, Math.PI * 2);
      ctx.fillStyle = "rgba(255,255,255," + (1 - i / 20) + ")";
      ctx.fill();
    }
  }
  requestAnimationFrame(animateStars);
}
animateStars();
</script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HTML)

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    query = data.get('query', '').strip()
    if not query:
        return jsonify({"error": "Empty query"}), 400
    page = wiki.page(query)
    if not page.exists():
        return jsonify({"error": "No result found"}), 404
    summary = page.summary[:1500]
    return jsonify({"title": page.title, "summary": summary})

@app.route('/ai_explain', methods=['POST'])
def ai_explain():
    data = request.json
    summary = data.get('summary', '')
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        prompt = f"आप एक दोस्ताना भारतीय AI सहायक 'आशी' हैं। इस टेक्स्ट को आसान हिंदी में 200 शब्दों में समझाइए:\n{summary}"
        response = model.generate_content(prompt)
        return jsonify({"result": response.text.strip()})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
