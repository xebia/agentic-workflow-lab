"""Task repository interface and implementations."""
from abc import ABC, abstractmethod
from typing import List, Optional
from src.data.task import Task


class TaskRepository(ABC):
    """Abstract base class for task repositories."""

    @abstractmethod
    def add(self, task: Task) -> None:
        """Add a task to the repository.

        Args:
            task: The task to add
        """
        pass

    @abstractmethod
    def get_all(self) -> List[Task]:
        """Get all tasks from the repository.

        Returns:
            List of all tasks
        """
        pass

    @abstractmethod
    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by its id.

        Args:
            task_id: The id of the task to retrieve

        Returns:
            The task with the given id, or None if not found
        """
        pass

    @abstractmethod
    def update(self, task: Task) -> None:
        """Update a task in the repository.

        Args:
            task: The task to update
        """
        pass

    @abstractmethod
    def get_next_id(self) -> int:
        """Get the next available task id.

        Returns:
            The next task id
        """
        pass


class InMemoryTaskRepository(TaskRepository):
    """In-memory implementation of the task repository."""

    def __init__(self):
        """Initialize the in-memory repository."""
        self._tasks: dict[int, Task] = {}
        self._next_id = 1

    def add(self, task: Task) -> None:
        """Add a task to the repository."""
        self._tasks[task.task_id] = task
        if task.task_id >= self._next_id:
            self._next_id = task.task_id + 1

    def get_all(self) -> List[Task]:
        """Get all tasks from the repository."""
        return list(self._tasks.values())

    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Get a task by its id."""
        return self._tasks.get(task_id)

    def update(self, task: Task) -> None:
        """Update a task in the repository."""
        if task.task_id in self._tasks:
            self._tasks[task.task_id] = task

    def get_next_id(self) -> int:
        """Get the next available task id."""
        return self._next_id
