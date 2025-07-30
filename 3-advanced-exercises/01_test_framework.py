"""
Exercise 1: Test Framework Builder
Testing Focus: Framework design, test discovery, result reporting

Task: Build a custom testing framework from scratch with advanced features.
This exercise demonstrates framework architecture, plugin systems, and test execution.
"""

import inspect
import traceback
import time
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Any, Optional, Callable, Union
import uuid

class TestStatus(Enum):
    """Test execution status."""
    PENDING = "pending"
    RUNNING = "running"
    PASSED = "passed"
    FAILED = "failed"
    SKIPPED = "skipped"
    ERROR = "error"

class TestPriority(Enum):
    """Test priority levels."""
    LOW = 1
    NORMAL = 2
    HIGH = 3
    CRITICAL = 4

@dataclass
class TestResult:
    """Represents the result of a single test execution."""
    test_id: str
    test_name: str
    status: TestStatus
    start_time: datetime
    end_time: Optional[datetime] = None
    duration: float = 0.0
    error_message: Optional[str] = None
    traceback: Optional[str] = None
    output: List[str] = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)

@dataclass
class TestCase:
    """Represents a test case with metadata."""
    id: str
    name: str
    function: Callable
    description: Optional[str] = None
    tags: List[str] = field(default_factory=list)
    priority: TestPriority = TestPriority.NORMAL
    timeout: Optional[int] = None
    skip_reason: Optional[str] = None
    setup_func: Optional[Callable] = None
    teardown_func: Optional[Callable] = None
    data_provider: Optional[Callable] = None

class TestReporter(ABC):
    """Abstract base class for test reporters."""
    
    @abstractmethod
    def on_test_start(self, test_case: TestCase) -> None:
        """Called when a test starts."""
        pass
    
    @abstractmethod
    def on_test_end(self, result: TestResult) -> None:
        """Called when a test ends."""
        pass
    
    @abstractmethod
    def on_suite_start(self, suite_name: str, test_count: int) -> None:
        """Called when a test suite starts."""
        pass
    
    @abstractmethod
    def on_suite_end(self, results: List[TestResult]) -> None:
        """Called when a test suite ends."""
        pass

class ConsoleReporter(TestReporter):
    """Console-based test reporter."""
    
    def __init__(self, verbose: bool = False):
        """
        Initialize console reporter.
        
        Args:
            verbose (bool): Whether to show verbose output
        """
        self.verbose = verbose
    
    def on_test_start(self, test_case: TestCase) -> None:
        """
        Handle test start event.
        
        Args:
            test_case (TestCase): Test case being started
            
        TODO: Implement this method
        """
        pass
    
    def on_test_end(self, result: TestResult) -> None:
        """
        Handle test end event.
        
        Args:
            result (TestResult): Test result
            
        TODO: Implement this method
        """
        pass
    
    def on_suite_start(self, suite_name: str, test_count: int) -> None:
        """
        Handle suite start event.
        
        Args:
            suite_name (str): Name of the test suite
            test_count (int): Number of tests in suite
            
        TODO: Implement this method
        """
        pass
    
    def on_suite_end(self, results: List[TestResult]) -> None:
        """
        Handle suite end event.
        
        Args:
            results (list): List of test results
            
        TODO: Implement this method
        """
        pass

class JSONReporter(TestReporter):
    """JSON-based test reporter."""
    
    def __init__(self, output_file: str):
        """
        Initialize JSON reporter.
        
        Args:
            output_file (str): Output file path
        """
        self.output_file = output_file
        self.results = []
    
    def on_test_start(self, test_case: TestCase) -> None:
        """Handle test start event."""
        pass
    
    def on_test_end(self, result: TestResult) -> None:
        """
        Handle test end event.
        
        Args:
            result (TestResult): Test result
            
        TODO: Implement this method
        """
        pass
    
    def on_suite_start(self, suite_name: str, test_count: int) -> None:
        """Handle suite start event."""
        pass
    
    def on_suite_end(self, results: List[TestResult]) -> None:
        """
        Handle suite end event and write JSON output.
        
        Args:
            results (list): List of test results
            
        TODO: Implement this method
        """
        pass

class TestFilter:
    """Filter tests based on various criteria."""
    
    def __init__(self):
        """Initialize test filter."""
        self.included_tags: List[str] = []
        self.excluded_tags: List[str] = []
        self.name_pattern: Optional[str] = None
        self.min_priority: Optional[TestPriority] = None
    
    def should_run(self, test_case: TestCase) -> bool:
        """
        Determine if a test should run based on filter criteria.
        
        Args:
            test_case (TestCase): Test case to evaluate
            
        Returns:
            bool: True if test should run
            
        TODO: Implement this method
        """
        pass

class TestExecutor:
    """Executes individual tests with timeout and error handling."""
    
    def __init__(self, default_timeout: int = 30):
        """
        Initialize test executor.
        
        Args:
            default_timeout (int): Default timeout in seconds
        """
        self.default_timeout = default_timeout
        self.current_test: Optional[TestCase] = None
    
    def execute_test(self, test_case: TestCase) -> TestResult:
        """
        Execute a single test case.
        
        Args:
            test_case (TestCase): Test case to execute
            
        Returns:
            TestResult: Result of test execution
            
        TODO: Implement this method
        """
        pass
    
    def _run_with_timeout(self, func: Callable, timeout: int) -> Any:
        """
        Run a function with timeout.
        
        Args:
            func (Callable): Function to run
            timeout (int): Timeout in seconds
            
        Returns:
            Any: Function result
            
        Raises:
            TimeoutError: If function times out
            
        TODO: Implement this method
        """
        pass

class TestFramework:
    """Main test framework class."""
    
    def __init__(self, name: str = "CustomTestFramework"):
        """
        Initialize test framework.
        
        Args:
            name (str): Framework name
        """
        self.name = name
        self.test_cases: Dict[str, TestCase] = {}
        self.reporters: List[TestReporter] = []
        self.plugins: List['TestPlugin'] = []
        self.executor = TestExecutor()
        self.filter = TestFilter()
        self.config: Dict[str, Any] = {}
    
    def register_test(self, func: Callable, **kwargs) -> TestCase:
        """
        Register a test function.
        
        Args:
            func (Callable): Test function
            **kwargs: Test metadata
            
        Returns:
            TestCase: Created test case
            
        TODO: Implement this method
        """
        pass
    
    def discover_tests(self, module_or_path: Union[str, Any]) -> List[TestCase]:
        """
        Discover tests in a module or path.
        
        Args:
            module_or_path: Module object or path string
            
        Returns:
            list: Discovered test cases
            
        TODO: Implement this method
        """
        pass
    
    def add_reporter(self, reporter: TestReporter) -> None:
        """
        Add a test reporter.
        
        Args:
            reporter (TestReporter): Reporter to add
            
        TODO: Implement this method
        """
        pass
    
    def add_plugin(self, plugin: 'TestPlugin') -> None:
        """
        Add a test plugin.
        
        Args:
            plugin (TestPlugin): Plugin to add
            
        TODO: Implement this method
        """
        pass
    
    def run_tests(self, test_filter: Optional[TestFilter] = None) -> List[TestResult]:
        """
        Run all registered tests.
        
        Args:
            test_filter (TestFilter, optional): Filter to apply
            
        Returns:
            list: List of test results
            
        TODO: Implement this method
        """
        pass
    
    def run_test_by_id(self, test_id: str) -> TestResult:
        """
        Run a specific test by ID.
        
        Args:
            test_id (str): Test ID
            
        Returns:
            TestResult: Test result
            
        TODO: Implement this method
        """
        pass
    
    def get_test_statistics(self, results: List[TestResult]) -> Dict[str, Any]:
        """
        Calculate test statistics.
        
        Args:
            results (list): List of test results
            
        Returns:
            dict: Test statistics
            
        TODO: Implement this method
        """
        pass

class TestPlugin(ABC):
    """Abstract base class for test plugins."""
    
    @abstractmethod
    def initialize(self, framework: TestFramework) -> None:
        """Initialize the plugin."""
        pass
    
    @abstractmethod
    def before_test(self, test_case: TestCase) -> None:
        """Called before each test."""
        pass
    
    @abstractmethod
    def after_test(self, result: TestResult) -> None:
        """Called after each test."""
        pass

class RetryPlugin(TestPlugin):
    """Plugin to retry failed tests."""
    
    def __init__(self, max_retries: int = 3):
        """
        Initialize retry plugin.
        
        Args:
            max_retries (int): Maximum number of retries
        """
        self.max_retries = max_retries
        self.retry_counts: Dict[str, int] = {}
    
    def initialize(self, framework: TestFramework) -> None:
        """
        Initialize plugin with framework.
        
        Args:
            framework (TestFramework): Test framework instance
            
        TODO: Implement this method
        """
        pass
    
    def before_test(self, test_case: TestCase) -> None:
        """
        Handle before test event.
        
        Args:
            test_case (TestCase): Test case about to run
            
        TODO: Implement this method
        """
        pass
    
    def after_test(self, result: TestResult) -> None:
        """
        Handle after test event and implement retry logic.
        
        Args:
            result (TestResult): Test result
            
        TODO: Implement this method
        """
        pass

class TimingPlugin(TestPlugin):
    """Plugin to collect timing information."""
    
    def __init__(self):
        """Initialize timing plugin."""
        self.timings: Dict[str, float] = {}
        self.slow_tests: List[str] = []
        self.slow_threshold = 5.0  # seconds
    
    def initialize(self, framework: TestFramework) -> None:
        """Initialize plugin."""
        pass
    
    def before_test(self, test_case: TestCase) -> None:
        """Handle before test event."""
        pass
    
    def after_test(self, result: TestResult) -> None:
        """
        Handle after test event and collect timing data.
        
        Args:
            result (TestResult): Test result
            
        TODO: Implement this method
        """
        pass
    
    def get_timing_report(self) -> Dict[str, Any]:
        """
        Generate timing report.
        
        Returns:
            dict: Timing report data
            
        TODO: Implement this method
        """
        pass

# Decorators for test definition
def test(name: str = None, tags: List[str] = None, priority: TestPriority = TestPriority.NORMAL,
         timeout: int = None, skip: str = None):
    """
    Decorator to mark a function as a test.
    
    Args:
        name (str, optional): Test name
        tags (list, optional): Test tags
        priority (TestPriority): Test priority
        timeout (int, optional): Test timeout
        skip (str, optional): Skip reason
        
    Returns:
        Callable: Decorated function
        
    TODO: Implement this decorator
    """
    pass

def setup(func: Callable):
    """
    Decorator to mark a function as setup.
    
    Args:
        func (Callable): Setup function
        
    Returns:
        Callable: Decorated function
        
    TODO: Implement this decorator
    """
    pass

def teardown(func: Callable):
    """
    Decorator to mark a function as teardown.
    
    Args:
        func (Callable): Teardown function
        
    Returns:
        Callable: Decorated function
        
    TODO: Implement this decorator
    """
    pass

def data_provider(*data_sets):
    """
    Decorator to provide test data.
    
    Args:
        *data_sets: Data sets for parameterized testing
        
    Returns:
        Callable: Decorated function
        
    TODO: Implement this decorator
    """
    pass

# Assertion functions
class AssertionError(Exception):
    """Custom assertion error."""
    pass

def assert_equals(actual, expected, message: str = None):
    """
    Assert that two values are equal.
    
    Args:
        actual: Actual value
        expected: Expected value
        message (str, optional): Custom error message
        
    Raises:
        AssertionError: If values are not equal
        
    TODO: Implement this function
    """
    pass

def assert_true(condition: bool, message: str = None):
    """
    Assert that a condition is true.
    
    Args:
        condition (bool): Condition to check
        message (str, optional): Custom error message
        
    Raises:
        AssertionError: If condition is false
        
    TODO: Implement this function
    """
    pass

def assert_raises(exception_type: type, callable_obj: Callable, *args, **kwargs):
    """
    Assert that a callable raises a specific exception.
    
    Args:
        exception_type (type): Expected exception type
        callable_obj (Callable): Function to call
        *args: Function arguments
        **kwargs: Function keyword arguments
        
    Raises:
        AssertionError: If expected exception is not raised
        
    TODO: Implement this function
    """
    pass

# Example test suite using the framework
class ExampleTestSuite:
    """Example test suite to demonstrate the framework."""
    
    def setup_method(self):
        """Setup method called before each test."""
        self.test_data = {"value": 42}
    
    def teardown_method(self):
        """Teardown method called after each test."""
        self.test_data = None
    
    @test(name="Basic Math Test", tags=["math", "basic"], priority=TestPriority.HIGH)
    def test_basic_math(self):
        """Test basic mathematical operations."""
        result = 2 + 2
        assert_equals(result, 4, "Basic addition should work")
        
        result = 10 / 2
        assert_equals(result, 5.0, "Basic division should work")
    
    @test(name="String Operations", tags=["string"], timeout=5)
    def test_string_operations(self):
        """Test string operations."""
        text = "Hello, World!"
        assert_true(text.startswith("Hello"), "String should start with 'Hello'")
        assert_equals(text.upper(), "HELLO, WORLD!", "String upper() should work")
    
    @test(name="Exception Test", tags=["exceptions"])
    def test_exception_handling(self):
        """Test exception handling."""
        assert_raises(ZeroDivisionError, lambda: 1 / 0)
    
    @test(skip="This test is temporarily disabled")
    def test_skipped_example(self):
        """This test will be skipped."""
        pass
    
    @test(name="Slow Test", tags=["slow"], timeout=10)
    def test_slow_operation(self):
        """Test that takes some time."""
        time.sleep(2)  # Simulate slow operation
        assert_true(True, "Slow test completed")
    
    @data_provider(
        (1, 2, 3),
        (5, 5, 10),
        (10, -3, 7)
    )
    @test(name="Parameterized Addition Test", tags=["math", "parameterized"])
    def test_parameterized_addition(self, a, b, expected):
        """Test addition with multiple data sets."""
        result = a + b
        assert_equals(result, expected, f"Addition of {a} + {b} should equal {expected}")

# Test cases and demonstrations
if __name__ == "__main__":
    print("=== Test Framework Builder Exercise ===\n")
    
    # Initialize framework
    framework = TestFramework("CustomTestFramework")
    
    # Add reporters
    console_reporter = ConsoleReporter(verbose=True)
    json_reporter = JSONReporter("test_results.json")
    
    framework.add_reporter(console_reporter)
    framework.add_reporter(json_reporter)
    
    # Add plugins
    retry_plugin = RetryPlugin(max_retries=2)
    timing_plugin = TimingPlugin()
    
    framework.add_plugin(retry_plugin)
    framework.add_plugin(timing_plugin)
    
    print("1. Framework Initialization:")
    print(f"Framework: {framework.name}")
    print(f"Reporters: {len(framework.reporters)}")
    print(f"Plugins: {len(framework.plugins)}")
    
    # Discover tests in the example suite
    print("\n2. Test Discovery:")
    discovered_tests = framework.discover_tests(ExampleTestSuite)
    print(f"Discovered {len(discovered_tests)} tests")
    
    for test_case in discovered_tests:
        print(f"  - {test_case.name} (tags: {test_case.tags}, priority: {test_case.priority.name})")
    
    # Test filtering
    print("\n3. Test Filtering:")
    
    # Filter by tags
    framework.filter.included_tags = ["math"]
    math_tests = [tc for tc in discovered_tests if framework.filter.should_run(tc)]
    print(f"Math tests: {len(math_tests)}")
    
    # Filter by priority
    framework.filter = TestFilter()  # Reset filter
    framework.filter.min_priority = TestPriority.HIGH
    high_priority_tests = [tc for tc in discovered_tests if framework.filter.should_run(tc)]
    print(f"High priority tests: {len(high_priority_tests)}")
    
    # Reset filter for full run
    framework.filter = TestFilter()
    
    # Run tests
    print("\n4. Test Execution:")
    results = framework.run_tests()
    
    # Show statistics
    print("\n5. Test Statistics:")
    stats = framework.get_test_statistics(results)
    print(f"Total tests: {stats.get('total', 0)}")
    print(f"Passed: {stats.get('passed', 0)}")
    print(f"Failed: {stats.get('failed', 0)}")
    print(f"Skipped: {stats.get('skipped', 0)}")
    print(f"Error: {stats.get('error', 0)}")
    print(f"Total duration: {stats.get('total_duration', 0):.2f}s")
    
    # Show timing report
    print("\n6. Timing Report:")
    timing_report = timing_plugin.get_timing_report()
    print(f"Average test time: {timing_report.get('average_time', 0):.2f}s")
    print(f"Slowest test: {timing_report.get('slowest_test', 'N/A')}")
    print(f"Slow tests (>{timing_plugin.slow_threshold}s): {len(timing_report.get('slow_tests', []))}")
    
    # Test individual test execution
    print("\n7. Individual Test Execution:")
    if discovered_tests:
        individual_result = framework.run_test_by_id(discovered_tests[0].id)
        print(f"Individual test result: {individual_result.status.value}")
    
    # Test custom assertions
    print("\n8. Custom Assertion Tests:")
    
    try:
        assert_equals(5, 5)
        print("✓ assert_equals passed")
    except AssertionError as e:
        print(f"✗ assert_equals failed: {e}")
    
    try:
        assert_equals(5, 6)
        print("✗ assert_equals should have failed")
    except AssertionError as e:
        print(f"✓ assert_equals correctly failed: {e}")
    
    try:
        assert_true(True)
        print("✓ assert_true passed")
    except AssertionError as e:
        print(f"✗ assert_true failed: {e}")
    
    try:
        assert_raises(ValueError, lambda: int("not_a_number"))
        print("✓ assert_raises passed")
    except AssertionError as e:
        print(f"✗ assert_raises failed: {e}")
    
    print("\n9. Plugin Functionality:")
    print(f"Retry counts: {retry_plugin.retry_counts}")
    print(f"Test timings collected: {len(timing_plugin.timings)}")
    
    print("\n10. Reporter Output:")
    print("Console reporter output was shown above")
    print(f"JSON report written to: {json_reporter.output_file}")
    
    # Demonstrate framework extensibility
    print("\n11. Framework Extensibility:")
    
    # Register a dynamic test
    def dynamic_test():
        """Dynamically created test."""
        assert_equals(len("test"), 4)
    
    dynamic_test_case = framework.register_test(
        dynamic_test,
        name="Dynamic Test",
        tags=["dynamic"],
        priority=TestPriority.LOW
    )
    
    print(f"Registered dynamic test: {dynamic_test_case.name}")
    
    # Run just the dynamic test
    dynamic_result = framework.run_test_by_id(dynamic_test_case.id)
    print(f"Dynamic test result: {dynamic_result.status.value}")
    
    print(f"\nFramework demonstration complete!")
    print(f"Total registered tests: {len(framework.test_cases)}")
    print(f"Framework configuration: {framework.config}")
    
    # Show final summary
    failed_tests = [r for r in results if r.status == TestStatus.FAILED]
    if failed_tests:
        print(f"\nFailed Tests Summary:")
        for result in failed_tests:
            print(f"  - {result.test_name}: {result.error_message}")
    
    print("\\n" + "="*50)
    print("Test Framework Exercise Complete!")
    print("="*50)