"""Tests for the TaskService."""
import pytest
from src.data.task import Task
from src.data.task_repository import InMemoryTaskRepository
from src.business.task_service import TaskService


class TestTaskService:
    """Test cases for the TaskService."""

    def test_create_task(self):
        """Test creating a new task."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        
        task = service.create_task("Buy groceries")
        
        assert task.task_id == 1
        assert task.description == "Buy groceries"
        assert task.completed is False

    def test_create_task_with_empty_description_raises_error(self):
        """Test that creating a task with empty description raises ValueError."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        
        with pytest.raises(ValueError, match="Task description cannot be empty"):
            service.create_task("")

    def test_create_task_with_whitespace_only_description_raises_error(self):
        """Test that creating a task with whitespace only raises ValueError."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        
        with pytest.raises(ValueError, match="Task description cannot be empty"):
            service.create_task("   ")

    def test_create_multiple_tasks(self):
        """Test creating multiple tasks with sequential ids."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        
        task1 = service.create_task("Task 1")
        task2 = service.create_task("Task 2")
        
        assert task1.task_id == 1
        assert task2.task_id == 2

    def test_get_all_tasks(self):
        """Test retrieving all tasks."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        service.create_task("Task 1")
        service.create_task("Task 2")
        
        tasks = service.get_all_tasks()
        
        assert len(tasks) == 2
        assert tasks[0].description == "Task 1"
        assert tasks[1].description == "Task 2"

    def test_get_all_tasks_returns_empty_list_initially(self):
        """Test that get_all_tasks returns empty list for new service."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        
        tasks = service.get_all_tasks()
        
        assert tasks == []

    def test_complete_task(self):
        """Test completing a task by id."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        task = service.create_task("Buy groceries")
        
        service.complete_task(1)
        
        completed_task = repo.get_by_id(1)
        assert completed_task.completed is True

    def test_complete_nonexistent_task_raises_error(self):
        """Test that completing a nonexistent task raises ValueError."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        
        with pytest.raises(ValueError, match="Task with id 999 not found"):
            service.complete_task(999)

    def test_complete_already_completed_task(self):
        """Test that completing an already completed task works without error."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        task = service.create_task("Buy groceries")
        service.complete_task(1)
        
        service.complete_task(1)  # Complete again
        
        completed_task = repo.get_by_id(1)
        assert completed_task.completed is True

    def test_complete_task_with_invalid_id_raises_error(self):
        """Test that completing a task with invalid id raises ValueError."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        
        with pytest.raises(ValueError, match="Task id must be a positive integer"):
            service.complete_task(0)
        
        with pytest.raises(ValueError, match="Task id must be a positive integer"):
            service.complete_task(-1)
