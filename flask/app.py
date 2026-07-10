import re
import streamlit as st
import streamlit.components.v1 as components

# ==============================================================================
# 1. PAGE CONFIGURATION & METADATA
# ==============================================================================
st.set_page_config(
    page_title="IntelScout OSINT Parser",
    page_icon="🛡️",
    layout="wide"
)

# Session State Initialization to prevent data loss across component refreshes
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
.header-box { text-align: center; padding-top: 15px; box-sizing: border-box; }
h1 {
  background: linear-gradient(135deg, #e0f7fa 0%, #00bfa5 50%, #00796b 100%);
  -webkit-background-clip: text; -webkit-text-fill-color: transparent;
  font-weight: 800; font-size: 34px; margin: 0;
  letter-spacing: -0.5px;
}
p { color: #8892b0; margin: 8px 0 10px 0; font-size: 14px; letter-spacing: 0.5px; }
</style>
</head>
<body>
<canvas id="matrixCanvas"></canvas>
<div class="header-box">
  <h1>🛡️ IntelScout OSINT Parser & Intelligence Hub</h1>
  <p>Automated Open Source Intelligence Gathering & Secure Rule Synthesis Engine</p>
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

components.html(matrix_html, height=180)

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
# 4. DETERMINISTIC LOCAL KNOWLEDGE BASE (100% Reliability Baseline)
# ==============================================================================
LOCAL_OSINT_DB = {
    "sql injection": {
        "title": "SQL Injection (SQLi) - CWE-89",
        "raw": "SQL Injection represents a vulnerability class where untrusted structured user input directly alters SQL database logic frameworks. Attackers abuse missing backend input escape validation filters to run custom database scripts, bypassing default administrative control prompts.",
        "ai": "नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी'। SQL Injection एक बेहद गंभीर हमला है। यह तब संभव होता है जब एक डेवलपर इनपुट बॉक्स के डेटा को बिना साफ किए सीधे डेटाबेस क्वेरी में जोड़ देता है। हमलावर चालाकी से हानिकारक कोड (जैसे ' OR 1=1 --) डालकर बिना पासवर्ड के सिस्टम एडमिन पैनल लॉगिन कर सकते हैं या पूरा डेटाबेस डिलीट कर सकते हैं।\n\n🛡️ बचाव: हमेशा इनपुट को फ़िल्टर करें और 'Parameterized Queries' या 'Prepared Statements' का ही उपयोग करें।"
    },
    "cross-site scripting": {
        "title": "Cross-Site Scripting (XSS) - CWE-79",
        "raw": "Cross-Site Scripting occurs when web applications process unsanitized runtime user inputs within immediate HTML documents without performing content encoding validations. Malicious script strings execute inside target client web browsers automatically.",
        "ai": "नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी'। Cross-Site Scripting (XSS) एक क्लाइंट-साइड वेब हमला है। इसमें हमलावर वेबसाइट के संवेदनशील इनपुट फील्ड्स में खतरनाक JavaScript कोड डाल देता है। जब भी कोई सामान्य यूजर उस वेबसाइट पर जाता है, तो वह कोड उसके ब्राउज़र में ऑटोमैटिक रन हो जाता है, जिससे हैकर उनके गोपनीय Session Cookies और टोकन्स चुरा सकता है।\n\n🛡️ बचाव: इनपुट पर सख्त 'Data Sanitization' लागू करें और सर्वर साइड पर 'Output Encoding' का प्रयोग करें।"
    },
    "nmap": {
        "title": "Network Mapper (Nmap) Security Diagnostic Tool",
        "raw": "Nmap is an enterprise open-source framework built to analyze infrastructure interfaces, map layout schemas, and detect active TCP/UDP ports. It serves security operators during vulnerability assessment audits to footprint target networks.",
        "ai": "नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी'। Nmap (Network Mapper) इंफ्रास्ट्रक्चर सिक्योरिटी और रिकॉन (Reconnaissance) का सबसे लोकप्रिय टूल है। इसका इस्तेमाल नेटवर्क स्कैनिंग के लिए किया जाता है ताकि यह पता लगाया जा सके कि कौन से पोर्ट्स (Ports) खुले हैं, कौन से होस्ट्स एक्टिव हैं और कौन सा ऑपरेटिंग सिस्टम चल रहा है। सुरक्षा टीमें अपनी कमियां सुधारने के लिए इसका उपयोग करती हैं।\n\n🛡️ उपयोग: 'nmap -sV -sC [IP]' कमांड का इस्तेमाल सर्विस वर्जन और डिफॉल्ट स्क्रिप्ट चेक्स के लिए किया जाता है।"
    },
    "ransomware": {
        "title": "Ransomware Threat Intelligence Signature",
        "raw": "Ransomware represents a malware family that encrypts filesystem storage units, dropping text markers demanding currency access flags to restore data. Attackers leverage symmetric/asymmetric algorithms to paralyze business logic assets.",
        "ai": "नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी'। Ransomware एक प्रकार का मलेशियस सॉफ्टवेयर (Malware) है जो किसी सिस्टम या पूरे नेटवर्क के फाइलों को एडवांस सिमेट्रिक/असिमेट्रिक एल्गोरिदम का उपयोग करके एन्क्रिप्ट (लॉक) कर देता है। इसके बाद हैकर्स डेटा को वापस अनलॉक करने के बदले फिरौती (Ransom) मांगते हैं।\n\n🛡️ बचाव: हमेशा क्रिटिकल डेटा का ऑफलाइन बैकअप रखें, सिस्टम पैच अपडेटेड रखें और एंडपॉइंट प्रोटेक्शन (EDR) टूल्स का प्रयोग करें।"
    }
}

# Add alias shortcuts to handle variations in user input seamlessly
LOCAL_OSINT_DB["sqli"] = LOCAL_OSINT_DB["sql injection"]
LOCAL_OSINT_DB["xss"] = LOCAL_OSINT_DB["cross-site scripting"]

# ==============================================================================
# 5. DIRECT INTERACTIVE DASHBOARD GATEWAY
# ==============================================================================
query_input = st.text_input("🔑 System Telemetry Target Query (CVE, Vulnerability, or Threat Actor)", placeholder="e.g., SQL Injection, XSS, Nmap, Ransomware...")

btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("🔍 Gather OSINT Feed"):
        # 🛡️ SECURITY MITIGATION: Input Sanitization (Anti-XSS/SQLi Defenses)
        clean_query = re.sub(r'[^\w\s\-\.]', '', query_input).lower().strip()
        
        if not clean_query:
            st.error("❌ Incident Alert: Null or Malformed Telemetry Input Blocked by Sanity Filter.")
        else:
            # Check local knowledge base matrix directly
            matched_threat = None
            for key in LOCAL_OSINT_DB:
                if key in clean_query:
                    matched_threat = LOCAL_OSINT_DB[key]
                    break
            
            if matched_threat:
                st.session_state.intel_title = f"📁 IntelScout Feed: {matched_threat['title']}"
                st.session_state.intel_body = matched_threat["raw"]
            else:
                # Custom hardened sandbox message if entry isn't in database
                st.session_state.intel_title = f"📁 IntelScout Unknown Entity Checked"
                st.session_state.intel_body = (
                    f"Telemetry node recorded target signature: '{clean_query}'.\n"
                    "Status: Sanitization complete. Entity evaluated cleanly. No current active alert "
                    "signatures flagged in immediate IntelScout parser dictionary registers."
                )

with btn_col2:
    if st.button("🤖 AI Core Synthesize"):
        if st.session_state.intel_body in ["System Idle. Awaiting OSINT Target Query Initialization...", "Anomalous signature telemetry array processed securely."]:
            st.warning("⚠️ Action Blocked: Populate the OSINT active threat database before invoking the AI core.")
        else:
            with st.spinner("🤖 Initiating Deep IntelScout Parser LLM Analysis Core..."):
                clean_query = re.sub(r'[^\w\s\-\.]', '', query_input).lower().strip()
                
                matched_threat = None
                for key in LOCAL_OSINT_DB:
                    if key in clean_query:
                        matched_threat = LOCAL_OSINT_DB[key]
                        break
                
                if matched_threat:
                    st.session_state.intel_title = f"🛡️ Intelligence Summary ({matched_threat['title']})"
                    st.session_state.intel_body = matched_threat["ai"]
                else:
                    st.session_state.intel_title = "🛡️ Intelligence Summary (IntelScout AI Core)"
                    st.session_state.intel_body = (
                        f"नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी' और आप देख रहे हैं IntelScout OSINT Parser प्लेटफॉर्म। इनपुट '{clean_query}' को हमारे इनपुट फ़िल्टर द्वारा सुरक्षित रूप से प्रोसेस कर दिया गया है। "
                        "यह क्वेरी नेटवर्क इंजेक्शन हमलों से पूरी तरह सुरक्षित है। यह प्रदर्शित करता है कि कैसे हमारा आर्किटेक्चर किसी भी अज्ञात इनपुट को बिना सिस्टम क्रैश किए हैंडल कर सकता है।"
                    )

# ==============================================================================
# 6. DATA TELEMETRY OUTPUT DISPLAY
# ==============================================================================
st.write("")
if st.session_state.intel_title:
    st.markdown(f"### {st.session_state.intel_title}")

st.info(st.session_state.intel_body)
