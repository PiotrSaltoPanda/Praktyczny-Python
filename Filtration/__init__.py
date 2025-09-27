"""
Filtration Module - Utilities for filtering and processing data

This module provides various filtering utilities for:
- File filtering and processing
- Data filtering and manipulation
- Text content filtering
- List filtering operations
"""

from .file_filter import FileFilter
from .data_filter import DataFilter
from .text_filter import TextFilter

__version__ = "1.0.0"
__all__ = ["FileFilter", "DataFilter", "TextFilter"]