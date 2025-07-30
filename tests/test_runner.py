"""
Custom Test Runner for Python Exercises

This script provides a convenient way to run tests for specific exercises or levels.
"""

import argparse
import subprocess
import sys
import os
from pathlib import Path
import json
from datetime import datetime
from typing import Dict, List, Optional

class TestRunner:
    """Custom test runner for Python exercises."""
    
    def __init__(self):
        """Initialize the test runner."""
        self.base_dir = Path(__file__).parent
        self.project_root = self.base_dir.parent
        self.test_levels = {
            'basic': self.base_dir / 'basic',
            'intermediate': self.base_dir / 'intermediate',
            'advanced': self.base_dir / 'advanced'
        }
        
    def discover_tests(self, level: Optional[str] = None, exercise: Optional[str] = None) -> List[Path]:
        """
        Discover test files based on criteria.
        
        Args:
            level: Test level (basic, intermediate, advanced)
            exercise: Specific exercise name (e.g., "01_string_validation")
            
        Returns:
            List of test file paths
        """
        test_files = []
        
        if exercise:
            # Look for specific exercise across all levels
            for level_name, level_path in self.test_levels.items():
                test_file = level_path / f"test_{exercise}.py"
                if test_file.exists():
                    test_files.append(test_file)
        elif level:
            # Look for all tests in specific level
            if level in self.test_levels:
                level_path = self.test_levels[level]
                test_files.extend(level_path.glob("test_*.py"))
        else:
            # All tests
            for level_path in self.test_levels.values():
                test_files.extend(level_path.glob("test_*.py"))
                
        return sorted(test_files)
    
    def run_pytest(self, test_files: List[Path], verbose: bool = True, 
                   coverage: bool = False, html_report: bool = False,
                   markers: Optional[str] = None, timeout: Optional[int] = None) -> int:
        """
        Run pytest with specified options.
        
        Args:
            test_files: List of test files to run
            verbose: Use verbose output
            coverage: Generate coverage report
            html_report: Generate HTML coverage report
            markers: Pytest markers to use (e.g., "not slow")
            timeout: Test timeout in seconds
            
        Returns:
            Exit code from pytest
        """
        if not test_files:
            print("No test files found!")
            return 1
            
        cmd = [sys.executable, "-m", "pytest"]
        
        # Add test files
        cmd.extend(str(f) for f in test_files)
        
        # Add options
        if verbose:
            cmd.append("-v")
            
        if coverage:
            cmd.extend(["--cov=.", "--cov-report=term-missing"])
            if html_report:
                cmd.append("--cov-report=html")
                
        if markers:
            cmd.extend(["-m", markers])
            
        if timeout:
            cmd.extend(["--timeout", str(timeout)])
            
        # Add color output
        cmd.append("--color=yes")
        
        # Set working directory to project root
        print(f"Running command: {' '.join(cmd)}")
        print(f"Test files: {len(test_files)} files")
        print("-" * 50)
        
        try:
            result = subprocess.run(cmd, cwd=self.project_root)
            return result.returncode
        except KeyboardInterrupt:
            print("\nTests interrupted by user")
            return 130
    
    def generate_test_report(self, level: Optional[str] = None) -> Dict:
        """
        Generate a test discovery report.
        
        Args:
            level: Specific level to report on
            
        Returns:
            Dictionary with test information
        """
        report = {
            "timestamp": datetime.now().isoformat(),
            "levels": {}
        }
        
        levels_to_check = [level] if level else self.test_levels.keys()
        
        for level_name in levels_to_check:
            if level_name not in self.test_levels:
                continue
                
            level_path = self.test_levels[level_name]
            test_files = list(level_path.glob("test_*.py"))
            
            exercises = []
            for test_file in sorted(test_files):
                # Extract exercise name from filename
                name = test_file.stem
                if name.startswith("test_"):
                    exercise_name = name[5:]  # Remove "test_" prefix
                    exercises.append({
                        "name": exercise_name,
                        "file": str(test_file.relative_to(self.base_dir)),
                        "size": test_file.stat().st_size
                    })
            
            report["levels"][level_name] = {
                "path": str(level_path.relative_to(self.base_dir)),
                "test_count": len(exercises),
                "exercises": exercises
            }
        
        return report
    
    def list_exercises(self, level: Optional[str] = None) -> None:
        """
        List available exercises.
        
        Args:
            level: Specific level to list
        """
        report = self.generate_test_report(level)
        
        print("Available Exercises:")
        print("=" * 50)
        
        for level_name, level_info in report["levels"].items():
            print(f"\n{level_name.upper()} ({level_info['test_count']} exercises):")
            print("-" * 30)
            
            for exercise in level_info["exercises"]:
                size_kb = exercise["size"] / 1024
                print(f"  {exercise['name']:<30} ({size_kb:.1f} KB)")
        
        total_exercises = sum(info["test_count"] for info in report["levels"].values())
        print(f"\nTotal: {total_exercises} exercises across {len(report['levels'])} levels")
    
    def validate_setup(self) -> bool:
        """
        Validate that the test environment is set up correctly.
        
        Returns:
            True if setup is valid
        """
        issues = []
        
        # Check test directories exist
        for level_name, level_path in self.test_levels.items():
            if not level_path.exists():
                issues.append(f"Missing test directory: {level_path}")
        
        # Check conftest.py exists
        conftest_path = self.base_dir / "conftest.py"
        if not conftest_path.exists():
            issues.append(f"Missing conftest.py: {conftest_path}")
        
        # Check if pytest is available
        try:
            import pytest
        except ImportError:
            issues.append("pytest is not installed. Run: pip install pytest")
        
        # Check project structure
        exercise_dirs = [
            self.project_root / "1-basic-exercises",
            self.project_root / "2-intermediate-exercises", 
            self.project_root / "3-advanced-exercises"
        ]
        
        for exercise_dir in exercise_dirs:
            if not exercise_dir.exists():
                issues.append(f"Missing exercise directory: {exercise_dir}")
        
        if issues:
            print("Setup Issues Found:")
            print("=" * 30)
            for issue in issues:
                print(f"  ❌ {issue}")
            print("\nPlease fix these issues before running tests.")
            return False
        else:
            print("✅ Test environment setup is valid!")
            return True

def main():
    """Main entry point for the test runner."""
    parser = argparse.ArgumentParser(
        description="Run tests for Python exercises",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python test_runner.py --all                    # Run all tests
  python test_runner.py --level basic            # Run basic level tests
  python test_runner.py --exercise 01_string_validation  # Run specific exercise
  python test_runner.py --level intermediate --coverage  # Run with coverage
  python test_runner.py --level advanced --markers "not slow"  # Skip slow tests
  python test_runner.py --list                   # List available exercises
  python test_runner.py --validate               # Validate test environment
        """
    )
    
    # Test selection arguments
    parser.add_argument("--all", action="store_true", 
                       help="Run all tests")
    parser.add_argument("--level", choices=["basic", "intermediate", "advanced"],
                       help="Run tests for specific level")
    parser.add_argument("--exercise", 
                       help="Run tests for specific exercise (e.g., 01_string_validation)")
    
    # Test execution options
    parser.add_argument("--coverage", action="store_true",
                       help="Generate coverage report")
    parser.add_argument("--html", action="store_true",
                       help="Generate HTML coverage report (requires --coverage)")
    parser.add_argument("--markers", 
                       help="Pytest markers (e.g., 'not slow', 'unit')")
    parser.add_argument("--timeout", type=int,
                       help="Test timeout in seconds")
    parser.add_argument("--quiet", action="store_true",
                       help="Quiet output (less verbose)")
    
    # Utility arguments
    parser.add_argument("--list", action="store_true",
                       help="List available exercises")
    parser.add_argument("--validate", action="store_true", 
                       help="Validate test environment setup")
    parser.add_argument("--report", action="store_true",
                       help="Generate test discovery report")
    
    args = parser.parse_args()
    
    runner = TestRunner()
    
    # Handle utility commands
    if args.validate:
        return 0 if runner.validate_setup() else 1
    
    if args.list:
        runner.list_exercises(args.level)
        return 0
    
    if args.report:
        report = runner.generate_test_report(args.level)
        print(json.dumps(report, indent=2))
        return 0
    
    # Validate setup before running tests
    if not runner.validate_setup():
        return 1
    
    # Discover tests
    test_files = []
    
    if args.all:
        test_files = runner.discover_tests()
    elif args.level:
        test_files = runner.discover_tests(level=args.level)
    elif args.exercise:
        test_files = runner.discover_tests(exercise=args.exercise)
    else:
        # Default to basic level if no specific option given
        print("No test selection specified. Use --help for options.")
        parser.print_help()
        return 1
    
    if not test_files:
        print("No test files found matching criteria!")
        return 1
    
    # Run tests
    return runner.run_pytest(
        test_files=test_files,
        verbose=not args.quiet,
        coverage=args.coverage,
        html_report=args.html,
        markers=args.markers,
        timeout=args.timeout
    )

if __name__ == "__main__":
    sys.exit(main())