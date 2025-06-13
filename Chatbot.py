import streamlit as st
import nltk
from nltk.chat.util import Chat, reflections

# Define pairs (patterns and responses)
pairs = [
    [r"hi|hello|hey", ["Hello!", "Hey there!", "Hi! How can I help you?"]],
    [r"what is your name ?", ["I am a simple chatbot created by you!"]],
    [r"how are you ?", ["I'm good, thanks!", "Doing great! And you?"]],
    [r"sorry (.*)", ["It's okay", "No worries"]],
    [r"i'm (.*)", ["Nice to meet you %1", "Hello %1, how can I help you today?"]],
    [r"quit", ["Bye! Take care.", "Goodbye!"]],
    [r"(.*)", ["I'm not sure I understand. Can you say that another way?"]]
]

# Create chatbot instance
chatbot = Chat(pairs, reflections)

# Streamlit app UI
st.title("💬 NLTK Chatbot with Streamlit")
st.markdown("Ask me anything! Type 'quit' to end the conversation.")

# Store messages in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# User input box
user_input = st.text_input("You:", key="input")

# Handle user input
if user_input:
    if user_input.lower() == "quit":
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", "Goodbye!"))
    else:
        response = chatbot.respond(user_input)
        st.session_state.chat_history.append(("You", user_input))
        st.session_state.chat_history.append(("Bot", response))

# Display chat history
for sender, message in st.session_state.chat_history:
    with st.chat_message(sender if sender == "You" else "assistant"):
        st.markdown(message)
