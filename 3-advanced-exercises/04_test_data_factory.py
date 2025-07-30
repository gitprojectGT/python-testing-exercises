"""
Exercise 4: Test Data Factory
Testing Focus: Complex data relationships, data consistency

Task: Build an advanced test data generation and management system.
This exercise focuses on creating realistic, related test data with complex constraints and relationships.
"""

import random
import json
import uuid
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from enum import Enum
from typing import Dict, List, Any, Optional, Union, Callable, Set, Tuple
from collections import defaultdict, deque
import copy

class DataType(Enum):
    """Types of data that can be generated."""
    STRING = "string"
    INTEGER = "integer"
    FLOAT = "float"
    BOOLEAN = "boolean"
    DATE = "date"
    EMAIL = "email"
    PHONE = "phone"
    UUID = "uuid"
    ENUM = "enum"
    REFERENCE = "reference"
    LIST = "list"
    OBJECT = "object"

class RelationshipType(Enum):
    """Types of relationships between entities."""
    ONE_TO_ONE = "one_to_one"
    ONE_TO_MANY = "one_to_many"
    MANY_TO_ONE = "many_to_one"
    MANY_TO_MANY = "many_to_many"

@dataclass
class FieldConstraint:
    """Represents a constraint on a data field."""
    field_name: str
    constraint_type: str
    constraint_value: Any
    error_message: str = ""

@dataclass
class DataRelationship:
    """Represents a relationship between two entities."""
    source_entity: str
    target_entity: str
    relationship_type: RelationshipType
    source_field: str
    target_field: str
    cascade_delete: bool = False
    constraint_rules: List[str] = field(default_factory=list)

@dataclass
class EntitySchema:
    """Schema definition for a data entity."""
    entity_name: str
    fields: Dict[str, Dict[str, Any]]
    constraints: List[FieldConstraint] = field(default_factory=list)
    relationships: List[DataRelationship] = field(default_factory=list)
    generation_rules: Dict[str, Any] = field(default_factory=dict)
    data_dependencies: List[str] = field(default_factory=list)

class DataGenerator(ABC):
    """Abstract base class for data generators."""
    
    @abstractmethod
    def generate(self, **kwargs) -> Any:
        """Generate data based on specifications."""
        pass
    
    @abstractmethod
    def validate(self, value: Any) -> bool:
        """Validate generated data."""
        pass

class StringGenerator(DataGenerator):
    """Generator for string data."""
    
    def __init__(self, min_length: int = 1, max_length: int = 50, 
                 pattern: str = None, charset: str = None):
        """
        Initialize string generator.
        
        Args:
            min_length (int): Minimum string length
            max_length (int): Maximum string length
            pattern (str): Regex pattern to match
            charset (str): Character set to use
        """
        self.min_length = min_length
        self.max_length = max_length
        self.pattern = pattern
        self.charset = charset or "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    
    def generate(self, **kwargs) -> str:
        """
        Generate a random string.
        
        Returns:
            str: Generated string
            
        TODO: Implement this method
        """
        pass
    
    def validate(self, value: Any) -> bool:
        """
        Validate string value.
        
        Args:
            value: Value to validate
            
        Returns:
            bool: True if valid
            
        TODO: Implement this method
        """
        pass

class IntegerGenerator(DataGenerator):
    """Generator for integer data."""
    
    def __init__(self, min_value: int = 0, max_value: int = 1000000, 
                 step: int = 1, exclude_values: List[int] = None):
        """
        Initialize integer generator.
        
        Args:
            min_value (int): Minimum value
            max_value (int): Maximum value  
            step (int): Step size
            exclude_values (list): Values to exclude
        """
        self.min_value = min_value
        self.max_value = max_value
        self.step = step
        self.exclude_values = exclude_values or []
    
    def generate(self, **kwargs) -> int:
        """
        Generate a random integer.
        
        Returns:
            int: Generated integer
            
        TODO: Implement this method
        """
        pass
    
    def validate(self, value: Any) -> bool:
        """
        Validate integer value.
        
        Args:
            value: Value to validate
            
        Returns:
            bool: True if valid
            
        TODO: Implement this method
        """
        pass

class EmailGenerator(DataGenerator):
    """Generator for email addresses."""
    
    def __init__(self, domains: List[str] = None, local_patterns: List[str] = None):
        """
        Initialize email generator.
        
        Args:
            domains (list): List of domains to use
            local_patterns (list): Patterns for local part
        """
        self.domains = domains or ["example.com", "test.org", "demo.net"]
        self.local_patterns = local_patterns or ["user{}", "test{}", "{}.{}", "{}"]
    
    def generate(self, **kwargs) -> str:
        """
        Generate a random email address.
        
        Returns:
            str: Generated email
            
        TODO: Implement this method
        """
        pass
    
    def validate(self, value: Any) -> bool:
        """
        Validate email format.
        
        Args:
            value: Value to validate
            
        Returns:
            bool: True if valid email format
            
        TODO: Implement this method
        """
        pass

class ReferenceGenerator(DataGenerator):
    """Generator for reference fields (foreign keys)."""
    
    def __init__(self, target_entity: str, target_field: str, data_store: 'DataStore'):
        """
        Initialize reference generator.
        
        Args:
            target_entity (str): Name of target entity
            target_field (str): Field in target entity
            data_store (DataStore): Data store containing entities
        """
        self.target_entity = target_entity
        self.target_field = target_field
        self.data_store = data_store
    
    def generate(self, **kwargs) -> Any:
        """
        Generate a reference to existing data.
        
        Returns:
            Any: Reference value
            
        TODO: Implement this method
        """
        pass
    
    def validate(self, value: Any) -> bool:
        """
        Validate reference exists.
        
        Args:
            value: Reference value to validate
            
        Returns:
            bool: True if reference exists
            
        TODO: Implement this method
        """
        pass

class DataStore:
    """In-memory store for generated test data."""
    
    def __init__(self):
        """Initialize data store."""
        self.entities: Dict[str, List[Dict[str, Any]]] = {}
        self.indexes: Dict[str, Dict[str, Dict[Any, List[int]]]] = {}
        self.relationships: Dict[str, List[DataRelationship]] = {}
    
    def create_entity_table(self, entity_name: str) -> None:
        """
        Create a table for an entity.
        
        Args:
            entity_name (str): Name of the entity
            
        TODO: Implement this method
        """
        pass
    
    def insert_record(self, entity_name: str, record: Dict[str, Any]) -> str:
        """
        Insert a record into an entity table.
        
        Args:
            entity_name (str): Entity name
            record (dict): Record data
            
        Returns:
            str: Record ID
            
        TODO: Implement this method
        """
        pass
    
    def get_records(self, entity_name: str, filters: Dict[str, Any] = None) -> List[Dict[str, Any]]:
        """
        Get records from entity table.
        
        Args:
            entity_name (str): Entity name
            filters (dict): Filter criteria
            
        Returns:
            list: Matching records
            
        TODO: Implement this method
        """
        pass
    
    def create_index(self, entity_name: str, field_name: str) -> None:
        """
        Create an index on a field.
        
        Args:
            entity_name (str): Entity name
            field_name (str): Field to index
            
        TODO: Implement this method
        """
        pass
    
    def validate_relationships(self) -> List[str]:
        """
        Validate all relationships in the data store.
        
        Returns:
            list: List of validation errors
            
        TODO: Implement this method
        """
        pass
    
    def get_entity_statistics(self, entity_name: str) -> Dict[str, Any]:
        """
        Get statistics for an entity.
        
        Args:
            entity_name (str): Entity name
            
        Returns:
            dict: Entity statistics
            
        TODO: Implement this method
        """
        pass

class TestDataFactory:
    """Main factory class for generating test data."""
    
    def __init__(self):
        """Initialize test data factory."""
        self.schemas: Dict[str, EntitySchema] = {}
        self.generators: Dict[str, DataGenerator] = {}
        self.data_store = DataStore()
        self.generation_order: List[str] = []
        self.global_constraints: List[FieldConstraint] = []
    
    def register_schema(self, schema: EntitySchema) -> None:
        """
        Register an entity schema.
        
        Args:
            schema (EntitySchema): Entity schema to register
            
        TODO: Implement this method
        """
        pass
    
    def register_generator(self, data_type: str, generator: DataGenerator) -> None:
        """
        Register a data generator.
        
        Args:
            data_type (str): Data type name
            generator (DataGenerator): Generator instance
            
        TODO: Implement this method
        """
        pass
    
    def calculate_generation_order(self) -> List[str]:
        """
        Calculate order for generating entities based on dependencies.
        
        Returns:
            list: Ordered list of entity names
            
        TODO: Implement this method (topological sort)
        """
        pass
    
    def generate_entity_data(self, entity_name: str, count: int, 
                           seed: int = None) -> List[Dict[str, Any]]:
        """
        Generate data for a specific entity.
        
        Args:
            entity_name (str): Entity name
            count (int): Number of records to generate
            seed (int): Random seed for reproducibility
            
        Returns:
            list: Generated records
            
        TODO: Implement this method
        """
        pass
    
    def generate_all_data(self, entity_counts: Dict[str, int], 
                         seed: int = None) -> Dict[str, List[Dict[str, Any]]]:
        """
        Generate data for all registered entities.
        
        Args:
            entity_counts (dict): Number of records for each entity
            seed (int): Random seed for reproducibility
            
        Returns:
            dict: Generated data for all entities
            
        TODO: Implement this method
        """
        pass
    
    def validate_data_consistency(self) -> List[str]:
        """
        Validate consistency of generated data.
        
        Returns:
            list: List of consistency errors
            
        TODO: Implement this method
        """
        pass
    
    def apply_constraints(self, entity_name: str, 
                         data: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """
        Apply constraints to generated data.
        
        Args:
            entity_name (str): Entity name
            data (list): Generated data
            
        Returns:
            list: Data with constraints applied
            
        TODO: Implement this method
        """
        pass
    
    def export_data(self, format_type: str = "json", 
                   file_path: str = None) -> Union[str, Dict[str, Any]]:
        """
        Export generated data.
        
        Args:
            format_type (str): Export format ("json", "csv", "sql")
            file_path (str): File path to save to
            
        Returns:
            Export data as string or dict
            
        TODO: Implement this method
        """
        pass
    
    def clone_data_with_modifications(self, entity_name: str, 
                                    modifications: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Clone existing data with modifications.
        
        Args:
            entity_name (str): Entity name
            modifications (dict): Field modifications to apply
            
        Returns:
            list: Cloned and modified data
            
        TODO: Implement this method
        """
        pass

class DataTemplate:
    """Template system for predefined data patterns."""
    
    def __init__(self, name: str, description: str):
        """
        Initialize data template.
        
        Args:
            name (str): Template name
            description (str): Template description
        """
        self.name = name
        self.description = description
        self.schemas: List[EntitySchema] = []
        self.sample_data: Dict[str, List[Dict[str, Any]]] = {}
    
    def add_schema(self, schema: EntitySchema) -> None:
        """
        Add schema to template.
        
        Args:
            schema (EntitySchema): Schema to add
            
        TODO: Implement this method
        """
        pass
    
    def generate_sample_data(self, factory: TestDataFactory, 
                           scale_factor: float = 1.0) -> Dict[str, List[Dict[str, Any]]]:
        """
        Generate sample data using the template.
        
        Args:
            factory (TestDataFactory): Factory to use for generation
            scale_factor (float): Scale factor for data volume
            
        Returns:
            dict: Generated sample data
            
        TODO: Implement this method
        """
        pass

class DataConsistencyChecker:
    """Validates data consistency and relationships."""
    
    def __init__(self, data_store: DataStore):
        """
        Initialize consistency checker.
        
        Args:
            data_store (DataStore): Data store to check
        """
        self.data_store = data_store
        self.validation_rules: List[Callable] = []
    
    def add_validation_rule(self, rule: Callable[[Dict[str, Any]], bool]) -> None:
        """
        Add a custom validation rule.
        
        Args:
            rule (Callable): Validation rule function
            
        TODO: Implement this method
        """
        pass
    
    def check_referential_integrity(self) -> List[str]:
        """
        Check referential integrity of relationships.
        
        Returns:
            list: List of integrity violations
            
        TODO: Implement this method
        """
        pass
    
    def check_uniqueness_constraints(self) -> List[str]:
        """
        Check uniqueness constraints.
        
        Returns:
            list: List of uniqueness violations
            
        TODO: Implement this method
        """
        pass
    
    def check_business_rules(self) -> List[str]:
        """
        Check custom business rules.
        
        Returns:
            list: List of business rule violations
            
        TODO: Implement this method
        """
        pass
    
    def generate_consistency_report(self) -> Dict[str, Any]:
        """
        Generate comprehensive consistency report.
        
        Returns:
            dict: Consistency report
            
        TODO: Implement this method
        """
        pass

def create_ecommerce_template() -> DataTemplate:
    """
    Create an e-commerce data template.
    
    Returns:
        DataTemplate: E-commerce template
        
    TODO: Implement this function
    """
    pass

def create_user_management_template() -> DataTemplate:
    """
    Create a user management data template.
    
    Returns:
        DataTemplate: User management template
        
    TODO: Implement this function
    """
    pass

def create_financial_template() -> DataTemplate:
    """
    Create a financial data template.
    
    Returns:
        DataTemplate: Financial template
        
    TODO: Implement this function
    """
    pass

# Test cases and demonstrations
if __name__ == "__main__":
    print("=== Test Data Factory Exercise ===\n")
    
    # Initialize test data factory
    factory = TestDataFactory()
    
    print("1. Test Data Factory Initialization:")
    print(f"Data store initialized: {factory.data_store is not None}")
    print(f"Schemas registered: {len(factory.schemas)}")
    print(f"Generators registered: {len(factory.generators)}")
    
    # Register basic generators
    print("\n2. Registering Data Generators:")
    
    generators = [
        ("string", StringGenerator(min_length=5, max_length=20)),
        ("integer", IntegerGenerator(min_value=1, max_value=1000)),
        ("email", EmailGenerator()),
        ("phone", StringGenerator(min_length=10, max_length=15, pattern=r'\d{3}-\d{3}-\d{4}')),
    ]
    
    for gen_type, generator in generators:
        factory.register_generator(gen_type, generator)
        print(f"  Registered {gen_type} generator")
    
    # Test individual generators
    print("\n3. Testing Individual Generators:")
    
    for gen_type, generator in generators:
        try:
            sample_value = generator.generate()
            is_valid = generator.validate(sample_value)
            print(f"  {gen_type}: '{sample_value}' (valid: {is_valid})")
        except Exception as e:
            print(f"  {gen_type}: Error - {e}")
    
    # Create sample schemas
    print("\n4. Creating Entity Schemas:")
    
    # User schema
    user_schema = EntitySchema(
        entity_name="users",
        fields={
            "id": {"type": "integer", "primary_key": True, "auto_increment": True},
            "username": {"type": "string", "unique": True, "required": True},
            "email": {"type": "email", "unique": True, "required": True},
            "first_name": {"type": "string", "required": True},
            "last_name": {"type": "string", "required": True},
            "age": {"type": "integer", "min": 18, "max": 100},
            "created_at": {"type": "date", "default": "now"}
        },
        constraints=[
            FieldConstraint("age", "range", {"min": 18, "max": 100}, "Age must be between 18 and 100"),
            FieldConstraint("email", "format", "email", "Must be valid email format")
        ]
    )
    
    # Product schema
    product_schema = EntitySchema(
        entity_name="products",
        fields={
            "id": {"type": "integer", "primary_key": True, "auto_increment": True},
            "name": {"type": "string", "required": True},
            "price": {"type": "float", "min": 0.01},
            "category": {"type": "enum", "values": ["electronics", "books", "clothing", "home"]},
            "in_stock": {"type": "boolean", "default": True},
            "created_by": {"type": "reference", "entity": "users", "field": "id"}
        },
        relationships=[
            DataRelationship("products", "users", RelationshipType.MANY_TO_ONE, "created_by", "id")
        ]
    )
    
    # Order schema  
    order_schema = EntitySchema(
        entity_name="orders",
        fields={
            "id": {"type": "integer", "primary_key": True, "auto_increment": True},
            "user_id": {"type": "reference", "entity": "users", "field": "id"},
            "total_amount": {"type": "float", "min": 0},
            "status": {"type": "enum", "values": ["pending", "paid", "shipped", "delivered"]},
            "order_date": {"type": "date", "default": "now"}
        },
        relationships=[
            DataRelationship("orders", "users", RelationshipType.MANY_TO_ONE, "user_id", "id")
        ],
        data_dependencies=["users"]  # Orders depend on users existing first
    )
    
    schemas = [user_schema, product_schema, order_schema]
    
    for schema in schemas:
        factory.register_schema(schema)
        print(f"  Registered schema: {schema.entity_name} ({len(schema.fields)} fields)")
    
    # Test generation order calculation
    print("\n5. Calculating Generation Order:")
    
    generation_order = factory.calculate_generation_order()
    print(f"Generation order: {generation_order}")
    
    # Generate data for entities
    print("\n6. Generating Entity Data:")
    
    entity_counts = {"users": 10, "products": 20, "orders": 15}
    
    for entity_name, count in entity_counts.items():
        try:
            generated_data = factory.generate_entity_data(entity_name, count, seed=42)
            print(f"  Generated {len(generated_data)} {entity_name} records")
            
            # Show sample record
            if generated_data:
                sample_keys = list(generated_data[0].keys())[:3]  # Show first 3 fields
                sample_values = {k: generated_data[0][k] for k in sample_keys}
                print(f"    Sample: {sample_values}")
                
        except Exception as e:
            print(f"  Error generating {entity_name}: {e}")
    
    # Generate all data at once
    print("\n7. Generating All Data:")
    
    all_data = factory.generate_all_data(entity_counts, seed=42)
    print(f"Generated data for {len(all_data)} entities:")
    
    for entity_name, records in all_data.items():
        print(f"  {entity_name}: {len(records)} records")
    
    # Test data consistency validation
    print("\n8. Data Consistency Validation:")
    
    consistency_errors = factory.validate_data_consistency()
    print(f"Consistency errors found: {len(consistency_errors)}")
    
    for error in consistency_errors[:5]:  # Show first 5 errors
        print(f"  - {error}")
    
    # Test data store operations
    print("\n9. Data Store Operations:")
    
    # Get entity statistics
    for entity_name in ["users", "products", "orders"]:
        stats = factory.data_store.get_entity_statistics(entity_name)
        print(f"  {entity_name} statistics: {stats}")
    
    # Test queries
    user_records = factory.data_store.get_records("users", {"age": 25})
    print(f"  Users with age 25: {len(user_records)} found")
    
    # Test data templates
    print("\n10. Data Templates:")
    
    templates = [
        ("E-commerce", create_ecommerce_template()),
        ("User Management", create_user_management_template()),
        ("Financial", create_financial_template())
    ]
    
    for template_name, template in templates:
        try:
            sample_data = template.generate_sample_data(factory, scale_factor=0.5)
            total_records = sum(len(records) for records in sample_data.values())
            print(f"  {template_name} template: {total_records} total records")
        except Exception as e:
            print(f"  {template_name} template: Error - {e}")
    
    # Test consistency checker
    print("\n11. Data Consistency Checking:")
    
    checker = DataConsistencyChecker(factory.data_store)
    
    # Check referential integrity
    ref_errors = checker.check_referential_integrity()
    print(f"  Referential integrity errors: {len(ref_errors)}")
    
    # Check uniqueness constraints
    unique_errors = checker.check_uniqueness_constraints()
    print(f"  Uniqueness constraint errors: {len(unique_errors)}")
    
    # Generate consistency report
    consistency_report = checker.generate_consistency_report()
    print(f"  Consistency report sections: {list(consistency_report.keys())}")
    
    # Test data export
    print("\n12. Data Export:")
    
    export_formats = ["json", "csv", "sql"]
    
    for export_format in export_formats:
        try:
            exported_data = factory.export_data(format_type=export_format)
            print(f"  {export_format.upper()} export: {len(str(exported_data))} characters")
        except Exception as e:
            print(f"  {export_format.upper()} export: Error - {e}")
    
    # Test data cloning and modification
    print("\n13. Data Cloning and Modification:")
    
    modifications = {
        "age": lambda x: x + 1,  # Increase age by 1
        "status": "active",      # Set status to active
        "updated_at": datetime.now()  # Add update timestamp
    }
    
    try:
        cloned_users = factory.clone_data_with_modifications("users", modifications)
        print(f"  Cloned and modified {len(cloned_users)} user records")
        
        if cloned_users:
            original_user = factory.data_store.get_records("users")[0]
            cloned_user = cloned_users[0]
            print(f"    Original age: {original_user.get('age')}")
            print(f"    Modified age: {cloned_user.get('age')}")
            
    except Exception as e:
        print(f"  Data cloning error: {e}")
    
    # Test advanced relationships
    print("\n14. Advanced Relationship Testing:")
    
    # Test many-to-many relationships
    order_items_schema = EntitySchema(
        entity_name="order_items",
        fields={
            "id": {"type": "integer", "primary_key": True, "auto_increment": True},
            "order_id": {"type": "reference", "entity": "orders", "field": "id"},
            "product_id": {"type": "reference", "entity": "products", "field": "id"},
            "quantity": {"type": "integer", "min": 1},
            "unit_price": {"type": "float", "min": 0}
        },
        relationships=[
            DataRelationship("order_items", "orders", RelationshipType.MANY_TO_ONE, "order_id", "id"),
            DataRelationship("order_items", "products", RelationshipType.MANY_TO_ONE, "product_id", "id")
        ],
        data_dependencies=["orders", "products"]
    )
    
    factory.register_schema(order_items_schema)
    
    try:
        order_items_data = factory.generate_entity_data("order_items", 30, seed=42)
        print(f"  Generated {len(order_items_data)} order items with relationships")
    except Exception as e:
        print(f"  Order items generation error: {e}")
    
    # Test data factory performance  
    print("\n15. Performance Testing:")
    
    import time
    
    start_time = time.time()
    large_dataset = factory.generate_all_data({
        "users": 100,
        "products": 200, 
        "orders": 150,
        "order_items": 300
    }, seed=123)
    end_time = time.time()
    
    total_records = sum(len(records) for records in large_dataset.values())
    generation_time = end_time - start_time
    
    print(f"  Generated {total_records} total records in {generation_time:.2f}s")
    print(f"  Generation rate: {total_records/generation_time:.0f} records/second")
    
    print(f"\nTest Data Factory Exercise Complete!")
    print(f"Total schemas: {len(factory.schemas)}")
    print(f"Total generators: {len(factory.generators)}")
    print(f"Total entities in store: {len(factory.data_store.entities)}")
    
    # Final data summary
    final_summary = {}
    for entity_name, records in factory.data_store.entities.items():
        final_summary[entity_name] = len(records)
    
    print(f"Final data summary: {final_summary}")
    
    print("\n" + "="*50)
    print("Test Data Factory Exercise Complete!")
    print("="*50)