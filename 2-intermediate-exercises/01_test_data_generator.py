"""
Exercise 1: Test Data Generator
Testing Focus: Data generation, parameterized testing, boundary value analysis

Task: Create a comprehensive test data generator for various testing scenarios.
This tool helps generate realistic test data for different domains and use cases.
"""

import random
import string
import datetime
from enum import Enum
from dataclasses import dataclass
from typing import List, Dict, Any, Optional

class DataType(Enum):
    """Enum for different data types that can be generated."""
    USER = "user"
    PRODUCT = "product"
    ORDER = "order"
    EMAIL = "email"
    ADDRESS = "address"
    COMPANY = "company"
    FINANCIAL = "financial"

@dataclass
class GenerationConfig:
    """Configuration for data generation."""
    count: int = 10
    data_type: DataType = DataType.USER
    include_invalid: bool = False
    seed: Optional[int] = None
    custom_fields: Dict[str, Any] = None

class TestDataGenerator:
    """
    A comprehensive test data generator for various testing scenarios.
    """
    
    def __init__(self, config: GenerationConfig = None):
        """
        Initialize the test data generator.
        
        Args:
            config (GenerationConfig): Configuration for data generation
        """
        self.config = config or GenerationConfig()
        if self.config.seed:
            random.seed(self.config.seed)
        
        # Sample data pools
        self.first_names = ["John", "Jane", "Michael", "Sarah", "David", "Lisa", "Robert", "Emily"]
        self.last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"]
        self.domains = ["example.com", "test.org", "sample.net", "demo.co", "trial.io"]
        self.cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia"]
        self.states = ["NY", "CA", "IL", "TX", "AZ", "PA", "FL", "OH"]
        self.companies = ["TechCorp", "DataSoft", "InnovateLtd", "GlobalTech", "SmartSolutions"]
        self.products = ["Laptop", "Smartphone", "Tablet", "Headphones", "Monitor", "Keyboard"]
    
    def generate_random_string(self, length: int, include_special: bool = False) -> str:
        """
        Generate a random string of specified length.
        
        Args:
            length (int): Length of the string
            include_special (bool): Whether to include special characters
            
        Returns:
            str: Random string
            
        TODO: Implement this method
        """
        pass
    
    def generate_email(self, valid: bool = True) -> str:
        """
        Generate an email address.
        
        Args:
            valid (bool): Whether to generate a valid email format
            
        Returns:
            str: Email address
            
        TODO: Implement this method
        """
        pass
    
    def generate_phone_number(self, format_type: str = "us") -> str:
        """
        Generate a phone number in specified format.
        
        Args:
            format_type (str): Format type ("us", "international", "digits_only")
            
        Returns:
            str: Phone number
            
        TODO: Implement this method
        """
        pass
    
    def generate_date(self, start_date: str = "2020-01-01", end_date: str = "2024-12-31") -> str:
        """
        Generate a random date between start and end dates.
        
        Args:
            start_date (str): Start date in YYYY-MM-DD format
            end_date (str): End date in YYYY-MM-DD format
            
        Returns:
            str: Random date in YYYY-MM-DD format
            
        TODO: Implement this method
        """
        pass
    
    def generate_user_data(self, include_invalid: bool = False) -> Dict[str, Any]:
        """
        Generate user data.
        
        Args:
            include_invalid (bool): Whether to occasionally generate invalid data
            
        Returns:
            dict: User data dictionary
            
        Example output:
        {
            "id": 12345,
            "first_name": "John",
            "last_name": "Doe",
            "email": "john.doe@example.com",
            "phone": "555-123-4567",
            "date_of_birth": "1990-05-15",
            "is_active": True
        }
        
        TODO: Implement this method
        """
        pass
    
    def generate_product_data(self, include_invalid: bool = False) -> Dict[str, Any]:
        """
        Generate product data.
        
        Args:
            include_invalid (bool): Whether to occasionally generate invalid data
            
        Returns:
            dict: Product data dictionary
            
        TODO: Implement this method
        """
        pass
    
    def generate_order_data(self, include_invalid: bool = False) -> Dict[str, Any]:
        """
        Generate order data.
        
        Args:
            include_invalid (bool): Whether to occasionally generate invalid data
            
        Returns:
            dict: Order data dictionary
            
        TODO: Implement this method
        """
        pass
    
    def generate_address_data(self, include_invalid: bool = False) -> Dict[str, Any]:
        """
        Generate address data.
        
        Args:
            include_invalid (bool): Whether to occasionally generate invalid data
            
        Returns:
            dict: Address data dictionary
            
        TODO: Implement this method
        """
        pass
    
    def generate_financial_data(self, include_invalid: bool = False) -> Dict[str, Any]:
        """
        Generate financial data (credit card, account numbers, etc.).
        
        Args:
            include_invalid (bool): Whether to occasionally generate invalid data
            
        Returns:
            dict: Financial data dictionary
            
        Note: Generate fake data only - not real financial information
        
        TODO: Implement this method
        """
        pass
    
    def generate_boundary_values(self, data_type: str, field: str) -> List[Any]:
        """
        Generate boundary values for testing edge cases.
        
        Args:
            data_type (str): Type of data (e.g., "string", "integer", "email")
            field (str): Specific field name
            
        Returns:
            list: List of boundary values
            
        TODO: Implement this method
        """
        pass
    
    def generate_dataset(self) -> List[Dict[str, Any]]:
        """
        Generate a dataset based on configuration.
        
        Returns:
            list: List of generated data dictionaries
            
        TODO: Implement this method using other generate methods
        """
        pass
    
    def export_to_csv(self, dataset: List[Dict[str, Any]], filename: str) -> bool:
        """
        Export dataset to CSV file.
        
        Args:
            dataset (list): Dataset to export
            filename (str): Output filename
            
        Returns:
            bool: True if successful, False otherwise
            
        TODO: Implement this method
        """
        pass
    
    def export_to_json(self, dataset: List[Dict[str, Any]], filename: str) -> bool:
        """
        Export dataset to JSON file.
        
        Args:
            dataset (list): Dataset to export
            filename (str): Output filename
            
        Returns:
            bool: True if successful, False otherwise
            
        TODO: Implement this method
        """
        pass

def validate_generated_data(dataset: List[Dict[str, Any]], data_type: DataType) -> Dict[str, Any]:
    """
    Validate the quality and correctness of generated data.
    
    Args:
        dataset (list): Generated dataset
        data_type (DataType): Type of data to validate against
        
    Returns:
        dict: Validation results with statistics and issues found
        
    TODO: Implement this function
    """
    pass

def create_test_scenarios(data_type: DataType) -> List[GenerationConfig]:
    """
    Create predefined test scenarios for different data types.
    
    Args:
        data_type (DataType): Type of data to create scenarios for
        
    Returns:
        list: List of GenerationConfig objects for different scenarios
        
    TODO: Implement this function
    """
    pass

# Test cases and demonstrations
if __name__ == "__main__":
    print("=== Test Data Generator Exercise ===\n")
    
    # Test basic data generation
    print("1. Basic Data Generation Tests:")
    
    # Test user data generation
    config_user = GenerationConfig(count=5, data_type=DataType.USER)
    generator = TestDataGenerator(config_user)
    
    print("Generated Users:")
    for i in range(3):
        user = generator.generate_user_data()
        print(f"  User {i+1}: {user}")
    
    # Test product data generation
    print("\nGenerated Products:")
    for i in range(3):
        product = generator.generate_product_data()
        print(f"  Product {i+1}: {product}")
    
    # Test various data types
    print("\n2. Individual Data Type Tests:")
    
    print(f"Random string: {generator.generate_random_string(10)}")
    print(f"Email: {generator.generate_email()}")
    print(f"Invalid email: {generator.generate_email(valid=False)}")
    print(f"Phone (US): {generator.generate_phone_number('us')}")
    print(f"Phone (International): {generator.generate_phone_number('international')}")
    print(f"Random date: {generator.generate_date()}")
    
    # Test boundary values
    print("\n3. Boundary Value Tests:")
    boundary_tests = [
        ("string", "username"),
        ("integer", "age"),
        ("email", "email")
    ]
    
    for data_type, field in boundary_tests:
        boundaries = generator.generate_boundary_values(data_type, field)
        print(f"Boundaries for {data_type}.{field}: {boundaries}")
    
    # Test dataset generation
    print("\n4. Dataset Generation Tests:")
    
    test_configs = [
        GenerationConfig(count=3, data_type=DataType.USER),
        GenerationConfig(count=3, data_type=DataType.PRODUCT, include_invalid=True),
        GenerationConfig(count=3, data_type=DataType.ORDER)
    ]
    
    for config in test_configs:
        generator = TestDataGenerator(config)
        dataset = generator.generate_dataset()
        print(f"Dataset ({config.data_type.value}, count={config.count}):")
        for item in dataset:
            print(f"  {item}")
        
        # Validate the dataset
        validation = validate_generated_data(dataset, config.data_type)
        print(f"  Validation: {validation}")
        print()
    
    # Test export functionality
    print("5. Export Tests:")
    
    user_config = GenerationConfig(count=5, data_type=DataType.USER, seed=42)
    export_generator = TestDataGenerator(user_config)
    export_dataset = export_generator.generate_dataset()
    
    csv_success = export_generator.export_to_csv(export_dataset, "test_users.csv")
    json_success = export_generator.export_to_json(export_dataset, "test_users.json")
    
    print(f"CSV export successful: {csv_success}")
    print(f"JSON export successful: {json_success}")
    
    # Test scenario creation
    print("\n6. Test Scenario Creation:")
    
    for data_type in [DataType.USER, DataType.PRODUCT, DataType.ORDER]:
        scenarios = create_test_scenarios(data_type)
        print(f"Scenarios for {data_type.value}: {len(scenarios)} created")
        if scenarios:
            print(f"  Sample scenario: {scenarios[0]}")
    
    print("\n7. Reproducibility Test (with seed):")
    
    # Test that same seed produces same results
    seed_config = GenerationConfig(count=3, data_type=DataType.USER, seed=123)
    
    gen1 = TestDataGenerator(seed_config)
    dataset1 = gen1.generate_dataset()
    
    gen2 = TestDataGenerator(seed_config)
    dataset2 = gen2.generate_dataset()
    
    print(f"Dataset 1: {dataset1}")
    print(f"Dataset 2: {dataset2}")
    print(f"Datasets identical: {dataset1 == dataset2}")