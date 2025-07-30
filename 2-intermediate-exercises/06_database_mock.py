"""
Exercise 6: Database Mock
Testing Focus: Mock objects, database testing, CRUD operations

Task: Create a comprehensive database mock system for testing.
This exercise focuses on simulating database operations without requiring a real database.
"""

import json
import uuid
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional, Union, Callable
from dataclasses import dataclass, asdict
from enum import Enum
import copy

class QueryType(Enum):
    """Types of database queries."""
    SELECT = "SELECT"
    INSERT = "INSERT"
    UPDATE = "UPDATE"
    DELETE = "DELETE"
    CREATE_TABLE = "CREATE_TABLE"
    DROP_TABLE = "DROP_TABLE"

@dataclass
class QueryResult:
    """Result of a database query."""
    success: bool
    rows_affected: int
    data: List[Dict[str, Any]]
    error_message: Optional[str] = None
    execution_time_ms: float = 0.0

class DatabaseMock:
    """
    A comprehensive database mock for testing database operations.
    """
    
    def __init__(self, auto_commit: bool = True):
        """
        Initialize the database mock.
        
        Args:
            auto_commit (bool): Whether to auto-commit transactions
        """
        self.tables: Dict[str, List[Dict[str, Any]]] = {}
        self.table_schemas: Dict[str, Dict[str, Any]] = {}
        self.auto_commit = auto_commit
        self.transaction_active = False
        self.transaction_log: List[Dict[str, Any]] = []
        self.query_log: List[Dict[str, Any]] = []
        self.connection_count = 0
        self.latency_simulation = 0  # milliseconds
        self.failure_rate = 0.0  # 0.0 to 1.0
        self.max_connections = 100
    
    def create_table(self, table_name: str, schema: Dict[str, Any]) -> QueryResult:
        """
        Create a new table with specified schema.
        
        Args:
            table_name (str): Name of the table
            schema (dict): Table schema definition
                Example: {
                    "id": {"type": "int", "primary_key": True, "auto_increment": True},
                    "name": {"type": "str", "nullable": False, "max_length": 100},
                    "email": {"type": "str", "unique": True}
                }
        
        Returns:
            QueryResult: Result of the operation
            
        TODO: Implement this method
        """
        pass
    
    def drop_table(self, table_name: str) -> QueryResult:
        """
        Drop a table.
        
        Args:
            table_name (str): Name of the table to drop
            
        Returns:
            QueryResult: Result of the operation
            
        TODO: Implement this method
        """
        pass
    
    def insert(self, table_name: str, data: Dict[str, Any]) -> QueryResult:
        """
        Insert a record into a table.
        
        Args:
            table_name (str): Name of the table
            data (dict): Data to insert
            
        Returns:
            QueryResult: Result of the operation
            
        TODO: Implement this method
        """
        pass
    
    def insert_many(self, table_name: str, data_list: List[Dict[str, Any]]) -> QueryResult:
        """
        Insert multiple records into a table.
        
        Args:
            table_name (str): Name of the table
            data_list (list): List of data dictionaries to insert
            
        Returns:
            QueryResult: Result of the operation
            
        TODO: Implement this method
        """
        pass
    
    def select(self, table_name: str, conditions: Dict[str, Any] = None,
              columns: List[str] = None, limit: int = None,
              offset: int = 0, order_by: str = None) -> QueryResult:
        """
        Select records from a table.
        
        Args:
            table_name (str): Name of the table
            conditions (dict, optional): WHERE conditions
            columns (list, optional): Columns to select
            limit (int, optional): Maximum number of records
            offset (int): Number of records to skip
            order_by (str, optional): Column to order by
            
        Returns:
            QueryResult: Result of the operation
            
        TODO: Implement this method
        """
        pass
    
    def update(self, table_name: str, data: Dict[str, Any], 
              conditions: Dict[str, Any]) -> QueryResult:
        """
        Update records in a table.
        
        Args:
            table_name (str): Name of the table
            data (dict): Data to update
            conditions (dict): WHERE conditions
            
        Returns:
            QueryResult: Result of the operation
            
        TODO: Implement this method
        """
        pass
    
    def delete(self, table_name: str, conditions: Dict[str, Any]) -> QueryResult:
        """
        Delete records from a table.
        
        Args:
            table_name (str): Name of the table
            conditions (dict): WHERE conditions
            
        Returns:
            QueryResult: Result of the operation
            
        TODO: Implement this method
        """
        pass
    
    def execute_raw_query(self, query: str, params: List[Any] = None) -> QueryResult:
        """
        Execute a raw SQL query (simplified parsing).
        
        Args:
            query (str): SQL query string
            params (list, optional): Query parameters
            
        Returns:
            QueryResult: Result of the operation
            
        TODO: Implement this method
        """
        pass
    
    def begin_transaction(self) -> bool:
        """
        Begin a database transaction.
        
        Returns:
            bool: True if successful
            
        TODO: Implement this method
        """
        pass
    
    def commit_transaction(self) -> bool:
        """
        Commit the current transaction.
        
        Returns:
            bool: True if successful
            
        TODO: Implement this method
        """
        pass
    
    def rollback_transaction(self) -> bool:
        """
        Rollback the current transaction.
        
        Returns:
            bool: True if successful
            
        TODO: Implement this method
        """
        pass
    
    def validate_data(self, table_name: str, data: Dict[str, Any]) -> List[str]:
        """
        Validate data against table schema.
        
        Args:
            table_name (str): Name of the table
            data (dict): Data to validate
            
        Returns:
            list: List of validation errors
            
        TODO: Implement this method
        """
        pass
    
    def apply_conditions(self, records: List[Dict[str, Any]], 
                        conditions: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Apply WHERE conditions to filter records.
        
        Args:
            records (list): List of records
            conditions (dict): Conditions to apply
            
        Returns:
            list: Filtered records
            
        TODO: Implement this method
        """
        pass
    
    def simulate_latency(self) -> None:
        """
        Simulate database latency.
        
        TODO: Implement this method
        """
        pass
    
    def simulate_failure(self) -> bool:
        """
        Simulate database failures based on failure rate.
        
        Returns:
            bool: True if operation should fail
            
        TODO: Implement this method
        """
        pass
    
    def get_table_info(self, table_name: str) -> Dict[str, Any]:
        """
        Get information about a table.
        
        Args:
            table_name (str): Name of the table
            
        Returns:
            dict: Table information
            
        TODO: Implement this method
        """
        pass
    
    def get_query_log(self, limit: int = None) -> List[Dict[str, Any]]:
        """
        Get query execution log.
        
        Args:
            limit (int, optional): Maximum number of entries
            
        Returns:
            list: Query log entries
            
        TODO: Implement this method
        """
        pass
    
    def clear_query_log(self) -> None:
        """
        Clear the query log.
        
        TODO: Implement this method
        """
        pass
    
    def export_data(self, table_name: str, format_type: str = "json") -> str:
        """
        Export table data.
        
        Args:
            table_name (str): Name of the table
            format_type (str): Export format ("json", "csv")
            
        Returns:
            str: Exported data as string
            
        TODO: Implement this method
        """
        pass
    
    def import_data(self, table_name: str, data: str, format_type: str = "json") -> QueryResult:
        """
        Import data into a table.
        
        Args:
            table_name (str): Name of the table
            data (str): Data to import
            format_type (str): Data format ("json", "csv")
            
        Returns:
            QueryResult: Result of the operation
            
        TODO: Implement this method
        """
        pass

class ConnectionPool:
    """
    Database connection pool mock.
    """
    
    def __init__(self, database_mock: DatabaseMock, max_connections: int = 10):
        """
        Initialize connection pool.
        
        Args:
            database_mock (DatabaseMock): Database mock instance
            max_connections (int): Maximum number of connections
        """
        self.database_mock = database_mock
        self.max_connections = max_connections
        self.active_connections = 0
        self.connection_queue = []
    
    def get_connection(self) -> Optional[DatabaseMock]:
        """
        Get a database connection.
        
        Returns:
            DatabaseMock or None: Database connection or None if pool is full
            
        TODO: Implement this method
        """
        pass
    
    def release_connection(self, connection: DatabaseMock) -> bool:
        """
        Release a database connection back to the pool.
        
        Args:
            connection (DatabaseMock): Connection to release
            
        Returns:
            bool: True if successful
            
        TODO: Implement this method
        """
        pass
    
    def get_pool_stats(self) -> Dict[str, Any]:
        """
        Get connection pool statistics.
        
        Returns:
            dict: Pool statistics
            
        TODO: Implement this method
        """
        pass

class DatabaseTestHelper:
    """
    Helper class for database testing scenarios.
    """
    
    def __init__(self, database_mock: DatabaseMock):
        """
        Initialize database test helper.
        
        Args:
            database_mock (DatabaseMock): Database mock instance
        """
        self.database_mock = database_mock
        self.test_data_generators = {}
    
    def setup_test_tables(self) -> None:
        """
        Set up common test tables.
        
        TODO: Implement this method
        """
        pass
    
    def generate_test_data(self, table_name: str, count: int) -> List[Dict[str, Any]]:
        """
        Generate test data for a table.
        
        Args:
            table_name (str): Name of the table
            count (int): Number of records to generate
            
        Returns:
            list: Generated test data
            
        TODO: Implement this method
        """
        pass
    
    def create_user_data(self, count: int = 10) -> List[Dict[str, Any]]:
        """
        Create test user data.
        
        Args:
            count (int): Number of users to create
            
        Returns:
            list: User data
            
        TODO: Implement this method
        """
        pass
    
    def create_product_data(self, count: int = 20) -> List[Dict[str, Any]]:
        """
        Create test product data.
        
        Args:
            count (int): Number of products to create
            
        Returns:
            list: Product data
            
        TODO: Implement this method
        """
        pass
    
    def run_crud_tests(self, table_name: str) -> Dict[str, Any]:
        """
        Run comprehensive CRUD tests on a table.
        
        Args:
            table_name (str): Name of the table to test
            
        Returns:
            dict: Test results
            
        TODO: Implement this method
        """
        pass
    
    def run_performance_tests(self, operations: int = 1000) -> Dict[str, Any]:
        """
        Run performance tests.
        
        Args:
            operations (int): Number of operations to perform
            
        Returns:
            dict: Performance test results
            
        TODO: Implement this method
        """
        pass

def create_sample_schemas() -> Dict[str, Dict[str, Any]]:
    """
    Create sample table schemas for testing.
    
    Returns:
        dict: Dictionary of table schemas
        
    TODO: Implement this function
    """
    pass

# Test cases and demonstrations
if __name__ == "__main__":
    print("=== Database Mock Exercise ===\n")
    
    # Initialize database mock
    db = DatabaseMock()
    pool = ConnectionPool(db, max_connections=5)
    helper = DatabaseTestHelper(db)
    
    # Create sample schemas
    print("1. Creating Sample Schemas:")
    schemas = create_sample_schemas()
    
    for table_name, schema in schemas.items():
        result = db.create_table(table_name, schema)
        print(f"Created table '{table_name}': {result.success}")
    
    # Test basic CRUD operations
    print("\n2. Basic CRUD Operations:")
    
    # Test INSERT
    user_data = {
        "name": "John Doe",
        "email": "john@example.com",
        "age": 30,
        "active": True
    }
    
    insert_result = db.insert("users", user_data)
    print(f"Insert result: {insert_result.success}, rows affected: {insert_result.rows_affected}")
    
    # Test INSERT MANY
    users_data = [
        {"name": "Jane Smith", "email": "jane@example.com", "age": 25, "active": True},
        {"name": "Bob Johnson", "email": "bob@example.com", "age": 35, "active": False},
        {"name": "Alice Brown", "email": "alice@example.com", "age": 28, "active": True}
    ]
    
    insert_many_result = db.insert_many("users", users_data)
    print(f"Insert many result: {insert_many_result.success}, rows affected: {insert_many_result.rows_affected}")
    
    # Test SELECT
    select_result = db.select("users")
    print(f"Select all users: {len(select_result.data)} records")
    
    # Test SELECT with conditions
    active_users = db.select("users", conditions={"active": True})
    print(f"Active users: {len(active_users.data)} records")
    
    # Test SELECT with limit and offset
    limited_users = db.select("users", limit=2, offset=1)
    print(f"Limited users (2, offset 1): {len(limited_users.data)} records")
    
    # Test UPDATE
    update_result = db.update("users", {"age": 31}, {"name": "John Doe"})
    print(f"Update result: {update_result.success}, rows affected: {update_result.rows_affected}")
    
    # Test DELETE
    delete_result = db.delete("users", {"active": False})
    print(f"Delete result: {delete_result.success}, rows affected: {delete_result.rows_affected}")
    
    # Test transaction operations
    print("\n3. Transaction Tests:")
    
    # Begin transaction
    transaction_started = db.begin_transaction()
    print(f"Transaction started: {transaction_started}")
    
    # Perform operations in transaction
    db.insert("users", {"name": "Transaction User", "email": "trans@example.com", "age": 40, "active": True})
    db.update("users", {"age": 32}, {"name": "John Doe"})
    
    # Rollback transaction
    rollback_success = db.rollback_transaction()
    print(f"Transaction rolled back: {rollback_success}")
    
    # Verify rollback
    after_rollback = db.select("users")
    print(f"Users after rollback: {len(after_rollback.data)} records")
    
    # Test successful transaction
    db.begin_transaction()
    db.insert("users", {"name": "Committed User", "email": "commit@example.com", "age": 45, "active": True})
    commit_success = db.commit_transaction()
    print(f"Transaction committed: {commit_success}")
    
    # Test data validation
    print("\n4. Data Validation Tests:")
    
    # Test with invalid data
    invalid_data = {
        "name": None,  # Should be required
        "email": "invalid-email",  # Should be valid email format
        "age": "not-a-number",  # Should be integer
        "active": "maybe"  # Should be boolean
    }
    
    validation_errors = db.validate_data("users", invalid_data)
    print(f"Validation errors: {len(validation_errors)}")
    for error in validation_errors:
        print(f"  - {error}")
    
    # Test raw query execution
    print("\n5. Raw Query Tests:")
    
    raw_queries = [
        "SELECT * FROM users WHERE age > 25",
        "SELECT name, email FROM users WHERE active = true",
        "UPDATE users SET age = age + 1 WHERE name LIKE '%John%'"
    ]
    
    for query in raw_queries:
        result = db.execute_raw_query(query)
        print(f"Query: {query[:40]}... | Success: {result.success} | Rows: {result.rows_affected}")
    
    # Test connection pool
    print("\n6. Connection Pool Tests:")
    
    # Get multiple connections
    connections = []
    for i in range(7):  # Try to get more than max_connections
        conn = pool.get_connection()
        if conn:
            connections.append(conn)
            print(f"Got connection {i+1}")
        else:
            print(f"Failed to get connection {i+1} (pool full)")
    
    # Check pool stats
    pool_stats = pool.get_pool_stats()
    print(f"Pool stats: {pool_stats}")
    
    # Release connections
    for i, conn in enumerate(connections[:3]):
        pool.release_connection(conn)
        print(f"Released connection {i+1}")
    
    # Test failure simulation
    print("\n7. Failure Simulation Tests:")
    
    # Set failure rate
    db.failure_rate = 0.3  # 30% failure rate
    
    failures = 0
    total_ops = 10
    
    for i in range(total_ops):
        result = db.select("users", conditions={"id": i})
        if not result.success:
            failures += 1
    
    print(f"Simulated {failures}/{total_ops} failures ({failures/total_ops*100:.1f}%)")
    
    # Reset failure rate
    db.failure_rate = 0.0
    
    # Test latency simulation
    print("\n8. Latency Simulation Tests:")
    
    db.latency_simulation = 100  # 100ms latency
    
    start_time = datetime.now()
    db.select("users")
    end_time = datetime.now()
    
    actual_latency = (end_time - start_time).total_seconds() * 1000
    print(f"Simulated latency: {db.latency_simulation}ms, Actual: {actual_latency:.1f}ms")
    
    # Test helper functions
    print("\n9. Database Helper Tests:")
    
    # Setup test tables
    helper.setup_test_tables()
    print("Test tables set up")
    
    # Generate test data
    test_users = helper.create_user_data(5)
    test_products = helper.create_product_data(10)
    
    print(f"Generated {len(test_users)} test users and {len(test_products)} test products")
    
    # Run CRUD tests
    crud_results = helper.run_crud_tests("users")
    print(f"CRUD test results: {crud_results}")
    
    # Run performance tests
    perf_results = helper.run_performance_tests(100)
    print(f"Performance test results: {perf_results}")
    
    # Test data export/import
    print("\n10. Data Export/Import Tests:")
    
    # Export data
    exported_json = db.export_data("users", "json")
    exported_csv = db.export_data("users", "csv")
    
    print(f"Exported JSON: {len(exported_json)} characters")
    print(f"Exported CSV: {len(exported_csv)} characters")
    
    # Clear table and import data back
    db.delete("users", {})  # Delete all users
    
    import_result = db.import_data("users", exported_json, "json")
    print(f"Import result: {import_result.success}, rows affected: {import_result.rows_affected}")
    
    # Test query logging
    print("\n11. Query Logging Tests:")
    
    # Perform some operations
    db.select("users")
    db.insert("users", {"name": "Log Test", "email": "log@test.com", "age": 25, "active": True})
    db.update("users", {"age": 26}, {"name": "Log Test"})
    
    # Get query log
    query_log = db.get_query_log(5)
    print(f"Query log entries: {len(query_log)}")
    
    for entry in query_log:
        print(f"  {entry.get('timestamp', 'Unknown')} | {entry.get('query_type', 'Unknown')} | {entry.get('execution_time_ms', 0):.2f}ms")
    
    # Test table information
    print("\n12. Table Information Tests:")
    
    for table_name in schemas.keys():
        table_info = db.get_table_info(table_name)
        print(f"Table '{table_name}': {table_info.get('record_count', 0)} records, {len(table_info.get('columns', []))} columns")
    
    print(f"\nDatabase mock testing complete!")
    print(f"Total tables: {len(db.tables)}")
    print(f"Total query log entries: {len(db.query_log)}")
    
    # Clear query log
    db.clear_query_log()
    print("Query log cleared")