"""
Simple test script to verify Filtration module functionality
"""

from Filtration import FileFilter, DataFilter, TextFilter


def test_imports():
    """Test that all imports work correctly"""
    print("Testing imports...")
    
    # Test FileFilter
    ff = FileFilter("*.py")
    assert hasattr(ff, 'find_files')
    print("✓ FileFilter imported successfully")
    
    # Test DataFilter
    assert hasattr(DataFilter, 'filter_list')
    assert hasattr(DataFilter, 'filter_numeric')
    print("✓ DataFilter imported successfully")
    
    # Test TextFilter
    tf = TextFilter()
    assert hasattr(tf, 'clean_text')
    assert hasattr(tf, 'extract_words')
    print("✓ TextFilter imported successfully")


def test_basic_functionality():
    """Test basic functionality of each filter"""
    print("\nTesting basic functionality...")
    
    # Test DataFilter
    numbers = [1, 5, 10, 15, 20]
    filtered = DataFilter.filter_numeric(numbers, min_val=10)
    assert filtered == [10, 15, 20]
    print("✓ DataFilter.filter_numeric works")
    
    # Test TextFilter
    tf = TextFilter()
    text = "Hello, World! <p>Test</p>"
    cleaned = tf.clean_text(text)
    assert "hello world test" in cleaned.lower()
    print("✓ TextFilter.clean_text works")
    
    words = tf.extract_words("Hello world test")
    assert len(words) == 3
    print("✓ TextFilter.extract_words works")


def test_integration():
    """Test integration with repository files"""
    print("\nTesting integration...")
    
    # Test with actual files
    ff = FileFilter("*.txt")
    files = ff.find_files()
    print(f"✓ Found {len(files)} .txt files")
    
    if files:
        # Test file info extraction
        name, ext = ff.get_file_info(files[0])
        assert ext == '.txt'
        print("✓ File info extraction works")


if __name__ == "__main__":
    print("Filtration Module Test Suite")
    print("=" * 30)
    
    test_imports()
    test_basic_functionality()
    test_integration()
    
    print("\n🎉 All tests passed! Filtration module is working correctly.")