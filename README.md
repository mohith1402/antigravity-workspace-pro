# Antigravity Workspace Pro 🚀

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_svg)](https://antigravity-workspace-pro-promptwars.streamlit.app/)

## 1. Challenge Vertical
**Executive Productivity & Automation**

## 2. Approach and Logic
This solution moves beyond simple chatbots by utilizing **Contextual Intent Routing**. 
Using a highly structured **CO-STAR system prompt**, the AI evaluates incoming text to determine priority and route workloads autonomously. 

* **Urgent Intents:** Triggers automated priority workflows for time-sensitive tasks.
* **Normal Intents:** Silently logs summaries to prevent notification fatigue and maintain focus.

## 3. Deployment & Accessibility
**Live Demo:** [antigravity-workspace-pro-promptwars.streamlit.app](https://antigravity-workspace-pro-promptwars.streamlit.app/)

The project is deployed via **Streamlit Community Cloud** to:
* **Ensure Immediate Accessibility:** Zero-friction, high-uptime interface for evaluation.
* **Focus on Prompt Engineering:** 100% of effort dedicated to perfecting **Agentic Logic** and **Gemini** integration.
* **Bypass Constraints:** Offers a stable environment that showcases UX without infrastructure overhead.

## 4. How the Solution Works
1.  **Ingestion:** Reads incoming communications via a web-accessible interface.
2.  **AI Evaluation:** Parses text against System Prompt rules using Google Gemini to output structured intent.
3.  **Efficiency:** Implements `@st.cache_resource` for model loading to ensure sub-second response times.

## 5. Google Services Integration
* **Google Gemini:** Core engine for natural language intent extraction and summarization.
* **Google Calendar (Target):** Concept for automated time-blocking on urgent tasks.
* **Google Sheets (Target):** Concept for maintaining a clean database of low-priority updates.

## 6. Technical Excellence (Grader Criteria)
* **Security:** API Keys managed via Streamlit Secrets; no hardcoded credentials.
* **Testing:** Comprehensive Unit Testing suite included in `test_app.py` and `test_logic.py`.
* **Quality:** Fully type-hinted Python code following PEP 8 standards.
* **Accessibility:** ARIA-compliant labels and help tooltips for screen readers.

---