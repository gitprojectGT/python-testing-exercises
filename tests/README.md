
# Test Suite for Python Exercises

This directory contains comprehensive test suites for all Python exercises. The tests help you verify that your implementations work correctly and meet the expected requirements.

## 📁 Structure

```
tests/
├── README.md                    # This file
├── conftest.py                  # pytest configuration and fixtures
├── test_runner.py               # Custom test runner
├── requirements.txt             # Test dependencies
├── basic/                       # Tests for basic exercises
│   ├── test_01_string_validation.py
│   ├── test_02_list_operations.py
│   ├── test_03_simple_calculator.py
│   ├── test_04_password_validator.py
│   └── test_05_file_reader.py
├── intermediate/                # Tests for intermediate exercises
│   ├── test_01_test_data_generator.py
│   ├── test_02_api_response_parser.py
│   ├── test_03_test_case_manager.py
│   ├── test_04_config_validator.py
│   ├── test_05_log_analyzer.py
│   └── test_06_database_mock.py
└── advanced/                    # Tests for advanced exercises
    ├── test_01_test_framework.py
    ├── test_02_api_automation.py
    ├── test_03_performance_testing.py
    ├── test_04_test_data_factory.py
    ├── test_05_mock_server.py
    └── test_06_test_orchestrator.py
```

## 🚀 Running Tests

### Prerequisites
```bash
# Install test dependencies
pip install pytest pytest-asyncio pytest-mock

# Or install from requirements
pip install -r tests/requirements.txt
```

### Run All Tests
```bash
# From project root
python -m pytest tests/ -v

# With coverage
python -m pytest tests/ -v --cov=. --cov-report=html
```

### Run Tests by Level
```bash
# Basic exercises only
python -m pytest tests/basic/ -v

# Intermediate exercises only
python -m pytest tests/intermediate/ -v

# Advanced exercises only
python -m pytest tests/advanced/ -v
```

### Run Specific Exercise Tests
```bash
# Test specific exercise
python -m pytest tests/basic/test_01_string_validation.py -v

# Test specific function
python -m pytest tests/basic/test_01_string_validation.py::test_is_valid_email -v
```

### Run with Custom Test Runner
```bash
# Use custom test runner
python tests/test_runner.py --level basic
python tests/test_runner.py --exercise 01_string_validation
python tests/test_runner.py --all
```

## 📊 Test Categories

### ✅ Functionality Tests
- Test core functionality of each implementation
- Verify correct outputs for valid inputs
- Check proper handling of edge cases

### 🚨 Error Handling Tests
- Test exception handling
- Verify error messages and types
- Check graceful degradation

### 🎯 Edge Case Tests
- Boundary value testing
- Empty/null input handling
- Large input handling
- Invalid input scenarios

### 📈 Performance Tests
- Basic performance validation
- Memory usage checks
- Timeout verification

### 🔧 Integration Tests
- Test component interactions
- End-to-end workflow testing
- External dependency mocking

## 🎨 Test Patterns Used

### Parameterized Tests
```python
@pytest.mark.parametrize("input_data,expected", [
    ("test@example.com", True),
    ("invalid.email", False),
])
def test_email_validation(input_data, expected):
    assert is_valid_email(input_data) == expected
```

### Fixtures
```python
@pytest.fixture
def sample_data():
    return {"test": "data"}

def test_with_fixture(sample_data):
    assert sample_data["test"] == "data"
```

### Mocking
```python
@patch('module.external_call')
def test_with_mock(mock_call):
    mock_call.return_value = "mocked"
    result = function_under_test()
    assert result == "expected"
```

### Async Testing
```python
@pytest.mark.asyncio
async def test_async_function():
    result = await async_function()
    assert result is not None
```

## 🎯 Test Implementation Guidelines

### For Exercise Implementers
1. **Run tests first** - See what's expected before implementing
2. **Implement incrementally** - Make one test pass at a time
3. **Check edge cases** - Don't just make happy path tests pass
4. **Validate error handling** - Make sure exceptions are handled properly

### For Test Writers
1. **Comprehensive coverage** - Test all public methods and edge cases
2. **Clear test names** - Use descriptive names that explain what's being tested
3. **Independent tests** - Each test should be able to run in isolation
4. **Good test data** - Use realistic and varied test data

## 📋 Test Checklist

When implementing an exercise, ensure:
- [ ] All functionality tests pass
- [ ] Error handling tests pass
- [ ] Edge case tests pass
- [ ] Performance tests pass (if applicable)
- [ ] Integration tests pass (if applicable)
- [ ] No test failures or warnings
- [ ] Code coverage is reasonable (aim for >80%)

## 🐛 Debugging Failed Tests

### Common Issues
1. **Import errors** - Check your module structure and imports
2. **Missing methods** - Implement all required methods marked with TODO
3. **Wrong return types** - Check expected return types in test assertions
4. **Exception handling** - Make sure you handle expected exceptions

### Debug Commands
```bash
# Run with verbose output
python -m pytest tests/ -v -s

# Run with debugging on failure
python -m pytest tests/ --pdb

# Run with coverage to see what's not tested
python -m pytest tests/ --cov=. --cov-report=term-missing
```

## 🎓 Learning from Tests

Tests are excellent learning tools:
- **See expected behavior** - Tests show exactly how functions should work
- **Understand edge cases** - Learn what corner cases to handle
- **Learn best practices** - See how to structure and validate code
- **Get immediate feedback** - Know instantly if your implementation works

## 💡 Tips for Success

1. **Read tests first** - Understand requirements before coding
2. **Start simple** - Make basic tests pass before tackling complex ones
3. **Use TDD approach** - Write tests first, then implement
4. **Don't skip edge cases** - They often reveal important bugs
5. **Keep tests running** - Re-run tests frequently during development

Happy testing! 🧪✨