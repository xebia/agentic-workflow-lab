"""Tests for the CLI."""
import pytest
from io import StringIO
from src.presentation.cli import CLI
from src.business.task_service import TaskService
from src.data.task_repository import InMemoryTaskRepository


class TestCLI:
    """Test cases for the CLI."""

    def test_add_command(self):
        """Test the add command."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        cli = CLI(service)
        output = StringIO()
        
        cli.execute(["add", "Buy groceries"], output)
        
        result = output.getvalue()
        assert "Task added: 1. Buy groceries" in result
        
        tasks = service.get_all_tasks()
        assert len(tasks) == 1
        assert tasks[0].description == "Buy groceries"

    def test_add_command_with_quoted_description(self):
        """Test the add command with a quoted description."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        cli = CLI(service)
        output = StringIO()
        
        cli.execute(["add", "Buy groceries"], output)
        
        result = output.getvalue()
        assert "Task added: 1. Buy groceries" in result

    def test_add_command_without_description(self):
        """Test the add command without a description."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        cli = CLI(service)
        output = StringIO()
        
        cli.execute(["add"], output)
        
        result = output.getvalue()
        assert "Error: Task description is required" in result

    def test_list_command_with_no_tasks(self):
        """Test the list command when there are no tasks."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        cli = CLI(service)
        output = StringIO()
        
        cli.execute(["list"], output)
        
        result = output.getvalue()
        assert "No tasks found" in result

    def test_list_command_with_tasks(self):
        """Test the list command with tasks."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        service.create_task("Buy groceries")
        service.create_task("Walk the dog")
        cli = CLI(service)
        output = StringIO()
        
        cli.execute(["list"], output)
        
        result = output.getvalue()
        assert "1. Buy groceries" in result
        assert "2. Walk the dog" in result

    def test_list_command_with_completed_task(self):
        """Test the list command with a completed task."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        service.create_task("Buy groceries")
        service.complete_task(1)
        cli = CLI(service)
        output = StringIO()
        
        cli.execute(["list"], output)
        
        result = output.getvalue()
        assert "1. Buy groceries [✓]" in result

    def test_complete_command(self):
        """Test the complete command."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        service.create_task("Buy groceries")
        cli = CLI(service)
        output = StringIO()
        
        cli.execute(["complete", "1"], output)
        
        result = output.getvalue()
        assert "Task 1 completed" in result
        
        task = service.get_all_tasks()[0]
        assert task.completed is True

    def test_complete_command_without_id(self):
        """Test the complete command without a task id."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        cli = CLI(service)
        output = StringIO()
        
        cli.execute(["complete"], output)
        
        result = output.getvalue()
        assert "Error: Task id is required" in result

    def test_complete_command_with_invalid_id(self):
        """Test the complete command with an invalid task id."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        cli = CLI(service)
        output = StringIO()
        
        cli.execute(["complete", "abc"], output)
        
        result = output.getvalue()
        assert "Error: Task id must be a number" in result

    def test_complete_command_with_nonexistent_id(self):
        """Test the complete command with a nonexistent task id."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        cli = CLI(service)
        output = StringIO()
        
        cli.execute(["complete", "999"], output)
        
        result = output.getvalue()
        assert "Error: Task with id 999 not found" in result

    def test_unknown_command(self):
        """Test an unknown command."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        cli = CLI(service)
        output = StringIO()
        
        cli.execute(["unknown"], output)
        
        result = output.getvalue()
        assert "Error: Unknown command 'unknown'" in result
        assert "Available commands: add, list, complete" in result

    def test_no_command(self):
        """Test with no command provided."""
        repo = InMemoryTaskRepository()
        service = TaskService(repo)
        cli = CLI(service)
        output = StringIO()
        
        cli.execute([], output)
        
        result = output.getvalue()
        assert "Error: No command provided" in result
        assert "Available commands: add, list, complete" in result
