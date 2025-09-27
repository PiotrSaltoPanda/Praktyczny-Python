"""
Demo script showing Filtration module working with existing repository files
"""

import os
import sys

# Add parent directory to path to import from Filtration
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from Filtration import FileFilter, DataFilter, TextFilter


def demo_with_repository_files():
    """Demonstrate filtration with actual repository files"""
    print("=== Filtration Demo with Repository Files ===\n")
    
    # Change to the repository root
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    os.chdir(repo_root)
    
    # File filtering demo
    print("1. File Filtering:")
    file_filter = FileFilter("*.txt")
    txt_files = file_filter.find_files()
    print(f"   Found {len(txt_files)} .txt files in repository")
    
    # Show file sizes
    small_files = file_filter.filter_by_size(max_size=200)
    large_files = file_filter.filter_by_size(min_size=200)
    print(f"   Small files (< 200 bytes): {len(small_files)}")
    print(f"   Large files (>= 200 bytes): {len(large_files)}")
    
    # Python files filtering
    py_filter = FileFilter("**/*.py")
    py_files = py_filter.find_files()
    print(f"   Found {len(py_files)} .py files in repository")
    
    # Filter Python files by directory
    m03_files = [f for f in py_files if 'M03' in f]
    zadanie_files = [f for f in py_files if 'zadanie' in f]
    print(f"   Python files in M03: {len(m03_files)}")
    print(f"   Python files in zadanie: {len(zadanie_files)}")
    
    # Text processing demo
    print("\n2. Text Processing:")
    if txt_files:
        sample_file = txt_files[0]
        print(f"   Processing file: {sample_file}")
        
        try:
            with open(sample_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            text_filter = TextFilter()
            words = text_filter.extract_words(content)
            print(f"   Total words: {len(words)}")
            
            if words:
                long_words = text_filter.filter_words(words, min_length=5)
                print(f"   Words with 5+ characters: {len(long_words)}")
                
                frequency = text_filter.word_frequency(content)
                top_words = sorted(frequency.items(), key=lambda x: x[1], reverse=True)[:3]
                print(f"   Top 3 words: {top_words}")
        
        except Exception as e:
            print(f"   Could not process file: {e}")
    
    # Data filtering demo with file extensions
    print("\n3. Data Structure Filtering:")
    all_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            all_files.append(file)
    
    extensions = []
    for file in all_files:
        if '.' in file:
            _, ext = os.path.splitext(file)
            extensions.append(ext)
    
    unique_extensions = DataFilter.unique_values(extensions)
    print(f"   File extensions found: {sorted(unique_extensions)}")
    
    # Filter by extension type
    code_extensions = [ext for ext in unique_extensions 
                      if ext in {'.py', '.html', '.js', '.css', '.ipynb'}]
    print(f"   Code file extensions: {code_extensions}")


if __name__ == "__main__":
    demo_with_repository_files()