# Python Coding Exercises for Software Testers

A comprehensive collection of Python exercises specifically designed for software testers to develop programming skills, automation capabilities, and testing expertise.

## 🎯 Overview

This repository contains **17 carefully crafted exercises** organized into three difficulty levels, each focusing on real-world testing scenarios and practical skills that software testers need in their daily work.

## 📚 Exercise Structure

### 🌱 Basic Exercises (5 exercises)
**Location**: `1-basic-exercises/`
**Focus**: Fundamental Python concepts and basic testing scenarios

1. **String Validation** - Input validation, boundary conditions, string operations
2. **List Operations** - Data structure operations, edge cases, searching algorithms
3. **Simple Calculator** - Mathematical operations, exception handling, type validation
4. **Password Validator** - Multiple validation criteria, security testing concepts
5. **File Reader** - File I/O testing, error scenarios, data processing

### 🚀 Intermediate Exercises (6 exercises)
**Location**: `2-intermediate-exercises/`
**Focus**: Object-oriented programming, complex data structures, real-world testing applications

1. **Test Data Generator** - Generating realistic test data for various scenarios
2. **API Response Parser** - JSON validation, schema validation, error handling
3. **Test Case Manager** - Managing test cases and execution results
4. **Configuration Validator** - Validating application configurations
5. **Log File Analyzer** - Analyzing application logs for patterns and issues
6. **Database Mock** - Creating mock database operations for testing

### ⚡ Advanced Exercises (6+ exercises)
**Location**: `3-advanced-exercises/`
**Focus**: Framework design, advanced patterns, distributed systems

1. **Test Framework Builder** - Building a custom testing framework from scratch
2. **API Test Automation** - Comprehensive API testing automation framework
3. **Performance Test Suite** - Performance testing and load simulation framework
4. **Test Data Factory** - Advanced test data generation and management
5. **Mock Server Framework** - HTTP mock server for API testing
6. **Test Orchestrator** - Distributed test execution and orchestration

## 🛠 Getting Started

### Prerequisites
- Python 3.8 or higher
- Basic understanding of programming concepts
- Familiarity with testing terminology

### Setup
1. Clone or download this repository
2. Navigate to the project directory
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Windows
   .venv\\Scripts\\activate
   # Unix/macOS
   source .venv/bin/activate
   ```
4. Install basic dependencies (optional):
   ```bash
   pip install pytest requests
   ```

### Running Exercises
Each exercise is self-contained with detailed instructions:

```bash
# Navigate to an exercise level
cd 1-basic-exercises

# Run a specific exercise
python 01_string_validation.py
```

## 🧪 Running Tests

This repository includes a comprehensive test suite to validate your exercise implementations and track your progress.

### Quick Start
```bash
# Run all basic level tests
python -m pytest tests/basic/ -v

# Run specific exercise tests
python -m pytest tests/basic/test_01_string_validation.py -v

# Run tests for intermediate exercises
python -m pytest tests/intermediate/ -v
```

### Test Infrastructure
The `tests/` directory contains:
- **Basic tests**: `tests/basic/` - Tests for exercises 1-5
- **Intermediate tests**: `tests/intermediate/` - Tests for exercises 6-11  
- **Advanced tests**: `tests/advanced/` - Tests for exercises 12-17
- **Test utilities**: Fixtures, helpers, and configuration files

### Using the Test Runners

#### Interactive Test Runner
```bash
# Run the interactive test runner
python tests/run_tests.py
```
This will present a menu to choose which tests to run.

#### Command-Line Test Runner
```bash
# Run all tests
python tests/test_runner.py --all

# Run tests by level
python tests/test_runner.py --level basic
python tests/test_runner.py --level intermediate  
python tests/test_runner.py --level advanced

# Run specific exercise tests
python tests/test_runner.py --exercise 01_string_validation

# Generate coverage report
python tests/test_runner.py --level basic --coverage

# List available exercises
python tests/test_runner.py --list

# Validate test environment
python tests/test_runner.py --validate
```

### Test Features

#### Comprehensive Coverage
Each test file includes:
- **Unit tests** for individual functions
- **Integration tests** for complete workflows
- **Edge case testing** for boundary conditions
- **Error handling validation**
- **Performance tests** for larger inputs

#### Test Categories
Tests are organized into logical groups:
```bash
# Run only fast tests
python -m pytest tests/ -m "not slow"

# Run performance tests
python -m pytest tests/ -m "slow"

# Run specific test categories
python -m pytest tests/ -k "test_validation"
```

#### Test Status Tracking
- ✅ **Tests pass**: Exercise is correctly implemented
- ❌ **Tests fail**: Implementation needs work or doesn't exist yet
- ⏭️ **Tests skipped**: Module couldn't be imported (not implemented)

### Understanding Test Results

#### When Starting (Exercises Not Implemented)
```
FAILED tests/basic/test_01_string_validation.py - ImportError
SKIPPED - Could not import string validation module
```
This is expected - tests will fail until you implement the exercises.

#### During Development
```
FAILED tests/basic/test_01_string_validation.py::test_is_valid_email - AssertionError
```
Tests help guide your implementation by showing what functionality is expected.

#### When Complete
```
PASSED tests/basic/test_01_string_validation.py::test_is_valid_email
```
Green tests indicate your implementation meets the requirements.

### Test-Driven Development Workflow

1. **Read the exercise description** in the exercise file
2. **Run the tests** to see what needs to be implemented:
   ```bash
   python -m pytest tests/basic/test_01_string_validation.py -v
   ```
3. **Implement functions** until tests pass
4. **Refactor and improve** while keeping tests green
5. **Add additional features** and extend tests as needed

### Prerequisites for Testing
```bash
# Install testing dependencies
pip install pytest pytest-cov

# Optional: Install additional testing tools
pip install pytest-html pytest-xdist
```

### Advanced Test Options
```bash
# Generate HTML coverage report
python tests/test_runner.py --level basic --coverage --html

# Run tests in parallel
python -m pytest tests/ -n auto

# Generate detailed HTML test report
python -m pytest tests/ --html=reports/test_report.html

# Run with specific timeout
python tests/test_runner.py --level basic --timeout 30

# Skip slow tests
python tests/test_runner.py --level basic --markers "not slow"
```

## 📖 Learning Path

### For Beginners
1. Start with **Basic Exercises** (1-5)
2. Focus on understanding Python syntax and concepts
3. Practice writing simple test scenarios
4. Learn error handling and edge case testing

### For Intermediate Testers
1. Complete Basic Exercises first
2. Tackle **Intermediate Exercises** (1-6)
3. Focus on object-oriented programming
4. Learn to work with APIs, databases, and configurations
5. Practice building reusable testing utilities

### For Advanced Practitioners
1. Complete Basic and Intermediate exercises
2. Dive into **Advanced Exercises** (1-6)
3. Focus on framework design and architecture
4. Learn advanced patterns and distributed systems
5. Build production-ready testing tools

## 💡 Key Learning Objectives

By completing these exercises, you will:

✅ **Master Python fundamentals** relevant to testing
✅ **Build practical testing utilities** and automation tools
✅ **Understand testing frameworks** and their architecture
✅ **Learn data validation and processing** techniques
✅ **Practice error handling and edge case testing**
✅ **Develop API testing and mocking skills**
✅ **Create performance testing capabilities**
✅ **Design extensible and maintainable test code**

## 🔧 Skills Developed

### Programming Skills
- Python syntax, data structures, and OOP
- Error handling and exception management
- File I/O and data processing
- Regular expressions and pattern matching
- Async programming and concurrency

### Testing Skills
- Test case design and management
- Data-driven testing approaches
- Mock objects and test doubles
- API testing and validation
- Performance testing fundamentals
- Test automation frameworks

### Software Engineering
- Design patterns and architecture
- Plugin systems and extensibility
- Configuration management
- Logging and monitoring
- Documentation and code quality

## 📁 Repository Structure

```
PythonExercise/
├── README.md                          # This file
├── CLAUDE.md                          # AI assistant guidance
├── 1-basic-exercises/
│   ├── README.md                      # Basic exercises overview
│   ├── 01_string_validation.py        # String operations and validation
│   ├── 02_list_operations.py          # List manipulation and searching
│   ├── 03_simple_calculator.py        # Math operations with error handling
│   ├── 04_password_validator.py       # Complex validation rules
│   └── 05_file_reader.py              # File operations and processing
├── 2-intermediate-exercises/
│   ├── README.md                      # Intermediate exercises overview
│   ├── 01_test_data_generator.py      # Test data generation
│   ├── 02_api_response_parser.py      # API response validation
│   ├── 03_test_case_manager.py        # Test case organization
│   ├── 04_config_validator.py         # Configuration validation
│   ├── 05_log_analyzer.py             # Log file analysis
│   └── 06_database_mock.py            # Database mocking
└── 3-advanced-exercises/
    ├── README.md                      # Advanced exercises overview
    ├── 01_test_framework.py           # Custom testing framework
    ├── 02_api_automation.py           # API testing automation
    ├── 03_performance_testing.py      # Performance testing suite
    ├── 04_test_data_factory.py        # Advanced data generation
    ├── 05_mock_server.py              # HTTP mock server
    └── 06_test_orchestrator.py        # Distributed test execution
```

## 🎯 Exercise Features

### Progressive Difficulty
Each exercise builds upon previous concepts while introducing new challenges and techniques.

### Real-World Scenarios
All exercises are based on actual testing scenarios you'll encounter in professional software testing.

### Comprehensive Documentation
Each exercise includes:
- Clear problem statements
- Learning objectives
- Implementation guidelines
- Test cases for verification
- Extension suggestions

### Self-Contained
Each exercise is complete and runnable on its own, with no external dependencies required for core functionality.

## 🤝 Best Practices Emphasized

- **Code Quality**: Clean, readable, and well-documented code
- **Error Handling**: Proper exception handling and edge case management
- **Testing**: Writing tests for your testing tools
- **Documentation**: Clear docstrings and comments
- **Modularity**: Reusable components and separation of concerns
- **Performance**: Efficient algorithms and resource management

## 🔍 Common Testing Patterns

Throughout the exercises, you'll encounter and implement:

- **Page Object Model** patterns
- **Data-Driven Testing** approaches  
- **Mock and Stub** implementations
- **Factory and Builder** patterns
- **Observer and Command** patterns
- **Repository and Strategy** patterns

## 📊 Assessment and Progress

### Self-Assessment
Each exercise includes test cases and examples to verify your implementation.

### Progress Tracking
- Mark exercises as complete in your personal notes
- Build a portfolio of testing utilities
- Integrate tools across different exercises

### Extension Ideas
- Combine exercises to create larger systems
- Add new features and capabilities
- Integrate with popular testing frameworks
- Deploy tools in real testing environments

## 🌟 Beyond the Exercises

### Integration Opportunities
- Use the Test Data Generator with API Automation
- Combine the Mock Server with the Test Framework
- Integrate Log Analyzer with Performance Testing
- Use Database Mock across multiple test suites

### Production Readiness
Advanced exercises include production-ready features:
- Configuration management
- Logging and monitoring
- Error reporting and recovery
- Scalability considerations
- Security best practices

## 📚 Additional Resources

### Recommended Reading
- "Effective Python" by Brett Slatkin
- "Clean Code" by Robert C. Martin  
- "Test-Driven Development" by Kent Beck
- "Continuous Delivery" by Jez Humble

### Python Testing Frameworks
- **pytest** - Modern Python testing framework
- **unittest** - Built-in Python testing framework
- **Robot Framework** - Keyword-driven testing framework
- **behave** - Behavior-driven development framework

### API Testing Tools
- **requests** - HTTP library for Python
- **aiohttp** - Async HTTP client/server framework
- **httpx** - Modern HTTP client
- **Postman** - API development environment

## 🚀 Getting Help

Each exercise includes:
- Detailed problem descriptions
- Implementation hints and tips
- Common pitfalls to avoid
- Extension suggestions
- Reference implementations (in comments)

## 🎉 Completion Certificate

After completing all exercises, you'll have:
- A comprehensive portfolio of testing tools
- Deep understanding of Python for testing
- Experience with multiple testing patterns
- Ready-to-use utilities for real projects
- Foundation for advanced testing automation

---

**Happy coding and testing!** 🧪✨

This collection represents hundreds of hours of carefully crafted exercises designed specifically for software testers. Each exercise teaches practical skills you'll use in your testing career while building a strong foundation in Python programming.

Start with the basics, work your way through intermediate challenges, and tackle the advanced exercises to become a proficient testing automation engineer!