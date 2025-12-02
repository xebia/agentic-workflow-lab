"""Integration test for the Task Manager CLI."""
from src.data.task_repository import InMemoryTaskRepository
from src.business.task_service import TaskService
from src.presentation.cli import CLI
from io import StringIO


def test_complete_workflow():
    """Test the complete workflow: add, list, complete."""
    # Setup
    repo = InMemoryTaskRepository()
    service = TaskService(repo)
    cli = CLI(service)
    
    # Test 1: Add a task
    output = StringIO()
    cli.execute(["add", "Buy groceries"], output)
    assert "Task added: 1. Buy groceries" in output.getvalue()
    
    # Test 2: Add another task
    output = StringIO()
    cli.execute(["add", "Walk the dog"], output)
    assert "Task added: 2. Walk the dog" in output.getvalue()
    
    # Test 3: List tasks
    output = StringIO()
    cli.execute(["list"], output)
    result = output.getvalue()
    assert "1. Buy groceries" in result
    assert "2. Walk the dog" in result
    assert "[✓]" not in result  # No completed tasks yet
    
    # Test 4: Complete first task
    output = StringIO()
    cli.execute(["complete", "1"], output)
    assert "Task 1 completed" in output.getvalue()
    
    # Test 5: List tasks again
    output = StringIO()
    cli.execute(["list"], output)
    result = output.getvalue()
    assert "1. Buy groceries [✓]" in result
    assert "2. Walk the dog" in result
    assert "[✓]" in result  # At least one completed task
    
    # Verify final state
    all_tasks = service.get_all_tasks()
    assert len(all_tasks) == 2
    assert all_tasks[0].completed is True
    assert all_tasks[1].completed is False


if __name__ == "__main__":
    test_complete_workflow()
    print("✓ Integration test passed!")
