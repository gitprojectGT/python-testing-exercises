"""
Tests for Exercise 3: Simple Calculator
"""

import pytest
from unittest.mock import patch, Mock
import sys
import os
import math

# Import the exercise module
try:
    from _03_simple_calculator import (
        SimpleCalculator, validate_number_input, safe_calculation
    )
except ImportError:
    # Alternative import method
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '1-basic-exercises'))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "simple_calculator", 
            os.path.join(os.path.dirname(__file__), '..', '..', '1-basic-exercises', '03_simple_calculator.py')
        )
        simple_calculator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(simple_calculator)
        
        SimpleCalculator = simple_calculator.SimpleCalculator
        validate_number_input = simple_calculator.validate_number_input
        safe_calculation = simple_calculator.safe_calculation
    except:
        pytest.skip("Could not import simple calculator module")

class TestSimpleCalculator:
    """Test the SimpleCalculator class."""
    
    @pytest.fixture
    def calculator(self):
        """Create a calculator instance for testing."""
        return SimpleCalculator()
    
    def test_calculator_initialization(self, calculator):
        """Test calculator initializes correctly."""
        assert calculator is not None
        assert hasattr(calculator, 'history')
        assert isinstance(calculator.history, list)
        assert len(calculator.history) == 0

class TestBasicArithmetic:
    """Test basic arithmetic operations."""
    
    @pytest.fixture
    def calculator(self):
        return SimpleCalculator()
    
    @pytest.mark.parametrize("a,b,expected", [
        (2, 3, 5),
        (0, 0, 0),
        (-1, 1, 0),
        (10, -5, 5),
        (0.5, 0.5, 1.0),
        (100, 200, 300),
    ])
    def test_add(self, calculator, a, b, expected):
        """Test addition with various inputs."""
        result = calculator.add(a, b)
        assert result == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (5, 3, 2),
        (0, 0, 0),
        (1, -1, 2),
        (-5, -3, -2),
        (10.5, 0.5, 10.0),
        (100, 200, -100),
    ])
    def test_subtract(self, calculator, a, b, expected):
        """Test subtraction with various inputs."""
        result = calculator.subtract(a, b)
        assert result == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (3, 4, 12),
        (0, 5, 0),
        (5, 0, 0),
        (-2, 3, -6),
        (-2, -3, 6),
        (0.5, 4, 2.0),
        (2.5, 2, 5.0),
    ])
    def test_multiply(self, calculator, a, b, expected):
        """Test multiplication with various inputs."""
        result = calculator.multiply(a, b)
        assert result == expected
    
    @pytest.mark.parametrize("a,b,expected", [
        (6, 2, 3.0),
        (10, 4, 2.5),
        (0, 5, 0.0),
        (-6, 2, -3.0),
        (-6, -2, 3.0),
        (7, 2, 3.5),
    ])
    def test_divide(self, calculator, a, b, expected):
        """Test division with various inputs."""
        result = calculator.divide(a, b)
        assert result == expected
    
    def test_divide_by_zero(self, calculator):
        """Test division by zero raises appropriate error."""
        with pytest.raises(ZeroDivisionError):
            calculator.divide(5, 0)
    
    @pytest.mark.parametrize("base,exponent,expected", [
        (2, 3, 8),
        (5, 0, 1),
        (10, 2, 100),
        (2, -1, 0.5),
        (4, 0.5, 2.0),
        (0, 5, 0),
        (1, 100, 1),
    ])
    def test_power(self, calculator, base, exponent, expected):
        """Test power operation with various inputs."""
        result = calculator.power(base, exponent)
        assert result == expected
    
    @pytest.mark.parametrize("number,expected", [
        (4, 2.0),
        (9, 3.0),
        (16, 4.0),
        (25, 5.0),
        (0, 0.0),
        (1, 1.0),
        (0.25, 0.5),
    ])
    def test_sqrt(self, calculator, number, expected):
        """Test square root with various inputs."""
        result = calculator.sqrt(number)
        assert abs(result - expected) < 1e-10  # Account for floating point precision
    
    def test_sqrt_negative(self, calculator):
        """Test square root of negative number raises error."""
        with pytest.raises(ValueError):
            calculator.sqrt(-4)

class TestErrorHandling:
    """Test error handling for invalid inputs."""
    
    @pytest.fixture
    def calculator(self):
        return SimpleCalculator()
    
    def test_add_invalid_types(self, calculator):
        """Test addition with invalid types."""
        with pytest.raises(TypeError):
            calculator.add("5", 3)
        
        with pytest.raises(TypeError):
            calculator.add(5, None)
    
    def test_subtract_invalid_types(self, calculator):
        """Test subtraction with invalid types."""
        with pytest.raises(TypeError):
            calculator.subtract(5, "3")
        
        with pytest.raises(TypeError):
            calculator.subtract(None, 5)
    
    def test_multiply_invalid_types(self, calculator):
        """Test multiplication with invalid types."""
        with pytest.raises(TypeError):
            calculator.multiply("5", 3)
        
        with pytest.raises(TypeError):
            calculator.multiply(5, [])
    
    def test_divide_invalid_types(self, calculator):
        """Test division with invalid types."""
        with pytest.raises(TypeError):
            calculator.divide("10", 2)
        
        with pytest.raises(TypeError):
            calculator.divide(10, "2")
    
    def test_power_invalid_types(self, calculator):
        """Test power with invalid types."""
        with pytest.raises(TypeError):
            calculator.power("2", 3)
        
        with pytest.raises(TypeError):
            calculator.power(2, "3")
    
    def test_sqrt_invalid_types(self, calculator):
        """Test square root with invalid types."""
        with pytest.raises(TypeError):
            calculator.sqrt("4")
        
        with pytest.raises(TypeError):
            calculator.sqrt(None)

class TestHistoryManagement:
    """Test calculation history functionality."""
    
    @pytest.fixture
    def calculator(self):
        return SimpleCalculator()
    
    def test_add_to_history(self, calculator):
        """Test adding calculations to history."""
        calculator.add_to_history("add", 2, 3, 5)
        
        history = calculator.get_history()
        assert len(history) == 1
        assert history[0]["operation"] == "add"
        assert history[0]["operand1"] == 2
        assert history[0]["operand2"] == 3
        assert history[0]["result"] == 5
    
    def test_history_accumulation(self, calculator):
        """Test that history accumulates multiple operations."""
        calculator.add_to_history("add", 2, 3, 5)
        calculator.add_to_history("multiply", 4, 5, 20)
        calculator.add_to_history("divide", 10, 2, 5)
        
        history = calculator.get_history()
        assert len(history) == 3
        
        # Check operations are in order
        assert history[0]["operation"] == "add"
        assert history[1]["operation"] == "multiply"
        assert history[2]["operation"] == "divide"
    
    def test_clear_history(self, calculator):
        """Test clearing calculation history."""
        # Add some history
        calculator.add_to_history("add", 2, 3, 5)
        calculator.add_to_history("subtract", 10, 4, 6)
        
        assert len(calculator.get_history()) == 2
        
        # Clear history
        calculator.clear_history()
        
        assert len(calculator.get_history()) == 0
    
    def test_unary_operation_history(self, calculator):
        """Test history for unary operations like sqrt."""
        calculator.add_to_history("sqrt", 16, None, 4)
        
        history = calculator.get_history()
        assert len(history) == 1
        assert history[0]["operation"] == "sqrt"
        assert history[0]["operand1"] == 16
        assert history[0]["operand2"] is None
        assert history[0]["result"] == 4

class TestValidateNumberInput:
    """Test the validate_number_input helper function."""
    
    @pytest.mark.parametrize("value,expected", [
        (5, 5.0),
        (5.5, 5.5),
        ("5", 5.0),
        ("5.5", 5.5),
        ("-3", -3.0),
        ("0", 0.0),
    ])
    def test_validate_number_input_valid(self, value, expected):
        """Test validation with valid numeric inputs."""
        result = validate_number_input(value)
        assert result == expected
    
    @pytest.mark.parametrize("value", [
        "abc",
        "not_a_number",
        "",
        None,
        [],
        {},
        "5.5.5",
    ])
    def test_validate_number_input_invalid(self, value):
        """Test validation with invalid inputs."""
        with pytest.raises(TypeError):
            validate_number_input(value)

class TestSafeCalculation:
    """Test the safe_calculation wrapper function."""
    
    @pytest.fixture
    def calculator(self):
        return SimpleCalculator()
    
    def test_safe_calculation_success(self, calculator):
        """Test safe calculation with successful operation."""
        result = safe_calculation(calculator.add, 2, 3)
        
        assert result["success"] == True
        assert result["result"] == 5
        assert result["error"] is None
    
    def test_safe_calculation_division_by_zero(self, calculator):
        """Test safe calculation with division by zero."""
        result = safe_calculation(calculator.divide, 10, 0)
        
        assert result["success"] == False
        assert result["result"] is None
        assert "ZeroDivisionError" in result["error"]
    
    def test_safe_calculation_type_error(self, calculator):
        """Test safe calculation with type error."""
        result = safe_calculation(calculator.add, "5", 3)
        
        assert result["success"] == False
        assert result["result"] is None
        assert "TypeError" in result["error"]
    
    def test_safe_calculation_sqrt_negative(self, calculator):
        """Test safe calculation with square root of negative."""
        result = safe_calculation(calculator.sqrt, -4)
        
        assert result["success"] == False
        assert result["result"] is None
        assert "ValueError" in result["error"]

class TestIntegrationScenarios:
    """Test complete calculation scenarios."""
    
    @pytest.fixture
    def calculator(self):
        return SimpleCalculator()
    
    def test_complex_calculation_sequence(self, calculator):
        """Test a sequence of related calculations."""
        # Calculate (2 + 3) * 4 / 2 = 10
        step1 = calculator.add(2, 3)      # 5
        step2 = calculator.multiply(step1, 4)  # 20
        step3 = calculator.divide(step2, 2)    # 10
        
        assert step1 == 5
        assert step2 == 20
        assert step3 == 10.0
    
    def test_calculator_with_history_tracking(self, calculator):
        """Test calculations while tracking history."""
        # Perform operations and track them
        result1 = calculator.add(10, 5)
        calculator.add_to_history("add", 10, 5, result1)
        
        result2 = calculator.sqrt(result1)
        calculator.add_to_history("sqrt", result1, None, result2)
        
        result3 = calculator.power(result2, 2)
        calculator.add_to_history("power", result2, 2, result3)
        
        # Check results
        assert result1 == 15
        assert abs(result2 - math.sqrt(15)) < 1e-10
        assert abs(result3 - 15) < 1e-10  # Should be back to original
        
        # Check history
        history = calculator.get_history()
        assert len(history) == 3
        assert history[0]["operation"] == "add"
        assert history[1]["operation"] == "sqrt"
        assert history[2]["operation"] == "power"
    
    def test_error_recovery_scenario(self, calculator):
        """Test recovering from errors and continuing calculations."""
        # Start with successful calculation
        result1 = calculator.add(5, 3)  # 8
        assert result1 == 8
        
        # Attempt invalid operation
        with pytest.raises(ZeroDivisionError):
            calculator.divide(result1, 0)
        
        # Continue with valid operations
        result2 = calculator.multiply(result1, 2)  # 16
        result3 = calculator.sqrt(result2)          # 4
        
        assert result2 == 16
        assert result3 == 4.0

class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    @pytest.fixture
    def calculator(self):
        return SimpleCalculator()
    
    def test_very_large_numbers(self, calculator):
        """Test operations with very large numbers."""
        large_num = 10**15
        result = calculator.add(large_num, 1)
        assert result == large_num + 1
    
    def test_very_small_numbers(self, calculator):
        """Test operations with very small numbers."""
        small_num = 1e-15
        result = calculator.multiply(small_num, 2)
        assert abs(result - 2e-15) < 1e-20
    
    def test_precision_edge_cases(self, calculator):
        """Test floating point precision edge cases."""
        # Test that can reproduce common floating point issues
        result = calculator.add(0.1, 0.2)
        # Due to floating point precision, this might not be exactly 0.3
        assert abs(result - 0.3) < 1e-10
    
    def test_zero_operations(self, calculator):
        """Test operations involving zero."""
        assert calculator.add(0, 0) == 0
        assert calculator.subtract(0, 0) == 0
        assert calculator.multiply(0, 100) == 0
        assert calculator.multiply(100, 0) == 0
        assert calculator.divide(0, 5) == 0.0
        assert calculator.power(0, 5) == 0
        assert calculator.sqrt(0) == 0.0

class TestPerformance:
    """Test performance characteristics."""
    
    @pytest.fixture
    def calculator(self):
        return SimpleCalculator()
    
    @pytest.mark.slow
    def test_many_operations_performance(self, calculator):
        """Test performance with many operations."""
        # Perform many operations quickly
        for i in range(1000):
            result = calculator.add(i, i + 1)
            assert result == 2 * i + 1
    
    @pytest.mark.slow
    def test_large_history_performance(self, calculator):
        """Test performance with large history."""
        # Add many items to history
        for i in range(1000):
            calculator.add_to_history("add", i, i + 1, 2 * i + 1)
        
        # Getting history should still be fast
        history = calculator.get_history()
        assert len(history) == 1000
        
        # Clearing should be fast
        calculator.clear_history()
        assert len(calculator.get_history()) == 0

if __name__ == "__main__":
    pytest.main([__file__])