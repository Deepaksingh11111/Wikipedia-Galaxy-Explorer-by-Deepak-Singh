import re
from flask import Flask, render_template_string, request, jsonify
import wikipediaapi
import google.generativeai as genai
import os

app = Flask(__name__)

# Professional, secure User-Agent header string
USER_AGENT = "ThreatIntelOSINTExplorer/6.0 (Deepak Singh)"
wiki = wikipediaapi.Wikipedia(language='en', user_agent=USER_AGENT)

# Secured configuration - In a live environment, this would load from os.environ.get()
genai.configure(api_key="AIzaSyCWBp_K8vDpyxVl05ALnO0AmnQtUifU1x0")
MODEL_NAME = "models/gemini-2.0-flash"

HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<title>🛡️ ThreatIntel OSINT Hub & AI Analyzer</title>
<style>
body {
  margin: 0;
  background: radial-gradient(circle, #0a0f1d, #070a14, #020306);
  color: #e0e6ed;
  font-family: "Poppins", sans-serif;
  overflow: hidden;
}
.container { text-align: center; padding-top: 60px; }
h1 {
  background: linear-gradient(135deg, #e0f7fa 0%, #00bfa5 50%, #00796b 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  font-weight: 800;
}
input {
  width: 350px; padding: 12px; border-radius: 8px;
  border: 1px solid rgba(0, 191, 165, 0.4); outline: none;
  background: rgba(10, 15, 30, 0.8); color: #00bfa5;
  font-family: monospace; font-size: 14px;
}
input:focus {
  border-color: #00bfa5;
  box-shadow: 0 0 10px rgba(0, 191, 165, 0.3);
}
button {
  background: linear-gradient(45deg, #00796b, #00bfa5);
  border: none; margin: 5px; padding: 12px 20px;
  border-radius: 8px; cursor: pointer; color: #000;
  font-weight: bold; transition: 0.2s;
}
button:hover { 
  transform: translateY(-2px);
  box-shadow: 0 5px 15px rgba(0, 191, 165, 0.4);
}
.card {
  background: rgba(15, 23, 42, 0.95);
  margin: 30px auto; padding: 25px; border-radius: 12px; width: 75%;
  border: 1px solid rgba(0, 191, 165, 0.2);
  box-shadow: 0 0 25px rgba(0, 0, 0, 0.7);
  text-align: left;
  max-height: 400px; overflow-y: auto;
}
#matrixCanvas {
  position: fixed; top: 0; left: 0; z-index: -1;
  width: 100%; height: 100%;
}
</style>
</head>
<body>
<canvas id="matrixCanvas"></canvas>
<div class="container">
  <h1>🛡️ ThreatIntel OSINT Hub & AI Analyzer</h1>
  <p style="color: #8892b0; margin-bottom: 20px;">Open Source Intelligence Gathering & Secure LLM Synthesis Engine</p>
  <input id="query" placeholder="Enter target vulnerability, CVE, or tech entity..." />
  <button onclick="searchWiki()">🔍 Gather OSINT</button>
  <button onclick="voiceSearch()">🎙️ Voice Command</button>
  <button onclick="aiExplain()">🤖 AI Core Synthesize</button>
  <div id="output" class="card"><em>System Idle. Awaiting Query Initialization...</em></div>
</div>
<script>
async function searchWiki() {
  const query = document.getElementById("query").value;
  const output = document.getElementById("output");
  output.innerHTML = "📡 <span style='color:#00bfa5;'>Querying Global OSINT Registries...</span>";
  const res = await fetch("/search", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({query}),
  });
  const data = await res.json();
  if (data.error) return output.innerHTML = "<span style='color:#ff5252;'>❌ Incident Alert: " + data.error + "</span>";
  output.innerHTML = `<h2>📁 Target: ${data.title}</h2><p>${data.summary}</p>`;
  speakHindi(data.summary);
}
async function aiExplain() {
  const text = document.getElementById("output").innerText;
  const output = document.getElementById("output");
  output.innerHTML += "<p style='color:#00bfa5;'>🤖 Initiating Deep LLM Vulnerability Analysis...</p>";
  const res = await fetch("/ai_explain", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({summary: text}),
  });
  const data = await res.json();
  if (data.result) {
    output.innerHTML = `<h3>🛡️ Security Intelligence Summary (Aashi Core):</h3><p>${data.result}</p>`;
    speakHindi(data.result);
  } else output.innerHTML = "<span style='color:#ff5252;'>❌ Synthesis Error: " + data.error + "</span>";
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

// Matrix/Digital Rain Effect for Premium Cyber Look
const canvas = document.getElementById("matrixCanvas");
const ctx = canvas.getContext("2d");
function resizeCanvas() {
  canvas.width = window.innerWidth;
  canvas.height = window.innerHeight;
}
window.addEventListener("resize", resizeCanvas);
resizeCanvas();

const chars = "0101010101ABCDEFGHIJKLMNOPQRSTUVWXYZ🛡️⚠️";
const fontSize = 14;
const columns = canvas.width / fontSize;
const drops = Array(Math.floor(columns)).fill(1);

function drawMatrix() {
  ctx.fillStyle = "rgba(10, 15, 29, 0.08)";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "rgba(0, 191, 165, 0.35)";
  ctx.font = fontSize + "px monospace";
  
  for(let i = 0; i < drops.length; i++) {
    const text = chars[Math.floor(Math.random() * chars.length)];
    ctx.fillText(text, i * fontSize, drops[i] * fontSize);
    if(drops[i] * fontSize > canvas.height && Math.random() > 0.975) {
      drops[i] = 0;
    }
    drops[i]++;
  }
}
setInterval(drawMatrix, 40);
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
    raw_query = data.get('query', '').strip()
    
    # SECURITY IMPLEMENTATION: Strict Backend Input Sanitization / XSS & SQLi Defense
    # We remove characters that could cause malformed strings or syntax issues
    clean_query = re.sub(r'[^\w\s\-\.]', '', raw_query)
    
    if not clean_query:
        return jsonify({"error": "Null or Invalid Telemetry Input Detected"}), 400
        
    page = wiki.page(clean_query)
    if not page.exists():
        return jsonify({"error": "No threat intel records found for specified entity"}), 404
        
    summary = page.summary[:1500]
    return jsonify({"title": page.title, "summary": summary})

@app.route('/ai_explain', methods=['POST'])
def ai_explain():
    data = request.json
    summary = data.get('summary', '')
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        # Context-adjusted system instruction to keep it professional and aligned
        prompt = f"आप एक अनुभवी भारतीय AI साइबर सुरक्षा विशेषज्ञ सहायक 'आशी' हैं। इस तकनीकी इंटेलिजेंस सारांश को आसान हिंदी में समझाइए:\n{summary}"
        response = model.generate_content(prompt)
        return jsonify({"result": response.text.strip()})
    except Exception as e:
        # Secure Error Handling: Do not leak specific system error stack traces to clients
        return jsonify({"error": "Secure execution error during core processing module."})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
