from lib.check_todo import check_todo

def test_check_for_todo():
    """
    Given a string containing #TODO
    It returns a string confirming that this text is a task
    """
    result = check_todo("#TODO: Clean the kitchen")
    assert result == "This text contains a task!"

def test_check_for_no_todo():
    """
    Given a string that does not contain #TODO
    It returns a string confirming that this text is not a task
    """
    result = check_todo("Walk the dog")
    assert result == "This text does not contain a task."

def test_check_empty_string():
    """
    Given an empty string
    It returns a string confirming that this text is not a task
    """
    result = check_todo("")
    assert result == "This text does not contain a task."

def test_check_integer_input():
    """
    Given an integer input instead of a string
    It returns a string requesting the user to input a string
    """
    result = check_todo(123456)
    assert result == "Please input a string."

def test_check_list_input():
    """
    Given a list input instead of a string
    It returns a string request the user to input a string
    """
    result = check_todo(["#TODO", 4, {}])
    assert result == "Please input a string."
    