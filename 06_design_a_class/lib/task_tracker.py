class TaskTracker():
    def __init__(self):
        self.task_list = []

    def add_task(self, task):
        """
        Adds a task to a list of user generated tasks and returns the list

        Paramaters:
            task: The text being submitted as a task.

        Returns:
            The current task list.

        Side effects:
            Appends the task to the task list list stored in the state of the class.
        """
        self.task_list.append(task)
        return self.task_list

    def mark_done(self, target):
        """
        Removes a selected task from the task list

        Parameters:
            target: the target task to remove

        Returns:
            An updated dictionary with the entry removed
        """
        self.task_list.remove(target)
        return self.task_list
