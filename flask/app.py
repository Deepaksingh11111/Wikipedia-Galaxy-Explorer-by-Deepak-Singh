import re
import streamlit as st
import wikipediaapi
import google.generativeai as genai
import streamlit.components.v1 as components

# ==============================================================================
# 1. PAGE CONFIGURATION & METADATA
# ==============================================================================
st.set_page_config(
    page_title="CyberSentry OSINT Hub",
    page_icon="🛡️",
    layout="wide"
)

# Professional, secure User-Agent to comply with Wikimedia's API policy
USER_AGENT = "CyberSentryOSINTExplorer/6.0 (Deepak Singh)"
wiki = wikipediaapi.Wikipedia(language='en', user_agent=USER_AGENT)

# Google Gemini API Core Setup with your Fresh API Key
NEW_API_KEY = "AQ.Ab8RN6L63zUkuhTEQijR1Ve1U_r_j_B20kYyhftNefq4Q_h9Ug"
genai.configure(api_key=NEW_API_KEY)
MODEL_NAME = "models/gemini-2.0-flash"

# Session State Initialization to prevent data loss across Streamlit component refreshes
if "intel_title" not in st.session_state:
    st.session_state.intel_title = ""
if "intel_body" not in st.session_state:
    st.session_state.intel_body = "System Idle. Awaiting OSINT Target Query Initialization..."

# ==============================================================================
# 2. EMBEDDED MATRIX BACKGROUND UI (HTML/CSS/JS Canvas Injection)
# ==============================================================================
matrix_html = """
<!DOCTYPE html>
<html>
<head>
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;800&display=swap');
body {
  margin: 0; color: #e0e6ed; font-family: "Poppins", sans-serif; overflow: hidden; background: transparent;
}
#matrixCanvas {
  position: fixed; top: 0; left: 0; z-index: -1; width: 100%; height: 100%;
}
.header-box { text-align: center; padding-top: 20px; }
h1 {
  background: linear-gradient(135deg, #e0f7fa 0%, #00bfa5 50%, #00796b 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  font-weight: 800; font-size: 36px; margin: 0;
  letter-spacing: -0.5px;
}
p { color: #8892b0; margin: 5px 0 20px 0; font-size: 14px; letter-spacing: 0.5px; }
</style>
</head>
<body>
<canvas id="matrixCanvas"></canvas>
<div class="header-box">
  <h1>🛡️ CyberSentry OSINT & Threat Intelligence Hub</h1>
  <p>Automated Open Source Intelligence Gathering & Secure LLM Synthesis Engine</p>
</div>
<script>
const canvas = document.getElementById("matrixCanvas");
const ctx = canvas.getContext("2d");
function resizeCanvas() {
  canvas.width = window.innerWidth; canvas.height = window.innerHeight;
}
window.addEventListener("resize", resizeCanvas);
resizeCanvas();

const chars = "0101010101ABCDEFGHIJKLMNOPQRSTUVWXYZ🛡️⚠️";
const fontSize = 14;
const columns = canvas.width / fontSize;
const drops = Array(Math.floor(columns)).fill(1);

function drawMatrix() {
  ctx.fillStyle = "rgba(13, 17, 23, 0.08)";
  ctx.fillRect(0, 0, canvas.width, canvas.height);
  ctx.fillStyle = "rgba(0, 191, 165, 0.25)";
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

# Render the high-end matrix background header
components.html(matrix_html, height=140)

# ==============================================================================
# 3. STREAMLIT CYBERPUNK STYLING FOR SECURITY CONTROLS
# ==============================================================================
st.markdown("""
<style>
.stApp {
    background-color: #0d1117 !important;
    color: #e6edf3 !important;
}
div[data-testid="stVerticalBlock"] > div {
    background: rgba(15, 23, 42, 0.85) !important;
    border: 1px solid rgba(0, 191, 165, 0.3) !important;
    border-radius: 12px !important;
    padding: 25px !important;
    box-shadow: 0 10px 30px rgba(0,0,0,0.6) !important;
}
.stTextInput label p {
    color: #00bfa5 !important;
    font-weight: 600 !important;
    font-size: 15px !important;
}
.stTextInput input {
    background-color: #0a0f1d !important;
    border: 1px solid rgba(0, 191, 165, 0.4) !important;
    color: #00bfa5 !important;
    font-family: monospace;
    font-size: 14px;
}
.stButton > button {
    background: linear-gradient(45deg, #00796b, #00bfa5) !important;
    color: #000000 !important;
    font-weight: 800 !important;
    border: none !important;
    border-radius: 8px !important;
    height: 45px;
    width: 100%;
    transition: all 0.3s ease;
}
.stButton > button:hover {
    box-shadow: 0 0 20px rgba(0, 191, 165, 0.6) !important;
    transform: translateY(-1px);
}
div[data-testid="stNotification"] {
    background-color: #0a0f1d !important;
    border: 1px solid rgba(0, 191, 165, 0.2) !important;
}
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. DIRECT INTERACTIVE BACKEND BACKBONE
# ==============================================================================
query_input = st.text_input("🔑 System Telemetry Target Query (CVE, Vulnerability, or Threat Actor)", placeholder="e.g., Cross-Site Scripting, Ransomware, SQL Injection...")

btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("🔍 Gather OSINT Feed"):
        # 🛡️ SECURITY MITIGATION: Strict Backend Input Sanitization (Anti-XSS/SQLi)
        clean_query = re.sub(r'[^\w\s\-\.]', '', query_input).strip()
        
        if not clean_query:
            st.error("❌ Incident Alert: Null or Malformed Telemetry Input Blocked by Sanity Filter.")
        else:
            with st.spinner("📡 Querying Global OSINT Registries..."):
                page = wiki.page(clean_query)
                if page.exists():
                    st.session_state.intel_title = f"📁 CyberSentry Threat Profile: {page.title}"
                    st.session_state.intel_body = page.summary[:1500]
                else:
                    st.error("❌ Incident Alert: No threat intelligence patterns identified for specified entity.")

with btn_col2:
    if st.button("🤖 AI Core Synthesize"):
        if st.session_state.intel_body == "System Idle. Awaiting OSINT Target Query Initialization...":
            st.warning("⚠️ Action Blocked: Populate the OSINT active threat database before invoking the AI core.")
        else:
            with st.spinner("🤖 Initiating Deep CyberSentry LLM Vulnerability Analysis Core..."):
                try:
                    # 1. Attempting Live Google Gemini Processing
                    model = genai.GenerativeModel(MODEL_NAME)
                    prompt = f"आप एक अनुभवी भारतीय AI साइबर सुरक्षा विशेषज्ञ सहायक 'आशी' हैं जो 'CyberSentry' हब का संचालन करती हैं। इस तकनीकी इंटेलिजेंस सारांश को आसान हिंदी में समझाइए:\n{st.session_state.intel_body}"
                    response = model.generate_content(prompt)
                    
                    st.session_state.intel_title = "🛡️ Security Intelligence Summary (CyberSentry AI Core)"
                    st.session_state.intel_body = response.text.strip()
                except Exception as e:
                    # 2. EMERGENCY FALLBACK MATRIX: If Live API key triggers an exception, switch to deterministic logs
                    current_query = query_input.lower().strip()
                    
                    if "sql injection" in current_query or "sqli" in current_query:
                        st.session_state.intel_title = "🛡️ Security Intelligence Summary (CyberSentry Backup Matrix)"
                        st.session_state.intel_body = (
                            "नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी' और आप देख रहे हैं CyberSentry हब का बैकअप मोड। SQL Injection (SQLi) एक बेहद खतरनाक हमला है। "
                            "यह तब होता है जब एक डेवलपर यूजर के इनपुट को बिना साफ किए सीधे डेटाबेस क्वेरी में जोड़ देता है। "
                            "अटैकर इसका फायदा उठाकर चालाकी से हानिकारक SQL कोड (जैसे ' OR 1=1 --) इनपुट बॉक्स में डाल देता है। "
                            "इससे डेटाबेस भ्रमित हो जाता है और बिना पासवर्ड के लॉगिन की अनुमति दे देता है या संवेदनशील डेटा लीक कर देता है। "
                            "बचाव: इसे रोकने का एकमात्र सबसे अच्छा तरीका 'Parameterized Queries' या 'Prepared Statements' का उपयोग करना है।"
                        )
                    elif "cross-site scripting" in current_query or "xss" in current_query:
                        st.session_state.intel_title = "🛡️ Security Intelligence Summary (CyberSentry Backup Matrix)"
                        st.session_state.intel_body = (
                            "नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी' और आप देख रहे हैं CyberSentry हब का बैकअप मोड। Cross-Site Scripting (XSS) एक क्लाइंट-साइड हमला है। "
                            "इसमें हमलावर किसी वेबसाइट में दुर्भावनापूर्ण JavaScript कोड डाल देता है। जब कोई दूसरा सामान्य यूजर उस पेज पर जाता है, "
                            "तो वह कोड उसके ब्राउज़र में चल जाता है। इससे अटैकर उनके सेशन कुकीज़ (Session Cookies) चुरा सकता है। "
                            "बचाव: हमेशा इनपुट को फ़िल्टर करें और आउटपुट को एन्कोड (Output Encoding) करें।"
                        )
                    elif "nmap" in current_query:
                        st.session_state.intel_title = "🛡️ Security Intelligence Summary (CyberSentry Backup Matrix)"
                        st.session_state.intel_body = (
                            "नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी' और आप देख रहे हैं CyberSentry हब का बैकअप मोड। Nmap (Network Mapper) एक ओपन-सोर्स इंफ्रास्ट्रक्चर टूल है। "
                            "इसका उपयोग नेटवर्क में यह पता लगाने के लिए किया जाता है कि कौन से डिवाइसेस एक्टिव हैं और कौन से पोर्ट्स (Ports) खुले हैं। "
                            "यह सुरक्षा टीमों को उनकी कमियों को ढूंढने में मदद करता है, लेकिन इसका उपयोग हमलावर टोही (Reconnaissance) के लिए भी कर सकते हैं।"
                        )
                    else:
                        # 🛡️ SECURITY MITIGATION: Secure Error Handling against Information Leakage
                        st.error("❌ CyberSentry Exception: Core processing engine terminated data relay to protect framework integrity.")

# ==============================================================================
# 5. DATA TELEMETRY OUTPUT DISPLAY
# ==============================================================================
st.write("")
if st.session_state.intel_title:
    st.markdown(f"### {st.session_state.intel_title}")

st.info(st.session_state.intel_body)
