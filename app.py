import json
import os
from flask import Flask, jsonify

app = Flask(__name__)

# Define the PromptWars System Prompt (CO-STAR Framework)
SYSTEM_PROMPT = """
[CONTEXT] You are an elite Executive Assistant Agent operating inside Google Workspace.
[OBJECTIVE] Analyze the following email text. Extract key points and determine the priority level.
[STYLE] Highly analytical and machine-readable.
[TONE] Objective and decisive.
[AUDIENCE] Automated routing systems.
[RESPONSE] Return strictly valid JSON with no markdown formatting.
Format required: {"summary": "brief text", "priority": "Urgent/Normal/Low", "action": "SCHEDULE_CALENDAR" or "LOG_SHEETS"}

Logic Rules:
- If the email mentions deadlines, immediate action, or VIP clients, priority is "Urgent" and action is "SCHEDULE_CALENDAR".
- Otherwise, priority is "Normal/Low" and action is "LOG_SHEETS".
"""

def mock_gemini_evaluator(email_content):
    """
    In a production Antigravity environment, this calls Gemini 3 Pro.
    For this prototype, we simulate the LLM's logical routing based on the System Prompt.
    """
    content_lower = email_content.lower()
    if "urgent" in content_lower or "asap" in content_lower or "deadline" in content_lower:
        return json.dumps({
            "summary": "Time-sensitive request detected.",
            "priority": "Urgent",
            "action": "SCHEDULE_CALENDAR"
        })
    else:
        return json.dumps({
            "summary": "Standard update.",
            "priority": "Normal",
            "action": "LOG_SHEETS"
        })

@app.route("/", methods=["GET", "POST"])
def process_inbox():
    results = []
    
    mock_inbox = [
        "URGENT: The investor deck deadline is moved to 3 PM today. Please review ASAP.",
        "Weekly newsletter draft is ready for your review whenever you have time."
    ]

    for i, email in enumerate(mock_inbox):
        decision_raw = mock_gemini_evaluator(email)
        decision = json.loads(decision_raw)
        
        results.append({
            "email": email,
            "decision": decision
        })

    return jsonify({
        "status": "Antigravity Workspace Pro - Agent Initialized",
        "processed_emails": results
    })

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8080))
    app.run(debug=True, host='0.0.0.0', port=port)