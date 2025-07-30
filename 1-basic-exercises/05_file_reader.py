"""
Exercise 5: File Reader
Testing Focus: File I/O testing, error scenarios, data processing

Task: Create functions to read and process different types of files safely.
This exercise focuses on file handling, error management, and data validation.
"""

import os
import json
import csv
from pathlib import Path

def safe_read_text_file(file_path, encoding='utf-8'):
    """
    Safely read a text file with proper error handling.
    
    Args:
        file_path (str): Path to the text file
        encoding (str): File encoding (default: utf-8)
        
    Returns:
        dict: {
            'success': bool,
            'content': str or None,
            'error': str or None,
            'line_count': int,
            'char_count': int
        }
        
    TODO: Implement this function
    """
    pass

def read_csv_file(file_path):
    """
    Read a CSV file and return structured data.
    
    Args:
        file_path (str): Path to the CSV file
        
    Returns:
        dict: {
            'success': bool,
            'data': list of dictionaries or None,
            'error': str or None,
            'row_count': int,
            'column_names': list
        }
        
    TODO: Implement this function using csv module
    """
    pass

def read_json_file(file_path):
    """
    Read and parse a JSON file.
    
    Args:
        file_path (str): Path to the JSON file
        
    Returns:
        dict: {
            'success': bool,
            'data': dict/list or None,
            'error': str or None,
            'is_valid_json': bool
        }
        
    TODO: Implement this function
    """
    pass

def analyze_file_info(file_path):
    """
    Analyze basic information about a file.
    
    Args:
        file_path (str): Path to the file
        
    Returns:
        dict: {
            'exists': bool,
            'size_bytes': int or None,
            'extension': str or None,
            'is_readable': bool,
            'is_writable': bool,
            'modified_time': str or None  # formatted timestamp
        }
        
    TODO: Implement this function using os.path or pathlib
    """
    pass

def find_files_by_extension(directory, extension):
    """
    Find all files with a specific extension in a directory.
    
    Args:
        directory (str): Directory to search in
        extension (str): File extension to search for (e.g., '.txt', '.py')
        
    Returns:
        dict: {
            'success': bool,
            'files': list of file paths or None,
            'error': str or None,
            'count': int
        }
        
    TODO: Implement this function
    """
    pass

def count_lines_in_files(file_paths):
    """
    Count total lines across multiple text files.
    
    Args:
        file_paths (list): List of file paths
        
    Returns:
        dict: {
            'total_lines': int,
            'file_results': list of dicts with per-file results,
            'successful_files': int,
            'failed_files': int
        }
        
    TODO: Implement this function
    """
    pass

def search_text_in_file(file_path, search_term, case_sensitive=False):
    """
    Search for a text term in a file and return match information.
    
    Args:
        file_path (str): Path to the file
        search_term (str): Text to search for
        case_sensitive (bool): Whether search should be case sensitive
        
    Returns:
        dict: {
            'success': bool,
            'matches_found': int,
            'line_numbers': list of line numbers where matches found,
            'matching_lines': list of tuples (line_number, line_content),
            'error': str or None
        }
        
    TODO: Implement this function
    """
    pass

def create_test_files():
    """
    Create sample test files for testing purposes.
    Creates: sample.txt, sample.csv, sample.json
    
    TODO: Implement this function
    """
    pass

def cleanup_test_files():
    """
    Remove test files created by create_test_files().
    
    TODO: Implement this function
    """
    pass

# Test cases for manual verification
if __name__ == "__main__":
    print("=== File Reader Exercise ===\n")
    
    # Create test files first
    print("Creating test files...")
    create_test_files()
    
    # Test text file reading
    print("\n1. Text File Reading Tests:")
    text_results = safe_read_text_file("sample.txt")
    print(f"Text file result: {text_results}")
    
    # Test non-existent file
    missing_results = safe_read_text_file("missing.txt")
    print(f"Missing file result: {missing_results}")
    
    # Test CSV file reading
    print("\n2. CSV File Reading Tests:")
    csv_results = read_csv_file("sample.csv")
    print(f"CSV file result: {csv_results}")
    
    # Test JSON file reading
    print("\n3. JSON File Reading Tests:")
    json_results = read_json_file("sample.json")
    print(f"JSON file result: {json_results}")
    
    # Test file analysis
    print("\n4. File Analysis Tests:")
    test_files = ["sample.txt", "sample.csv", "sample.json", "missing.txt"]
    
    for file_path in test_files:
        info = analyze_file_info(file_path)
        print(f"Analysis of '{file_path}': {info}")
    
    # Test finding files by extension
    print("\n5. Find Files by Extension Tests:")
    current_dir = "."
    extensions = [".txt", ".csv", ".json", ".py"]
    
    for ext in extensions:
        result = find_files_by_extension(current_dir, ext)
        print(f"Files with {ext} extension: {result}")
    
    # Test line counting
    print("\n6. Line Counting Tests:")
    existing_files = [f for f in ["sample.txt", "sample.csv", "sample.json"] 
                     if os.path.exists(f)]
    line_count_result = count_lines_in_files(existing_files)
    print(f"Line count result: {line_count_result}")
    
    # Test text searching
    print("\n7. Text Search Tests:")
    if os.path.exists("sample.txt"):
        search_results = search_text_in_file("sample.txt", "test", case_sensitive=False)
        print(f"Search results: {search_results}")
        
        search_results_case = search_text_in_file("sample.txt", "Test", case_sensitive=True)
        print(f"Case-sensitive search results: {search_results_case}")
    
    # Test error handling with invalid files
    print("\n8. Error Handling Tests:")
    
    # Try to read a directory as a file
    dir_result = safe_read_text_file(".")
    print(f"Reading directory as file: {dir_result}")
    
    # Try to read with invalid encoding
    encoding_result = safe_read_text_file("sample.txt", "invalid-encoding")
    print(f"Invalid encoding result: {encoding_result}")
    
    # Cleanup
    print("\n9. Cleanup:")
    cleanup_test_files()
    print("Test files cleaned up.")
    
    # Verify cleanup
    print("\nVerifying cleanup:")
    for file_name in ["sample.txt", "sample.csv", "sample.json"]:
        exists = os.path.exists(file_name)
        print(f"{file_name} exists: {exists}")