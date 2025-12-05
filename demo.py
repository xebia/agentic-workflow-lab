#!/usr/bin/env python3
"""Demo script showing Task Manager CLI usage."""
import sys
sys.path.insert(0, '.')

from src.data.task_repository import InMemoryTaskRepository
from src.business.task_service import TaskService
from src.presentation.cli import CLI
from io import StringIO


def demo():
    """Demonstrate the Task Manager CLI functionality."""
    print("=" * 60)
    print("Task Manager CLI - Demo")
    print("=" * 60)
    print()
    
    # Setup
    repo = InMemoryTaskRepository()
    service = TaskService(repo)
    cli = CLI(service)
    
    # Demo 1: Add tasks
    print("1. Adding tasks:")
    print("   Command: add 'Buy groceries'")
    output = StringIO()
    cli.execute(["add", "Buy groceries"], output)
    print(f"   {output.getvalue()}", end="")
    
    print("   Command: add 'Walk the dog'")
    output = StringIO()
    cli.execute(["add", "Walk the dog"], output)
    print(f"   {output.getvalue()}", end="")
    
    print("   Command: add 'Read a book'")
    output = StringIO()
    cli.execute(["add", "Read a book"], output)
    print(f"   {output.getvalue()}", end="")
    print()
    
    # Demo 2: List tasks
    print("2. Listing all tasks:")
    print("   Command: list")
    output = StringIO()
    cli.execute(["list"], output)
    for line in output.getvalue().split('\n'):
        if line:
            print(f"   {line}")
    print()
    
    # Demo 3: Complete a task
    print("3. Completing a task:")
    print("   Command: complete 1")
    output = StringIO()
    cli.execute(["complete", "1"], output)
    print(f"   {output.getvalue()}", end="")
    print()
    
    # Demo 4: List tasks again
    print("4. Listing tasks after completion:")
    print("   Command: list")
    output = StringIO()
    cli.execute(["list"], output)
    for line in output.getvalue().split('\n'):
        if line:
            print(f"   {line}")
    print()
    
    # Demo 5: Complete another task
    print("5. Completing another task:")
    print("   Command: complete 3")
    output = StringIO()
    cli.execute(["complete", "3"], output)
    print(f"   {output.getvalue()}", end="")
    print()
    
    # Demo 6: Final list
    print("6. Final task list:")
    print("   Command: list")
    output = StringIO()
    cli.execute(["list"], output)
    for line in output.getvalue().split('\n'):
        if line:
            print(f"   {line}")
    print()
    
    print("=" * 60)
    print("Demo completed successfully! ✓")
    print("=" * 60)


if __name__ == "__main__":
    demo()
