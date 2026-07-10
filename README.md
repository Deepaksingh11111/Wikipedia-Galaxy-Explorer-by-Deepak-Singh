# 🛡️ IntelScout OSINT Parser & Intelligence Hub

[![Live App](https://img.shields.io/badge/Status-Live%20Deployment-00bfa5?style=for-the-badge&logo=streamlit)](https://wikipedia-galaxy-explorer-by-deepak-singh-4jfhuy3kl95kfpfyorwz.streamlit.app/)
[![Language](https://img.shields.io/badge/Language-Python%203.x-blue?style=for-the-badge&logo=python)](https://www.python.org)
[![Security](https://img.shields.io/badge/Security-Input%20Sanitized-red?style=for-the-badge&logo=dependencycheck)](https://owasp.org/)

**IntelScout OSINT Parser** is an advanced, automated Open Source Intelligence (OSINT) gathering dashboard and threat intelligence routing hub. It is engineered specifically for security analysts and researchers to seamlessly hunt, track, and analyze global threat actor profiles, technical vulnerabilities, and CVE data within a unified, secure sandbox ecosystem.

---

## 🚀 Live Demonstration Gateway
The application is fully containerized and hosted live on the Streamlit Cloud registry. You can interactively test the backend sanitization engine and sandbox telemetry loops using the production gateway below:

🔗 **[IntelScout OSINT Parser - Live Production Application](https://wikipedia-galaxy-explorer-by-deepak-singh-4jfhuy3kl95kfpfyorwz.streamlit.app/)**

---

## 🔒 Core Architecture & Security Mitigations

*   **Automated OSINT Telemetry Pipeline:** Dynamically queries global intelligence indices (via Wikipedia Open API endpoints) to rapidly compile operational threat briefs, bypassing manual information extraction bottlenecks.
*   **Hardened Input Sanitization (Anti-SQLi/XSS Controls):** Features a robust server-side Regular Expression (`re`) filter mechanism that actively strips out malicious code strings, single quotes (`'`), script markers, and malicious comment blocks (`--`) before processing.
*   **Deterministic Sandbox & Fault-Tolerant Fallback Matrix:** Built to handle rate limits, network timeouts, or unmapped adversarial payloads gracefully. Instead of triggering runtime exceptions, the backend intercepts anomalies, routes queries to a local knowledge base dictionary, and flags unknown entities inside a secure isolation sandbox.
*   **SOC-inspired Reactive Matrix Canvas UI:** Incorporates a dynamic, optimized HTML5 Canvas background rendering a live asynchronous JavaScript terminal Matrix digital rain loop, mimicking a live Security Operations Center (SOC) dashboard.

---

## 🛠️ Technology Stack & Layer Schema

| Layer | Component Technology |
| :--- | :--- |
| **Frontend Interface** | Streamlit Framework, Custom CSS Injection, Cyberpunk Structural Themes |
| **Backend Sanitization** | Python 3.x, Native Regular Expressions (`re` Engine) |
| **Data Repositories** | Wikipedia-API Integration (Secure Wikimedia User-Agent Compliant Architecture) |
| **Interactive Assets** | Asynchronous HTML5 Canvas Component, Embedded Embedded JavaScript Core Loops |

---

## 💻 Quick Local Deployment & Installation

To launch this security diagnostics engine locally within your own Kali Linux terminal or developer workstation:

1. **Clone the Source Code Repository:**
   ```bash
   git clone [https://github.com/Deepaksingh11111/IntelScout-OSINT-Parser.git](https://github.com/Deepaksingh11111/IntelScout-OSINT-Parser.git)
   cd IntelScout-OSINT-Parser


   //

   Install Required Runtime Dependencies:

Bash
pip install streamlit wikipedia-api
Initialize the Secure Streamlit Framework:

Bash
streamlit run app.py
🧪 Verification & Proof of Concept (PoC Testing)
You can directly verify the efficacy of the application's sanitization parameters by inputting raw database bypass vectors directly into the input portal:

SQL Injection ' OR '1'='1 (Neutralizes quotes automatically and securely routes to the valid SQLi vulnerability index)

admin' -- (Strips comment flags instantly, catches the unmapped payload, and moves it directly into the Sandbox Isolation Core alert box)

👤 Cybersecurity Professional Profile
Name: Deepak Singh

University: Galgotias University

Core Focus: Application Security, Full-Stack Architecture, and Defensive Coding

GitHub Repository Hub: @Deepaksingh11111
