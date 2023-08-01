from lib.todo_list import TodoList
from lib.todo import Todo

def test_adding_multiple_todos():
    # Given multiple calls of the add method
    # Adds multiple tasks to the list.
    task_1 = Todo("Walk the dog")
    task_2 = Todo("Feed the fish")
    task_3 = Todo("Water the plants")
    todo_list = TodoList()
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    result = todo_list.task_list
    assert result == [task_1, task_2, task_3]

def test_checking_complete_tasks():
    # Given a list of tasks
    # Returns a list of only those tasks where complete = True
    task_1 = Todo("Walk the dog")
    task_2 = Todo("Feed the fish")
    task_3 = Todo("Water the plants")
    task_4 = Todo("Clean the kitchen")
    todo_list = TodoList()
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.add(task_4)
    todo_list.task_list[1].mark_complete()
    todo_list.task_list[3].mark_complete()
    result = todo_list.complete()
    assert result == [task_2, task_4]

def test_checking_incomplete_tasks():
    # Given a list of tasks
    # Returns a lis of only those tasks where conplete = False
    task_1 = Todo("Walk the dog")
    task_2 = Todo("Feed the fish")
    task_3 = Todo("Water the plants")
    task_4 = Todo("Clean the kitchen")
    todo_list = TodoList()
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.add(task_4)
    todo_list.task_list[1].mark_complete()
    todo_list.task_list[3].mark_complete()
    result = todo_list.incomplete()
    assert result == [task_1, task_3]

def test_giving_up():
    # Given a list of tasks
    # It marks all current tasks as complete in spite of how true that is (you terrible person you).
    task_1 = Todo("Walk the dog")
    task_2 = Todo("Feed the fish")
    task_3 = Todo("Water the plants")
    task_4 = Todo("Clean the kitchen")
    todo_list = TodoList()
    todo_list.add(task_1)
    todo_list.add(task_2)
    todo_list.add(task_3)
    todo_list.add(task_4)
    todo_list.give_up()
    result = []
    for task in todo_list.task_list:
        result.append(task.complete)
    assert result == [True, True, True, True]
