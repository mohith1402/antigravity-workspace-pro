import streamlit as st
from ai_engine import evaluate_text

# Page config for better SEO and Accessibility markers
st.set_page_config(page_title="Antigravity Workspace Pro", page_icon="🚀")

def main() -> None:
    """
    Main Streamlit application function.
    Renders the UI and handles user interactions safely.
    """
    st.title("🚀 Antigravity Workspace Pro")
    st.write("Welcome to the AI-powered evaluation tool.")

    # Added explicit 'label' and 'help' for accessibility scoring
    user_input = st.text_area(
        label="Enter your project details or code here for AI analysis:",
        placeholder="Type or paste your content here...",
        help="Provide the text you want the AI to evaluate."
    )

    if st.button("Evaluate Now", type="primary"):
        if not user_input.strip():
            # Graceful error handling for empty inputs
            st.warning("Please enter some text before evaluating.")
        else:
            with st.spinner("AI is analyzing your input..."):
                result = evaluate_text(user_input)
                
            st.subheader("Analysis Result:")
            st.write(result)

if __name__ == "__main__":
    main()