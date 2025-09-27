"""
Examples demonstrating the Filtration module functionality

Run this script to see various filtering operations in action.
"""

import os
from file_filter import FileFilter
from data_filter import DataFilter
from text_filter import TextFilter


def demo_file_filtering():
    """Demonstrate file filtering capabilities"""
    print("=== File Filtering Demo ===")
    
    # Create a FileFilter instance
    file_filter = FileFilter("*.txt")
    
    # Find all .txt files
    txt_files = file_filter.find_files()
    print(f"Found {len(txt_files)} .txt files:")
    for file in txt_files[:5]:  # Show first 5
        print(f"  - {file}")
    if len(txt_files) > 5:
        print(f"  ... and {len(txt_files) - 5} more")
    
    # Filter by size (files smaller than 1000 bytes)
    small_files = file_filter.filter_by_size(max_size=1000)
    print(f"\nSmall files (< 1000 bytes): {len(small_files)}")
    
    # Demonstrate file info extraction
    if txt_files:
        sample_file = txt_files[0]
        name, ext = file_filter.get_file_info(sample_file)
        print(f"\nSample file '{sample_file}':")
        print(f"  Name: {name}")
        print(f"  Extension: {ext}")
    
    print()


def demo_data_filtering():
    """Demonstrate data filtering capabilities"""
    print("=== Data Filtering Demo ===")
    
    # Sample data
    numbers = [1, 5, 10, 15, 20, 25, 30, 35, 40]
    strings = ["hello", "world", "python", "filtering", "data", "test"]
    
    # Filter numeric data
    filtered_numbers = DataFilter.filter_numeric(numbers, min_val=10, max_val=30)
    print(f"Numbers between 10-30: {filtered_numbers}")
    
    # Filter strings
    long_strings = DataFilter.filter_strings(strings, min_length=5)
    print(f"Strings with 5+ characters: {long_strings}")
    
    # Filter strings containing specific text
    python_related = DataFilter.filter_strings(strings, contains="th")
    print(f"Strings containing 'th': {python_related}")
    
    # Unique values demo
    duplicated_list = [1, 2, 2, 3, 3, 3, 4, 5, 5]
    unique_list = DataFilter.unique_values(duplicated_list)
    print(f"Original: {duplicated_list}")
    print(f"Unique: {unique_list}")
    
    # Dictionary filtering
    sample_dict = {
        "name": "Jan",
        "age": 25,
        "city": "Warsaw",
        "score": 85,
        "active": True
    }
    
    # Filter by value type
    string_values = DataFilter.filter_dict(
        sample_dict, 
        value_condition=lambda x: isinstance(x, str)
    )
    print(f"\nString values only: {string_values}")
    
    print()


def demo_text_filtering():
    """Demonstrate text filtering capabilities"""
    print("=== Text Filtering Demo ===")
    
    # Sample text with HTML and punctuation
    sample_text = """
    <p>To jest przykład tekstu z <br />znacznikami HTML i różnymi znakami!
    Czy można go dobrze przefiltrować? Oczywiście, że tak.</p>
    """
    
    text_filter = TextFilter()
    
    # Clean text
    cleaned = text_filter.clean_text(sample_text)
    print("Original text:")
    print(sample_text.strip())
    print(f"\nCleaned text: {cleaned}")
    
    # Extract words
    words = text_filter.extract_words(sample_text)
    print(f"\nExtracted words: {words}")
    
    # Filter words by length
    long_words = text_filter.filter_words(words, min_length=4)
    print(f"Words with 4+ characters: {long_words}")
    
    # Word frequency
    frequency = text_filter.word_frequency(sample_text)
    print(f"\nWord frequency: {dict(list(frequency.items())[:5])}")
    
    # Filter common words
    content_words = text_filter.filter_common_words(words)
    print(f"Content words (no stop words): {content_words}")
    
    # Extract sentences
    sentences = text_filter.extract_sentences(sample_text)
    print(f"\nSentences found: {len(sentences)}")
    for i, sentence in enumerate(sentences, 1):
        print(f"  {i}. {sentence}")
    
    print()


def main():
    """Run all demonstrations"""
    print("Filtration Module Demonstration")
    print("=" * 40)
    print()
    
    demo_file_filtering()
    demo_data_filtering()
    demo_text_filtering()
    
    print("Demo completed!")


if __name__ == "__main__":
    main()