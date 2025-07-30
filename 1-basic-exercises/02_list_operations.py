"""
Exercise 2: List Operations
Testing Focus: Data structure operations, edge cases, searching algorithms

Task: Implement functions that manipulate and search through lists.
These operations are common in test data management and result validation.
"""

def find_duplicates(items):
    """
    Find all duplicate items in a list.
    
    Args:
        items (list): List of items to check for duplicates
        
    Returns:
        list: List of duplicate items (without duplicates in result)
        
    Examples:
        find_duplicates([1, 2, 2, 3, 4, 4, 5]) -> [2, 4]
        find_duplicates([1, 2, 3]) -> []
        find_duplicates([]) -> []
        
    TODO: Implement this function
    """
    pass

def filter_by_type(items, data_type):
    """
    Filter list items by their data type.
    
    Args:
        items (list): List of mixed-type items
        data_type (type): Type to filter by (e.g., str, int, float)
        
    Returns:
        list: List containing only items of the specified type
        
    Examples:
        filter_by_type([1, "hello", 2.5, "world", 3], str) -> ["hello", "world"]
        filter_by_type([1, "hello", 2.5, "world", 3], int) -> [1, 3]
        
    TODO: Implement this function
    """
    pass

def merge_sorted_lists(list1, list2):
    """
    Merge two sorted lists into one sorted list.
    
    Args:
        list1 (list): First sorted list
        list2 (list): Second sorted list
        
    Returns:
        list: Merged sorted list
        
    Examples:
        merge_sorted_lists([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
        merge_sorted_lists([], [1, 2, 3]) -> [1, 2, 3]
        merge_sorted_lists([1, 2, 3], []) -> [1, 2, 3]
        
    TODO: Implement this function
    """
    pass

def validate_test_results(test_results):
    """
    Validate a list of test results and return summary statistics.
    
    Args:
        test_results (list): List of test results ("PASS", "FAIL", "SKIP")
        
    Returns:
        dict: Dictionary with counts and percentages
        {
            "total": int,
            "passed": int,
            "failed": int,
            "skipped": int,
            "pass_rate": float  # percentage
        }
        
    Examples:
        validate_test_results(["PASS", "FAIL", "PASS", "SKIP"]) -> 
        {"total": 4, "passed": 2, "failed": 1, "skipped": 1, "pass_rate": 50.0}
        
    TODO: Implement this function
    """
    pass

def find_missing_numbers(numbers, start, end):
    """
    Find missing numbers in a sequence within a given range.
    
    Args:
        numbers (list): List of integers
        start (int): Start of the range (inclusive)
        end (int): End of the range (inclusive)
        
    Returns:
        list: List of missing numbers in the range
        
    Examples:
        find_missing_numbers([1, 3, 5, 7], 1, 7) -> [2, 4, 6]
        find_missing_numbers([1, 2, 3, 4, 5], 1, 5) -> []
        
    TODO: Implement this function
    """
    pass

# Test cases for manual verification
if __name__ == "__main__":
    print("=== List Operations Exercise ===\n")
    
    # Test find_duplicates
    print("Find Duplicates Tests:")
    test_lists = [
        [1, 2, 2, 3, 4, 4, 5],
        [1, 2, 3],
        [],
        ["a", "b", "a", "c", "b"],
        [1, 1, 1, 1]
    ]
    
    for lst in test_lists:
        result = find_duplicates(lst)
        print(f"{lst} -> {result}")
    
    # Test filter_by_type
    print("\nFilter by Type Tests:")
    mixed_list = [1, "hello", 2.5, "world", 3, True, None, 4.7]
    
    for data_type in [str, int, float, bool]:
        result = filter_by_type(mixed_list, data_type)
        print(f"Filter {data_type.__name__}: {result}")
    
    # Test merge_sorted_lists
    print("\nMerge Sorted Lists Tests:")
    test_merges = [
        ([1, 3, 5], [2, 4, 6]),
        ([], [1, 2, 3]),
        ([1, 2, 3], []),
        ([1, 1, 2], [1, 3, 3])
    ]
    
    for list1, list2 in test_merges:
        result = merge_sorted_lists(list1, list2)
        print(f"{list1} + {list2} -> {result}")
    
    # Test validate_test_results
    print("\nTest Results Validation:")
    test_result_lists = [
        ["PASS", "FAIL", "PASS", "SKIP"],
        ["PASS", "PASS", "PASS"],
        ["FAIL", "FAIL"],
        [],
        ["PASS", "FAIL", "SKIP", "PASS", "PASS", "FAIL"]
    ]
    
    for results in test_result_lists:
        result = validate_test_results(results)
        print(f"{results} -> {result}")
    
    # Test find_missing_numbers
    print("\nFind Missing Numbers Tests:")
    test_missing = [
        ([1, 3, 5, 7], 1, 7),
        ([1, 2, 3, 4, 5], 1, 5),
        ([], 1, 5),
        ([2, 4, 6, 8, 10], 1, 10)
    ]
    
    for numbers, start, end in test_missing:
        result = find_missing_numbers(numbers, start, end)
        print(f"Numbers: {numbers}, Range: {start}-{end} -> Missing: {result}")