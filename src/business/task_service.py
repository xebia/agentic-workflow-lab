"""Task service for business logic."""
from src.data.task import Task
from src.data.task_repository import TaskRepository


class TaskService:
    """Service for managing tasks with business logic."""

    def __init__(self, repository: TaskRepository):
        """Initialize the task service.

        Args:
            repository: The task repository to use for data access
        """
        self.repository = repository

    def create_task(self, description: str) -> Task:
        """Create a new task.

        Args:
            description: Description of the task

        Returns:
            The newly created task

        Raises:
            ValueError: If description is empty or whitespace only
        """
        if not description or not description.strip():
            raise ValueError("Task description cannot be empty")

        task_id = self.repository.get_next_id()
        task = Task(task_id=task_id, description=description.strip())
        self.repository.add(task)
        return task

    def get_all_tasks(self) -> list[Task]:
        """Get all tasks.

        Returns:
            List of all tasks
        """
        return self.repository.get_all()

    def complete_task(self, task_id: int) -> None:
        """Mark a task as completed.

        Args:
            task_id: The id of the task to complete

        Raises:
            ValueError: If task_id is invalid or task not found
        """
        if task_id <= 0:
            raise ValueError("Task id must be a positive integer")

        task = self.repository.get_by_id(task_id)
        if task is None:
            raise ValueError(f"Task with id {task_id} not found")

        task.mark_completed()
        self.repository.update(task)
