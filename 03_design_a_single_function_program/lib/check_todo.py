def check_todo(text):
    """
    Returns a string confirming if the provided text is a task, based on the pressence of #TODO in the string.

    Paramaters:
        text: The text being analysed for #TODO

    Returns:
        a string confirming if the provided text is a task or not.

    Side effects:
        This function doesn't print anything or have any other side effects.
    """
    if not isinstance(text, str):
        return "Please input a string."
    if "#TODO" in text:
        return "This text contains a task!"
    return "This text does not contain a task."
