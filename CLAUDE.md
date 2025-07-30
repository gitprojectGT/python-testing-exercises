# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python exercise/learning repository with a virtual environment setup using Python 3.12.4. The project uses PyCharm as the IDE and has a clean virtual environment configured.

## Development Environment

- **Python Version**: 3.12.4
- **Virtual Environment**: Located in `.venv/` directory
- **IDE**: PyCharm (configuration in `.idea/`)

## Common Commands

### Environment Setup
```bash
# Activate virtual environment (Windows)
.venv\Scripts\activate

# Activate virtual environment (Unix/macOS - if applicable)
source .venv/bin/activate

# Install dependencies (when requirements.txt exists)
pip install -r requirements.txt

# Install packages for development
pip install pytest black flake8 mypy
```

### Running Code
```bash
# Run Python files
python filename.py

# Run with virtual environment activated
.venv\Scripts\python filename.py
```

### Testing and Code Quality
```bash
# Run tests (when test files exist)
python -m pytest

# Run tests with verbose output
python -m pytest -v

# Format code with black
black .

# Lint with flake8
flake8 .

# Type checking with mypy
mypy .
```

## Project Structure

Currently empty - this is a fresh Python project setup. When adding code:

- Place source files in the root directory or create appropriate package directories
- Create `tests/` directory for test files
- Add `requirements.txt` for project dependencies
- Consider adding `pyproject.toml` for modern Python project configuration

## Notes

- The virtual environment is already configured and should be activated before development
- PyCharm project files are present in `.idea/` directory
- No existing source code or configuration files - this is a blank slate for Python exercises