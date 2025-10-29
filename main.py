# Separate tone for "no results" situations
OPENING_PHRASES_NORESULTS = [
    "Hmm, looks like I couldn’t find anything on that.",
    "That’s interesting — I couldn’t locate any matching documents.",
    "Seems like there’s nothing relevant to that just yet.",
    "I searched everywhere, but couldn’t find a match for that query."
]

CLOSING_PHRASES_NORESULTS = [
    "Maybe try rephrasing your question or adding more details?",
    "You could upload more relevant documents and try again.",
    "Let’s refine the question and see if we can find something next time.",
    "Try using simpler or more specific search terms."
]


def style_response(core_response: str, no_results: bool = False) -> str:
    """Add conversational tone. Use special tone if no results found."""
    core = core_response.strip()
    if not core:
        return core

    if CONVERSATIONAL_MODE:
        if no_results:
            opening = random.choice(OPENING_PHRASES_NORESULTS)
            closing = random.choice(CLOSING_PHRASES_NORESULTS)
        else:
            opening = random.choice(OPENING_PHRASES)
            closing = random.choice(CLOSING_PHRASES)
        return f"{opening} {core} {closing}"
    else:
        return core



# After assistant_msg is assigned and before displaying it:
no_results_mode = "No documents found" in assistant_msg
core_response = shorten_response(str(assistant_msg), MAX_SENTENCES)
final_response = style_response(core_response, no_results=no_results_mode)

with st.chat_message("assistant"):
    st.markdown(final_response)
st.session_state.chat_history.append({"role": "assistant", "content": final_response})





