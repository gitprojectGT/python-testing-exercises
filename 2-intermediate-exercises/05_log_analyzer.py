"""
Exercise 5: Log File Analyzer
Testing Focus: Log analysis, pattern matching, performance monitoring

Task: Create a comprehensive log file analyzer for application monitoring.
This exercise focuses on parsing logs, finding patterns, and generating insights.
"""

import re
import json
from datetime import datetime, timedelta
from collections import defaultdict, Counter
from typing import Dict, List, Any, Optional, Tuple
from dataclasses import dataclass
from enum import Enum

class LogLevel(Enum):
    """Log severity levels."""
    DEBUG = "DEBUG"
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    CRITICAL = "CRITICAL"

@dataclass
class LogEntry:
    """Represents a single log entry."""
    timestamp: datetime
    level: LogLevel
    message: str
    source: Optional[str] = None
    thread_id: Optional[str] = None
    user_id: Optional[str] = None
    request_id: Optional[str] = None
    raw_line: str = ""

class LogAnalyzer:
    """
    Comprehensive log file analyzer with pattern matching and statistics.
    """
    
    def __init__(self):
        """Initialize the log analyzer."""
        self.log_entries: List[LogEntry] = []
        self.patterns = {
            'timestamp': r'(\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})',
            'level': r'(DEBUG|INFO|WARNING|ERROR|CRITICAL)',
            'ip_address': r'\b(?:\d{1,3}\.){3}\d{1,3}\b',
            'url': r'https?://[^\s]+',
            'email': r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b',
            'error_code': r'\b[45]\d{2}\b',
            'user_id': r'user[_-]?id[:\s=]+(\w+)',
            'request_id': r'request[_-]?id[:\s=]+([a-zA-Z0-9-]+)'
        }
        self.custom_patterns = {}
    
    def parse_log_line(self, line: str, log_format: str = "standard") -> Optional[LogEntry]:
        """
        Parse a single log line into a LogEntry object.
        
        Args:
            line (str): Raw log line
            log_format (str): Log format type ("standard", "apache", "nginx", "custom")
            
        Returns:
            LogEntry or None: Parsed log entry or None if parsing fails
            
        TODO: Implement this method
        """
        pass
    
    def load_log_file(self, file_path: str, log_format: str = "standard") -> int:
        """
        Load and parse a log file.
        
        Args:
            file_path (str): Path to log file
            log_format (str): Log format type
            
        Returns:
            int: Number of successfully parsed entries
            
        TODO: Implement this method
        """
        pass
    
    def filter_by_level(self, level: LogLevel) -> List[LogEntry]:
        """
        Filter log entries by severity level.
        
        Args:
            level (LogLevel): Log level to filter by
            
        Returns:
            list: Filtered log entries
            
        TODO: Implement this method
        """
        pass
    
    def filter_by_time_range(self, start_time: datetime, 
                           end_time: datetime) -> List[LogEntry]:
        """
        Filter log entries by time range.
        
        Args:
            start_time (datetime): Start of time range
            end_time (datetime): End of time range
            
        Returns:
            list: Filtered log entries
            
        TODO: Implement this method
        """
        pass
    
    def search_by_pattern(self, pattern: str, use_regex: bool = True) -> List[LogEntry]:
        """
        Search log entries by pattern.
        
        Args:
            pattern (str): Search pattern
            use_regex (bool): Whether to use regex matching
            
        Returns:
            list: Matching log entries
            
        TODO: Implement this method
        """
        pass
    
    def find_error_patterns(self) -> Dict[str, List[LogEntry]]:
        """
        Find common error patterns in logs.
        
        Returns:
            dict: Dictionary mapping error patterns to matching entries
            
        TODO: Implement this method
        """
        pass
    
    def analyze_response_times(self, pattern: str = None) -> Dict[str, Any]:
        """
        Analyze response times from log entries.
        
        Args:
            pattern (str, optional): Pattern to extract response times
            
        Returns:
            dict: Response time statistics
            
        TODO: Implement this method
        """
        pass
    
    def detect_anomalies(self, threshold_multiplier: float = 2.0) -> List[Dict[str, Any]]:
        """
        Detect anomalies in log patterns.
        
        Args:
            threshold_multiplier (float): Multiplier for anomaly detection threshold
            
        Returns:
            list: List of detected anomalies
            
        TODO: Implement this method
        """
        pass
    
    def generate_statistics(self) -> Dict[str, Any]:
        """
        Generate comprehensive log statistics.
        
        Returns:
            dict: Log statistics including counts, levels, time ranges
            
        TODO: Implement this method
        """
        pass
    
    def find_frequent_errors(self, top_n: int = 10) -> List[Tuple[str, int]]:
        """
        Find most frequent error messages.
        
        Args:
            top_n (int): Number of top errors to return
            
        Returns:
            list: List of (error_message, count) tuples
            
        TODO: Implement this method
        """
        pass
    
    def analyze_user_activity(self) -> Dict[str, Any]:
        """
        Analyze user activity patterns from logs.
        
        Returns:
            dict: User activity analysis
            
        TODO: Implement this method
        """
        pass
    
    def detect_security_issues(self) -> List[Dict[str, Any]]:
        """
        Detect potential security issues in logs.
        
        Returns:
            list: List of potential security issues
            
        TODO: Implement this method
        """
        pass
    
    def generate_timeline(self, interval_minutes: int = 60) -> Dict[datetime, Dict[str, int]]:
        """
        Generate a timeline of log events.
        
        Args:
            interval_minutes (int): Time interval for grouping events
            
        Returns:
            dict: Timeline mapping timestamps to event counts
            
        TODO: Implement this method
        """
        pass
    
    def export_analysis_report(self, file_path: str, format_type: str = "json") -> bool:
        """
        Export analysis report to file.
        
        Args:
            file_path (str): Output file path
            format_type (str): Output format ("json", "csv", "html")
            
        Returns:
            bool: True if successful
            
        TODO: Implement this method
        """
        pass
    
    def add_custom_pattern(self, name: str, pattern: str) -> None:
        """
        Add a custom pattern for log analysis.
        
        Args:
            name (str): Pattern name
            pattern (str): Regex pattern
            
        TODO: Implement this method
        """
        pass
    
    def extract_custom_fields(self, entry: LogEntry) -> Dict[str, str]:
        """
        Extract custom fields from log entry using registered patterns.
        
        Args:
            entry (LogEntry): Log entry to analyze
            
        Returns:
            dict: Extracted custom fields
            
        TODO: Implement this method
        """
        pass

class PerformanceAnalyzer:
    """
    Specialized analyzer for performance monitoring logs.
    """
    
    def __init__(self, log_analyzer: LogAnalyzer):
        """
        Initialize performance analyzer.
        
        Args:
            log_analyzer (LogAnalyzer): Main log analyzer instance
        """
        self.log_analyzer = log_analyzer
        self.performance_metrics = {}
    
    def analyze_request_latency(self) -> Dict[str, Any]:
        """
        Analyze request latency patterns.
        
        Returns:
            dict: Latency analysis results
            
        TODO: Implement this method
        """
        pass
    
    def find_slow_queries(self, threshold_ms: int = 1000) -> List[Dict[str, Any]]:
        """
        Find slow database queries in logs.
        
        Args:
            threshold_ms (int): Threshold in milliseconds
            
        Returns:
            list: List of slow queries
            
        TODO: Implement this method
        """
        pass
    
    def analyze_memory_usage(self) -> Dict[str, Any]:
        """
        Analyze memory usage patterns from logs.
        
        Returns:
            dict: Memory usage analysis
            
        TODO: Implement this method
        """
        pass
    
    def detect_performance_degradation(self) -> List[Dict[str, Any]]:
        """
        Detect performance degradation over time.
        
        Returns:
            list: List of performance issues
            
        TODO: Implement this method
        """
        pass

def create_sample_log_data() -> List[str]:
    """
    Create sample log data for testing.
    
    Returns:
        list: List of sample log lines
        
    TODO: Implement this function
    """
    pass

def create_test_log_file(filename: str, num_entries: int = 1000) -> None:
    """
    Create a test log file with sample data.
    
    Args:
        filename (str): Output filename
        num_entries (int): Number of log entries to generate
        
    TODO: Implement this function
    """
    pass

# Test cases and demonstrations
if __name__ == "__main__":
    print("=== Log Analyzer Exercise ===\n")
    
    analyzer = LogAnalyzer()
    perf_analyzer = PerformanceAnalyzer(analyzer)
    
    # Create sample log data
    print("1. Creating Sample Log Data:")
    sample_logs = create_sample_log_data()
    print(f"Created {len(sample_logs)} sample log entries")
    
    # Create test log file
    test_log_file = "test_app.log"
    create_test_log_file(test_log_file, 500)
    print(f"Created test log file: {test_log_file}")
    
    # Test log parsing
    print("\n2. Log Parsing Tests:")
    
    sample_lines = [
        "2024-01-15 10:30:15 INFO [main] Application started successfully",
        "2024-01-15 10:30:16 DEBUG [worker-1] Processing request req-123",
        "2024-01-15 10:30:17 ERROR [worker-2] Database connection failed: timeout after 30s",
        "2024-01-15 10:30:18 WARNING [auth] Failed login attempt for user: admin from IP: 192.168.1.100"
    ]
    
    for line in sample_lines:
        entry = analyzer.parse_log_line(line)
        if entry:
            print(f"Parsed: {entry.timestamp} | {entry.level.value} | {entry.message[:50]}...")
        else:
            print(f"Failed to parse: {line[:50]}...")
    
    # Load complete log file
    print("\n3. Log File Loading Tests:")
    
    try:
        entries_loaded = analyzer.load_log_file(test_log_file)
        print(f"Loaded {entries_loaded} entries from {test_log_file}")
    except FileNotFoundError:
        print(f"Test log file {test_log_file} not found")
    
    # Test filtering
    print("\n4. Log Filtering Tests:")
    
    if analyzer.log_entries:
        # Filter by level
        error_entries = analyzer.filter_by_level(LogLevel.ERROR)
        warning_entries = analyzer.filter_by_level(LogLevel.WARNING)
        
        print(f"Error entries: {len(error_entries)}")
        print(f"Warning entries: {len(warning_entries)}")
        
        # Filter by time range
        if analyzer.log_entries:
            start_time = analyzer.log_entries[0].timestamp
            end_time = start_time + timedelta(hours=1)
            
            time_filtered = analyzer.filter_by_time_range(start_time, end_time)
            print(f"Entries in first hour: {len(time_filtered)}")
    
    # Test pattern searching
    print("\n5. Pattern Search Tests:")
    
    search_patterns = [
        ("failed", False),  # Simple text search
        (r"\d{3}\.\d{3}\.\d{3}\.\d{3}", True),  # IP addresses
        (r"user[_-]?\w+", True),  # User references
        ("timeout", False)  # Error keyword
    ]
    
    for pattern, use_regex in search_patterns:
        matches = analyzer.search_by_pattern(pattern, use_regex)
        search_type = "regex" if use_regex else "text"
        print(f"Pattern '{pattern}' ({search_type}): {len(matches)} matches")
    
    # Test error pattern analysis
    print("\n6. Error Pattern Analysis:")
    
    error_patterns = analyzer.find_error_patterns()
    print(f"Found {len(error_patterns)} distinct error patterns")
    
    for pattern, entries in list(error_patterns.items())[:3]:  # Show top 3
        print(f"  Pattern: {pattern[:50]}... ({len(entries)} occurrences)")
    
    # Test statistics generation
    print("\n7. Statistics Generation:")
    
    stats = analyzer.generate_statistics()
    print(f"Log statistics:")
    print(f"  Total entries: {stats.get('total_entries', 0)}")
    print(f"  Time span: {stats.get('time_span', 'Unknown')}")
    print(f"  Log levels: {stats.get('level_counts', {})}")
    
    # Test frequent errors
    print("\n8. Frequent Error Analysis:")
    
    frequent_errors = analyzer.find_frequent_errors(5)
    print(f"Top 5 frequent errors:")
    
    for i, (error, count) in enumerate(frequent_errors, 1):
        print(f"  {i}. {error[:60]}... ({count} times)")
    
    # Test user activity analysis
    print("\n9. User Activity Analysis:")
    
    user_activity = analyzer.analyze_user_activity()
    print(f"User activity analysis:")
    print(f"  Active users: {user_activity.get('active_users', 0)}")
    print(f"  Total user actions: {user_activity.get('total_actions', 0)}")
    
    # Test security issue detection
    print("\n10. Security Issue Detection:")
    
    security_issues = analyzer.detect_security_issues()
    print(f"Detected {len(security_issues)} potential security issues")
    
    for issue in security_issues[:3]:  # Show first 3
        print(f"  Issue: {issue.get('type', 'Unknown')} - {issue.get('description', '')[:50]}...")
    
    # Test timeline generation
    print("\n11. Timeline Analysis:")
    
    timeline = analyzer.generate_timeline(30)  # 30-minute intervals
    print(f"Generated timeline with {len(timeline)} time intervals")
    
    if timeline:
        # Show first few timeline entries
        for timestamp, counts in list(timeline.items())[:3]:
            print(f"  {timestamp}: {counts}")
    
    # Test performance analysis
    print("\n12. Performance Analysis:")
    
    # Response time analysis
    response_analysis = perf_analyzer.analyze_request_latency()
    print(f"Response time analysis: {response_analysis.get('avg_latency', 0):.2f}ms average")
    
    # Slow query detection
    slow_queries = perf_analyzer.find_slow_queries(500)  # 500ms threshold
    print(f"Slow queries found: {len(slow_queries)}")
    
    # Memory usage analysis
    memory_analysis = perf_analyzer.analyze_memory_usage()
    print(f"Memory analysis: {memory_analysis.get('peak_usage', 'Unknown')} peak usage")
    
    # Performance degradation detection
    perf_issues = perf_analyzer.detect_performance_degradation()
    print(f"Performance issues detected: {len(perf_issues)}")
    
    # Test anomaly detection
    print("\n13. Anomaly Detection:")
    
    anomalies = analyzer.detect_anomalies(2.5)  # 2.5x threshold
    print(f"Anomalies detected: {len(anomalies)}")
    
    for anomaly in anomalies[:3]:  # Show first 3
        print(f"  Anomaly: {anomaly.get('type', 'Unknown')} at {anomaly.get('timestamp', 'Unknown')}")
    
    # Test custom patterns
    print("\n14. Custom Pattern Tests:")
    
    # Add custom patterns
    custom_patterns = {
        "transaction_id": r"txn[_-]?([a-zA-Z0-9]+)",
        "response_time": r"response_time[:\s=]+(\d+)ms",
        "api_endpoint": r"(GET|POST|PUT|DELETE)\s+(/[\w/]+)"
    }
    
    for name, pattern in custom_patterns.items():
        analyzer.add_custom_pattern(name, pattern)
        print(f"Added custom pattern: {name}")
    
    # Test custom field extraction
    if analyzer.log_entries:
        sample_entry = analyzer.log_entries[0]
        custom_fields = analyzer.extract_custom_fields(sample_entry)
        print(f"Custom fields extracted: {custom_fields}")
    
    # Test report export
    print("\n15. Report Export Tests:")
    
    export_formats = ["json", "csv"]
    
    for format_type in export_formats:
        filename = f"log_analysis_report.{format_type}"
        success = analyzer.export_analysis_report(filename, format_type)
        print(f"Export to {format_type}: {'Success' if success else 'Failed'}")
    
    # Cleanup
    print("\n16. Cleanup:")
    
    cleanup_files = [test_log_file, "log_analysis_report.json", "log_analysis_report.csv"]
    
    for filename in cleanup_files:
        try:
            import os
            os.remove(filename)
            print(f"Removed {filename}")
        except FileNotFoundError:
            pass
    
    print(f"\nAnalysis complete. Processed {len(analyzer.log_entries)} log entries.")