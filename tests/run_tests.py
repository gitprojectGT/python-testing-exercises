"""
Simple test runner script for Python exercises.
"""

import subprocess
import sys
import os
from pathlib import Path

def run_tests():
    """Run tests with proper setup."""
    
    # Get the project root directory
    project_root = Path(__file__).parent.parent
    os.chdir(project_root)
    
    print("🧪 Python Exercise Test Runner")
    print("=" * 50)
    print(f"Project Root: {project_root}")
    print(f"Python Version: {sys.version}")
    
    # Check if pytest is available
    try:
        import pytest
        print(f"Pytest Version: {pytest.__version__}")
    except ImportError:
        print("❌ pytest not found. Installing...")
        subprocess.run([sys.executable, "-m", "pip", "install", "pytest"])
        try:
            import pytest
            print(f"✅ Pytest installed: {pytest.__version__}")
        except ImportError:
            print("❌ Failed to install pytest")
            return 1
    
    print("\n📁 Available Test Categories:")
    print("  1. Basic exercises (5 exercises)")
    print("  2. Intermediate exercises (6 exercises)")  
    print("  3. Advanced exercises (6 exercises)")
    print("  4. All exercises")
    
    # Get user choice
    while True:
        choice = input("\nSelect category (1-4) or 'q' to quit: ").strip()
        
        if choice.lower() == 'q':
            return 0
        elif choice == '1':
            test_path = "tests/basic/"
            category = "Basic"
            break
        elif choice == '2':
            test_path = "tests/intermediate/"
            category = "Intermediate"
            break
        elif choice == '3':
            test_path = "tests/advanced/"
            category = "Advanced"
            break
        elif choice == '4':
            test_path = "tests/"
            category = "All"
            break
        else:
            print("Invalid choice. Please enter 1-4 or 'q'.")
    
    print(f"\n🚀 Running {category} Tests...")
    print("-" * 30)
    
    # Run pytest
    cmd = [
        sys.executable, "-m", "pytest", 
        test_path,
        "-v",  # verbose
        "--tb=short",  # shorter tracebacks
        "--color=yes"  # colored output
    ]
    
    try:
        result = subprocess.run(cmd, cwd=project_root)
        
        if result.returncode == 0:
            print("\n✅ All tests passed!")
        else:
            print(f"\n❌ Some tests failed (exit code: {result.returncode})")
            print("\n💡 Tips:")
            print("  - Tests are designed to fail until you implement the exercises")
            print("  - Look at the test failures to understand what needs to be implemented")
            print("  - Start with basic exercises and work your way up")
        
        return result.returncode
        
    except KeyboardInterrupt:
        print("\n⏹️  Tests interrupted by user")
        return 130
    except Exception as e:
        print(f"\n❌ Error running tests: {e}")
        return 1

if __name__ == "__main__":
    sys.exit(run_tests())