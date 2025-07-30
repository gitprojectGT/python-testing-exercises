"""
Tests for Exercise 2: List Operations
"""

import pytest
from unittest.mock import patch
import sys
import os

# Import the exercise module
try:
    from _02_list_operations import (
        find_duplicates, filter_by_type, merge_sorted_lists,
        validate_test_results, find_missing_numbers
    )
except ImportError:
    # Alternative import method
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '1-basic-exercises'))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "list_operations", 
            os.path.join(os.path.dirname(__file__), '..', '..', '1-basic-exercises', '02_list_operations.py')
        )
        list_operations = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(list_operations)
        
        find_duplicates = list_operations.find_duplicates
        filter_by_type = list_operations.filter_by_type
        merge_sorted_lists = list_operations.merge_sorted_lists
        validate_test_results = list_operations.validate_test_results
        find_missing_numbers = list_operations.find_missing_numbers
    except:
        pytest.skip("Could not import list operations module")

class TestFindDuplicates:
    """Test duplicate finding functionality."""
    
    @pytest.mark.parametrize("items,expected", [
        ([1, 2, 2, 3, 4, 4, 5], [2, 4]),
        ([1, 2, 3], []),
        ([], []),
        ([1, 1, 1, 1], [1]),
        (["a", "b", "a", "c", "b"], ["a", "b"]),
        ([1, 2, 3, 1, 2, 4, 1], [1, 2]),
        ([True, False, True], [True]),
    ])
    def test_find_duplicates(self, items, expected):
        """Test finding duplicates in various lists."""
        result = find_duplicates(items)
        assert sorted(result) == sorted(expected), f"Failed for {items}"
    
    def test_find_duplicates_preserves_order(self):
        """Test that duplicates are returned in order of first appearance."""
        items = [3, 1, 2, 1, 3, 4, 2]
        result = find_duplicates(items)
        # Should maintain order: 3 appears first, then 1, then 2
        expected_order = [3, 1, 2]
        assert result == expected_order
    
    def test_find_duplicates_mixed_types(self):
        """Test finding duplicates with mixed data types."""
        items = [1, "1", 1, "1", 2]
        result = find_duplicates(items)
        expected = [1, "1"]
        assert sorted(result, key=str) == sorted(expected, key=str)
    
    def test_find_duplicates_empty_list(self):
        """Test with empty list."""
        assert find_duplicates([]) == []
    
    def test_find_duplicates_single_item(self):
        """Test with single item list."""
        assert find_duplicates([1]) == []

class TestFilterByType:
    """Test type filtering functionality."""
    
    def test_filter_by_type_strings(self):
        """Test filtering strings from mixed list."""
        items = [1, "hello", 2.5, "world", 3, True]
        result = filter_by_type(items, str)
        expected = ["hello", "world"]
        assert result == expected
    
    def test_filter_by_type_integers(self):
        """Test filtering integers from mixed list."""
        items = [1, "hello", 2.5, "world", 3, True]
        result = filter_by_type(items, int)
        expected = [1, 3, True]  # Note: bool is subclass of int in Python
        assert result == expected
    
    def test_filter_by_type_floats(self):
        """Test filtering floats from mixed list."""
        items = [1, "hello", 2.5, "world", 3.14, True]
        result = filter_by_type(items, float)
        expected = [2.5, 3.14]
        assert result == expected
    
    def test_filter_by_type_booleans(self):
        """Test filtering booleans from mixed list."""
        items = [1, "hello", True, False, 3, "world"]
        result = filter_by_type(items, bool)
        expected = [True, False]
        assert result == expected
    
    def test_filter_by_type_empty_list(self):
        """Test filtering empty list."""
        result = filter_by_type([], str)
        assert result == []
    
    def test_filter_by_type_no_matches(self):
        """Test filtering when no items match type."""
        items = [1, 2, 3, 4, 5]
        result = filter_by_type(items, str)
        assert result == []
    
    def test_filter_by_type_all_match(self):
        """Test filtering when all items match type."""
        items = ["a", "b", "c", "d"]
        result = filter_by_type(items, str)
        assert result == items

class TestMergeSortedLists:
    """Test sorted list merging functionality."""
    
    @pytest.mark.parametrize("list1,list2,expected", [
        ([1, 3, 5], [2, 4, 6], [1, 2, 3, 4, 5, 6]),
        ([], [1, 2, 3], [1, 2, 3]),
        ([1, 2, 3], [], [1, 2, 3]),
        ([1, 1, 2], [1, 3, 3], [1, 1, 1, 2, 3, 3]),
        ([1], [2], [1, 2]),
        ([], [], []),
    ])
    def test_merge_sorted_lists(self, list1, list2, expected):
        """Test merging sorted lists."""
        result = merge_sorted_lists(list1, list2)
        assert result == expected
    
    def test_merge_sorted_lists_strings(self):
        """Test merging sorted string lists."""
        list1 = ["apple", "cherry"]
        list2 = ["banana", "date"]
        result = merge_sorted_lists(list1, list2)
        expected = ["apple", "banana", "cherry", "date"]
        assert result == expected
    
    def test_merge_sorted_lists_different_lengths(self):
        """Test merging lists of very different lengths."""
        list1 = [1, 10, 20, 30, 40, 50]
        list2 = [5]
        result = merge_sorted_lists(list1, list2)
        expected = [1, 5, 10, 20, 30, 40, 50]
        assert result == expected
    
    def test_merge_sorted_lists_maintains_stability(self):
        """Test that merge maintains relative order of equal elements."""
        list1 = [1, 3, 3, 5]
        list2 = [2, 3, 4, 6]
        result = merge_sorted_lists(list1, list2)
        # Should have all 3s, with list1's 3s appearing first
        assert result == [1, 2, 3, 3, 3, 4, 5, 6]

class TestValidateTestResults:
    """Test test result validation functionality."""
    
    def test_validate_test_results_mixed(self):
        """Test validation with mixed test results."""
        results = ["PASS", "FAIL", "PASS", "SKIP"]
        result = validate_test_results(results)
        
        expected = {
            "total": 4,
            "passed": 2,
            "failed": 1,
            "skipped": 1,
            "pass_rate": 50.0
        }
        assert result == expected
    
    def test_validate_test_results_all_pass(self):
        """Test validation with all passing tests."""
        results = ["PASS", "PASS", "PASS"]
        result = validate_test_results(results)
        
        expected = {
            "total": 3,
            "passed": 3,
            "failed": 0,
            "skipped": 0,
            "pass_rate": 100.0
        }
        assert result == expected
    
    def test_validate_test_results_all_fail(self):
        """Test validation with all failing tests."""
        results = ["FAIL", "FAIL"]
        result = validate_test_results(results)
        
        expected = {
            "total": 2,
            "passed": 0,
            "failed": 2,
            "skipped": 0,
            "pass_rate": 0.0
        }
        assert result == expected
    
    def test_validate_test_results_empty(self):
        """Test validation with empty results."""
        result = validate_test_results([])
        
        expected = {
            "total": 0,
            "passed": 0,
            "failed": 0,
            "skipped": 0,
            "pass_rate": 0.0
        }
        assert result == expected
    
    def test_validate_test_results_case_insensitive(self):
        """Test validation handles different cases."""
        results = ["pass", "FAIL", "Skip", "PASS"]
        result = validate_test_results(results)
        
        # Should handle different cases correctly
        assert result["total"] == 4
        assert result["passed"] >= 1  # At least the "PASS" should count
        assert result["failed"] >= 1  # At least the "FAIL" should count

class TestFindMissingNumbers:
    """Test missing number finding functionality."""
    
    @pytest.mark.parametrize("numbers,start,end,expected", [
        ([1, 3, 5, 7], 1, 7, [2, 4, 6]),
        ([1, 2, 3, 4, 5], 1, 5, []),
        ([], 1, 5, [1, 2, 3, 4, 5]),
        ([2, 4, 6, 8, 10], 1, 10, [1, 3, 5, 7, 9]),
        ([1], 1, 3, [2, 3]),
        ([5], 1, 5, [1, 2, 3, 4]),
    ])
    def test_find_missing_numbers(self, numbers, start, end, expected):
        """Test finding missing numbers in various ranges."""
        result = find_missing_numbers(numbers, start, end)
        assert sorted(result) == sorted(expected)
    
    def test_find_missing_numbers_unsorted_input(self):
        """Test with unsorted input numbers."""
        numbers = [5, 1, 3, 7]
        result = find_missing_numbers(numbers, 1, 7)
        expected = [2, 4, 6]
        assert sorted(result) == sorted(expected)
    
    def test_find_missing_numbers_duplicates_in_input(self):
        """Test with duplicate numbers in input."""
        numbers = [1, 2, 2, 4, 4, 5]
        result = find_missing_numbers(numbers, 1, 5)
        expected = [3]
        assert result == expected
    
    def test_find_missing_numbers_negative_range(self):
        """Test with negative number range."""
        numbers = [-2, 0, 2]
        result = find_missing_numbers(numbers, -3, 3)
        expected = [-3, -1, 1, 3]
        assert sorted(result) == sorted(expected)
    
    def test_find_missing_numbers_single_range(self):
        """Test with single number range."""
        numbers = []
        result = find_missing_numbers(numbers, 5, 5)
        expected = [5]
        assert result == expected

class TestIntegrationScenarios:
    """Test integration scenarios combining multiple functions."""
    
    def test_data_processing_pipeline(self):
        """Test a complete data processing pipeline."""
        # Start with mixed data
        data = [1, "test", 2.5, 1, "test", 3, True, 2.5]
        
        # Find duplicates
        duplicates = find_duplicates(data)
        assert len(duplicates) >= 2  # At least 1 and "test" should be duplicated
        
        # Filter by type
        integers = filter_by_type(data, int)
        strings = filter_by_type(data, str)
        
        assert len(integers) >= 2  # Should have integers including bool
        assert len(strings) >= 1   # Should have string(s)
    
    def test_test_result_analysis_workflow(self):
        """Test analyzing test results workflow."""
        # Generate test results
        all_results = ["PASS"] * 80 + ["FAIL"] * 15 + ["SKIP"] * 5
        
        # Validate results
        validation = validate_test_results(all_results)
        
        assert validation["total"] == 100
        assert validation["passed"] == 80
        assert validation["failed"] == 15
        assert validation["skipped"] == 5
        assert validation["pass_rate"] == 80.0
        
        # Find patterns in failures (simulate test case IDs)
        failed_test_ids = [15, 23, 45, 67, 89]  # Failed test case IDs
        missing_in_range = find_missing_numbers(failed_test_ids, 1, 100)
        
        # Should find many missing numbers (passing tests)
        assert len(missing_in_range) == 95  # 100 - 5 failed tests

class TestErrorHandling:
    """Test error handling and edge cases."""
    
    def test_functions_handle_none_input(self):
        """Test functions handle None input gracefully."""
        # These should not crash
        try:
            find_duplicates(None)
            assert False, "Should handle None input"
        except (TypeError, AttributeError):
            pass  # Expected behavior
    
    def test_functions_handle_invalid_types(self):
        """Test functions handle invalid input types."""
        # Test with non-list inputs where appropriate
        try:
            result = filter_by_type("not a list", str)
            # If it doesn't crash, result should be reasonable
            assert isinstance(result, (list, type(None)))
        except (TypeError, AttributeError):
            pass  # Expected behavior
    
    def test_merge_sorted_lists_unsorted_input(self):
        """Test merge function with unsorted input."""
        list1 = [3, 1, 2]  # Not sorted
        list2 = [6, 4, 5]  # Not sorted
        
        # Function should still work or handle gracefully
        result = merge_sorted_lists(list1, list2)
        
        # Result should contain all elements
        all_elements = list1 + list2
        assert len(result) == len(all_elements)
        for item in all_elements:
            assert item in result

class TestPerformance:
    """Test performance with larger datasets."""
    
    @pytest.mark.slow
    def test_find_duplicates_large_list(self):
        """Test duplicate finding with large list."""
        large_list = list(range(10000)) * 2  # 20,000 items with duplicates
        result = find_duplicates(large_list)
        
        # Should find all numbers 0-9999 as duplicates
        assert len(result) == 10000
        assert all(i in result for i in range(10000))
    
    @pytest.mark.slow
    def test_merge_large_sorted_lists(self):
        """Test merging large sorted lists."""
        list1 = list(range(0, 10000, 2))    # Even numbers
        list2 = list(range(1, 10000, 2))    # Odd numbers
        
        result = merge_sorted_lists(list1, list2)
        
        # Should be sorted and contain all numbers
        assert len(result) == 10000
        assert result == list(range(10000))
    
    def test_filter_large_mixed_list(self):
        """Test filtering large mixed-type list."""
        mixed_list = []
        for i in range(1000):
            mixed_list.extend([i, str(i), float(i), bool(i % 2)])
        
        strings = filter_by_type(mixed_list, str)
        integers = filter_by_type(mixed_list, int)
        
        assert len(strings) == 1000  # One string per iteration
        assert len(integers) >= 1000  # Integers + booleans

if __name__ == "__main__":
    pytest.main([__file__])