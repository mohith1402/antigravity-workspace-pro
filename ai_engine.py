import os
import google.generativeai as genai

def mock_gemini_evaluator(system_prompt, user_text):
    """
    Calls the Gemini API to evaluate the given text based on the system prompt.
    """
    # Grab the API key from environment variables (Streamlit Secrets)
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        return "⚠️ Error: GEMINI_API_KEY is missing. Please add it to your Streamlit Secrets."
    
    # Configure the Gemini client
    genai.configure(api_key=api_key)
    
    try:
        # gemini-1.5-flash is fast and great for general text evaluation
        model = genai.GenerativeModel('gemini-1.5-flash')
        
        # Combine the instructions and the user's text
        full_prompt = f"System Instructions:\n{system_prompt}\n\nText to Evaluate:\n{user_text}"
        
        # Call the API
        response = model.generate_content(full_prompt)
        return response.text
        
    except Exception as e:
        # Catch any API errors so the app doesn't crash completely
        return f"Uh oh, something went wrong with the AI request: {str(e)}"            "priority": "Normal",
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
