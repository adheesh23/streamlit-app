import streamlit as st

# Set page configuration
st.set_page_config(page_title="LLM Cost Estimator Chatbot", layout="centered")

# App title
st.title("🤖 LLM Cost Estimator Chatbot")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input box for user query
user_query = st.text_input("💬 Ask me about LLM pricing (e.g., 'What is the cost of Claude for 100k tokens?')")

# If user submits a query
if user_query:
    # Add user message to chat history
    st.session_state.chat_history.append(("user", user_query))

    # ✨ Placeholder response (you'll replace this with real logic later)
    bot_reply = "Sure! Based on your query, the estimated cost is approximately $15.00."

    # Add bot reply to chat history
    st.session_state.chat_history.append(("bot", bot_reply))

# Display the chat history
st.markdown("---")
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"🧑‍💻 **You:** {message}")
    else:
        st.markdown(f"🤖 **Bot:** {message}")
