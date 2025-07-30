"""
pytest configuration and shared fixtures for all test modules.
"""

import pytest
import tempfile
import os
import sys
from pathlib import Path
from unittest.mock import Mock, MagicMock
from datetime import datetime, timedelta
import json

# Add the project root to Python path so we can import exercises
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(project_root / "1-basic-exercises"))
sys.path.insert(0, str(project_root / "2-intermediate-exercises"))
sys.path.insert(0, str(project_root / "3-advanced-exercises"))

@pytest.fixture
def temp_dir():
    """Create a temporary directory for tests."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir

@pytest.fixture
def temp_file():
    """Create a temporary file for tests."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False) as tmp:
        yield tmp.name
    # Cleanup
    try:
        os.unlink(tmp.name)
    except FileNotFoundError:
        pass

@pytest.fixture
def sample_text_data():
    """Sample text data for testing."""
    return [
        "Hello, World!",
        "This is a test string.",
        "Python is awesome!",
        "Testing 123",
        "",
        "   spaces   around   ",
        "Mixed CASE text",
        "Special chars: !@#$%^&*()",
    ]

@pytest.fixture
def sample_user_data():
    """Sample user data for testing."""
    return [
        {
            "id": 1,
            "name": "John Doe",
            "email": "john@example.com",
            "age": 30,
            "active": True
        },
        {
            "id": 2,
            "name": "Jane Smith", 
            "email": "jane@example.com",
            "age": 25,
            "active": True
        },
        {
            "id": 3,
            "name": "Bob Johnson",
            "email": "bob@example.com", 
            "age": 35,
            "active": False
        }
    ]

@pytest.fixture
def sample_json_data():
    """Sample JSON data for testing."""
    return {
        "users": [
            {"id": 1, "name": "John", "email": "john@test.com"},
            {"id": 2, "name": "Jane", "email": "jane@test.com"}
        ],
        "metadata": {
            "total": 2,
            "page": 1,
            "per_page": 10
        },
        "timestamp": "2024-01-15T10:30:00Z"
    }

@pytest.fixture
def sample_csv_data():
    """Sample CSV data for testing."""
    return """id,name,email,age
1,John Doe,john@example.com,30
2,Jane Smith,jane@example.com,25
3,Bob Johnson,bob@example.com,35"""

@pytest.fixture
def sample_log_data():
    """Sample log data for testing."""
    return [
        "2024-01-15 10:30:15 INFO [main] Application started successfully",
        "2024-01-15 10:30:16 DEBUG [worker-1] Processing request req-123",
        "2024-01-15 10:30:17 ERROR [worker-2] Database connection failed: timeout after 30s",
        "2024-01-15 10:30:18 WARNING [auth] Failed login attempt for user: admin from IP: 192.168.1.100",
        "2024-01-15 10:30:19 INFO [api] Request completed in 150ms",
        "2024-01-15 10:30:20 ERROR [payment] Credit card validation failed for user 12345"
    ]

@pytest.fixture
def mock_api_response():
    """Mock API response for testing."""
    mock_response = Mock()
    mock_response.status_code = 200
    mock_response.headers = {"Content-Type": "application/json"}
    mock_response.json.return_value = {"message": "success", "data": {"id": 123}}
    mock_response.text = '{"message": "success", "data": {"id": 123}}'
    mock_response.content = b'{"message": "success", "data": {"id": 123}}'
    return mock_response

@pytest.fixture
def mock_database():
    """Mock database for testing."""
    db = MagicMock()
    db.execute.return_value = Mock(fetchall=lambda: [], fetchone=lambda: None, rowcount=0)
    db.commit.return_value = None
    db.rollback.return_value = None
    return db

@pytest.fixture
def sample_config_data():
    """Sample configuration data for testing."""
    return {
        "server": {
            "host": "localhost",
            "port": 8080,
            "ssl_enabled": True
        },
        "database": {
            "host": "db.example.com",
            "port": 5432,
            "username": "testuser",
            "password": "testpass",
            "database": "testdb"
        },
        "logging": {
            "level": "INFO",
            "format": "%(asctime)s - %(name)s - %(levelname)s - %(message)s",
            "file_path": "/var/log/app.log"
        }
    }

@pytest.fixture
def sample_test_cases():
    """Sample test case data for testing."""
    return [
        {
            "id": "tc001",
            "title": "Login with valid credentials",
            "description": "Test successful login with valid username and password",
            "steps": [
                "Navigate to login page",
                "Enter valid username",
                "Enter valid password", 
                "Click login button"
            ],
            "expected_result": "User is logged in successfully",
            "priority": "HIGH",
            "tags": ["login", "authentication", "smoke"]
        },
        {
            "id": "tc002", 
            "title": "Login with invalid credentials",
            "description": "Test login failure with invalid credentials",
            "steps": [
                "Navigate to login page",
                "Enter invalid username",
                "Enter invalid password",
                "Click login button"
            ],
            "expected_result": "Error message is displayed",
            "priority": "MEDIUM",
            "tags": ["login", "authentication", "negative"]
        }
    ]

@pytest.fixture
def current_datetime():
    """Current datetime for consistent testing."""
    return datetime(2024, 1, 15, 10, 30, 0)

@pytest.fixture
def time_range():
    """Time range for testing."""
    start = datetime(2024, 1, 1, 0, 0, 0)
    end = datetime(2024, 1, 31, 23, 59, 59)
    return start, end

# Pytest configuration
def pytest_configure(config):
    """Configure pytest."""
    config.addinivalue_line(
        "markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')"
    )
    config.addinivalue_line(
        "markers", "integration: marks tests as integration tests"
    )
    config.addinivalue_line(
        "markers", "unit: marks tests as unit tests"
    )

def pytest_collection_modifyitems(config, items):
    """Modify collected test items."""
    # Add markers automatically based on test names or paths
    for item in items:
        if "integration" in item.nodeid:
            item.add_marker(pytest.mark.integration)
        elif "unit" in item.nodeid:
            item.add_marker(pytest.mark.unit)
        
        if "slow" in item.name or "performance" in item.name:
            item.add_marker(pytest.mark.slow)

# Helper functions for tests
def create_temp_file_with_content(content: str, suffix: str = ".txt"):
    """Create a temporary file with specific content."""
    with tempfile.NamedTemporaryFile(mode='w', suffix=suffix, delete=False) as f:
        f.write(content)
        return f.name

def create_temp_json_file(data: dict):
    """Create a temporary JSON file with data."""
    content = json.dumps(data, indent=2)
    return create_temp_file_with_content(content, ".json")

def create_temp_csv_file(data: str):
    """Create a temporary CSV file with data."""
    return create_temp_file_with_content(data, ".csv")

# Make helper functions available as fixtures
@pytest.fixture
def create_temp_file_with_content_fixture():
    """Fixture version of create_temp_file_with_content."""
    created_files = []
    
    def _create_file(content: str, suffix: str = ".txt"):
        filename = create_temp_file_with_content(content, suffix)
        created_files.append(filename)
        return filename
    
    yield _create_file
    
    # Cleanup
    for filename in created_files:
        try:
            os.unlink(filename)
        except FileNotFoundError:
            pass