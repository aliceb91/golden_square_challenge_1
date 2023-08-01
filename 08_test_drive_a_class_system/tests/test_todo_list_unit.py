from lib.todo_list import TodoList

def test_add_todo_to_list():
    # Given a class instance of Todo
    # It adds this instance to the task list.
    class SampleTodo():
        def __init__(self, task):
            self.task = task
            self.complete = False
    todo = SampleTodo("Walk the dog")
    todo_list = TodoList()
    todo_list.add(todo)
    result = todo_list.task_list
    assert result == [todo]