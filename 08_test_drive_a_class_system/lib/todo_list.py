class TodoList():
    def __init__(self):
        self.task_list = []

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        self.task_list.append(todo)
      
    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        incomplete_tasks = []
        for task in self.task_list:
            if task.complete == False:
                incomplete_tasks.append(task)
        return incomplete_tasks

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        complete_tasks = []
        for task in self.task_list:
            if task.complete == True:
                complete_tasks.append(task)
        return complete_tasks

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        for task in self.task_list:
            task.mark_complete()
