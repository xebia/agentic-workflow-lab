"""Tests for the Task model."""
import pytest
from src.data.task import Task


class TestTask:
    """Test cases for the Task model."""

    def test_create_task_with_id_and_description(self):
        """Test creating a task with id and description."""
        task = Task(task_id=1, description="Buy groceries")
        
        assert task.task_id == 1
        assert task.description == "Buy groceries"
        assert task.completed is False

    def test_create_task_defaults_to_not_completed(self):
        """Test that a new task is not completed by default."""
        task = Task(task_id=1, description="Test task")
        
        assert task.completed is False

    def test_create_task_with_completed_status(self):
        """Test creating a task with a specific completed status."""
        task = Task(task_id=1, description="Test task", completed=True)
        
        assert task.completed is True

    def test_mark_task_as_completed(self):
        """Test marking a task as completed."""
        task = Task(task_id=1, description="Test task")
        
        task.mark_completed()
        
        assert task.completed is True

    def test_task_string_representation(self):
        """Test the string representation of a task."""
        task = Task(task_id=1, description="Buy groceries")
        
        assert str(task) == "1. Buy groceries"

    def test_completed_task_string_representation(self):
        """Test the string representation of a completed task."""
        task = Task(task_id=1, description="Buy groceries", completed=True)
        
        assert str(task) == "1. Buy groceries [✓]"
