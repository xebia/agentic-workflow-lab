"""Tests for the TaskRepository."""
import pytest
from src.data.task import Task
from src.data.task_repository import TaskRepository, InMemoryTaskRepository


class TestInMemoryTaskRepository:
    """Test cases for the InMemoryTaskRepository."""

    def test_add_task(self):
        """Test adding a task to the repository."""
        repo = InMemoryTaskRepository()
        task = Task(task_id=1, description="Buy groceries")
        
        repo.add(task)
        
        tasks = repo.get_all()
        assert len(tasks) == 1
        assert tasks[0].task_id == 1
        assert tasks[0].description == "Buy groceries"

    def test_add_multiple_tasks(self):
        """Test adding multiple tasks to the repository."""
        repo = InMemoryTaskRepository()
        task1 = Task(task_id=1, description="Buy groceries")
        task2 = Task(task_id=2, description="Walk the dog")
        
        repo.add(task1)
        repo.add(task2)
        
        tasks = repo.get_all()
        assert len(tasks) == 2

    def test_get_all_returns_empty_list_initially(self):
        """Test that get_all returns an empty list for a new repository."""
        repo = InMemoryTaskRepository()
        
        tasks = repo.get_all()
        
        assert tasks == []

    def test_get_by_id_returns_task(self):
        """Test retrieving a task by its id."""
        repo = InMemoryTaskRepository()
        task = Task(task_id=1, description="Buy groceries")
        repo.add(task)
        
        retrieved_task = repo.get_by_id(1)
        
        assert retrieved_task is not None
        assert retrieved_task.task_id == 1
        assert retrieved_task.description == "Buy groceries"

    def test_get_by_id_returns_none_for_nonexistent_task(self):
        """Test that get_by_id returns None for a task that doesn't exist."""
        repo = InMemoryTaskRepository()
        
        retrieved_task = repo.get_by_id(999)
        
        assert retrieved_task is None

    def test_update_task(self):
        """Test updating a task in the repository."""
        repo = InMemoryTaskRepository()
        task = Task(task_id=1, description="Buy groceries")
        repo.add(task)
        
        task.mark_completed()
        repo.update(task)
        
        retrieved_task = repo.get_by_id(1)
        assert retrieved_task.completed is True

    def test_update_nonexistent_task_does_nothing(self):
        """Test that updating a nonexistent task doesn't cause errors."""
        repo = InMemoryTaskRepository()
        task = Task(task_id=999, description="Nonexistent")
        
        repo.update(task)  # Should not raise an exception
        
        assert repo.get_by_id(999) is None

    def test_get_next_id_starts_at_one(self):
        """Test that the first task id is 1."""
        repo = InMemoryTaskRepository()
        
        next_id = repo.get_next_id()
        
        assert next_id == 1

    def test_get_next_id_increments(self):
        """Test that get_next_id returns sequential ids."""
        repo = InMemoryTaskRepository()
        task1 = Task(task_id=repo.get_next_id(), description="Task 1")
        repo.add(task1)
        
        next_id = repo.get_next_id()
        
        assert next_id == 2

    def test_get_next_id_after_multiple_tasks(self):
        """Test that get_next_id returns correct id after multiple tasks."""
        repo = InMemoryTaskRepository()
        
        for i in range(1, 4):
            task = Task(task_id=repo.get_next_id(), description=f"Task {i}")
            repo.add(task)
        
        next_id = repo.get_next_id()
        assert next_id == 4
