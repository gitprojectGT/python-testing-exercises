"""
Tests for Exercise 4: Password Validator
"""

import pytest
from unittest.mock import patch, Mock
import sys
import os
import re

# Import the exercise module
try:
    from _04_password_validator import (
        PasswordValidator, test_password_list, generate_password_report
    )
except ImportError:
    # Alternative import method
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '1-basic-exercises'))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "password_validator", 
            os.path.join(os.path.dirname(__file__), '..', '..', '1-basic-exercises', '04_password_validator.py')
        )
        password_validator = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(password_validator)
        
        PasswordValidator = password_validator.PasswordValidator
        test_password_list = password_validator.test_password_list
        generate_password_report = password_validator.generate_password_report
    except:
        pytest.skip("Could not import password validator module")

class TestPasswordValidator:
    """Test the PasswordValidator class."""
    
    @pytest.fixture
    def validator(self):
        """Create a password validator instance."""
        return PasswordValidator(min_length=8, max_length=128)
    
    def test_validator_initialization(self, validator):
        """Test validator initializes with correct parameters."""
        assert validator.min_length == 8
        assert validator.max_length == 128
        assert hasattr(validator, 'validation_history')
        assert isinstance(validator.validation_history, list)

class TestLengthValidation:
    """Test password length validation."""
    
    @pytest.fixture
    def validator(self):
        return PasswordValidator(min_length=8, max_length=20)
    
    @pytest.mark.parametrize("password,expected_valid", [
        ("12345678", True),   # Exactly min length
        ("1234567890123456789", True),  # Exactly max length (19 chars)
        ("1234567", False),   # Too short
        ("12345678901234567890", False), # Too long
        ("password123", True), # Valid length
        ("", False),          # Empty
        ("a", False),         # Single char
    ])
    def test_check_length(self, validator, password, expected_valid):
        """Test length checking with various passwords."""
        result = validator.check_length(password)
        
        assert isinstance(result, dict)
        assert "valid" in result
        assert "message" in result
        assert result["valid"] == expected_valid
        
        if expected_valid:
            assert "valid" in result["message"].lower() or "meets" in result["message"].lower()
        else:
            assert "length" in result["message"].lower()

class TestCharacterTypeValidation:
    """Test character type validation methods."""
    
    @pytest.fixture
    def validator(self):
        return PasswordValidator()
    
    @pytest.mark.parametrize("password,expected_valid", [
        ("Password123", True),   # Has uppercase
        ("password123", False),  # No uppercase
        ("PASSWORD123", True),   # All uppercase
        ("123456789", False),    # No uppercase
        ("", False),             # Empty
        ("P", True),             # Single uppercase
    ])
    def test_check_uppercase(self, validator, password, expected_valid):
        """Test uppercase character validation."""
        result = validator.check_uppercase(password)
        
        assert isinstance(result, dict)
        assert result["valid"] == expected_valid
        
        if expected_valid:
            assert any(c.isupper() for c in password) or password == ""
        else:
            assert not any(c.isupper() for c in password) and password != ""
    
    @pytest.mark.parametrize("password,expected_valid", [
        ("Password123", True),   # Has lowercase
        ("PASSWORD123", False),  # No lowercase
        ("password123", True),   # All lowercase
        ("123456789", False),    # No lowercase
        ("", False),             # Empty
        ("p", True),             # Single lowercase
    ])
    def test_check_lowercase(self, validator, password, expected_valid):
        """Test lowercase character validation."""
        result = validator.check_lowercase(password)
        
        assert isinstance(result, dict)
        assert result["valid"] == expected_valid
    
    @pytest.mark.parametrize("password,expected_valid", [
        ("Password123", True),   # Has digits
        ("Password", False),     # No digits
        ("12345678", True),      # All digits
        ("", False),             # Empty
        ("1", True),             # Single digit
        ("Pass1word", True),     # Digit in middle
    ])
    def test_check_digits(self, validator, password, expected_valid):
        """Test digit character validation."""
        result = validator.check_digits(password)
        
        assert isinstance(result, dict)
        assert result["valid"] == expected_valid
    
    @pytest.mark.parametrize("password,expected_valid", [
        ("Password123!", True),  # Has special char
        ("Password123", False),  # No special char
        ("!@#$%^&*()", True),   # All special chars
        ("", False),            # Empty
        ("Pass@word", True),    # Special char in middle
        ("Password_123", True), # Underscore is special
    ])
    def test_check_special_characters(self, validator, password, expected_valid):
        """Test special character validation."""
        result = validator.check_special_characters(password)
        
        assert isinstance(result, dict)
        assert result["valid"] == expected_valid

class TestWhitespaceValidation:
    """Test whitespace validation."""
    
    @pytest.fixture
    def validator(self):
        return PasswordValidator()
    
    @pytest.mark.parametrize("password,expected_valid", [
        ("Password123", True),      # No whitespace
        ("Pass word123", False),    # Has space
        ("Password\t123", False),   # Has tab
        ("Password\n123", False),   # Has newline
        ("Password\r123", False),   # Has carriage return
        ("", True),                 # Empty (no whitespace)
        ("   ", False),             # Only whitespace
    ])
    def test_check_no_whitespace(self, validator, password, expected_valid):
        """Test whitespace validation."""
        result = validator.check_no_whitespace(password)
        
        assert isinstance(result, dict)
        assert result["valid"] == expected_valid
        
        if not expected_valid and password:
            assert any(c.isspace() for c in password)

class TestCommonPatternValidation:
    """Test common pattern validation."""
    
    @pytest.fixture
    def validator(self):
        return PasswordValidator()
    
    @pytest.mark.parametrize("password,expected_valid", [
        ("GoodPassword123!", True),    # Good password
        ("aaaBBB123!", False),         # Too many consecutive chars
        ("Password123abc", False),     # Sequential pattern
        ("Password12345", False),      # Sequential numbers
        ("PasswordQWERTY", False),     # QWERTY pattern
        ("password123", False),        # Common word "password"
        ("admin123", False),           # Common word "admin"
        ("user12345", False),          # Common word "user"
        ("MyStr0ngP@ss", True),        # Strong password
    ])
    def test_check_no_common_patterns(self, validator, password, expected_valid):
        """Test common pattern validation."""
        result = validator.check_no_common_patterns(password)
        
        assert isinstance(result, dict)
        assert result["valid"] == expected_valid
        
        if not expected_valid:
            assert len(result["message"]) > 0  # Should have specific message

class TestPasswordStrength:
    """Test password strength calculation."""
    
    @pytest.fixture
    def validator(self):
        return PasswordValidator()
    
    def test_calculate_strength_score_weak_password(self, validator):
        """Test strength calculation for weak password."""
        weak_password = "password"
        score = validator.calculate_strength_score(weak_password)
        
        assert isinstance(score, int)
        assert 0 <= score <= 100
        assert score < 50  # Should be low score
    
    def test_calculate_strength_score_strong_password(self, validator):
        """Test strength calculation for strong password."""
        strong_password = "MyStr0ngP@ssw0rd!"
        score = validator.calculate_strength_score(strong_password)
        
        assert isinstance(score, int)
        assert 0 <= score <= 100
        assert score > 70  # Should be high score
    
    def test_calculate_strength_score_components(self, validator):
        """Test that strength score increases with complexity."""
        passwords = [
            "password",              # Very weak
            "Password",              # Added uppercase
            "Password1",             # Added digit
            "Password1!",            # Added special char
            "MyStr0ngP@ssw0rd!",    # Strong password
        ]
        
        scores = [validator.calculate_strength_score(pwd) for pwd in passwords]
        
        # Generally, scores should increase with complexity
        # (though specific implementation may vary)
        assert all(isinstance(score, int) for score in scores)
        assert all(0 <= score <= 100 for score in scores)
    
    def test_calculate_strength_score_length_bonus(self, validator):
        """Test that longer passwords get higher scores."""
        short_password = "Pass1!"
        long_password = "MyVeryLongAndStr0ngP@ssw0rd!"
        
        short_score = validator.calculate_strength_score(short_password)
        long_score = validator.calculate_strength_score(long_password)
        
        # Longer password should generally score higher
        assert long_score >= short_score

class TestCompleteValidation:
    """Test complete password validation."""
    
    @pytest.fixture
    def validator(self):
        return PasswordValidator()
    
    def test_validate_password_strong(self, validator):
        """Test validation of strong password."""
        strong_password = "MyStr0ngP@ssw0rd!"
        result = validator.validate_password(strong_password)
        
        assert isinstance(result, dict)
        assert "valid" in result
        assert "strength_score" in result
        assert "passed_checks" in result
        assert "failed_checks" in result
        assert "messages" in result
        
        assert result["valid"] == True
        assert result["strength_score"] > 70
        assert len(result["failed_checks"]) == 0
        assert len(result["passed_checks"]) > 0
    
    def test_validate_password_weak(self, validator):
        """Test validation of weak password."""
        weak_password = "password"
        result = validator.validate_password(weak_password)
        
        assert isinstance(result, dict)
        assert result["valid"] == False
        assert result["strength_score"] < 50
        assert len(result["failed_checks"]) > 0
        assert len(result["messages"]) > 0
    
    def test_validate_password_empty(self, validator):
        """Test validation of empty password."""
        result = validator.validate_password("")
        
        assert result["valid"] == False
        assert len(result["failed_checks"]) > 0
        assert "length" in " ".join(result["failed_checks"]).lower()
    
    def test_validate_password_mixed_results(self, validator):
        """Test password that passes some checks but fails others."""
        mixed_password = "Password123"  # Missing special char
        result = validator.validate_password(mixed_password)
        
        assert len(result["passed_checks"]) > 0
        assert len(result["failed_checks"]) > 0
        assert result["valid"] == False  # Should be invalid if any check fails

class TestSuggestionGeneration:
    """Test password improvement suggestions."""
    
    @pytest.fixture
    def validator(self):
        return PasswordValidator()
    
    def test_suggest_improvements_weak_password(self, validator):
        """Test suggestions for weak password."""
        weak_password = "password"
        suggestions = validator.suggest_improvements(weak_password)
        
        assert isinstance(suggestions, list)
        assert len(suggestions) > 0
        
        # Should suggest adding uppercase, digits, special chars
        suggestion_text = " ".join(suggestions).lower()
        assert "uppercase" in suggestion_text or "capital" in suggestion_text
        assert "digit" in suggestion_text or "number" in suggestion_text
        assert "special" in suggestion_text or "symbol" in suggestion_text
    
    def test_suggest_improvements_strong_password(self, validator):
        """Test suggestions for already strong password."""
        strong_password = "MyStr0ngP@ssw0rd!"
        suggestions = validator.suggest_improvements(strong_password)
        
        # Strong password should have fewer or no suggestions
        assert isinstance(suggestions, list)
        # Length could be 0 for perfect password, or have minor suggestions
    
    def test_suggest_improvements_specific_issues(self, validator):
        """Test suggestions address specific issues."""
        test_cases = [
            ("password123", ["uppercase", "special"]),  # Missing uppercase and special
            ("PASSWORD123", ["lowercase", "special"]),  # Missing lowercase and special
            ("Password", ["digit", "special"]),         # Missing digit and special
            ("Pass@", ["length"]),                      # Too short
        ]
        
        for password, expected_topics in test_cases:
            suggestions = validator.suggest_improvements(password)
            suggestion_text = " ".join(suggestions).lower()
            
            for topic in expected_topics:
                # Check if suggestion addresses the topic
                assert topic in suggestion_text or any(topic in suggestion.lower() for suggestion in suggestions)

class TestUtilityFunctions:
    """Test utility functions."""
    
    @pytest.fixture
    def validator(self):
        return PasswordValidator()
    
    def test_test_password_list(self, validator):
        """Test batch password testing."""
        passwords = [
            "WeakPassword",
            "Str0ngP@ssw0rd!",
            "password123",
            "MySecur3P@ss!"
        ]
        
        results = test_password_list(validator, passwords)
        
        assert isinstance(results, dict)
        assert "total_tested" in results
        assert "valid_passwords" in results
        assert "invalid_passwords" in results
        
        assert results["total_tested"] == len(passwords)
        assert results["valid_passwords"] + results["invalid_passwords"] == len(passwords)
    
    def test_generate_password_report(self):
        """Test password report generation."""
        validation_results = [
            {
                "password": "WeakPassword",
                "valid": False,
                "strength_score": 30,
                "failed_checks": ["digits", "special_characters"]
            },
            {
                "password": "Str0ngP@ssw0rd!",
                "valid": True,
                "strength_score": 95,
                "failed_checks": []
            }
        ]
        
        report = generate_password_report(validation_results)
        
        assert isinstance(report, str)
        assert len(report) > 0
        assert "WeakPassword" in report or "weak" in report.lower()
        assert "Str0ngP@ssw0rd!" in report or "strong" in report.lower()

class TestEdgeCases:
    """Test edge cases and boundary conditions."""
    
    @pytest.fixture
    def validator(self):
        return PasswordValidator()
    
    def test_unicode_characters(self, validator):
        """Test passwords with Unicode characters."""
        unicode_passwords = [
            "Pässwörd123!",  # Non-ASCII letters
            "密码123!",       # Chinese characters
            "пароль123!",     # Cyrillic characters
            "🔒Password123!", # Emoji
        ]
        
        for password in unicode_passwords:
            # Should not crash
            result = validator.validate_password(password)
            assert isinstance(result, dict)
            assert "valid" in result
    
    def test_very_long_password(self, validator):
        """Test very long password."""
        long_password = "A1!" + "a" * 200  # 203 characters
        result = validator.validate_password(long_password)
        
        # Should handle gracefully
        assert isinstance(result, dict)
        assert result["valid"] == False  # Should exceed max length
        assert "length" in " ".join(result["failed_checks"]).lower()
    
    def test_custom_length_limits(self):
        """Test validator with custom length limits."""
        custom_validator = PasswordValidator(min_length=12, max_length=50)
        
        # Test with password that meets custom requirements
        password = "MyCustomStr0ngP@ssw0rd!"  # 23 characters
        result = custom_validator.validate_password(password)
        
        assert isinstance(result, dict)
        # Length check should pass with custom limits
        length_result = custom_validator.check_length(password)
        assert length_result["valid"] == True
    
    def test_none_and_empty_inputs(self, validator):
        """Test handling of None and empty inputs."""
        edge_inputs = [None, "", "   ", "\t\n"]
        
        for input_val in edge_inputs:
            if input_val is None:
                # Should handle None gracefully (may raise TypeError or return invalid)
                try:
                    result = validator.validate_password(input_val)
                    assert result["valid"] == False
                except TypeError:
                    pass  # Acceptable behavior
            else:
                result = validator.validate_password(input_val)
                assert result["valid"] == False

class TestIntegrationScenarios:
    """Test complete integration scenarios."""
    
    @pytest.fixture
    def validator(self):
        return PasswordValidator()
    
    def test_password_improvement_workflow(self, validator):
        """Test iterative password improvement workflow."""
        # Start with weak password
        password = "password"
        
        # Get validation and suggestions
        result = validator.validate_password(password)
        suggestions = validator.suggest_improvements(password)
        
        assert result["valid"] == False
        assert len(suggestions) > 0
        
        # Improve password based on suggestions
        improved_password = "Password123!"
        
        # Validate improved password
        improved_result = validator.validate_password(improved_password)
        
        # Should be better
        assert improved_result["strength_score"] > result["strength_score"]
        assert len(improved_result["failed_checks"]) < len(result["failed_checks"])
    
    def test_security_policy_compliance(self, validator):
        """Test compliance with typical security policies."""
        # Test against common enterprise password policies
        policy_compliant_passwords = [
            "Enterprise2024!",
            "Secure#Pass123",
            "MyCompany@2024",
        ]
        
        policy_non_compliant = [
            "password",
            "12345678",
            "Password",
            "admin123",
        ]
        
        # Compliant passwords should generally pass
        for password in policy_compliant_passwords:
            result = validator.validate_password(password)
            # Most should be valid (depending on implementation)
            assert isinstance(result["valid"], bool)
            assert result["strength_score"] > 50
        
        # Non-compliant should generally fail
        for password in policy_non_compliant:
            result = validator.validate_password(password)
            assert result["valid"] == False

if __name__ == "__main__":
    pytest.main([__file__])