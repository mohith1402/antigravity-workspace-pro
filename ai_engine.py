import os
import google.generativeai as genai

def mock_gemini_evaluator(system_prompt, user_text):
    """
    Calls the Gemini API to evaluate the given text based on the system prompt.
    """
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        return "⚠️ Error: GEMINI_API_KEY is missing. Please add it to your Streamlit Secrets."
    
    genai.configure(api_key=api_key)
    
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        full_prompt = f"System Instructions:\n{system_prompt}\n\nText to Evaluate:\n{user_text}"
        response = model.generate_content(full_prompt)
        return response.text
        
    except Exception as e:
        return f"Uh oh, something went wrong with the AI request: {str(e)}"