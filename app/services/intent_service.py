def detect_intent(user_message: str):
    msg = user_message.lower()

    if "compare" in msg:
        return "compare"

    if "add" in msg or "also" in msg:
        return "refine"

    if len(msg.split()) < 4:
        return "clarify"

    return "recommend"
