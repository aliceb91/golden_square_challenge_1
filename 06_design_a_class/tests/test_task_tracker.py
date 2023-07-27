from lib.task_tracker import TaskTracker

def test_returns_single_item_list():
    """
    Given a single task
    Returns a list with a single entry.
    """
    task_tracker = TaskTracker()
    result = task_tracker.add_task("Walk the dog")
    assert result == ['Walk the dog']

def test_returns_multi_item_list():
    """
    Given multiple tasks
    Returns a list of all task entries.
    """
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    task_tracker.add_task("Mow the lawn")
    result = task_tracker.add_task("Feed the fish")
    assert result == ['Walk the dog', "Mow the lawn", "Feed the fish"]

def test_removes_single_task():
    """
    Given a target task
    Removes the task form the list and returns the updated list.
    """
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    result = task_tracker.mark_done("Walk the dog")
    assert result == []

def test_removes_taks_from_multi_list():
    """
    Given a target task
    Removes the task from a list of multiple elements and returns the updated list.
    """
    task_tracker = TaskTracker()
    task_tracker.add_task("Walk the dog")
    task_tracker.add_task("Mow the lawn")
    task_tracker.add_task("Feed the fish")
    result = task_tracker.mark_done("Mow the lawn")
    assert result == ["Walk the dog", "Feed the fish"]