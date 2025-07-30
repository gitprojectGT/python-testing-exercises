"""
Exercise 5: Mock Server Framework
Testing Focus: Service virtualization, contract testing

Task: Build an HTTP mock server for API testing and service virtualization.
This exercise focuses on creating realistic API mocks with state management and contract validation.
"""

import json
import re
import time
import threading
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Any, Optional, Union, Callable, Tuple
from urllib.parse import parse_qs, urlparse
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

class ResponseType(Enum):
    """Types of responses."""
    STATIC = "static"
    DYNAMIC = "dynamic"
    TEMPLATED = "templated"
    CALLBACK = "callback"
    PROXY = "proxy"

@dataclass
class MockRequest:
    """Represents an incoming mock request."""
    method: HTTPMethod
    path: str
    headers: Dict[str, str]
    query_params: Dict[str, List[str]]
    body: bytes
    json_body: Optional[Dict[str, Any]] = None
    remote_addr: str = "127.0.0.1"
    timestamp: datetime = field(default_factory=datetime.now)

@dataclass
class MockResponse:
    """Represents a mock response."""
    status_code: int = 200
    headers: Dict[str, str] = field(default_factory=dict)
    body: Union[str, bytes, Dict[str, Any]] = ""
    delay_ms: int = 0
    response_type: ResponseType = ResponseType.STATIC

@dataclass
class RoutePattern:
    """Represents a route pattern for matching requests."""
    method: HTTPMethod
    path_pattern: str
    path_regex: Optional[re.Pattern] = None
    headers_match: Dict[str, str] = field(default_factory=dict)
    query_match: Dict[str, str] = field(default_factory=dict)
    body_match: Optional[str] = None
    priority: int = 0

@dataclass
class MockEndpoint:
    """Represents a mock API endpoint."""
    id: str
    name: str
    route_pattern: RoutePattern
    responses: List[MockResponse]
    current_response_index: int = 0
    call_count: int = 0
    state_data: Dict[str, Any] = field(default_factory=dict)
    is_enabled: bool = True
    conditional_logic: Optional[Callable] = None

class RequestMatcher:
    """Matches incoming requests to mock endpoints."""
    
    def __init__(self):
        """Initialize request matcher."""
        self.endpoints: List[MockEndpoint] = []
    
    def add_endpoint(self, endpoint: MockEndpoint) -> None:
        """
        Add an endpoint to match against.
        
        Args:
            endpoint (MockEndpoint): Endpoint to add
            
        TODO: Implement this method
        """
        pass
    
    def find_matching_endpoint(self, request: MockRequest) -> Optional[MockEndpoint]:
        """
        Find the best matching endpoint for a request.
        
        Args:
            request (MockRequest): Incoming request
            
        Returns:
            MockEndpoint or None: Best matching endpoint
            
        TODO: Implement this method
        """
        pass
    
    def match_path(self, pattern: str, path: str) -> Tuple[bool, Dict[str, str]]:
        """
        Match a path pattern against actual path.
        
        Args:
            pattern (str): Path pattern with variables like /users/{id}
            path (str): Actual request path
            
        Returns:
            tuple: (is_match, path_variables)
            
        TODO: Implement this method
        """
        pass
    
    def match_headers(self, required_headers: Dict[str, str], 
                     actual_headers: Dict[str, str]) -> bool:
        """
        Match required headers against actual headers.
        
        Args:
            required_headers (dict): Required header patterns
            actual_headers (dict): Actual request headers
            
        Returns:
            bool: True if headers match
            
        TODO: Implement this method
        """
        pass

class ResponseGenerator:
    """Generates responses based on endpoint configuration."""
    
    def __init__(self):
        """Initialize response generator."""
        self.template_functions: Dict[str, Callable] = {}
        self.global_state: Dict[str, Any] = {}
    
    def generate_response(self, endpoint: MockEndpoint, 
                         request: MockRequest) -> MockResponse:
        """
        Generate a response for the given endpoint and request.
        
        Args:
            endpoint (MockEndpoint): Matching endpoint
            request (MockRequest): Incoming request
            
        Returns:
            MockResponse: Generated response
            
        TODO: Implement this method
        """
        pass
    
    def apply_template_variables(self, template: str, 
                                variables: Dict[str, Any]) -> str:
        """
        Apply template variables to response template.
        
        Args:
            template (str): Response template with {{variable}} placeholders
            variables (dict): Variables to substitute
            
        Returns:
            str: Response with variables substituted
            
        TODO: Implement this method
        """
        pass
    
    def register_template_function(self, name: str, func: Callable) -> None:
        """
        Register a template function for dynamic responses.
        
        Args:
            name (str): Function name
            func (Callable): Function implementation
            
        TODO: Implement this method
        """
        pass
    
    def execute_callback_response(self, callback: Callable, 
                                 request: MockRequest) -> MockResponse:
        """
        Execute a callback function to generate response.
        
        Args:
            callback (Callable): Callback function
            request (MockRequest): Request object
            
        Returns:
            MockResponse: Generated response
            
        TODO: Implement this method
        """
        pass

class StateManager:
    """Manages server state for stateful mocking."""
    
    def __init__(self):
        """Initialize state manager."""
        self.global_state: Dict[str, Any] = {}
        self.endpoint_states: Dict[str, Dict[str, Any]] = {}
        self.session_states: Dict[str, Dict[str, Any]] = {}
    
    def get_global_state(self, key: str, default: Any = None) -> Any:
        """
        Get global state value.
        
        Args:
            key (str): State key
            default: Default value if key not found
            
        Returns:
            Any: State value
            
        TODO: Implement this method
        """
        pass
    
    def set_global_state(self, key: str, value: Any) -> None:
        """
        Set global state value.
        
        Args:
            key (str): State key
            value: State value
            
        TODO: Implement this method
        """
        pass
    
    def get_endpoint_state(self, endpoint_id: str, key: str, 
                          default: Any = None) -> Any:
        """
        Get endpoint-specific state.
        
        Args:
            endpoint_id (str): Endpoint ID
            key (str): State key
            default: Default value
            
        Returns:
            Any: State value
            
        TODO: Implement this method
        """
        pass
    
    def set_endpoint_state(self, endpoint_id: str, key: str, value: Any) -> None:
        """
        Set endpoint-specific state.
        
        Args:
            endpoint_id (str): Endpoint ID
            key (str): State key
            value: State value
            
        TODO: Implement this method
        """
        pass
    
    def reset_state(self, scope: str = "all") -> None:
        """
        Reset state for given scope.
        
        Args:
            scope (str): Scope to reset ("all", "global", "endpoints", "sessions")
            
        TODO: Implement this method
        """
        pass

class RequestLogger:
    """Logs and tracks mock server requests."""
    
    def __init__(self, max_entries: int = 1000):
        """
        Initialize request logger.
        
        Args:
            max_entries (int): Maximum log entries to keep
        """
        self.max_entries = max_entries
        self.request_log: List[Dict[str, Any]] = []
        self.response_log: List[Dict[str, Any]] = []
        self.statistics: Dict[str, Any] = {}
    
    def log_request(self, request: MockRequest, endpoint: MockEndpoint = None) -> None:
        """
        Log an incoming request.
        
        Args:
            request (MockRequest): Request to log
            endpoint (MockEndpoint): Matched endpoint if any
            
        TODO: Implement this method
        """
        pass
    
    def log_response(self, request: MockRequest, response: MockResponse, 
                    processing_time_ms: float) -> None:
        """
        Log a response.
        
        Args:
            request (MockRequest): Original request
            response (MockResponse): Generated response
            processing_time_ms (float): Processing time in milliseconds
            
        TODO: Implement this method
        """
        pass
    
    def get_request_history(self, filter_criteria: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Get request history with optional filtering.
        
        Args:
            filter_criteria (dict): Filter criteria
            
        Returns:
            list: Filtered request history
            
        TODO: Implement this method
        """
        pass
    
    def generate_statistics(self) -> Dict[str, Any]:
        """
        Generate request/response statistics.
        
        Returns:
            dict: Statistics summary
            
        TODO: Implement this method
        """
        pass
    
    def export_logs(self, format_type: str = "json", 
                   file_path: str = None) -> str:
        """
        Export logs to file or string.
        
        Args:
            format_type (str): Export format ("json", "csv", "txt")
            file_path (str): File path to save to
            
        Returns:
            str: Exported logs as string
            
        TODO: Implement this method
        """
        pass

class ContractValidator:
    """Validates API contracts and schemas."""
    
    def __init__(self):
        """Initialize contract validator."""
        self.schemas: Dict[str, Dict[str, Any]] = {}
        self.validation_rules: List[Callable] = []
    
    def register_schema(self, endpoint_id: str, schema: Dict[str, Any]) -> None:
        """
        Register a schema for an endpoint.
        
        Args:
            endpoint_id (str): Endpoint ID
            schema (dict): JSON schema for validation
            
        TODO: Implement this method
        """
        pass
    
    def validate_request(self, endpoint_id: str, request: MockRequest) -> List[str]:
        """
        Validate request against registered schema.
        
        Args:
            endpoint_id (str): Endpoint ID
            request (MockRequest): Request to validate
            
        Returns:
            list: List of validation errors
            
        TODO: Implement this method
        """
        pass
    
    def validate_response(self, endpoint_id: str, response: MockResponse) -> List[str]:
        """
        Validate response against registered schema.
        
        Args:
            endpoint_id (str): Endpoint ID
            response (MockResponse): Response to validate
            
        Returns:
            list: List of validation errors
            
        TODO: Implement this method
        """
        pass
    
    def add_custom_validation_rule(self, rule: Callable) -> None:
        """
        Add a custom validation rule.
        
        Args:
            rule (Callable): Validation rule function
            
        TODO: Implement this method
        """
        pass

class MockServer:
    """Main mock server class."""
    
    def __init__(self, port: int = 8080, host: str = "localhost"):
        """
        Initialize mock server.
        
        Args:
            port (int): Server port
            host (str): Server host
        """
        self.port = port
        self.host = host
        self.is_running = False
        self.request_matcher = RequestMatcher()
        self.response_generator = ResponseGenerator()
        self.state_manager = StateManager()
        self.request_logger = RequestLogger()
        self.contract_validator = ContractValidator()
        self.server_thread: Optional[threading.Thread] = None
        self.middleware: List[Callable] = []
    
    def add_endpoint(self, endpoint: MockEndpoint) -> None:
        """
        Add a mock endpoint.
        
        Args:
            endpoint (MockEndpoint): Endpoint to add
            
        TODO: Implement this method
        """
        pass
    
    def add_middleware(self, middleware: Callable) -> None:
        """
        Add middleware for request/response processing.
        
        Args:
            middleware (Callable): Middleware function
            
        TODO: Implement this method
        """
        pass
    
    def start(self) -> None:
        """
        Start the mock server.
        
        TODO: Implement this method
        """
        pass
    
    def stop(self) -> None:
        """
        Stop the mock server.
        
        TODO: Implement this method
        """
        pass
    
    def handle_request(self, request: MockRequest) -> MockResponse:
        """
        Handle an incoming request.
        
        Args:
            request (MockRequest): Incoming request
            
        Returns:
            MockResponse: Generated response
            
        TODO: Implement this method
        """
        pass
    
    def apply_middleware(self, request: MockRequest) -> MockRequest:
        """
        Apply middleware to incoming request.
        
        Args:
            request (MockRequest): Original request
            
        Returns:
            MockRequest: Modified request
            
        TODO: Implement this method
        """
        pass
    
    def create_default_endpoints(self) -> None:
        """
        Create default endpoints for common scenarios.
        
        TODO: Implement this method
        """
        pass
    
    def load_endpoints_from_config(self, config_path: str) -> None:
        """
        Load endpoints from configuration file.
        
        Args:
            config_path (str): Path to configuration file
            
        TODO: Implement this method
        """
        pass
    
    def get_server_status(self) -> Dict[str, Any]:
        """
        Get server status information.
        
        Returns:
            dict: Server status
            
        TODO: Implement this method
        """
        pass

class ScenarioManager:
    """Manages test scenarios with multiple endpoints."""
    
    def __init__(self, mock_server: MockServer):
        """
        Initialize scenario manager.
        
        Args:
            mock_server (MockServer): Mock server instance
        """
        self.mock_server = mock_server
        self.scenarios: Dict[str, Dict[str, Any]] = {}
        self.active_scenario: Optional[str] = None
    
    def create_scenario(self, name: str, description: str = "") -> None:
        """
        Create a new test scenario.
        
        Args:
            name (str): Scenario name
            description (str): Scenario description
            
        TODO: Implement this method
        """
        pass
    
    def add_endpoint_to_scenario(self, scenario_name: str, 
                                endpoint: MockEndpoint) -> None:
        """
        Add an endpoint to a scenario.
        
        Args:
            scenario_name (str): Scenario name
            endpoint (MockEndpoint): Endpoint to add
            
        TODO: Implement this method
        """
        pass
    
    def activate_scenario(self, scenario_name: str) -> None:
        """
        Activate a test scenario.
        
        Args:
            scenario_name (str): Scenario name
            
        TODO: Implement this method
        """
        pass
    
    def deactivate_scenario(self) -> None:
        """
        Deactivate current scenario.
        
        TODO: Implement this method
        """
        pass
    
    def get_scenario_status(self, scenario_name: str) -> Dict[str, Any]:
        """
        Get status of a scenario.
        
        Args:
            scenario_name (str): Scenario name
            
        Returns:
            dict: Scenario status
            
        TODO: Implement this method
        """
        pass

def create_rest_api_endpoints() -> List[MockEndpoint]:
    """
    Create sample REST API endpoints.
    
    Returns:
        list: List of REST API endpoints
        
    TODO: Implement this function
    """
    pass

def create_authentication_endpoints() -> List[MockEndpoint]:
    """
    Create authentication-related endpoints.
    
    Returns:
        list: List of authentication endpoints
        
    TODO: Implement this function
    """
    pass

def create_file_upload_endpoints() -> List[MockEndpoint]:
    """
    Create file upload endpoints.
    
    Returns:
        list: List of file upload endpoints
        
    TODO: Implement this function
    """
    pass

# Test cases and demonstrations
if __name__ == "__main__":
    print("=== Mock Server Framework Exercise ===\n")
    
    # Initialize mock server
    mock_server = MockServer(port=8081, host="localhost")
    scenario_manager = ScenarioManager(mock_server)
    
    print("1. Mock Server Initialization:")
    print(f"Server initialized on {mock_server.host}:{mock_server.port}")
    print(f"Request matcher ready: {mock_server.request_matcher is not None}")
    print(f"Response generator ready: {mock_server.response_generator is not None}")
    print(f"State manager ready: {mock_server.state_manager is not None}")
    
    # Create sample endpoints
    print("\n2. Creating Mock Endpoints:")
    
    # Simple GET endpoint
    users_endpoint = MockEndpoint(
        id="get_users",
        name="Get Users",
        route_pattern=RoutePattern(HTTPMethod.GET, "/api/users"),
        responses=[
            MockResponse(
                status_code=200,
                headers={"Content-Type": "application/json"},
                body={"users": [{"id": 1, "name": "John Doe"}, {"id": 2, "name": "Jane Smith"}]}
            )
        ]
    )
    
    # Dynamic endpoint with path variables
    user_detail_endpoint = MockEndpoint(
        id="get_user_detail",
        name="Get User Detail",
        route_pattern=RoutePattern(HTTPMethod.GET, "/api/users/{id}"),
        responses=[
            MockResponse(
                status_code=200,
                headers={"Content-Type": "application/json"},
                body='{"id": {{id}}, "name": "User {{id}}", "email": "user{{id}}@example.com"}',
                response_type=ResponseType.TEMPLATED
            )
        ]
    )
    
    # POST endpoint with state management
    create_user_endpoint = MockEndpoint(
        id="create_user",
        name="Create User",
        route_pattern=RoutePattern(HTTPMethod.POST, "/api/users"),
        responses=[
            MockResponse(
                status_code=201,
                headers={"Content-Type": "application/json"},
                body='{"id": {{next_id}}, "message": "User created successfully"}',
                response_type=ResponseType.DYNAMIC
            )
        ]
    )
    
    endpoints = [users_endpoint, user_detail_endpoint, create_user_endpoint]
    
    for endpoint in endpoints:
        mock_server.add_endpoint(endpoint)
        print(f"  Added endpoint: {endpoint.name}")
    
    # Test request matching
    print("\n3. Request Matching Tests:")
    
    test_requests = [
        MockRequest(HTTPMethod.GET, "/api/users", {}, {}, b""),
        MockRequest(HTTPMethod.GET, "/api/users/123", {}, {}, b""),
        MockRequest(HTTPMethod.POST, "/api/users", {"Content-Type": "application/json"}, {}, b'{"name": "New User"}'),
        MockRequest(HTTPMethod.GET, "/api/nonexistent", {}, {}, b"")
    ]
    
    for request in test_requests:
        matching_endpoint = mock_server.request_matcher.find_matching_endpoint(request)
        if matching_endpoint:
            print(f"  {request.method.value} {request.path} -> {matching_endpoint.name}")
        else:
            print(f"  {request.method.value} {request.path} -> No match")
    
    # Test path matching with variables
    print("\n4. Path Variable Matching:")
    
    path_tests = [
        ("/api/users/{id}", "/api/users/123"),
        ("/api/orders/{order_id}/items/{item_id}", "/api/orders/456/items/789"),
        ("/api/files/{filename}.{extension}", "/api/files/document.pdf"),
        ("/static/{path:.*}", "/static/css/styles.css")
    ]
    
    for pattern, path in path_tests:
        is_match, variables = mock_server.request_matcher.match_path(pattern, path)
        print(f"  Pattern: {pattern}")
        print(f"  Path: {path}")
        print(f"  Match: {is_match}, Variables: {variables}")
        print()
    
    # Test response generation
    print("\n5. Response Generation Tests:")
    
    # Register template functions
    def next_id():
        current = mock_server.state_manager.get_global_state("next_user_id", 1)
        mock_server.state_manager.set_global_state("next_user_id", current + 1)
        return current
    
    def current_timestamp():
        return datetime.now().isoformat()
    
    mock_server.response_generator.register_template_function("next_id", next_id)
    mock_server.response_generator.register_template_function("timestamp", current_timestamp)
    
    for request in test_requests[:3]:  # Test first 3 requests
        matching_endpoint = mock_server.request_matcher.find_matching_endpoint(request)
        if matching_endpoint:
            response = mock_server.response_generator.generate_response(matching_endpoint, request)
            print(f"  {request.method.value} {request.path}")
            print(f"    Status: {response.status_code}")
            print(f"    Body: {str(response.body)[:100]}...")
            print()
    
    # Test state management
    print("\n6. State Management Tests:")
    
    # Set and get global state
    mock_server.state_manager.set_global_state("api_version", "v1.0")
    mock_server.state_manager.set_global_state("server_mode", "test")
    
    api_version = mock_server.state_manager.get_global_state("api_version")
    server_mode = mock_server.state_manager.get_global_state("server_mode")
    
    print(f"  API Version: {api_version}")
    print(f"  Server Mode: {server_mode}")
    
    # Set endpoint-specific state
    mock_server.state_manager.set_endpoint_state("get_users", "call_count", 0)
    mock_server.state_manager.set_endpoint_state("get_users", "last_accessed", datetime.now())
    
    call_count = mock_server.state_manager.get_endpoint_state("get_users", "call_count")
    last_accessed = mock_server.state_manager.get_endpoint_state("get_users", "last_accessed")
    
    print(f"  Users endpoint call count: {call_count}")
    print(f"  Users endpoint last accessed: {last_accessed}")
    
    # Test request logging
    print("\n7. Request Logging Tests:")
    
    for request in test_requests:
        matching_endpoint = mock_server.request_matcher.find_matching_endpoint(request)
        mock_server.request_logger.log_request(request, matching_endpoint)
        
        if matching_endpoint:
            response = mock_server.response_generator.generate_response(matching_endpoint, request)
            mock_server.request_logger.log_response(request, response, 15.5)  # Simulated processing time
    
    request_history = mock_server.request_logger.get_request_history()
    print(f"  Logged {len(request_history)} requests")
    
    stats = mock_server.request_logger.generate_statistics()
    print(f"  Request statistics: {stats}")
    
    # Test contract validation
    print("\n8. Contract Validation Tests:")
    
    # Register schemas
    user_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "integer"},
            "name": {"type": "string", "minLength": 1},
            "email": {"type": "string", "format": "email"}
        },
        "required": ["name"]
    }
    
    mock_server.contract_validator.register_schema("create_user", user_schema)
    
    # Validate sample requests
    valid_request = MockRequest(
        HTTPMethod.POST, "/api/users", 
        {"Content-Type": "application/json"}, {}, 
        b'{"name": "John Doe", "email": "john@example.com"}'
    )
    
    invalid_request = MockRequest(
        HTTPMethod.POST, "/api/users",
        {"Content-Type": "application/json"}, {},
        b'{"email": "invalid-email"}'  # Missing required name field
    )
    
    for request in [valid_request, invalid_request]:
        request.json_body = json.loads(request.body.decode()) if request.body else {}
        errors = mock_server.contract_validator.validate_request("create_user", request)
        print(f"  Request validation errors: {len(errors)}")
        for error in errors:
            print(f"    - {error}")
    
    # Test scenario management
    print("\n9. Scenario Management Tests:")
    
    # Create test scenarios
    scenarios = [
        ("happy_path", "Happy path user operations"),
        ("error_scenarios", "Error handling scenarios"),
        ("load_test", "High load scenarios")
    ]
    
    for scenario_name, description in scenarios:
        scenario_manager.create_scenario(scenario_name, description)
        print(f"  Created scenario: {scenario_name}")
    
    # Add endpoints to scenarios
    scenario_manager.add_endpoint_to_scenario("happy_path", users_endpoint)
    scenario_manager.add_endpoint_to_scenario("happy_path", user_detail_endpoint)
    
    # Activate scenario
    scenario_manager.activate_scenario("happy_path")
    print(f"  Activated scenario: happy_path")
    
    scenario_status = scenario_manager.get_scenario_status("happy_path")
    print(f"  Scenario status: {scenario_status}")
    
    # Test middleware
    print("\n10. Middleware Tests:")
    
    def logging_middleware(request):
        print(f"    Middleware: Processing {request.method.value} {request.path}")
        return request
    
    def auth_middleware(request):
        if "Authorization" in request.headers:
            print(f"    Middleware: Authenticated request")
        else:
            print(f"    Middleware: Unauthenticated request")
        return request
    
    mock_server.add_middleware(logging_middleware)
    mock_server.add_middleware(auth_middleware)
    
    # Test middleware processing
    auth_request = MockRequest(
        HTTPMethod.GET, "/api/users",
        {"Authorization": "Bearer token123"}, {}, b""
    )
    
    processed_request = mock_server.apply_middleware(auth_request)
    print(f"  Middleware processing completed")
    
    # Test different endpoint types
    print("\n11. Advanced Endpoint Types:")
    
    # Create different types of endpoints
    rest_endpoints = create_rest_api_endpoints()
    auth_endpoints = create_authentication_endpoints()
    upload_endpoints = create_file_upload_endpoints()
    
    all_advanced_endpoints = rest_endpoints + auth_endpoints + upload_endpoints
    
    for endpoint in all_advanced_endpoints:
        mock_server.add_endpoint(endpoint)
    
    print(f"  Added {len(all_advanced_endpoints)} advanced endpoints")
    print(f"    REST API endpoints: {len(rest_endpoints)}")
    print(f"    Authentication endpoints: {len(auth_endpoints)}")
    print(f"    File upload endpoints: {len(upload_endpoints)}")
    
    # Test server operations
    print("\n12. Server Operations:")
    
    # Create default endpoints
    mock_server.create_default_endpoints()
    print("  Created default endpoints")
    
    # Get server status
    server_status = mock_server.get_server_status()
    print(f"  Server status: {server_status}")
    
    # Test log export
    print("\n13. Log Export Tests:")
    
    export_formats = ["json", "csv", "txt"]
    
    for format_type in export_formats:
        try:
            exported_logs = mock_server.request_logger.export_logs(format_type)
            print(f"  {format_type.upper()} export: {len(exported_logs)} characters")
        except Exception as e:
            print(f"  {format_type.upper()} export: Error - {e}")
    
    # Test server start/stop simulation
    print("\n14. Server Lifecycle Tests:")
    
    print("  Starting mock server...")
    mock_server.start()
    print(f"  Server running: {mock_server.is_running}")
    
    # Simulate some requests
    time.sleep(0.1)  # Brief pause
    
    print("  Stopping mock server...")
    mock_server.stop()
    print(f"  Server running: {mock_server.is_running}")
    
    # Test configuration loading
    print("\n15. Configuration Management:")
    
    # Create sample configuration
    sample_config = {
        "endpoints": [
            {
                "id": "config_endpoint",
                "name": "Config Loaded Endpoint",
                "method": "GET",
                "path": "/api/config",
                "response": {
                    "status_code": 200,
                    "headers": {"Content-Type": "application/json"},
                    "body": {"message": "Loaded from config"}
                }
            }
        ],
        "global_settings": {
            "default_delay": 100,
            "enable_logging": True
        }
    }
    
    # Save and load config (simulated)
    config_file = "mock_server_config.json"
    try:
        with open(config_file, 'w') as f:
            json.dump(sample_config, f, indent=2)
        
        mock_server.load_endpoints_from_config(config_file)
        print(f"  Loaded configuration from {config_file}")
        
        # Cleanup
        import os
        os.remove(config_file)
        
    except Exception as e:
        print(f"  Configuration loading error: {e}")
    
    print(f"\nMock Server Framework Exercise Complete!")
    print(f"Total endpoints registered: {len(mock_server.request_matcher.endpoints)}")
    print(f"Total requests logged: {len(mock_server.request_logger.request_log)}")
    print(f"Active scenarios: {len(scenario_manager.scenarios)}")
    print(f"Global state variables: {len(mock_server.state_manager.global_state)}")
    
    # Final statistics
    final_stats = mock_server.request_logger.generate_statistics()
    print(f"Final request statistics: {final_stats}")
    
    print("\n" + "="*50)
    print("Mock Server Framework Exercise Complete!")
    print("="*50)