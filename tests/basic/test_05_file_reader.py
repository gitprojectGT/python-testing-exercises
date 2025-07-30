"""
Tests for Exercise 5: File Reader
"""

import pytest
import tempfile
import os
import json
import csv
from unittest.mock import patch, mock_open, Mock
import sys
from pathlib import Path

# Import the exercise module
try:
    from _05_file_reader import (
        safe_read_text_file, read_csv_file, read_json_file,
        analyze_file_info, find_files_by_extension, count_lines_in_files,
        search_text_in_file, create_test_files, cleanup_test_files
    )
except ImportError:
    # Alternative import method
    sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '1-basic-exercises'))
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            "file_reader", 
            os.path.join(os.path.dirname(__file__), '..', '..', '1-basic-exercises', '05_file_reader.py')
        )
        file_reader = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(file_reader)
        
        safe_read_text_file = file_reader.safe_read_text_file
        read_csv_file = file_reader.read_csv_file
        read_json_file = file_reader.read_json_file
        analyze_file_info = file_reader.analyze_file_info
        find_files_by_extension = file_reader.find_files_by_extension
        count_lines_in_files = file_reader.count_lines_in_files
        search_text_in_file = file_reader.search_text_in_file
        create_test_files = file_reader.create_test_files
        cleanup_test_files = file_reader.cleanup_test_files
    except:
        pytest.skip("Could not import file reader module")

class TestSafeReadTextFile:
    """Test safe text file reading functionality."""
    
    def test_read_existing_file(self, create_temp_file_with_content_fixture):
        """Test reading an existing text file."""
        content = "Hello, World!\nThis is a test file.\nThird line."
        temp_file = create_temp_file_with_content_fixture(content)
        
        result = safe_read_text_file(temp_file)
        
        assert isinstance(result, dict)
        assert result["success"] == True
        assert result["content"] == content
        assert result["error"] is None
        assert result["line_count"] == 3
        assert result["char_count"] == len(content)
    
    def test_read_nonexistent_file(self):
        """Test reading a non-existent file."""
        result = safe_read_text_file("nonexistent_file.txt")
        
        assert isinstance(result, dict)
        assert result["success"] == False
        assert result["content"] is None
        assert result["error"] is not None
        assert "not found" in result["error"].lower() or "no such file" in result["error"].lower()
        assert result["line_count"] == 0
        assert result["char_count"] == 0
    
    def test_read_empty_file(self, create_temp_file_with_content_fixture):
        """Test reading an empty file."""
        temp_file = create_temp_file_with_content_fixture("")
        
        result = safe_read_text_file(temp_file)
        
        assert result["success"] == True
        assert result["content"] == ""
        assert result["line_count"] == 0
        assert result["char_count"] == 0
    
    def test_read_file_different_encodings(self, create_temp_file_with_content_fixture):
        """Test reading files with different encodings."""
        content = "Hello, 世界! Hëllö, Wörld!"
        temp_file = create_temp_file_with_content_fixture(content)
        
        # Test UTF-8 (default)
        result = safe_read_text_file(temp_file)
        assert result["success"] == True
        
        # Test explicit UTF-8
        result_utf8 = safe_read_text_file(temp_file, encoding='utf-8')
        assert result_utf8["success"] == True
        assert result_utf8["content"] == content
    
    def test_read_file_invalid_encoding(self, create_temp_file_with_content_fixture):
        """Test reading file with invalid encoding."""
        content = "Simple ASCII content"
        temp_file = create_temp_file_with_content_fixture(content)
        
        # Try with invalid encoding
        result = safe_read_text_file(temp_file, encoding='invalid-encoding')
        
        # Should handle error gracefully
        assert result["success"] == False
        assert result["error"] is not None
    
    def test_read_large_file(self, create_temp_file_with_content_fixture):
        """Test reading a large file."""
        # Create content with many lines
        lines = [f"Line {i}" for i in range(1000)]
        content = "\n".join(lines)
        temp_file = create_temp_file_with_content_fixture(content)
        
        result = safe_read_text_file(temp_file)
        
        assert result["success"] == True
        assert result["line_count"] == 1000
        assert "Line 999" in result["content"]

class TestReadCSVFile:
    """Test CSV file reading functionality."""
    
    def test_read_valid_csv(self, create_temp_file_with_content_fixture):
        """Test reading a valid CSV file."""
        csv_content = """name,age,city
John,30,New York
Jane,25,Los Angeles
Bob,35,Chicago"""
        
        temp_file = create_temp_file_with_content_fixture(csv_content, ".csv")
        result = read_csv_file(temp_file)
        
        assert isinstance(result, dict)
        assert result["success"] == True
        assert result["data"] is not None
        assert result["error"] is None
        assert result["row_count"] == 3
        assert result["column_names"] == ["name", "age", "city"]
        
        # Check data content
        assert len(result["data"]) == 3
        assert result["data"][0]["name"] == "John"
        assert result["data"][0]["age"] == "30"
        assert result["data"][1]["name"] == "Jane"
    
    def test_read_csv_with_quotes(self, create_temp_file_with_content_fixture):
        """Test reading CSV with quoted fields."""
        csv_content = '''name,description,price
"Product 1","A great product, with comma",19.99
"Product 2","Another ""quoted"" product",29.99'''
        
        temp_file = create_temp_file_with_content_fixture(csv_content, ".csv")
        result = read_csv_file(temp_file)
        
        assert result["success"] == True
        assert len(result["data"]) == 2
        assert "comma" in result["data"][0]["description"]
        assert "quoted" in result["data"][1]["description"]
    
    def test_read_empty_csv(self, create_temp_file_with_content_fixture):
        """Test reading an empty CSV file."""
        temp_file = create_temp_file_with_content_fixture("", ".csv")
        result = read_csv_file(temp_file)
        
        assert result["success"] == True
        assert result["data"] == []
        assert result["row_count"] == 0
        assert result["column_names"] == []
    
    def test_read_csv_headers_only(self, create_temp_file_with_content_fixture):
        """Test reading CSV with only headers."""
        csv_content = "name,age,city"
        temp_file = create_temp_file_with_content_fixture(csv_content, ".csv")
        result = read_csv_file(temp_file)
        
        assert result["success"] == True
        assert result["data"] == []
        assert result["row_count"] == 0
        assert result["column_names"] == ["name", "age", "city"]
    
    def test_read_nonexistent_csv(self):
        """Test reading non-existent CSV file."""
        result = read_csv_file("nonexistent.csv")
        
        assert result["success"] == False
        assert result["data"] is None
        assert result["error"] is not None
        assert result["row_count"] == 0
        assert result["column_names"] == []

class TestReadJSONFile:
    """Test JSON file reading functionality."""
    
    def test_read_valid_json(self, create_temp_file_with_content_fixture):
        """Test reading a valid JSON file."""
        json_data = {
            "name": "Test",
            "age": 30,
            "active": True,
            "scores": [85, 90, 78],
            "address": {
                "street": "123 Main St",
                "city": "Anytown"
            }
        }
        json_content = json.dumps(json_data, indent=2)
        
        temp_file = create_temp_file_with_content_fixture(json_content, ".json")
        result = read_json_file(temp_file)
        
        assert isinstance(result, dict)
        assert result["success"] == True
        assert result["data"] == json_data
        assert result["error"] is None
        assert result["is_valid_json"] == True
    
    def test_read_invalid_json(self, create_temp_file_with_content_fixture):
        """Test reading invalid JSON file."""
        invalid_json = '{"name": "Test", "age": 30, "active": true'  # Missing closing brace
        
        temp_file = create_temp_file_with_content_fixture(invalid_json, ".json")
        result = read_json_file(temp_file)
        
        assert result["success"] == False
        assert result["data"] is None
        assert result["error"] is not None
        assert result["is_valid_json"] == False
        assert "json" in result["error"].lower()
    
    def test_read_empty_json_file(self, create_temp_file_with_content_fixture):
        """Test reading empty JSON file."""
        temp_file = create_temp_file_with_content_fixture("", ".json")
        result = read_json_file(temp_file)
        
        assert result["success"] == False
        assert result["is_valid_json"] == False
    
    def test_read_json_array(self, create_temp_file_with_content_fixture):
        """Test reading JSON array."""
        json_array = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
        json_content = json.dumps(json_array)
        
        temp_file = create_temp_file_with_content_fixture(json_content, ".json")
        result = read_json_file(temp_file)
        
        assert result["success"] == True
        assert result["data"] == json_array
        assert result["is_valid_json"] == True
    
    def test_read_nonexistent_json(self):
        """Test reading non-existent JSON file."""
        result = read_json_file("nonexistent.json")
        
        assert result["success"] == False
        assert result["data"] is None
        assert result["error"] is not None

class TestAnalyzeFileInfo:
    """Test file information analysis."""
    
    def test_analyze_existing_file(self, create_temp_file_with_content_fixture):
        """Test analyzing an existing file."""
        content = "Test file content"
        temp_file = create_temp_file_with_content_fixture(content, ".txt")
        
        result = analyze_file_info(temp_file)
        
        assert isinstance(result, dict)
        assert result["exists"] == True
        assert result["size_bytes"] == len(content)
        assert result["extension"] == ".txt"
        assert result["is_readable"] == True
        assert result["is_writable"] == True
        assert result["modified_time"] is not None
    
    def test_analyze_nonexistent_file(self):
        """Test analyzing non-existent file."""
        result = analyze_file_info("nonexistent_file.txt")
        
        assert result["exists"] == False
        assert result["size_bytes"] is None
        assert result["extension"] == ".txt"  # Can still extract extension
        assert result["is_readable"] == False
        assert result["is_writable"] == False
        assert result["modified_time"] is None
    
    def test_analyze_file_without_extension(self, create_temp_file_with_content_fixture):
        """Test analyzing file without extension."""
        content = "No extension file"
        # Create file without extension
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='') as f:
            f.write(content)
            temp_file = f.name
        
        try:
            result = analyze_file_info(temp_file)
            
            assert result["exists"] == True
            assert result["extension"] is None or result["extension"] == ""
        finally:
            os.unlink(temp_file)
    
    def test_analyze_directory(self, temp_dir):
        """Test analyzing directory instead of file."""
        result = analyze_file_info(temp_dir)
        
        # Behavior may vary - should handle gracefully
        assert isinstance(result, dict)
        assert "exists" in result

class TestFindFilesByExtension:
    """Test finding files by extension."""
    
    def test_find_files_in_directory(self, temp_dir):
        """Test finding files with specific extension."""
        # Create test files
        test_files = [
            ("test1.txt", "content1"),
            ("test2.txt", "content2"),
            ("test3.py", "content3"),
            ("test4.json", "content4"),
        ]
        
        for filename, content in test_files:
            file_path = os.path.join(temp_dir, filename)
            with open(file_path, 'w') as f:
                f.write(content)
        
        # Find .txt files
        result = find_files_by_extension(temp_dir, ".txt")
        
        assert isinstance(result, dict)
        assert result["success"] == True
        assert result["files"] is not None
        assert result["error"] is None
        assert result["count"] == 2
        
        # Check that found files are correct
        found_filenames = [os.path.basename(f) for f in result["files"]]
        assert "test1.txt" in found_filenames
        assert "test2.txt" in found_filenames
        assert "test3.py" not in found_filenames
    
    def test_find_files_no_matches(self, temp_dir):
        """Test finding files when no matches exist."""
        # Create files with different extensions
        with open(os.path.join(temp_dir, "test.py"), 'w') as f:
            f.write("content")
        
        result = find_files_by_extension(temp_dir, ".txt")
        
        assert result["success"] == True
        assert result["files"] == []
        assert result["count"] == 0
    
    def test_find_files_nonexistent_directory(self):
        """Test finding files in non-existent directory."""
        result = find_files_by_extension("nonexistent_dir", ".txt")
        
        assert result["success"] == False
        assert result["files"] is None
        assert result["error"] is not None
        assert result["count"] == 0
    
    def test_find_files_case_sensitivity(self, temp_dir):
        """Test case sensitivity in extension matching."""
        # Create files with different case extensions
        test_files = ["test.TXT", "test.txt", "test.Txt"]
        
        for filename in test_files:
            file_path = os.path.join(temp_dir, filename)
            with open(file_path, 'w') as f:
                f.write("content")
        
        # Search for lowercase extension
        result = find_files_by_extension(temp_dir, ".txt")
        
        # Should find at least the exact match
        assert result["success"] == True
        assert result["count"] >= 1

class TestCountLinesInFiles:
    """Test counting lines across multiple files."""
    
    def test_count_lines_multiple_files(self, create_temp_file_with_content_fixture):
        """Test counting lines in multiple files."""
        files_content = [
            ("file1", "Line 1\nLine 2\nLine 3"),  # 3 lines
            ("file2", "Single line"),              # 1 line
            ("file3", "Line A\nLine B"),           # 2 lines
        ]
        
        file_paths = []
        for name, content in files_content:
            temp_file = create_temp_file_with_content_fixture(content)
            file_paths.append(temp_file)
        
        result = count_lines_in_files(file_paths)
        
        assert isinstance(result, dict)
        assert result["total_lines"] == 6  # 3 + 1 + 2
        assert result["successful_files"] == 3
        assert result["failed_files"] == 0
        assert len(result["file_results"]) == 3
        
        # Check individual file results
        line_counts = [fr["line_count"] for fr in result["file_results"]]
        assert sorted(line_counts) == [1, 2, 3]
    
    def test_count_lines_empty_files(self, create_temp_file_with_content_fixture):
        """Test counting lines in empty files."""
        empty_file = create_temp_file_with_content_fixture("")
        
        result = count_lines_in_files([empty_file])
        
        assert result["total_lines"] == 0
        assert result["successful_files"] == 1
        assert result["failed_files"] == 0
    
    def test_count_lines_mixed_success_failure(self, create_temp_file_with_content_fixture):
        """Test counting lines with mix of existing and non-existing files."""
        existing_file = create_temp_file_with_content_fixture("Line 1\nLine 2")
        nonexistent_file = "nonexistent_file.txt"
        
        result = count_lines_in_files([existing_file, nonexistent_file])
        
        assert result["total_lines"] == 2  # Only from existing file
        assert result["successful_files"] == 1
        assert result["failed_files"] == 1
        assert len(result["file_results"]) == 2
    
    def test_count_lines_empty_file_list(self):
        """Test counting lines with empty file list."""
        result = count_lines_in_files([])
        
        assert result["total_lines"] == 0
        assert result["successful_files"] == 0
        assert result["failed_files"] == 0
        assert result["file_results"] == []

class TestSearchTextInFile:
    """Test text searching functionality."""
    
    def test_search_text_found(self, create_temp_file_with_content_fixture):
        """Test searching for text that exists in file."""
        content = """Line 1: Hello World
Line 2: This is a test
Line 3: Hello again
Line 4: Final line"""
        
        temp_file = create_temp_file_with_content_fixture(content)
        result = search_text_in_file(temp_file, "Hello")
        
        assert isinstance(result, dict)
        assert result["success"] == True
        assert result["matches_found"] == 2
        assert result["error"] is None
        assert len(result["line_numbers"]) == 2
        assert 1 in result["line_numbers"]  # Line 1
        assert 3 in result["line_numbers"]  # Line 3
        assert len(result["matching_lines"]) == 2
    
    def test_search_text_not_found(self, create_temp_file_with_content_fixture):
        """Test searching for text that doesn't exist."""
        content = "Line 1\nLine 2\nLine 3"
        temp_file = create_temp_file_with_content_fixture(content)
        
        result = search_text_in_file(temp_file, "NotFound")
        
        assert result["success"] == True
        assert result["matches_found"] == 0
        assert result["line_numbers"] == []
        assert result["matching_lines"] == []
    
    def test_search_case_sensitive(self, create_temp_file_with_content_fixture):
        """Test case-sensitive search."""
        content = "Hello world\nhello WORLD\nHELLO world"
        temp_file = create_temp_file_with_content_fixture(content)
        
        # Case sensitive search
        result_sensitive = search_text_in_file(temp_file, "Hello", case_sensitive=True)
        assert result_sensitive["matches_found"] == 1  # Only first line
        
        # Case insensitive search
        result_insensitive = search_text_in_file(temp_file, "Hello", case_sensitive=False)
        assert result_insensitive["matches_found"] == 2  # First and third lines
    
    def test_search_empty_file(self, create_temp_file_with_content_fixture):
        """Test searching in empty file."""
        temp_file = create_temp_file_with_content_fixture("")
        
        result = search_text_in_file(temp_file, "test")
        
        assert result["success"] == True
        assert result["matches_found"] == 0
        assert result["line_numbers"] == []
    
    def test_search_nonexistent_file(self):
        """Test searching in non-existent file."""
        result = search_text_in_file("nonexistent.txt", "test")
        
        assert result["success"] == False
        assert result["error"] is not None
        assert result["matches_found"] == 0
    
    def test_search_special_characters(self, create_temp_file_with_content_fixture):
        """Test searching for special characters."""
        content = "Email: test@example.com\nPrice: $19.99\nRegex: \\d+"
        temp_file = create_temp_file_with_content_fixture(content)
        
        # Search for email
        result_email = search_text_in_file(temp_file, "@")
        assert result_email["matches_found"] == 1
        
        # Search for dollar sign
        result_dollar = search_text_in_file(temp_file, "$")
        assert result_dollar["matches_found"] == 1

class TestCreateAndCleanupTestFiles:
    """Test test file creation and cleanup."""
    
    def test_create_test_files(self):
        """Test creating test files."""
        # This function should create sample files
        create_test_files()
        
        # Check that files were created
        expected_files = ["sample.txt", "sample.csv", "sample.json"]
        for filename in expected_files:
            assert os.path.exists(filename), f"File {filename} was not created"
            assert os.path.getsize(filename) > 0, f"File {filename} is empty"
    
    def test_cleanup_test_files(self):
        """Test cleaning up test files."""
        # First create the files
        create_test_files()
        
        # Verify they exist
        expected_files = ["sample.txt", "sample.csv", "sample.json"]
        for filename in expected_files:
            assert os.path.exists(filename)
        
        # Clean them up
        cleanup_test_files()
        
        # Verify they're gone
        for filename in expected_files:
            assert not os.path.exists(filename), f"File {filename} was not cleaned up"
    
    def test_cleanup_nonexistent_files(self):
        """Test cleanup when files don't exist."""
        # Should not crash if files don't exist
        cleanup_test_files()  # Should handle gracefully

class TestIntegrationScenarios:
    """Test integration scenarios combining multiple functions."""
    
    def test_complete_file_processing_workflow(self, temp_dir):
        """Test complete file processing workflow."""
        # Create various test files
        files_to_create = [
            ("data.txt", "Text file content\nSecond line"),
            ("data.csv", "name,age\nJohn,30\nJane,25"),
            ("data.json", '{"name": "Test", "value": 123}'),
            ("readme.md", "# Documentation\nThis is a readme."),
        ]
        
        for filename, content in files_to_create:
            file_path = os.path.join(temp_dir, filename)
            with open(file_path, 'w') as f:
                f.write(content)
        
        # Analyze directory
        txt_files = find_files_by_extension(temp_dir, ".txt")
        csv_files = find_files_by_extension(temp_dir, ".csv")
        json_files = find_files_by_extension(temp_dir, ".json")
        
        assert txt_files["count"] == 1
        assert csv_files["count"] == 1
        assert json_files["count"] == 1
        
        # Process each type of file
        if txt_files["files"]:
            txt_result = safe_read_text_file(txt_files["files"][0])
            assert txt_result["success"] == True
            assert txt_result["line_count"] == 2
        
        if csv_files["files"]:
            csv_result = read_csv_file(csv_files["files"][0])
            assert csv_result["success"] == True
            assert csv_result["row_count"] == 2
            assert len(csv_result["column_names"]) == 2
        
        if json_files["files"]:
            json_result = read_json_file(json_files["files"][0])
            assert json_result["success"] == True
            assert json_result["data"]["name"] == "Test"
        
        # Count total lines across all text files
        all_files = []
        for file_list in [txt_files["files"], csv_files["files"], json_files["files"]]:
            all_files.extend(file_list)
        
        line_count_result = count_lines_in_files(all_files)
        assert line_count_result["successful_files"] >= 3
        assert line_count_result["total_lines"] > 0

class TestErrorHandling:
    """Test error handling and edge cases."""
    
    def test_permission_errors(self):
        """Test handling of permission errors."""
        # This test might not work on all systems, so we'll simulate
        with patch('builtins.open', side_effect=PermissionError("Permission denied")):
            result = safe_read_text_file("some_file.txt")
            
            assert result["success"] == False
            assert "permission" in result["error"].lower()
    
    def test_large_file_handling(self, create_temp_file_with_content_fixture):
        """Test handling of large files."""
        # Create a moderately large file
        large_content = "Line content\n" * 10000  # 10,000 lines
        temp_file = create_temp_file_with_content_fixture(large_content)
        
        result = safe_read_text_file(temp_file)
        
        assert result["success"] == True  # Should handle reasonably large files
        assert result["line_count"] == 10000
    
    def test_binary_file_as_text(self, temp_dir):
        """Test reading binary file as text."""
        # Create a binary file
        binary_file = os.path.join(temp_dir, "binary.bin")
        with open(binary_file, 'wb') as f:
            f.write(b'\x00\x01\x02\x03\xFF\xFE\xFD')
        
        result = safe_read_text_file(binary_file)
        
        # Should handle gracefully (might succeed with garbled text or fail)
        assert isinstance(result, dict)
        assert "success" in result

class TestPerformance:
    """Test performance with various file sizes and operations."""
    
    @pytest.mark.slow
    def test_search_in_large_file(self, create_temp_file_with_content_fixture):
        """Test searching in a large file."""
        # Create file with many lines
        lines = [f"Line {i} with some content" for i in range(5000)]
        lines[2500] = "Line 2500 with SPECIAL content"  # Target line
        content = "\n".join(lines)
        
        temp_file = create_temp_file_with_content_fixture(content)
        
        result = search_text_in_file(temp_file, "SPECIAL")
        
        assert result["success"] == True
        assert result["matches_found"] == 1
        assert 2501 in result["line_numbers"]  # Line numbers are 1-based
    
    @pytest.mark.slow
    def test_process_many_files(self, temp_dir):
        """Test processing many files."""
        # Create many small files
        file_paths = []
        for i in range(100):
            filename = f"file_{i:03d}.txt"
            file_path = os.path.join(temp_dir, filename)
            with open(file_path, 'w') as f:
                f.write(f"Content of file {i}\nSecond line {i}")
            file_paths.append(file_path)
        
        # Count lines across all files
        result = count_lines_in_files(file_paths)
        
        assert result["successful_files"] == 100
        assert result["total_lines"] == 200  # 2 lines per file * 100 files
        assert result["failed_files"] == 0

if __name__ == "__main__":
    pytest.main([__file__])