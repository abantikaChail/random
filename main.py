import re
import random

def detect_user_intent(user_query: str):
    """
    Detects if user input expresses gratitude or negative feedback.
    Works with flexible, conversational phrases — purely rule-based.
    """
    query = user_query.lower().strip()

    # Base keywords for both sentiments
    positive_keywords = [
        "thank", "appreciate", "grateful", "good", "great", "awesome",
        "amazing", "nice", "helpful", "useful", "perfect", "well done"
    ]
    negative_keywords = [
        "wrong", "bad", "confusing", "useless", "irrelevant", "repeating",
        "repeat", "not working", "doesn't work", "didn't help", "error", "issue", "problem"
    ]

    # Detect explicit positive or negative signals
    positive_match = any(word in query for word in positive_keywords)
    negative_match = any(word in query for word in negative_keywords)

    # Smart negation handling (e.g., "not helpful", "wasn't great", "not good")
    negation_pattern = r"\b(not|no|never|isn'?t|wasn'?t|doesn'?t|didn'?t)\b"
    if re.search(negation_pattern, query):
        for pos_word in positive_keywords:
            if pos_word in query:
                negative_match = True
                positive_match = False
                break

    # Intent classification
    if positive_match and not negative_match:
        return "gratitude"
    elif negative_match and not positive_match:
        return "negative"
    else:
        return None


# ----------------- Example usage in your chat flow ----------------- #
intent = detect_user_intent(user_query)

if intent == "gratitude":
    assistant_msg = random.choice([
        "I’m really glad I could help! 😊",
        "That sounds great — happy to hear that!",
        "Always a pleasure to assist!",
        "Wonderful! I’m happy that was helpful.",
        "Awesome! Glad it worked out for you."
    ])

elif intent == "negative":
    assistant_msg = random.choice([
        "I’m sorry that didn’t help much. Could you tell me what went wrong?",
        "Apologies — I’m still improving and will try to do better next time.",
        "I appreciate your feedback. Could you share more details so I can refine my responses?",
        "Sorry about that! I’m still learning and might miss things sometimes, but I’ll do my best to improve."
    ])



intent = detect_user_intent(user_query)
if intent:
    # handle accordingly
    # and skip the search logic below
    st.chat_message("assistant").markdown(assistant_msg)
    st.stop()


