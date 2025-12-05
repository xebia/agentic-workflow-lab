# Task Manager CLI

A simple command-line task manager application for quick demos. Built with Python following a clean layered architecture.

## Features

- **Add Task** - Create a new task with a description
- **List Tasks** - Display all tasks with their status
- **Complete Task** - Mark a task as completed

## Installation

1. Clone the repository
2. Install Python 3.10 or higher
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Add a Task
```bash
python task-manager add "Buy groceries"
```

Output:
```
Task added: 1. Buy groceries
```

### List All Tasks
```bash
python task-manager list
```

Output:
```
1. Buy groceries
2. Walk the dog [✓]
```

### Complete a Task
```bash
python task-manager complete 1
```

Output:
```
Task 1 completed
```

### Windows Users
You can also use the batch file:
```bash
task-manager.bat add "Buy groceries"
task-manager.bat list
task-manager.bat complete 1
```

## Architecture

The application follows a layered architecture with clear separation of concerns:

```
src/
├── data/              # Data layer - Task models and repositories
│   ├── task.py        # Task model
│   └── task_repository.py  # Repository interface and in-memory implementation
├── business/          # Business logic layer
│   └── task_service.py     # Task service with validation
└── presentation/      # Presentation layer
    └── cli.py         # Command-line interface
```

### Key Design Patterns

- **Layered Architecture** - Separation between presentation, business, and data layers
- **Repository Pattern** - Abstract data access through repository interfaces
- **Dependency Injection** - Dependencies passed through constructors

## Testing

Run all tests:
```bash
python -m pytest tests/ -v
```

Run tests with coverage:
```bash
python -m pytest tests/ -v --cov=src --cov-report=term-missing
```

Run integration test:
```bash
python -m pytest tests/test_integration.py -v
```

## Development

### Project Structure
```
agentic-workflow-lab/
├── src/                    # Source code
│   ├── data/              # Data layer
│   ├── business/          # Business logic
│   └── presentation/      # CLI interface
├── tests/                 # Test files
├── docs/                  # Documentation
│   ├── ARCHITECTURE.md    # Architecture design
│   ├── CONTRIBUTING.md    # Coding guidelines
│   └── PRODUCT.md         # Product requirements
├── task-manager           # Main executable (Python script)
├── task-manager.bat       # Windows launcher
└── requirements.txt       # Python dependencies
```

### Contributing

See [CONTRIBUTING.md](docs/CONTRIBUTING.md) for code style guidelines and best practices.

### Key Technologies

- **Python 3.10+** - Programming language
- **pytest** - Testing framework
- **Type hints** - For better IDE support and documentation

## Limitations

- **In-memory storage** - Tasks are not persisted between runs
- **Single user** - No authentication or multi-user support
- **No task editing** - Can only add and complete tasks
- **No task deletion** - Completed tasks remain in the list

These limitations are intentional for the demo scope. See `PRODUCT.md` for the minimal feature set.

## License

This is a learning lab project for demonstrating GitHub Copilot's context engineering features.
