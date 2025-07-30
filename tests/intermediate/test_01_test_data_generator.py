"""
Tests for Exercise 1: Test Data Generator (Intermediate)
"""

import pytest
from unittest.mock import patch, Mock
import sys
import os
import json
from datetime import datetime

# Import the exercise module
try:
    from _01_test_data_generator import (
        GenerationConfig, TestDataGenerator, DataType,
        validate_generated_data, create_test_scenarios
    )
except ImportError:
    # Alternative import method
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '2-intermediate-exercises'))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "test_data_generator", 
            os.path.join(os.path.dirname(__file__), '..', '..', '2-intermediate-exercises', '01_test_data_generator.py')
        )
        test_data_generator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(test_data_generator)
        
        GenerationConfig = test_data_generator.GenerationConfig
        TestDataGenerator = test_data_generator.TestDataGenerator
        DataType = test_data_generator.DataType
        validate_generated_data = test_data_generator.validate_generated_data
        create_test_scenarios = test_data_generator.create_test_scenarios
    except:
        pytest.skip("Could not import test data generator module")

class TestGenerationConfig:
    """Test the GenerationConfig dataclass."""
    
    def test_default_config(self):
        """Test default configuration values."""
        config = GenerationConfig()
        
        assert config.count == 10
        assert config.data_type == DataType.USER
        assert config.include_invalid == False
        assert config.seed is None
        assert config.custom_fields is None
    
    def test_custom_config(self):
        """Test custom configuration values."""
        config = GenerationConfig(
            count=50,
            data_type=DataType.PRODUCT,
            include_invalid=True,
            seed=12345,
            custom_fields={"extra_field": "value"}
        )
        
        assert config.count == 50
        assert config.data_type == DataType.PRODUCT
        assert config.include_invalid == True
        assert config.seed == 12345
        assert config.custom_fields["extra_field"] == "value"

class TestTestDataGenerator:
    """Test the TestDataGenerator class."""
    
    @pytest.fixture
    def generator(self):
        """Create a test data generator instance."""
        config = GenerationConfig(count=5, seed=42)
        return TestDataGenerator(config)
    
    def test_generator_initialization(self, generator):
        """Test generator initializes correctly."""
        assert generator is not None
        assert generator.config is not None
        assert generator.config.count == 5
        assert generator.config.seed == 42
        
        # Check that sample data pools exist
        assert hasattr(generator, 'first_names')
        assert hasattr(generator, 'last_names')
        assert hasattr(generator, 'domains')
        assert len(generator.first_names) > 0
        assert len(generator.last_names) > 0
        assert len(generator.domains) > 0

class TestRandomStringGeneration:
    """Test random string generation."""
    
    @pytest.fixture
    def generator(self):
        return TestDataGenerator(GenerationConfig(seed=42))
    
    def test_generate_random_string_basic(self, generator):
        """Test basic random string generation."""
        result = generator.generate_random_string(10)
        
        assert isinstance(result, str)
        assert len(result) == 10
        assert result.isalnum() or any(c in result for c in generator.charset if c.isalnum())
    
    def test_generate_random_string_with_special_chars(self, generator):
        """Test random string generation with special characters."""
        result = generator.generate_random_string(15, include_special=True)
        
        assert isinstance(result, str)
        assert len(result) == 15
    
    def test_generate_random_string_reproducible(self, generator):
        """Test that random string generation is reproducible with seed."""
        result1 = generator.generate_random_string(10)
        
        # Create new generator with same seed
        generator2 = TestDataGenerator(GenerationConfig(seed=42))
        result2 = generator2.generate_random_string(10)
        
        assert result1 == result2
    
    @pytest.mark.parametrize("length", [1, 5, 10, 25, 100])
    def test_generate_random_string_lengths(self, generator, length):
        """Test random string generation with various lengths."""
        result = generator.generate_random_string(length)
        
        assert len(result) == length
        assert isinstance(result, str)

class TestEmailGeneration:
    """Test email generation."""
    
    @pytest.fixture
    def generator(self):
        return TestDataGenerator(GenerationConfig(seed=42))
    
    def test_generate_email_basic(self, generator):
        """Test basic email generation."""
        email = generator.generate_email()
        
        assert isinstance(email, str)
        assert "@" in email
        assert "." in email.split("@")[1]  # Domain has dot
        
        parts = email.split("@")
        assert len(parts) == 2
        assert len(parts[0]) > 0  # Local part not empty
        assert len(parts[1]) > 0  # Domain part not empty
    
    def test_generate_email_valid_format(self, generator):
        """Test that generated emails have valid format."""
        for _ in range(10):
            email = generator.generate_email(valid=True)
            
            # Basic email validation
            assert email.count("@") == 1
            local, domain = email.split("@")
            assert len(local) > 0
            assert "." in domain
            assert not email.startswith(".")
            assert not email.endswith(".")
    
    def test_generate_email_invalid_format(self, generator):
        """Test generation of invalid emails."""
        invalid_email = generator.generate_email(valid=False)
        
        assert isinstance(invalid_email, str)
        # Should be intentionally invalid in some way
        # (exact validation depends on implementation)

class TestPhoneGeneration:
    """Test phone number generation."""
    
    @pytest.fixture
    def generator(self):
        return TestDataGenerator(GenerationConfig(seed=42))
    
    def test_generate_phone_us_format(self, generator):
        """Test US format phone generation."""
        phone = generator.generate_phone_number("us")
        
        assert isinstance(phone, str)
        # Should contain digits and formatting characters
        digit_count = sum(1 for c in phone if c.isdigit())
        assert digit_count == 10  # US phone numbers have 10 digits
    
    def test_generate_phone_international_format(self, generator):
        """Test international format phone generation."""
        phone = generator.generate_phone_number("international")
        
        assert isinstance(phone, str)
        assert len(phone) > 0
    
    def test_generate_phone_digits_only(self, generator):
        """Test digits-only phone generation."""
        phone = generator.generate_phone_number("digits_only")
        
        assert isinstance(phone, str)
        assert phone.isdigit()
        assert len(phone) == 10

class TestDateGeneration:
    """Test date generation."""
    
    @pytest.fixture
    def generator(self):
        return TestDataGenerator(GenerationConfig(seed=42))
    
    def test_generate_date_basic(self, generator):
        """Test basic date generation."""
        date_str = generator.generate_date()
        
        assert isinstance(date_str, str)
        
        # Try to parse the date
        try:
            parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
            assert isinstance(parsed_date, datetime)
        except ValueError:
            pytest.fail(f"Generated date '{date_str}' is not in YYYY-MM-DD format")
    
    def test_generate_date_within_range(self, generator):
        """Test date generation within specified range."""
        start_date = "2020-01-01"
        end_date = "2020-12-31"
        
        date_str = generator.generate_date(start_date, end_date)
        
        parsed_date = datetime.strptime(date_str, "%Y-%m-%d")
        start_dt = datetime.strptime(start_date, "%Y-%m-%d")
        end_dt = datetime.strptime(end_date, "%Y-%m-%d")
        
        assert start_dt <= parsed_date <= end_dt
    
    def test_generate_multiple_dates_unique(self, generator):
        """Test that multiple date generations produce variety."""
        dates = [generator.generate_date() for _ in range(20)]
        
        # Should have some variety (not all identical)
        unique_dates = set(dates)
        assert len(unique_dates) > 1  # Should have at least some variety

class TestUserDataGeneration:
    """Test user data generation."""
    
    @pytest.fixture
    def generator(self):
        return TestDataGenerator(GenerationConfig(seed=42))
    
    def test_generate_user_data_structure(self, generator):
        """Test user data has correct structure."""
        user = generator.generate_user_data()
        
        assert isinstance(user, dict)
        
        # Check required fields exist
        required_fields = ["id", "first_name", "last_name", "email", "phone", "date_of_birth", "is_active"]
        for field in required_fields:
            assert field in user, f"Missing required field: {field}"
    
    def test_generate_user_data_types(self, generator):
        """Test user data field types."""
        user = generator.generate_user_data()
        
        assert isinstance(user["id"], int)
        assert isinstance(user["first_name"], str)
        assert isinstance(user["last_name"], str)
        assert isinstance(user["email"], str)
        assert isinstance(user["phone"], str)
        assert isinstance(user["date_of_birth"], str)
        assert isinstance(user["is_active"], bool)
    
    def test_generate_user_data_valid_email(self, generator):
        """Test that generated user has valid email."""
        user = generator.generate_user_data()
        
        email = user["email"]
        assert "@" in email
        assert "." in email.split("@")[1]
    
    def test_generate_user_data_with_invalid(self, generator):
        """Test user data generation with invalid flag."""
        valid_user = generator.generate_user_data(include_invalid=False)
        invalid_user = generator.generate_user_data(include_invalid=True)
        
        # Both should be dictionaries with same structure
        assert isinstance(valid_user, dict)
        assert isinstance(invalid_user, dict)
        
        # Invalid user might have some invalid data
        # (specific validation depends on implementation)

class TestProductDataGeneration:
    """Test product data generation."""
    
    @pytest.fixture
    def generator(self):
        return TestDataGenerator(GenerationConfig(seed=42))
    
    def test_generate_product_data_structure(self, generator):
        """Test product data has correct structure."""
        product = generator.generate_product_data()
        
        assert isinstance(product, dict)
        
        # Check for typical product fields
        expected_fields = ["id", "name", "price", "category", "in_stock"]
        for field in expected_fields:
            if field in product:  # Some fields might be optional
                assert product[field] is not None
    
    def test_generate_product_data_types(self, generator):
        """Test product data field types."""
        product = generator.generate_product_data()
        
        if "id" in product:
            assert isinstance(product["id"], int)
        if "name" in product:
            assert isinstance(product["name"], str)
        if "price" in product:
            assert isinstance(product["price"], (int, float))
        if "category" in product:
            assert isinstance(product["category"], str)
        if "in_stock" in product:
            assert isinstance(product["in_stock"], bool)

class TestDatasetGeneration:
    """Test complete dataset generation."""
    
    @pytest.fixture
    def generator(self):
        return TestDataGenerator(GenerationConfig(count=10, seed=42))
    
    def test_generate_dataset_basic(self, generator):
        """Test basic dataset generation."""
        dataset = generator.generate_dataset()
        
        assert isinstance(dataset, list)
        assert len(dataset) == 10  # Should match config count
        
        # All items should be dictionaries
        for item in dataset:
            assert isinstance(item, dict)
    
    def test_generate_dataset_user_type(self):
        """Test dataset generation for user type."""
        config = GenerationConfig(count=5, data_type=DataType.USER, seed=42)
        generator = TestDataGenerator(config)
        
        dataset = generator.generate_dataset()
        
        assert len(dataset) == 5
        
        # Check that all items look like user data
        for user in dataset:
            assert "first_name" in user or "name" in user
            assert "email" in user
    
    def test_generate_dataset_product_type(self):
        """Test dataset generation for product type."""
        config = GenerationConfig(count=3, data_type=DataType.PRODUCT, seed=42)
        generator = TestDataGenerator(config)
        
        dataset = generator.generate_dataset()
        
        assert len(dataset) == 3
        
        # Check that all items look like product data
        for product in dataset:
            assert "name" in product
            assert "price" in product or "cost" in product
    
    def test_generate_dataset_reproducible(self):
        """Test that dataset generation is reproducible."""
        config = GenerationConfig(count=5, seed=123)
        
        generator1 = TestDataGenerator(config)
        dataset1 = generator1.generate_dataset()
        
        generator2 = TestDataGenerator(config)
        dataset2 = generator2.generate_dataset()
        
        assert dataset1 == dataset2

class TestBoundaryValues:
    """Test boundary value generation."""
    
    @pytest.fixture
    def generator(self):
        return TestDataGenerator(GenerationConfig(seed=42))
    
    def test_generate_boundary_values_string(self, generator):
        """Test boundary values for string type."""
        boundaries = generator.generate_boundary_values("string", "username")
        
        assert isinstance(boundaries, list)
        assert len(boundaries) > 0
        
        # Should include edge cases like empty string, very long string, etc.
        boundary_lengths = [len(str(b)) for b in boundaries]
        assert min(boundary_lengths) == 0 or min(boundary_lengths) == 1  # Very short
        assert max(boundary_lengths) > 10  # Some longer values
    
    def test_generate_boundary_values_integer(self, generator):
        """Test boundary values for integer type."""
        boundaries = generator.generate_boundary_values("integer", "age")
        
        assert isinstance(boundaries, list)
        assert len(boundaries) > 0
        
        # Should include edge cases
        assert 0 in boundaries or 1 in boundaries  # Lower boundary
        assert any(b > 100 for b in boundaries)    # Higher values
        assert any(b < 0 for b in boundaries)      # Negative values
    
    def test_generate_boundary_values_email(self, generator):
        """Test boundary values for email type."""
        boundaries = generator.generate_boundary_values("email", "email")
        
        assert isinstance(boundaries, list)
        assert len(boundaries) > 0
        
        # Should include valid and invalid email examples
        has_valid_email = any("@" in str(b) and "." in str(b) for b in boundaries)
        has_invalid_email = any("@" not in str(b) or "." not in str(b) for b in boundaries)
        
        assert has_valid_email or has_invalid_email  # Should have some variety

class TestExportFunctionality:
    """Test data export functionality."""
    
    @pytest.fixture
    def generator(self):
        config = GenerationConfig(count=3, seed=42)
        generator = TestDataGenerator(config)
        generator.generate_dataset()  # Generate some data first
        return generator
    
    def test_export_to_csv(self, generator):
        """Test CSV export."""
        dataset = [
            {"name": "John", "age": 30, "city": "NY"},
            {"name": "Jane", "age": 25, "city": "LA"}
        ]
        
        success = generator.export_to_csv(dataset, "test_export.csv")
        
        assert isinstance(success, bool)
        
        if success:
            # Check file was created
            assert os.path.exists("test_export.csv")
            
            # Clean up
            try:
                os.remove("test_export.csv")
            except FileNotFoundError:
                pass
    
    def test_export_to_json(self, generator):
        """Test JSON export."""
        dataset = [
            {"name": "John", "age": 30, "city": "NY"},
            {"name": "Jane", "age": 25, "city": "LA"}
        ]
        
        success = generator.export_to_json(dataset, "test_export.json")
        
        assert isinstance(success, bool)
        
        if success:
            # Check file was created
            assert os.path.exists("test_export.json")
            
            # Verify it's valid JSON
            with open("test_export.json", 'r') as f:
                loaded_data = json.load(f)
                assert isinstance(loaded_data, list)
                assert len(loaded_data) == 2
            
            # Clean up
            try:
                os.remove("test_export.json")
            except FileNotFoundError:
                pass

class TestValidationFunctions:
    """Test data validation functions."""
    
    def test_validate_generated_data_user(self):
        """Test validation of user data."""
        user_dataset = [
            {"id": 1, "name": "John Doe", "email": "john@example.com", "age": 30},
            {"id": 2, "name": "Jane Smith", "email": "jane@example.com", "age": 25},
        ]
        
        validation_result = validate_generated_data(user_dataset, DataType.USER)
        
        assert isinstance(validation_result, dict)
        assert "valid_records" in validation_result or "total_records" in validation_result
        assert "issues" in validation_result or "errors" in validation_result
    
    def test_create_test_scenarios(self):
        """Test test scenario creation."""
        scenarios = create_test_scenarios(DataType.USER)
        
        assert isinstance(scenarios, list)
        assert len(scenarios) > 0
        
        # Each scenario should be a GenerationConfig
        for scenario in scenarios:
            assert isinstance(scenario, GenerationConfig)
            assert scenario.data_type == DataType.USER

class TestErrorHandling:
    """Test error handling and edge cases."""
    
    def test_invalid_data_type(self):
        """Test handling of invalid data type."""
        config = GenerationConfig(data_type="INVALID")
        
        try:
            generator = TestDataGenerator(config)
            # Should either handle gracefully or raise appropriate error
            dataset = generator.generate_dataset()
            assert isinstance(dataset, list)  # Should return something reasonable
        except (ValueError, AttributeError):
            pass  # Acceptable to raise error for invalid type
    
    def test_negative_count(self):
        """Test handling of negative count."""
        config = GenerationConfig(count=-5)
        generator = TestDataGenerator(config)
        
        dataset = generator.generate_dataset()
        
        # Should handle gracefully (return empty list or positive count)
        assert isinstance(dataset, list)
        assert len(dataset) >= 0
    
    def test_zero_count(self):
        """Test handling of zero count."""
        config = GenerationConfig(count=0)
        generator = TestDataGenerator(config)
        
        dataset = generator.generate_dataset()
        
        assert isinstance(dataset, list)
        assert len(dataset) == 0
    
    def test_very_large_count(self):
        """Test handling of very large count."""
        config = GenerationConfig(count=10000)  # Large but reasonable
        generator = TestDataGenerator(config)
        
        # Should handle without crashing (might be slow)
        dataset = generator.generate_dataset()
        
        assert isinstance(dataset, list)
        # Don't require exact count for very large numbers
        assert len(dataset) > 0

class TestPerformance:
    """Test performance characteristics."""
    
    @pytest.mark.slow
    def test_large_dataset_generation(self):
        """Test generation of large datasets."""
        config = GenerationConfig(count=1000, seed=42)
        generator = TestDataGenerator(config)
        
        dataset = generator.generate_dataset()
        
        assert len(dataset) == 1000
        assert all(isinstance(item, dict) for item in dataset)
    
    @pytest.mark.slow
    def test_multiple_data_types_performance(self):
        """Test performance across different data types."""
        data_types = [DataType.USER, DataType.PRODUCT, DataType.ORDER]
        
        for data_type in data_types:
            config = GenerationConfig(count=100, data_type=data_type, seed=42)
            generator = TestDataGenerator(config)
            
            dataset = generator.generate_dataset()
            
            assert len(dataset) == 100
            assert all(isinstance(item, dict) for item in dataset)

class TestIntegrationScenarios:
    """Test complete integration scenarios."""
    
    def test_end_to_end_data_generation_workflow(self):
        """Test complete data generation workflow."""
        # Create configuration
        config = GenerationConfig(
            count=10,
            data_type=DataType.USER,
            include_invalid=False,
            seed=42
        )
        
        # Generate data
        generator = TestDataGenerator(config)
        dataset = generator.generate_dataset()
        
        # Validate data
        validation_result = validate_generated_data(dataset, DataType.USER)
        
        # Export data
        csv_success = generator.export_to_csv(dataset, "integration_test.csv")
        json_success = generator.export_to_json(dataset, "integration_test.json")
        
        # Assertions
        assert len(dataset) == 10
        assert isinstance(validation_result, dict)
        assert isinstance(csv_success, bool)
        assert isinstance(json_success, bool)
        
        # Cleanup
        for filename in ["integration_test.csv", "integration_test.json"]:
            try:
                os.remove(filename)
            except FileNotFoundError:
                pass
    
    def test_multiple_scenarios_execution(self):
        """Test executing multiple test scenarios."""
        scenarios = create_test_scenarios(DataType.USER)
        
        results = []
        for scenario in scenarios[:3]:  # Test first 3 scenarios
            generator = TestDataGenerator(scenario)
            dataset = generator.generate_dataset()
            validation = validate_generated_data(dataset, scenario.data_type)
            
            results.append({
                "scenario": scenario,
                "dataset_size": len(dataset),
                "validation": validation
            })
        
        assert len(results) == 3
        assert all(r["dataset_size"] > 0 for r in results)

if __name__ == "__main__":
    pytest.main([__file__])