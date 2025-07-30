"""
Tests for Exercise 1: String Validation
"""

import pytest
from unittest.mock import patch
import sys
import os

# Import the exercise module
try:
    from _01_string_validation import (
        is_valid_email, is_valid_phone_number, 
        clean_whitespace, count_words
    )
except ImportError:
    # Alternative import method
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '1-basic-exercises'))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "string_validation", 
            os.path.join(os.path.dirname(__file__), '..', '..', '1-basic-exercises', '01_string_validation.py')
        )
        string_validation = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(string_validation)
        
        is_valid_email = string_validation.is_valid_email
        is_valid_phone_number = string_validation.is_valid_phone_number
        clean_whitespace = string_validation.clean_whitespace
        count_words = string_validation.count_words
    except:
        pytest.skip("Could not import string validation module")

class TestEmailValidation:
    """Test email validation functionality."""
    
    @pytest.mark.parametrize("email,expected", [
        ("user@example.com", True),
        ("test.email@domain.org", True),
        ("valid+email@test-domain.net", True),
        ("user123@example123.com", True),
        # Invalid cases
        ("invalid.email", False),
        ("@example.com", False),
        ("user@", False),
        ("user@domain", False),
        ("user with spaces@example.com", False),
        ("user@@example.com", False),
        ("", False),
        ("user@.com", False),
        ("user@domain.", False),
    ])
    def test_is_valid_email(self, email, expected):
        """Test email validation with various inputs."""
        result = is_valid_email(email)
        assert result == expected, f"Email '{email}' validation failed"
    
    def test_is_valid_email_none_input(self):
        """Test email validation with None input."""
        result = is_valid_email(None)
        assert result == False
    
    def test_is_valid_email_empty_string(self):
        """Test email validation with empty string."""
        result = is_valid_email("")
        assert result == False
    
    def test_is_valid_email_whitespace_only(self):
        """Test email validation with whitespace only."""
        result = is_valid_email("   ")
        assert result == False

class TestPhoneValidation:
    """Test phone number validation functionality."""
    
    @pytest.mark.parametrize("phone,expected", [
        ("123-456-7890", True),
        ("(123) 456-7890", True),
        ("1234567890", True),
        ("123 456 7890", True),
        ("(123)456-7890", True),
        # Invalid cases
        ("123-456-78901", False),  # too long
        ("123-456-789", False),    # too short
        ("abc-def-ghij", False),   # non-numeric
        ("12-34-56789", False),    # wrong format
        ("", False),
        ("123", False),
        ("phone", False),
    ])
    def test_is_valid_phone_number(self, phone, expected):
        """Test phone number validation with various inputs."""
        result = is_valid_phone_number(phone)
        assert result == expected, f"Phone '{phone}' validation failed"
    
    def test_is_valid_phone_none_input(self):
        """Test phone validation with None input."""
        result = is_valid_phone_number(None)
        assert result == False

class TestWhitespaceCleaning:
    """Test whitespace cleaning functionality."""
    
    @pytest.mark.parametrize("text,expected", [
        ("  hello   world  ", "hello world"),
        ("normal text", "normal text"),
        ("", ""),
        ("   ", ""),
        ("  multiple    spaces   between   words  ", "multiple spaces between words"),
        ("leading spaces", "leading spaces"),
        ("trailing spaces   ", "trailing spaces"),
        ("\t\n  mixed\t\n  whitespace  \t\n", "mixed whitespace"),
    ])
    def test_clean_whitespace(self, text, expected):
        """Test whitespace cleaning with various inputs."""
        result = clean_whitespace(text)
        assert result == expected, f"Whitespace cleaning failed for '{text}'"
    
    def test_clean_whitespace_none_input(self):
        """Test whitespace cleaning with None input."""
        result = clean_whitespace(None)
        assert result == ""
    
    def test_clean_whitespace_preserves_internal_structure(self):
        """Test that cleaning preserves meaningful internal structure."""
        text = "  word1   word2   word3  "
        result = clean_whitespace(text)
        assert result == "word1 word2 word3"
        assert result.count(" ") == 2  # Should have exactly 2 spaces

class TestWordCounting:
    """Test word counting functionality."""
    
    @pytest.mark.parametrize("text,expected", [
        ("hello world", 2),
        ("single", 1),
        ("", 0),
        ("  spaced   out   text  ", 3),
        ("one two three four five", 5),
        ("word", 1),
        ("  ", 0),
        ("multiple    spaces    between", 3),
        ("punctuation, matters! right?", 3),
    ])
    def test_count_words(self, text, expected):
        """Test word counting with various inputs."""
        result = count_words(text)
        assert result == expected, f"Word count failed for '{text}'"
    
    def test_count_words_none_input(self):
        """Test word counting with None input."""
        result = count_words(None)
        assert result == 0
    
    def test_count_words_special_characters(self):
        """Test word counting with special characters."""
        text = "hello-world test_case name@domain.com"
        result = count_words(text)
        # Depending on implementation, this could be 1, 3, or other values
        assert isinstance(result, int)
        assert result >= 0

class TestIntegrationScenarios:
    """Test integration scenarios combining multiple functions."""
    
    def test_email_cleaning_and_validation(self):
        """Test cleaning email and then validating."""
        dirty_email = "  user@example.com  "
        cleaned = clean_whitespace(dirty_email)
        is_valid = is_valid_email(cleaned)
        assert is_valid == True
    
    def test_phone_cleaning_and_validation(self):
        """Test cleaning phone and then validating."""
        dirty_phone = "  123-456-7890  "
        cleaned = clean_whitespace(dirty_phone)
        is_valid = is_valid_phone_number(cleaned)
        assert is_valid == True
    
    def test_text_processing_pipeline(self):
        """Test a complete text processing pipeline."""
        text = "  hello   world   test@example.com   123-456-7890  "
        cleaned = clean_whitespace(text)
        word_count = count_words(cleaned)
        
        assert cleaned == "hello world test@example.com 123-456-7890"
        assert word_count == 4
        
        # Extract and validate components
        words = cleaned.split()
        email_found = any(is_valid_email(word) for word in words)
        phone_found = any(is_valid_phone_number(word) for word in words)
        
        assert email_found == True
        assert phone_found == True

class TestErrorHandling:
    """Test error handling and edge cases."""
    
    def test_functions_handle_none_gracefully(self):
        """Test all functions handle None input gracefully."""
        assert is_valid_email(None) == False
        assert is_valid_phone_number(None) == False
        assert clean_whitespace(None) == ""
        assert count_words(None) == 0
    
    def test_functions_handle_empty_string(self):
        """Test all functions handle empty string gracefully."""
        assert is_valid_email("") == False
        assert is_valid_phone_number("") == False
        assert clean_whitespace("") == ""
        assert count_words("") == 0
    
    def test_functions_return_correct_types(self):
        """Test functions return correct data types."""
        # Boolean returns
        assert isinstance(is_valid_email("test@example.com"), bool)
        assert isinstance(is_valid_phone_number("123-456-7890"), bool)
        
        # String returns
        assert isinstance(clean_whitespace("test"), str)
        
        # Integer returns
        assert isinstance(count_words("test"), int)

class TestPerformance:
    """Test performance with larger inputs."""
    
    @pytest.mark.slow
    def test_large_text_processing(self):
        """Test functions with large text inputs."""
        large_text = "word " * 10000  # 10,000 words
        
        # Should complete without timeout
        result = count_words(large_text)
        assert result == 10000
        
        cleaned = clean_whitespace(large_text)
        assert len(cleaned) > 0
    
    @pytest.mark.slow
    def test_many_email_validations(self):
        """Test email validation with many inputs."""
        emails = [f"user{i}@example{i}.com" for i in range(1000)]
        
        results = [is_valid_email(email) for email in emails]
        assert all(results)  # All should be valid
    
    def test_edge_case_phone_formats(self):
        """Test phone validation with various edge case formats."""
        edge_cases = [
            "+1-123-456-7890",
            "1.123.456.7890", 
            "123/456/7890",
            "(123)-456-7890",
            "123 - 456 - 7890",
        ]
        
        # Test that function doesn't crash on edge cases
        for phone in edge_cases:
            result = is_valid_phone_number(phone)
            assert isinstance(result, bool)

if __name__ == "__main__":
    pytest.main([__file__])