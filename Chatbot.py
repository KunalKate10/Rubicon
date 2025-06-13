pip install nltk

import nltk
from nltk.chat.util import Chat, reflections

# Pair of patterns and responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello!", "Hey there!", "Hi! How can I help you?"]
    ],
    [
        r"what is your name ?",
        ["I am a simple chatbot created by you!"]
    ],
    [
        r"how are you ?",
        ["I'm good, thanks!", "Doing great! And you?"]
    ],
    [
        r"sorry (.*)",
        ["It's okay", "No worries"]
    ],
    [
        r"i'm (.*)",
        ["Nice to meet you %1", "Hello %1, how can I help you today?"]
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye!"]
    ],
    [
        r"(.*)",
        ["I'm not sure I understand. Can you say that another way?"]
    ]
]

# Create chatbot
chatbot = Chat(pairs, reflections)

# Run chatbot
print("Hi! I'm your chatbot. Type 'quit' to exit.")
chatbot.converse()
