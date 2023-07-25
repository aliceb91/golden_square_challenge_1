def grammar_checker(text):
    """
    Checks a given string for correct punctuation at it's start and end.

    Parameters:
        text: The Text being analysed

    Returns:
        A string stating that the text is acceptable, or if not, what requires changing
    """
    if text == "" or not text[0].isupper() and text[-1] not in ".!?":
        return "Error: No starting capital letter or valid punctuation at end of string."
    if not text[0].isupper():
        return "Error: No capital letter."
    if text[-1] not in ".!?":
        return "Error: No valid punctuation at end of string."
    return "No errors detected, good job!"
