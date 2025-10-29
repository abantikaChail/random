# Friendly short responses when user appreciates or says thanks
FRIENDLY_RESPONSES = [
    "I'm glad I could help!",
    "That sounds great!",
    "Happy to hear that!",
    "Anytime — I’m here to help!",
    "Awesome! Let me know if you need anything else.",
    "Glad I was helpful!",
    "You're welcome!"
]

# Polite responses when user is unhappy or says the answer was wrong
APOLOGY_RESPONSES = [
    "I'm really sorry about that. I'm still improving and will try to do better next time.",
    "Apologies if my answer wasn’t helpful — I’m learning and would love to know what went wrong.",
    "My bad! I’ll do my best to improve. Could you share a bit more detail so I can help you better?",
    "Sorry about that! I’m still in my early phase and will try to respond more accurately next time.",
    "Thanks for pointing that out. I’ll work on improving — could you tell me what part wasn’t right?",
]



def is_gratitude_message(user_input: str) -> bool:
    gratitude_keywords = [
        "thank", "thanks", "thank you", "thx",
        "good job", "nice", "great", "awesome",
        "helpful", "cool", "perfect", "amazing",
        "appreciate", "well done", "good work"
    ]
    user_input_lower = user_input.lower()
    return any(kw in user_input_lower for kw in gratitude_keywords)


def is_negative_feedback(user_input: str) -> bool:
    negative_keywords = [
        "not helpful", "wrong", "incorrect", "bad", "terrible",
        "repeating", "same answer", "again", "you said that",
        "useless", "makes no sense", "didn't help", "poor",
        "doesn't work", "confusing", "irrelevant"
    ]
    user_input_lower = user_input.lower()
    return any(kw in user_input_lower for kw in negative_keywords)



    # --- Handle special user messages (gratitude or negative feedback) ---
    if is_gratitude_message(user_query):
        assistant_msg = random.choice(FRIENDLY_RESPONSES)
        with st.chat_message("assistant"):
            st.markdown(assistant_msg)
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_msg})
        st.stop()

    if is_negative_feedback(user_query):
        assistant_msg = random.choice(APOLOGY_RESPONSES)
        with st.chat_message("assistant"):
            st.markdown(assistant_msg)
        st.session_state.chat_history.append({"role": "assistant", "content": assistant_msg})
        st.stop()




