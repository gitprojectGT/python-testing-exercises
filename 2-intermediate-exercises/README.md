# Intermediate Python Exercises for Software Testers

## Overview
These exercises build upon basic concepts and introduce more complex testing scenarios, object-oriented programming, data structures, and real-world testing applications.

## Prerequisites
- Completion of basic exercises
- Understanding of Python classes and objects
- Familiarity with JSON and CSV data formats
- Basic knowledge of testing concepts

## Exercise List

### 1. Test Data Generator (`01_test_data_generator.py`)
**Concept**: Generating realistic test data for various scenarios
**Testing Focus**: Data generation, parameterized testing, boundary value analysis
**Skills**: Random data generation, data validation, configuration management

### 2. API Response Parser (`02_api_response_parser.py`)
**Concept**: Parsing and validating API responses
**Testing Focus**: JSON validation, schema validation, error handling
**Skills**: JSON manipulation, data structure validation, error reporting

### 3. Test Case Manager (`03_test_case_manager.py`)
**Concept**: Managing test cases and execution results
**Testing Focus**: Test organization, result tracking, reporting
**Skills**: Class design, data persistence, result analysis

### 4. Configuration Validator (`04_config_validator.py`)
**Concept**: Validating application configurations
**Testing Focus**: Configuration testing, environment validation
**Skills**: Schema validation, type checking, error reporting

### 5. Log File Analyzer (`05_log_analyzer.py`)
**Concept**: Analyzing application logs for patterns and issues
**Testing Focus**: Log analysis, pattern matching, performance monitoring
**Skills**: Regular expressions, data aggregation, statistical analysis

### 6. Database Mock (`06_database_mock.py`)
**Concept**: Creating mock database operations for testing
**Testing Focus**: Mock objects, database testing, CRUD operations
**Skills**: Object-oriented design, data modeling, transaction simulation

## Running the Exercises

1. Navigate to the intermediate exercises directory:
   ```bash
   cd 2-intermediate-exercises
   ```

2. Run individual exercises:
   ```bash
   python 01_test_data_generator.py
   ```

3. Run with different parameters:
   ```bash
   python 01_test_data_generator.py --count 100 --type user
   ```

4. Run tests:
   ```bash
   python -m pytest test_*.py -v
   ```

## Learning Objectives
By completing these exercises, you will:
- Master object-oriented programming concepts
- Learn to work with complex data structures
- Understand mock objects and test doubles
- Practice data validation and schema checking
- Develop skills in log analysis and pattern matching
- Create reusable test utilities and frameworks
- Build experience with configuration management

## Integration with Testing Frameworks
These exercises are designed to integrate with popular testing frameworks:
- **pytest**: For unit testing and parameterized tests
- **unittest.mock**: For creating mock objects
- **jsonschema**: For JSON validation
- **faker**: For generating realistic test data