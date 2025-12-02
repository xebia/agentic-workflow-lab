"""Task model representing a single task."""


class Task:
    """A task with an id, description, and completion status."""

    def __init__(self, task_id: int, description: str, completed: bool = False):
        """Initialize a task.

        Args:
            task_id: Unique identifier for the task
            description: Description of the task
            completed: Whether the task is completed (default: False)
        """
        self.task_id = task_id
        self.description = description
        self.completed = completed

    def mark_completed(self) -> None:
        """Mark the task as completed."""
        self.completed = True

    def __str__(self) -> str:
        """Return string representation of the task."""
        status = " [✓]" if self.completed else ""
        return f"{self.task_id}. {self.description}{status}"
