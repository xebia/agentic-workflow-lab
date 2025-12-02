"""Command-line interface for the task manager."""
import sys
from typing import List, TextIO
from src.business.task_service import TaskService


class CLI:
    """Command-line interface for managing tasks."""

    def __init__(self, service: TaskService):
        """Initialize the CLI.

        Args:
            service: The task service to use for operations
        """
        self.service = service

    def execute(self, args: List[str], output: TextIO = sys.stdout) -> None:
        """Execute a CLI command.

        Args:
            args: Command-line arguments (command and parameters)
            output: Output stream for writing results
        """
        if not args:
            output.write("Error: No command provided\n")
            output.write("Available commands: add, list, complete\n")
            return

        command = args[0]

        if command == "add":
            self._handle_add(args[1:], output)
        elif command == "list":
            self._handle_list(output)
        elif command == "complete":
            self._handle_complete(args[1:], output)
        else:
            output.write(f"Error: Unknown command '{command}'\n")
            output.write("Available commands: add, list, complete\n")

    def _handle_add(self, args: List[str], output: TextIO) -> None:
        """Handle the add command.

        Args:
            args: Command arguments (task description)
            output: Output stream for writing results
        """
        if not args:
            output.write("Error: Task description is required\n")
            return

        description = " ".join(args)
        
        try:
            task = self.service.create_task(description)
            output.write(f"Task added: {task}\n")
        except ValueError as e:
            output.write(f"Error: {e}\n")

    def _handle_list(self, output: TextIO) -> None:
        """Handle the list command.

        Args:
            output: Output stream for writing results
        """
        tasks = self.service.get_all_tasks()
        
        if not tasks:
            output.write("No tasks found\n")
            return

        for task in tasks:
            output.write(f"{task}\n")

    def _handle_complete(self, args: List[str], output: TextIO) -> None:
        """Handle the complete command.

        Args:
            args: Command arguments (task id)
            output: Output stream for writing results
        """
        if not args:
            output.write("Error: Task id is required\n")
            return

        try:
            task_id = int(args[0])
            self.service.complete_task(task_id)
            output.write(f"Task {task_id} completed\n")
        except ValueError as e:
            if "invalid literal" in str(e):
                output.write("Error: Task id must be a number\n")
            else:
                output.write(f"Error: {e}\n")
