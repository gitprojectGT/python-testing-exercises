"""
Exercise 1: String Validation
Testing Focus: Input validation, boundary conditions, string operations

Task: Create functions to validate different types of string inputs.
This simulates common validation scenarios in software testing.
"""

def is_valid_email(email):
    """
    Validate if a string is a valid email address.
    
    Rules:
    - Must contain exactly one @ symbol
    - Must have characters before and after @
    - Domain part must contain at least one dot
    - No spaces allowed
    
    Args:
        email (str): Email string to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    TODO: Implement this function
    """
    pass

def is_valid_phone_number(phone):
    """
    Validate if a string is a valid phone number.
    
    Rules:
    - Must be exactly 10 digits
    - Can contain spaces, dashes, or parentheses
    - Examples: "123-456-7890", "(123) 456 7890", "1234567890"
    
    Args:
        phone (str): Phone number string to validate
        
    Returns:
        bool: True if valid, False otherwise
        
    TODO: Implement this function
    """
    pass

def clean_whitespace(text):
    """
    Clean extra whitespace from text.
    
    Rules:
    - Remove leading and trailing whitespace
    - Replace multiple consecutive spaces with single space
    - Handle None input gracefully
    
    Args:
        text (str or None): Text to clean
        
    Returns:
        str: Cleaned text, or empty string if input is None
        
    TODO: Implement this function
    """
    pass

def count_words(text):
    """
    Count the number of words in a text string.
    
    Rules:
    - Words are separated by whitespace
    - Empty string should return 0
    - None input should return 0
    
    Args:
        text (str or None): Text to count words in
        
    Returns:
        int: Number of words
        
    TODO: Implement this function
    """
    pass

# Test cases for manual verification
if __name__ == "__main__":
    print("=== String Validation Exercise ===\n")
    
    # Test email validation
    print("Email Validation Tests:")
    test_emails = [
        "user@example.com",
        "invalid.email",
        "@example.com",
        "user@",
        "user@domain",
        "user with spaces@example.com",
        ""
    ]
    
    for email in test_emails:
        result = is_valid_email(email)
        print(f"'{email}' -> {result}")
    
    print("\nPhone Number Validation Tests:")
    test_phones = [
        "123-456-7890",
        "(123) 456-7890",
        "1234567890",
        "123-456-78901",  # too long
        "123-456-789",    # too short
        "abc-def-ghij",   # non-numeric
        ""
    ]
    
    for phone in test_phones:
        result = is_valid_phone_number(phone)
        print(f"'{phone}' -> {result}")
    
    print("\nWhitespace Cleaning Tests:")
    test_texts = [
        "  hello   world  ",
        "normal text",
        "",
        None,
        "   multiple    spaces   between   words   "
    ]
    
    for text in test_texts:
        result = clean_whitespace(text)
        print(f"'{text}' -> '{result}'")
    
    print("\nWord Counting Tests:")
    test_word_texts = [
        "hello world",
        "  spaced   out   text  ",
        "",
        None,
        "single",
        "one two three four five"
    ]
    
    for text in test_word_texts:
        result = count_words(text)
        print(f"'{text}' -> {result} words")