"""
Exercise 2: API Test Automation
Testing Focus: HTTP testing, authentication, data-driven testing

Task: Build a comprehensive API testing automation framework.
This exercise focuses on HTTP client automation, authentication handling, and data-driven API testing.
"""

import json
import time
import asyncio
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Any, Optional, Union, Callable, Tuple
from urllib.parse import urljoin, urlparse
import uuid

class HTTPMethod(Enum):
    """HTTP methods."""
    GET = "GET"
    POST = "POST"
    PUT = "PUT"
    DELETE = "DELETE"
    PATCH = "PATCH"
    HEAD = "HEAD"
    OPTIONS = "OPTIONS"

class AuthType(Enum):
    """Authentication types."""
    NONE = "none"
    BASIC = "basic"
    BEARER = "bearer"
    API_KEY = "api_key"
    OAUTH2 = "oauth2"
    CUSTOM = "custom"

@dataclass
class APIRequest:
    """Represents an API request."""
    method: HTTPMethod
    endpoint: str
    headers: Dict[str, str] = field(default_factory=dict)
    params: Dict[str, Any] = field(default_factory=dict)
    data: Any = None
    json_data: Dict[str, Any] = field(default_factory=dict)
    files: Dict[str, Any] = field(default_factory=dict)
    timeout: int = 30
    follow_redirects: bool = True

@dataclass
class APIResponse:
    """Represents an API response."""
    status_code: int
    headers: Dict[str, str]
    content: bytes
    text: str
    json_data: Optional[Dict[str, Any]] = None
    elapsed_time: float = 0.0
    request: Optional[APIRequest] = None
    error: Optional[str] = None

@dataclass
class TestCase:
    """Represents an API test case."""
    id: str
    name: str
    description: str
    request: APIRequest
    expected_status: int = 200
    expected_response: Dict[str, Any] = field(default_factory=dict)
    validations: List[Callable] = field(default_factory=list)
    setup: Optional[Callable] = None
    teardown: Optional[Callable] = None
    data_provider: Optional[Callable] = None
    tags: List[str] = field(default_factory=list)

class AuthenticationHandler(ABC):
    """Abstract base class for authentication handlers."""
    
    @abstractmethod
    def apply_auth(self, request: APIRequest) -> APIRequest:
        """Apply authentication to request."""
        pass

class BasicAuthHandler(AuthenticationHandler):
    """Basic authentication handler."""
    
    def __init__(self, username: str, password: str):
        """
        Initialize basic auth handler.
        
        Args:
            username (str): Username
            password (str): Password
        """
        self.username = username
        self.password = password
    
    def apply_auth(self, request: APIRequest) -> APIRequest:
        """
        Apply basic authentication to request.
        
        Args:
            request (APIRequest): Request to authenticate
            
        Returns:
            APIRequest: Authenticated request
            
        TODO: Implement this method (use base64 encoding)
        """
        pass

class BearerTokenHandler(AuthenticationHandler):
    """Bearer token authentication handler."""
    
    def __init__(self, token: str):
        """
        Initialize bearer token handler.
        
        Args:
            token (str): Bearer token
        """
        self.token = token
    
    def apply_auth(self, request: APIRequest) -> APIRequest:
        """
        Apply bearer token authentication.
        
        Args:
            request (APIRequest): Request to authenticate
            
        Returns:
            APIRequest: Authenticated request
            
        TODO: Implement this method
        """
        pass

class APIKeyHandler(AuthenticationHandler):
    """API key authentication handler."""
    
    def __init__(self, api_key: str, header_name: str = "X-API-Key"):
        """
        Initialize API key handler.
        
        Args:
            api_key (str): API key
            header_name (str): Header name for API key
        """
        self.api_key = api_key
        self.header_name = header_name
    
    def apply_auth(self, request: APIRequest) -> APIRequest:
        """
        Apply API key authentication.
        
        Args:
            request (APIRequest): Request to authenticate
            
        Returns:
            APIRequest: Authenticated request
            
        TODO: Implement this method
        """
        pass

class HTTPClient:
    """HTTP client for making API requests."""
    
    def __init__(self, base_url: str = "", default_headers: Dict[str, str] = None):
        """
        Initialize HTTP client.
        
        Args:
            base_url (str): Base URL for all requests
            default_headers (dict): Default headers for all requests
        """
        self.base_url = base_url
        self.default_headers = default_headers or {}
        self.session_cookies = {}
        self.request_history: List[Tuple[APIRequest, APIResponse]] = []
    
    def send_request(self, request: APIRequest) -> APIResponse:
        """
        Send an HTTP request.
        
        Args:
            request (APIRequest): Request to send
            
        Returns:
            APIResponse: Response from server
            
        TODO: Implement this method (simulate HTTP calls or use requests library)
        """
        pass
    
    def get(self, endpoint: str, **kwargs) -> APIResponse:
        """
        Send GET request.
        
        Args:
            endpoint (str): API endpoint
            **kwargs: Additional request parameters
            
        Returns:
            APIResponse: Response from server
            
        TODO: Implement this method
        """
        pass
    
    def post(self, endpoint: str, **kwargs) -> APIResponse:
        """
        Send POST request.
        
        Args:
            endpoint (str): API endpoint
            **kwargs: Additional request parameters
            
        Returns:
            APIResponse: Response from server
            
        TODO: Implement this method
        """
        pass
    
    def put(self, endpoint: str, **kwargs) -> APIResponse:
        """
        Send PUT request.
        
        Args:
            endpoint (str): API endpoint
            **kwargs: Additional request parameters
            
        Returns:
            APIResponse: Response from server
            
        TODO: Implement this method
        """
        pass
    
    def delete(self, endpoint: str, **kwargs) -> APIResponse:
        """
        Send DELETE request.
        
        Args:
            endpoint (str): API endpoint
            **kwargs: Additional request parameters
            
        Returns:
            APIResponse: Response from server
            
        TODO: Implement this method
        """
        pass

class APITestRunner:
    """Runs API test cases with validation and reporting."""
    
    def __init__(self, client: HTTPClient, auth_handler: AuthenticationHandler = None):
        """
        Initialize API test runner.
        
        Args:
            client (HTTPClient): HTTP client to use
            auth_handler (AuthenticationHandler): Authentication handler
        """
        self.client = client
        self.auth_handler = auth_handler
        self.test_results: List[Dict[str, Any]] = []
        self.global_variables: Dict[str, Any] = {}
    
    def run_test_case(self, test_case: TestCase) -> Dict[str, Any]:
        """
        Run a single test case.
        
        Args:
            test_case (TestCase): Test case to run
            
        Returns:
            dict: Test result
            
        TODO: Implement this method
        """
        pass
    
    def run_test_suite(self, test_cases: List[TestCase]) -> List[Dict[str, Any]]:
        """
        Run a suite of test cases.
        
        Args:
            test_cases (list): List of test cases
            
        Returns:
            list: List of test results
            
        TODO: Implement this method
        """
        pass
    
    def validate_response(self, response: APIResponse, expected: Dict[str, Any]) -> List[str]:
        """
        Validate API response against expected values.
        
        Args:
            response (APIResponse): Actual response
            expected (dict): Expected response values
            
        Returns:
            list: List of validation errors
            
        TODO: Implement this method
        """
        pass
    
    def extract_variable(self, response: APIResponse, variable_name: str, 
                        json_path: str) -> Any:
        """
        Extract a variable from response for use in subsequent tests.
        
        Args:
            response (APIResponse): Response to extract from
            variable_name (str): Name to store variable as
            json_path (str): JSON path to extract value from
            
        Returns:
            Any: Extracted value
            
        TODO: Implement this method
        """
        pass
    
    def substitute_variables(self, template: str) -> str:
        """
        Substitute variables in template strings.
        
        Args:
            template (str): Template string with {{variable}} placeholders
            
        Returns:
            str: String with variables substituted
            
        TODO: Implement this method
        """
        pass

class DataDrivenTester:
    """Handles data-driven API testing."""
    
    def __init__(self, test_runner: APITestRunner):
        """
        Initialize data-driven tester.
        
        Args:
            test_runner (APITestRunner): Test runner to use
        """
        self.test_runner = test_runner
        self.data_sources: Dict[str, Any] = {}
    
    def load_test_data(self, source_name: str, data: Union[List[Dict], str]) -> None:
        """
        Load test data from various sources.
        
        Args:
            source_name (str): Name for the data source
            data (list or str): Test data or file path
            
        TODO: Implement this method
        """
        pass
    
    def generate_test_cases(self, template: TestCase, 
                          data_source: str) -> List[TestCase]:
        """
        Generate test cases from template and data source.
        
        Args:
            template (TestCase): Test case template
            data_source (str): Name of data source
            
        Returns:
            list: Generated test cases
            
        TODO: Implement this method
        """
        pass
    
    def run_data_driven_tests(self, template: TestCase, 
                            data_source: str) -> List[Dict[str, Any]]:
        """
        Run data-driven tests.
        
        Args:
            template (TestCase): Test case template
            data_source (str): Name of data source
            
        Returns:
            list: Test results
            
        TODO: Implement this method
        """
        pass

class PerformanceProfiler:
    """Profiles API performance and generates metrics."""
    
    def __init__(self):
        """Initialize performance profiler."""
        self.metrics: Dict[str, List[float]] = {}
        self.response_times: List[float] = []
    
    def start_profiling(self, test_name: str) -> None:
        """
        Start profiling a test.
        
        Args:
            test_name (str): Name of test being profiled
            
        TODO: Implement this method
        """
        pass
    
    def record_response_time(self, test_name: str, response_time: float) -> None:
        """
        Record response time for a test.
        
        Args:
            test_name (str): Test name
            response_time (float): Response time in seconds
            
        TODO: Implement this method
        """
        pass
    
    def generate_performance_report(self) -> Dict[str, Any]:
        """
        Generate performance report.
        
        Returns:
            dict: Performance metrics and statistics
            
        TODO: Implement this method
        """
        pass
    
    def detect_performance_regressions(self, baseline: Dict[str, float],
                                     threshold: float = 0.2) -> List[Dict[str, Any]]:
        """
        Detect performance regressions compared to baseline.
        
        Args:
            baseline (dict): Baseline performance metrics
            threshold (float): Regression threshold (20% by default)
            
        Returns:
            list: List of detected regressions
            
        TODO: Implement this method
        """
        pass

class MockAPIServer:
    """Simple mock API server for testing."""
    
    def __init__(self, port: int = 8080):
        """
        Initialize mock API server.
        
        Args:
            port (int): Port to run server on
        """
        self.port = port
        self.routes: Dict[str, Dict[str, Any]] = {}
        self.request_log: List[Dict[str, Any]] = []
        self.running = False
    
    def add_route(self, method: HTTPMethod, path: str, 
                 response_data: Dict[str, Any], status_code: int = 200) -> None:
        """
        Add a route to the mock server.
        
        Args:
            method (HTTPMethod): HTTP method
            path (str): URL path
            response_data (dict): Response data
            status_code (int): HTTP status code
            
        TODO: Implement this method
        """
        pass
    
    def start_server(self) -> None:
        """
        Start the mock server.
        
        TODO: Implement this method (simulate server or use actual HTTP server)
        """
        pass
    
    def stop_server(self) -> None:
        """
        Stop the mock server.
        
        TODO: Implement this method
        """
        pass
    
    def get_request_log(self) -> List[Dict[str, Any]]:
        """
        Get logged requests.
        
        Returns:
            list: List of logged requests
            
        TODO: Implement this method
        """
        pass

def create_sample_api_tests() -> List[TestCase]:
    """
    Create sample API test cases.
    
    Returns:
        list: List of sample test cases
        
    TODO: Implement this function
    """
    pass

def create_test_data_sets() -> Dict[str, List[Dict[str, Any]]]:
    """
    Create sample test data sets for data-driven testing.
    
    Returns:
        dict: Dictionary of test data sets
        
    TODO: Implement this function
    """
    pass

# Test cases and demonstrations
if __name__ == "__main__":
    print("=== API Test Automation Exercise ===\n")
    
    # Initialize components
    client = HTTPClient("https://jsonplaceholder.typicode.com")
    auth_handler = BearerTokenHandler("sample-token")
    test_runner = APITestRunner(client, auth_handler)
    data_tester = DataDrivenTester(test_runner)
    profiler = PerformanceProfiler()
    mock_server = MockAPIServer(port=8081)
    
    print("1. HTTP Client Tests:")
    
    # Test basic HTTP methods
    methods_to_test = [
        ("GET", "/posts/1"),
        ("POST", "/posts", {"title": "Test Post", "body": "Test Body", "userId": 1}),
        ("PUT", "/posts/1", {"id": 1, "title": "Updated Post", "body": "Updated Body", "userId": 1}),
        ("DELETE", "/posts/1")
    ]
    
    for method, endpoint, *data in methods_to_test:
        try:
            if method == "GET":
                response = client.get(endpoint)
            elif method == "POST":
                response = client.post(endpoint, json_data=data[0] if data else {})
            elif method == "PUT":
                response = client.put(endpoint, json_data=data[0] if data else {})
            elif method == "DELETE":
                response = client.delete(endpoint)
            
            print(f"{method} {endpoint}: Status {response.status_code}")
        except Exception as e:
            print(f"{method} {endpoint}: Error - {e}")
    
    print("\n2. Authentication Handler Tests:")
    
    # Test different authentication methods
    auth_handlers = [
        ("Basic Auth", BasicAuthHandler("user", "pass")),
        ("Bearer Token", BearerTokenHandler("test-token-123")),
        ("API Key", APIKeyHandler("api-key-456", "X-API-Key"))
    ]
    
    test_request = APIRequest(HTTPMethod.GET, "/test")
    
    for auth_name, handler in auth_handlers:
        try:
            authenticated_request = handler.apply_auth(test_request)
            print(f"{auth_name}: Headers added - {len(authenticated_request.headers)} items")
        except Exception as e:
            print(f"{auth_name}: Error - {e}")
    
    print("\n3. Test Case Creation:")
    
    sample_tests = create_sample_api_tests()
    print(f"Created {len(sample_tests)} sample test cases")
    
    for test_case in sample_tests[:3]:  # Show first 3
        print(f"  - {test_case.name}: {test_case.request.method.value} {test_case.request.endpoint}")
    
    print("\n4. Test Execution:")
    
    if sample_tests:
        # Run individual test
        first_test = sample_tests[0]
        result = test_runner.run_test_case(first_test)
        print(f"Individual test result: {result.get('status', 'Unknown')}")
        
        # Run test suite
        suite_results = test_runner.run_test_suite(sample_tests[:3])
        passed = sum(1 for r in suite_results if r.get('status') == 'passed')
        print(f"Test suite results: {passed}/{len(suite_results)} passed")
    
    print("\n5. Data-Driven Testing:")
    
    # Load test data
    test_data_sets = create_test_data_sets()
    
    for data_name, data_set in test_data_sets.items():
        data_tester.load_test_data(data_name, data_set)
        print(f"Loaded {data_name}: {len(data_set)} data records")
    
    # Generate and run data-driven tests
    if sample_tests and test_data_sets:
        template_test = sample_tests[0]
        data_source_name = list(test_data_sets.keys())[0]
        
        generated_tests = data_tester.generate_test_cases(template_test, data_source_name)
        print(f"Generated {len(generated_tests)} data-driven test cases")
        
        dd_results = data_tester.run_data_driven_tests(template_test, data_source_name)
        dd_passed = sum(1 for r in dd_results if r.get('status') == 'passed')
        print(f"Data-driven test results: {dd_passed}/{len(dd_results)} passed")
    
    print("\n6. Performance Profiling:")
    
    # Start profiling
    profiler.start_profiling("API Performance Test")
    
    # Simulate some API calls with timing
    test_names = ["GET /posts", "POST /posts", "PUT /posts/1", "DELETE /posts/1"]
    
    for test_name in test_names:
        # Simulate response times
        response_time = 0.1 + (hash(test_name) % 100) / 1000  # 0.1-0.2 seconds
        profiler.record_response_time(test_name, response_time)
        print(f"Recorded {test_name}: {response_time:.3f}s")
    
    # Generate performance report
    perf_report = profiler.generate_performance_report()
    print(f"Performance report: {perf_report}")
    
    print("\n7. Mock Server Tests:")
    
    # Setup mock server routes
    mock_routes = [
        (HTTPMethod.GET, "/api/users/1", {"id": 1, "name": "John Doe", "email": "john@example.com"}),
        (HTTPMethod.POST, "/api/users", {"message": "User created successfully"}, 201),
        (HTTPMethod.GET, "/api/products", {"products": [{"id": 1, "name": "Product 1"}]})
    ]
    
    for method, path, response_data, *status in mock_routes:
        status_code = status[0] if status else 200
        mock_server.add_route(method, path, response_data, status_code)
        print(f"Added mock route: {method.value} {path}")
    
    # Start mock server
    try:
        mock_server.start_server()
        print("Mock server started successfully")
        
        # Test against mock server
        mock_client = HTTPClient(f"http://localhost:{mock_server.port}")
        
        mock_response = mock_client.get("/api/users/1")
        print(f"Mock server response: Status {mock_response.status_code}")
        
        # Stop mock server
        mock_server.stop_server()
        print("Mock server stopped")
        
    except Exception as e:
        print(f"Mock server error: {e}")
    
    print("\n8. Variable Extraction and Substitution:")
    
    # Test variable handling
    test_runner.global_variables["user_id"] = "12345"
    test_runner.global_variables["api_version"] = "v1"
    
    template_string = "/api/{{api_version}}/users/{{user_id}}"
    substituted = test_runner.substitute_variables(template_string)
    print(f"Template: {template_string}")
    print(f"Substituted: {substituted}")
    
    # Test response variable extraction
    sample_response = APIResponse(
        status_code=200,
        headers={},
        content=b'',
        text='{"id": 456, "name": "Test User"}',
        json_data={"id": 456, "name": "Test User"}
    )
    
    extracted_id = test_runner.extract_variable(sample_response, "extracted_user_id", "$.id")
    print(f"Extracted user ID: {extracted_id}")
    
    print("\n9. Response Validation:")
    
    # Test response validation
    expected_response = {
        "status_code": 200,
        "json.id": 456,
        "json.name": "Test User",
        "headers.content-type": "application/json"
    }
    
    validation_errors = test_runner.validate_response(sample_response, expected_response)
    print(f"Validation errors: {len(validation_errors)}")
    
    for error in validation_errors:
        print(f"  - {error}")
    
    print("\n10. Request History and Debugging:")
    
    # Show request history
    request_history = client.request_history
    print(f"Total requests made: {len(request_history)}")
    
    for i, (request, response) in enumerate(request_history[-3:], 1):  # Last 3 requests
        print(f"  {i}. {request.method.value} {request.endpoint} -> {response.status_code}")
    
    # Show mock server request log
    mock_requests = mock_server.get_request_log()
    print(f"Mock server logged {len(mock_requests)} requests")
    
    print("\n11. Performance Regression Detection:")
    
    # Create baseline performance metrics
    baseline_metrics = {
        "GET /posts": 0.15,
        "POST /posts": 0.25,
        "PUT /posts/1": 0.20,
        "DELETE /posts/1": 0.12
    }
    
    # Detect regressions
    regressions = profiler.detect_performance_regressions(baseline_metrics, threshold=0.1)
    print(f"Performance regressions detected: {len(regressions)}")
    
    for regression in regressions:
        print(f"  - {regression.get('test_name', 'Unknown')}: {regression.get('regression_percent', 0):.1f}% slower")
    
    print("\n12. Advanced Test Scenarios:")
    
    # Chain requests (use response from one request in the next)
    print("Testing request chaining:")
    
    # First request: Get user
    get_user_response = client.get("/posts/1")
    if get_user_response.status_code == 200:
        print("✓ Got user data")
        
        # Extract user ID for next request
        if get_user_response.json_data:
            user_id = get_user_response.json_data.get("userId")
            test_runner.global_variables["current_user_id"] = user_id
            
            # Second request: Use extracted user ID
            user_posts_endpoint = f"/users/{user_id}/posts"
            user_posts_response = client.get(user_posts_endpoint)
            print(f"✓ Got user posts: Status {user_posts_response.status_code}")
    
    print(f"\nAPI Test Automation Exercise Complete!")
    print(f"Global variables: {len(test_runner.global_variables)}")
    print(f"Test results recorded: {len(test_runner.test_results)}")
    print(f"Performance metrics: {len(profiler.metrics)} endpoints tracked")
    
    # Final statistics
    total_requests = len(client.request_history)
    if total_requests > 0:
        avg_response_time = sum(resp.elapsed_time for _, resp in client.request_history) / total_requests
        print(f"Average response time: {avg_response_time:.3f}s")
    
    print("\n" + "="*50)
    print("API Test Automation Exercise Complete!")
    print("="*50)