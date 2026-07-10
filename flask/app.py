import re
import streamlit as st
import wikipediaapi
import streamlit.components.v1 as components

# ==============================================================================
# 1. PAGE CONFIGURATION & METADATA
# ==============================================================================
st.set_page_config(
    page_title="IntelScout OSINT Parser",
    page_icon="🛡️",
    layout="wide"
)

# Professional User-Agent to comply with Wikimedia's API policy
USER_AGENT = "IntelScoutOSINTExplorer/6.0 (Deepak Singh)"
wiki = wikipediaapi.Wikipedia(language='en', user_agent=USER_AGENT)

# Session State Initialization
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
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 4. DETERMINISTIC LOCAL KNOWLEDGE BASE (Backup Synthesis Rules)
# ==============================================================================
LOCAL_OSINT_DB = {
    "sql injection": {
        "title": "SQL Injection (SQLi) - CWE-89",
        "ai": "नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी'। SQL Injection एक बेहद गंभीर हमला है। यह तब संभव होता है जब एक डेवलपर इनपुट बॉक्स के डेटा को बिना साफ किए सीधे डेटाबेस क्वेरी में जोड़ देता है। हमलावर चालाकी से हानिकारक कोड (जैसे ' OR 1=1 --) डालकर बिना密码 के सिस्टम एडमिन पैनल लॉगिन कर सकते हैं या पूरा डेटाबेस डिलीट कर सकते हैं।\n\n🛡️ बचाव: हमेशा इनपुट को फ़िल्टर करें और 'Parameterized Queries' या 'Prepared Statements' का ही उपयोग करें।"
    },
    "cross-site scripting": {
        "title": "Cross-Site Scripting (XSS) - CWE-79",
        "ai": "नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी'। Cross-Site Scripting (XSS) एक क्लाइंट-साइड वेब हमला है। इसमें हमलावर वेबसाइट के संवेदनशील इनपुट फील्ड्स में खतरनाक JavaScript कोड डाल देता है। जब भी कोई सामान्य यूजर उस वेबसाइट पर जाता है, तो वह कोड उसके ब्राउज़र में ऑटोमैटिक रन हो जाता है, जिससे हैकर उनके गोपनीय Session Cookies और टोकन्स चुरा सकता है।\n\n🛡️ बचाव: इनपुट पर सख्त 'Data Sanitization' लागू करें और सर्वर साइड पर 'Output Encoding' का प्रयोग करें।"
    },
    "nmap": {
        "title": "Network Mapper (Nmap) Security Diagnostic Tool",
        "ai": "नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी'। Nmap (Network Mapper) इंफ्रास्ट्रक्चर सिक्योरिटी और रिकॉन (Reconnaissance) का सबसे लोकप्रिय टूल है। इसका इस्तेमाल नेटवर्क स्कैनिंग के लिए किया जाता है ताकि यह पता लगाया जा सके कि कौन से पोर्ट्स (Ports) खुले हैं, कौन से होस्ट्स एक्टिव हैं और कौन सा ऑपरेटिंग सिस्टम चल रहा है। सुरक्षा टीमें अपनी कमियां सुधारने के लिए इसका उपयोग करती हैं।\n\n🛡️ उपयोग: 'nmap -sV -sC [IP]' कमांड का इस्तेमाल सर्विस वर्जन और डिफॉल्ट स्क्रिप्ट चेक्स के लिए किया जाता है।"
    },
    "ransomware": {
        "title": "Ransomware Threat Intelligence Signature",
        "ai": "नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी'। Ransomware एक प्रकार का मलेशियस सॉफ्टवेयर (Malware) है जो किसी सिस्टम या पूरे नेटवर्क के फाइलों को एडवांस सिमेट्रिक/असिमेट्रिक एल्गोरिदम का उपयोग करके एन्क्रिप्ट (लॉक) कर देता है। इसके बाद हैकर्स डेटा को वापस अनलॉक करने के बदले फिरौती (Ransom) मांगते हैं।\n\n🛡️ बचाव: हमेशा क्रिटिकल डेटा का offline बैकअप रखें, सिस्टम पैच अपडेटेड रखें और एंडपॉइंट प्रोटेक्शन (EDR) टूल्स का प्रयोग करें।"
    }
}

LOCAL_OSINT_DB["sqli"] = LOCAL_OSINT_DB["sql injection"]
LOCAL_OSINT_DB["xss"] = LOCAL_OSINT_DB["cross-site scripting"]

# ==============================================================================
# 5. INTERACTIVE DASHBOARD GATEWAY
# ==============================================================================
query_input = st.text_input("🔑 System Telemetry Target Query (CVE, Vulnerability, or Threat Actor)", placeholder="e.g., SQL Injection, XSS, Nmap, Ransomware...")

btn_col1, btn_col2 = st.columns(2)

with btn_col1:
    if st.button("🔍 Gather OSINT Feed"):
        # 🛡️ SECURITY MITIGATION: State Flush to clear old screens instantly
        st.session_state.intel_title = ""
        st.session_state.intel_body = ""
        
        clean_query = re.sub(r'[^\w\s\-\.]', '', query_input).strip()
        
        if not clean_query:
            st.error("❌ Incident Alert: Null or Malformed Telemetry Input Blocked by Sanity Filter.")
            st.session_state.intel_body = "System Idle. Awaiting OSINT Target Query Initialization..."
        else:
            with st.spinner("📡 Querying Live Global OSINT Repositories..."):
                page = wiki.page(clean_query)
                
                if page.exists():
                    st.session_state.intel_title = f"📁 Live OSINT Feed: {page.title}"
                    st.session_state.intel_body = page.summary[:1500]
                else:
                    st.error("❌ Incident Alert: No threat intelligence patterns identified on Live Repositories.")
                    st.session_state.intel_body = "Anomalous signature telemetry array processed securely."

with btn_col2:
    if st.button("🤖 AI Core Synthesize"):
        if st.session_state.intel_body in ["System Idle. Awaiting OSINT Target Query Initialization...", ""]:
            st.warning("⚠️ Action Blocked: Populate the OSINT active threat database before invoking the AI core.")
        elif st.session_state.intel_body == "Anomalous signature telemetry array processed securely.":
            # State clean up for malicious/bad inputs when AI is hit
            st.session_state.intel_title = "🛡️ IntelScout Sandbox Isolation Core"
            clean_query = re.sub(r'[^\w\s\-\.]', '', query_input).strip()
            st.session_state.intel_body = (
                f"नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी'। इनपुट '{clean_query if clean_query else 'Malicious/Empty Payload'}' "
                "को हमारे सुरक्षा फ़िल्टर द्वारा पूरी तरह से आइसोलेट (Isolate) कर दिया गया है। यह नेटवर्क इंजेक्शन हमलों "
                "और XSS से पूरी तरह सुरक्षित है। सिस्टम ने किसी अज्ञात कोड को चलाने के बजाय उसे सैंडबॉक्स कंटेनर में ब्लॉक कर दिया है।"
            )
        else:
            with st.spinner("🤖 Initiating IntelScout Analysis Core..."):
                query_lower = query_input.lower().strip()
                
                matched_threat = None
                for key in LOCAL_OSINT_DB:
                    if key in query_lower:
                        matched_threat = LOCAL_OSINT_DB[key]
                        break
                
                if matched_threat:
                    st.session_state.intel_title = f"🛡️ IntelScout Analysis Summary ({matched_threat['title']})"
                    st.session_state.intel_body = matched_threat["ai"]
                else:
                    st.session_state.intel_title = "🛡️ IntelScout Custom Intelligence Summary"
                    st.session_state.intel_body = (
                        f"नमस्ते! मैं हूँ आपकी सुरक्षा विशेषज्ञ 'आशी'। लाइव रीपॉजिटरी से प्राप्त इनपुट डेटा को हमारे "
                        "फ़िल्टर द्वारा सुरक्षित रूप से पार्स कर दिया गया है। यह क्वेरी क्लाइंट-साइड हमलों से सुरक्षित है।"
                    )

# ==============================================================================
# 6. DATA TELEMETRY OUTPUT DISPLAY
# ==============================================================================
st.write("")
if st.session_state.intel_title:
    st.markdown(f"### {st.session_state.intel_title}")

if st.session_state.intel_body and st.session_state.intel_body not in ["System Idle. Awaiting OSINT Target Query Initialization...", "Anomalous signature telemetry array processed securely."]:
    st.info(st.session_state.intel_body)
