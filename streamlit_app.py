import streamlit as st
import json
from app import mock_gemini_evaluator

st.set_page_config(page_title="Antigravity Workspace Pro", page_icon="🚀", layout="centered")

st.title("🚀 Antigravity Workspace Pro")
st.subheader("Agent Evaluator UI")

st.markdown("This app wraps the core logic of the Antigravity Agent, automatically categorizing emails based on priority and routing them.")

st.divider()

st.markdown("### Test Custom Email")
email_content = st.text_area("Enter an email to be evaluated:", "URGENT: The investor deck deadline is moved to 3 PM today. Please review ASAP.")

if st.button("Evaluate Email", type="primary"):
    with st.spinner("Agent is thinking..."):
        decision_raw = mock_gemini_evaluator(email_content)
        decision = json.loads(decision_raw)
        
        st.success("Evaluation complete!")
        
        # Display nicely based on priority
        if decision.get("priority") == "Urgent":
            st.error(f"Priority: {decision.get('priority')} | Action: {decision.get('action')}")
        else:
            st.info(f"Priority: {decision.get('priority')} | Action: {decision.get('action')}")
            
        st.write("**Summary:**")
        st.write(decision.get("summary"))
        
        with st.expander("Raw JSON output"):
            st.json(decision)

st.divider()

st.markdown("### Process Mock Inbox")
st.markdown("Run the standard test inbox through the agent (like the original `app.py`).")

if st.button("Process Default Inbox"):
    mock_inbox = [
        "URGENT: The investor deck deadline is moved to 3 PM today. Please review ASAP.",
        "Weekly newsletter draft is ready for your review whenever you have time."
    ]
    
    results = []
    with st.spinner("Processing inbox..."):
        for email in mock_inbox:
            decision_raw = mock_gemini_evaluator(email)
            decision = json.loads(decision_raw)
            results.append({
                "email": email,
                "decision": decision
            })
    
    st.success("Inbox processed successfully!")
    for res in results:
        with st.container():
            st.markdown(f"**Email:** {res['email']}")
            st.json(res["decision"])
            st.markdown("---")
