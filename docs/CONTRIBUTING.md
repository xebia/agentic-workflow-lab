# Contributing Guidelines

This document provides code style guidelines and best practices for the Task Manager CLI project written in Python.

## Code Style and Standards

### Naming Conventions

- **Classes**: Use `PascalCase` (e.g., `TaskService`, `InMemoryTaskRepository`)
- **Functions and methods**: Use `snake_case` (e.g., `create_task`, `get_all_tasks`)
- **Variables**: Use `snake_case` (e.g., `task_id`, `description`)
- **Constants**: Use `UPPER_SNAKE_CASE` (e.g., `MAX_TASKS`, `DEFAULT_STATUS`)
- **Private methods/attributes**: Prefix with single underscore (e.g., `_handle_add`, `_tasks`)

### Code Formatting

- Follow [PEP 8](https://pep.python.org/pep-0008/) style guide
- Use 4 spaces for indentation (no tabs)
- Maximum line length: 100 characters
- Use double quotes `"` for strings (consistently throughout the project)
- Add blank lines to separate logical sections within functions
- Use type hints for function parameters and return values

### File Organization

```
src/
├── data/              # Data layer - models and repositories
├── business/          # Business logic layer - services
└── presentation/      # Presentation layer - CLI interface
tests/                 # Test files mirroring src/ structure
```

- Each layer has its own package with `__init__.py`
- One class per file (when practical)
- Test files named `test_<module_name>.py`
- Keep imports organized: standard library, third-party, local modules

## Architecture and Design Principles

### Design Patterns

- **Layered Architecture**: Strict separation between presentation, business, and data layers
- **Repository Pattern**: Abstract data access through repository interfaces
- **Dependency Injection**: Pass dependencies through constructors (e.g., `TaskService(repository)`)
- **Single Responsibility**: Each class has one clear purpose

### Error Handling

- Raise `ValueError` for invalid input or business logic violations
- Use descriptive error messages that help users understand the problem
- Catch exceptions at the presentation layer and display user-friendly messages
- Let unexpected exceptions bubble up for debugging

Example:
```python
if not description or not description.strip():
    raise ValueError("Task description cannot be empty")
```

### Performance Considerations

- For this demo application, simplicity takes priority over optimization
- In-memory storage is acceptable for the current scope
- Avoid premature optimization - focus on clean, maintainable code
- Consider scalability when extending beyond the MVP

## Language-Specific Best Practices

### Python-Specific Guidelines

1. **Type Hints**: Always use type hints for better IDE support and documentation
   ```python
   def create_task(self, description: str) -> Task:
   ```

2. **Docstrings**: Use Google-style docstrings for all public classes and methods
   ```python
   def create_task(self, description: str) -> Task:
       """Create a new task.

       Args:
           description: Description of the task

       Returns:
           The newly created task

       Raises:
           ValueError: If description is empty
       """
   ```

3. **List Comprehensions**: Use when appropriate for clarity and performance
   ```python
   completed_tasks = [task for task in tasks if task.completed]
   ```

4. **Context Managers**: Use `with` statements for file operations (when persistence is added)

5. **Abstract Base Classes**: Use `ABC` and `@abstractmethod` for interfaces
   ```python
   from abc import ABC, abstractmethod
   
   class TaskRepository(ABC):
       @abstractmethod
       def add(self, task: Task) -> None:
           pass
   ```

6. **Testing**: 
   - Use `pytest` for all tests
   - Follow the Arrange-Act-Assert pattern
   - Test one behavior per test method
   - Use descriptive test names that explain what is being tested

7. **Imports**:
   - Use absolute imports from project root (e.g., `from src.data.task import Task`)
   - Group imports: standard library, third-party, local
   - Avoid wildcard imports (`from module import *`)

## Testing Standards

- Write tests first (TDD approach)
- Achieve comprehensive test coverage for all layers
- Test both success paths and error conditions
- Use descriptive test method names starting with `test_`
- Organize tests in classes mirroring the structure of the code


