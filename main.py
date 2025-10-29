# --- Paste near top of app_vox.py (after other imports) ---

import random
import re

# Configuration: tweak these
CONVERSATIONAL_MODE = True   # Set False to disable openings/closings
MAX_SENTENCES = 2            # Max sentences to return in the core answer
OPENING_PHRASES = [
    "Sure, let me explain that.",
    "Good question!",
    "Absolutely — here’s the short answer.",
    "Alright, let’s go over it."
]
CLOSING_PHRASES = [
    "Hope that helps!",
    "Let me know if you'd like more details.",
    "Was that helpful?",
    "Happy to help!"
]

_sentence_split_re = re.compile(r'(?<=[.!?])\s+')

def shorten_response(response: str, max_sentences: int = MAX_SENTENCES) -> str:
    """
    Keep only the first `max_sentences` sentences from response.
    If the response has fewer sentences, return unchanged.
    """
    if not response or not isinstance(response, str):
        return response
    # split into sentences while preserving punctuation
    sentences = _sentence_split_re.split(response.strip())
    if len(sentences) <= max_sentences:
        return response.strip()
    trimmed = " ".join(sentences[:max_sentences]).strip()
    # Ensure ends with punctuation
    if not re.search(r'[.!?]$', trimmed):
        trimmed += '.'
    return trimmed

def style_response(core_response: str) -> str:
    """
    Add a friendly opening and closing phrase around the core response.
    """
    core = core_response.strip()
    if not core:
        return core
    if CONVERSATIONAL_MODE:
        opening = random.choice(OPENING_PHRASES)
        closing = random.choice(CLOSING_PHRASES)
        # If core already looks short (1 sentence) avoid overly long wrappers
        return f"{opening} {core} {closing}"
    else:
        return core
# --- end helper block ---





best_response = search.get_best_response(query)
# or
result = search.search(query)
# or
response = model.predict(query)
# then
print(response)
# or
st.write(response)





# Example: find the current lines that send the reply and replace with below
# (adapt variable names to match your code: if it uses 'answer' or 'best_answer' use that name)

raw_response = best_response  # or whatever variable your code sets
core_response = shorten_response(raw_response, max_sentences=MAX_SENTENCES)
final_response = style_response(core_response)

# send to user (example; adapt to your code)
# if your code uses `print()`
print(final_response)

# or if your code uses streamlit:
# st.write(final_response)
# or
# st.chat_message("assistant").write(final_response)





# in search.py - after the matched text is assembled as `response_text`
# import at top: from typing import Optional
def _safety_trim(response_text: str, max_sentences: int = 3) -> str:
    import re
    split_re = re.compile(r'(?<=[.!?])\s+')
    parts = split_re.split(response_text.strip())
    if len(parts) <= max_sentences:
        return response_text.strip()
    return " ".join(parts[:max_sentences]).strip() + '.'

# then set:
response_text = _safety_trim(response_text, max_sentences=3)





