from lib.todo import Todo
import pytest

def test_create_todo():
    # Given a task as a string
    # Creates an instance of Todo containing the task with the complete property set to False.
    todo = Todo("Walk the dog")
    result = {todo.task: todo.complete}
    assert result == {"Walk the dog": False}

def test_mark_todo_as_complete():
    # Given a task as a string
    # It changes the value of complete from False to True.
    todo = Todo("Walk the dog")
    todo.mark_complete()
    result = {todo.task: todo.complete}
    assert result == {"Walk the dog": True}

def test_input_is_string():
    # Given a non string argument for the task
    # Returns an error message requesting a string
    with pytest.raises(Exception) as e:
        todo = Todo(1234567890)
    error_message = str(e.value)
    assert error_message == "String input is required for the Todo() class"