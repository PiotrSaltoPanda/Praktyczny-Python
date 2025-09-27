# Filtration Module

A comprehensive Python module for filtering and processing various types of data including files, data structures, and text content.

## Overview

The Filtration module provides three main components:

- **FileFilter**: Utilities for filtering and processing files
- **DataFilter**: Utilities for filtering data structures (lists, dictionaries, etc.)
- **TextFilter**: Utilities for filtering and processing text content

## Features

### FileFilter
- Find files using glob patterns
- Filter files by extension, size, and other criteria
- Extract file name and extension information
- Batch rename files with preview functionality

### DataFilter
- Filter lists based on custom conditions
- Filter dictionaries by keys and/or values
- Filter numeric data by range
- Filter strings by various criteria (length, content, patterns)
- Remove duplicates while preserving order
- Group data by specific keys

### TextFilter
- Clean text (remove HTML, punctuation, normalize case)
- Extract words and sentences from text
- Filter words by length and content
- Calculate word frequency
- Remove common stop words
- Filter text using regular expressions

## Usage Examples

### File Filtering

```python
from Filtration import FileFilter

# Create a file filter for .txt files
file_filter = FileFilter("*.txt")

# Find all matching files
txt_files = file_filter.find_files()

# Filter by size (files smaller than 1000 bytes)
small_files = file_filter.filter_by_size(max_size=1000)

# Preview file renaming
operations = file_filter.rename_files('.bak', preview=True)
```

### Data Filtering

```python
from Filtration import DataFilter

# Filter numeric data
numbers = [1, 5, 10, 15, 20, 25, 30]
filtered = DataFilter.filter_numeric(numbers, min_val=10, max_val=25)

# Filter strings
strings = ["hello", "world", "python", "test"]
long_strings = DataFilter.filter_strings(strings, min_length=5)

# Remove duplicates
unique_items = DataFilter.unique_values([1, 2, 2, 3, 3, 4])
```

### Text Filtering

```python
from Filtration import TextFilter

text_filter = TextFilter()

# Clean HTML and punctuation from text
cleaned = text_filter.clean_text("<p>Hello, world!</p>")

# Extract words
words = text_filter.extract_words("This is a sample text.")

# Filter words by length
long_words = text_filter.filter_words(words, min_length=4)

# Get word frequency
frequency = text_filter.word_frequency("hello world hello")
```

## Installation

Simply place the Filtration directory in your Python project and import the classes you need.

## Requirements

- Python 3.6+
- No external dependencies required

## Examples

Run the `examples.py` file to see all functionality in action:

```bash
python examples.py
```

## Module Structure

```
Filtration/
├── __init__.py          # Module initialization
├── file_filter.py       # File filtering utilities
├── data_filter.py       # Data structure filtering utilities
├── text_filter.py       # Text processing utilities
├── examples.py          # Usage examples
└── README.md           # This documentation
```

## License

This module is part of the Praktyczny-Python repository and follows the same licensing terms.