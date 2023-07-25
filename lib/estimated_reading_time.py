import datetime

def estimated_reading_time(text):
    """
    Estimates the required reading time of a text message, based on a speed of 200 words per minute.

    Parameters:
        text: The text message being analysed

    Returns:
        a string depicting the time required in an "hours : minuites : seconds : miliseconds" format

    Side effects: This function doesn't print anything or have any other side efects
    """
    word_second = 200/60
    string_list = len(text.split())
    seconds = string_list / word_second
    time_string = str(datetime.timedelta(seconds=seconds))
    if seconds % 1 == 0:
        return f"Estimated reading time: 0{time_string}.00"
    else:
        return f"Estimated reading time: 0{time_string[:10]}"
