import streamlit as st
from ai_engine import mock_gemini_evaluator

# 1. Page Setup (Must be the first Streamlit command)
st.set_page_config(
    page_title="Antigravity Workspace", 
    page_icon="🚀",
    layout="centered"
)

# 2. Header
st.title("🚀 Antigravity Prompt Evaluator")
import os
test_key = os.environ.get("GEMINI_API_KEY", "")
st.info(f"🔍 DEBUG: Key is {len(test_key)} characters long and starts with: {test_key[:6]}")
st.markdown("Drop your text below and let Gemini evaluate it based on your custom rules.")

# 3. User Inputs
st.subheader("1. Setup the AI")
system_prompt = st.text_area(
    "System Prompt (How should the AI behave?)", 
    value="You are an expert editor. Evaluate the following text for clarity, tone, and grammar.",
    height=100
)

st.subheader("2. Add your Content")
user_input = st.text_area("Paste the text or email you want to evaluate here:", height=150)

# 4. Action Button
if st.button("Evaluate Now", type="primary"):
    # Don't run if the user didn't type anything
    if not user_input.strip():
        st.warning("Please enter some text to evaluate first!")
    else:
        # Show a friendly loading state while waiting for Gemini
        with st.spinner("AI is analyzing your text..."):
            result = mock_gemini_evaluator(system_prompt, user_input)
            
            # Display the output
            st.success("Evaluation Complete!")
            st.markdown("### AI Feedback")
            st.write(result)