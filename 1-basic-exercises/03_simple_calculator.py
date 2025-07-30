"""
Exercise 3: Simple Calculator
Testing Focus: Mathematical operations, exception handling, type validation

Task: Create a calculator class with basic operations and proper error handling.
This exercise focuses on testing mathematical functions and edge cases.
"""

class SimpleCalculator:
    """
    A simple calculator with basic arithmetic operations.
    Includes proper error handling for common edge cases.
    """
    
    def __init__(self):
        """Initialize the calculator."""
        self.history = []  # Store calculation history
    
    def add(self, a, b):
        """
        Add two numbers.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Sum of a and b
            
        Raises:
            TypeError: If inputs are not numbers
            
        TODO: Implement this method
        """
        pass
    
    def subtract(self, a, b):
        """
        Subtract b from a.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Difference of a and b
            
        Raises:
            TypeError: If inputs are not numbers
            
        TODO: Implement this method
        """
        pass
    
    def multiply(self, a, b):
        """
        Multiply two numbers.
        
        Args:
            a (int/float): First number
            b (int/float): Second number
            
        Returns:
            int/float: Product of a and b
            
        Raises:
            TypeError: If inputs are not numbers
            
        TODO: Implement this method
        """
        pass
    
    def divide(self, a, b):
        """
        Divide a by b.
        
        Args:
            a (int/float): Dividend
            b (int/float): Divisor
            
        Returns:
            float: Quotient of a and b
            
        Raises:
            TypeError: If inputs are not numbers
            ZeroDivisionError: If b is zero
            
        TODO: Implement this method
        """
        pass
    
    def power(self, base, exponent):
        """
        Raise base to the power of exponent.
        
        Args:
            base (int/float): Base number
            exponent (int/float): Exponent
            
        Returns:
            int/float: Result of base^exponent
            
        Raises:
            TypeError: If inputs are not numbers
            
        TODO: Implement this method
        """
        pass
    
    def sqrt(self, number):
        """
        Calculate square root of a number.
        
        Args:
            number (int/float): Number to find square root of
            
        Returns:
            float: Square root of the number
            
        Raises:
            TypeError: If input is not a number
            ValueError: If number is negative
            
        TODO: Implement this method (hint: use number ** 0.5)
        """
        pass
    
    def add_to_history(self, operation, a, b, result):
        """
        Add calculation to history.
        
        Args:
            operation (str): Operation performed
            a (int/float): First operand
            b (int/float): Second operand (None for unary operations)
            result (int/float): Result of operation
            
        TODO: Implement this method
        """
        pass
    
    def get_history(self):
        """
        Get calculation history.
        
        Returns:
            list: List of calculation records
            
        TODO: Implement this method
        """
        pass
    
    def clear_history(self):
        """
        Clear calculation history.
        
        TODO: Implement this method
        """
        pass

def validate_number_input(value):
    """
    Validate if a value can be converted to a number.
    
    Args:
        value: Value to validate
        
    Returns:
        float: Converted number
        
    Raises:
        TypeError: If value cannot be converted to number
        
    TODO: Implement this function
    """
    pass

def safe_calculation(calc_func, *args):
    """
    Safely perform a calculation with error handling.
    
    Args:
        calc_func: Calculator method to call
        *args: Arguments for the calculator method
        
    Returns:
        dict: Result dictionary with 'success', 'result', and 'error' keys
        
    Example:
        safe_calculation(calc.divide, 10, 2) -> 
        {'success': True, 'result': 5.0, 'error': None}
        
        safe_calculation(calc.divide, 10, 0) -> 
        {'success': False, 'result': None, 'error': 'ZeroDivisionError: division by zero'}
        
    TODO: Implement this function
    """
    pass

# Test cases for manual verification
if __name__ == "__main__":
    print("=== Simple Calculator Exercise ===\n")
    
    calc = SimpleCalculator()
    
    # Test basic operations
    print("Basic Operations Tests:")
    test_operations = [
        ("add", 5, 3),
        ("subtract", 10, 4),
        ("multiply", 6, 7),
        ("divide", 15, 3),
        ("power", 2, 8),
        ("sqrt", 16, None)  # None for second argument in unary operations
    ]
    
    for operation, a, b in test_operations:
        try:
            if operation == "sqrt":
                result = getattr(calc, operation)(a)
                print(f"{operation}({a}) = {result}")
            else:
                result = getattr(calc, operation)(a, b)
                print(f"{operation}({a}, {b}) = {result}")
        except Exception as e:
            print(f"{operation}({a}, {b}) -> Error: {e}")
    
    # Test error cases
    print("\nError Handling Tests:")
    error_tests = [
        ("divide", 10, 0),  # Division by zero
        ("add", "5", 3),    # String input
        ("sqrt", -4, None), # Negative square root
        ("multiply", None, 5) # None input
    ]
    
    for operation, a, b in error_tests:
        try:
            if b is None and operation != "sqrt":
                result = getattr(calc, operation)(a)
            elif operation == "sqrt":
                result = getattr(calc, operation)(a)
            else:
                result = getattr(calc, operation)(a, b)
            print(f"{operation}({a}, {b}) = {result}")
        except Exception as e:
            print(f"{operation}({a}, {b}) -> Expected Error: {type(e).__name__}: {e}")
    
    # Test safe calculation wrapper
    print("\nSafe Calculation Tests:")
    safe_tests = [
        (calc.add, 5, 3),
        (calc.divide, 10, 0),
        (calc.sqrt, -4)
    ]
    
    for calc_func, *args in safe_tests:
        result = safe_calculation(calc_func, *args)
        print(f"Safe call with args {args}: {result}")
    
    # Test history functionality
    print("\nHistory Tests:")
    print(f"Current history: {calc.get_history()}")
    print("Adding some calculations to history...")
    calc.add_to_history("add", 5, 3, 8)
    calc.add_to_history("multiply", 4, 6, 24)
    print(f"History after additions: {calc.get_history()}")
    calc.clear_history()
    print(f"History after clear: {calc.get_history()}")