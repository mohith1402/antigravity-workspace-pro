import os
import google.generativeai as genai
import streamlit as st

@st.cache_resource
def load_model() -> genai.GenerativeModel:
    """
    Initializes and caches the Google Gemini Generative Model.
    Ensures efficiency by preventing redundant model loading on every UI click.
    """
    # Fetch API key securely from Streamlit Secrets
    api_key = st.secrets.get("GEMINI_API_KEY") or os.environ.get("GEMINI_API_KEY")
    if api_key:
        genai.configure(api_key=api_key)
    
    return genai.GenerativeModel('gemini-2.5-flash')

def evaluate_text(user_input: str) -> str:
    """
    Evaluates the user's text input using the Google Gemini AI model.
    
    Args:
        user_input (str): The text provided by the user.
        
    Returns:
        str: The AI-generated evaluation response or a safe error message.
    """
    if not user_input or not user_input.strip():
        return "Error: No input provided for evaluation."
        
    try:
        model = load_model()
        response = model.generate_content(user_input)
        return response.text
    except Exception as e:
        # Handles 429 quota errors and generic crashes safely
        return f"Service currently unavailable. Please try again later. (System note: {str(e)})"