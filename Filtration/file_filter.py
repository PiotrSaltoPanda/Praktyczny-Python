"""
File Filter Module - Utilities for filtering and processing files

Based on the existing file processing functionality in M03 module.
"""

import glob
import os
from typing import List, Tuple, Optional


class FileFilter:
    """Class for filtering and processing files"""
    
    def __init__(self, pattern: str = "*"):
        """
        Initialize FileFilter with a pattern
        
        Args:
            pattern: Glob pattern for file matching (default: "*")
        """
        self.pattern = pattern
        self.files = []
        
    def find_files(self, pattern: Optional[str] = None) -> List[str]:
        """
        Find files matching the pattern
        
        Args:
            pattern: Optional pattern to override the default
            
        Returns:
            List of matching filenames
        """
        search_pattern = pattern or self.pattern
        self.files = glob.glob(search_pattern)
        return self.files
    
    def filter_by_extension(self, extension: str) -> List[str]:
        """
        Filter files by extension
        
        Args:
            extension: File extension to filter by (e.g., '.txt', '.py')
            
        Returns:
            List of files with the specified extension
        """
        if not self.files:
            self.find_files()
            
        return [f for f in self.files if f.endswith(extension)]
    
    def get_file_info(self, filename: str) -> Tuple[str, str]:
        """
        Extract name and extension from filename
        
        Args:
            filename: Name of the file
            
        Returns:
            Tuple of (name, extension)
        """
        if '.' in filename:
            tokens = filename.rsplit('.', maxsplit=1)
            name = tokens[0]
            extension = '.' + tokens[1]
        else:
            name = filename
            extension = ''
        return name, extension
    
    def rename_files(self, new_extension: str, preview: bool = True) -> List[Tuple[str, str]]:
        """
        Rename files with a new extension
        
        Args:
            new_extension: New extension to apply
            preview: If True, only show what would be renamed
            
        Returns:
            List of (old_name, new_name) tuples
        """
        operations = []
        
        for filename in self.files:
            name, _ = self.get_file_info(filename)
            new_filename = name + new_extension
            operations.append((filename, new_filename))
            
            if not preview:
                os.rename(filename, new_filename)
        
        return operations
    
    def filter_by_size(self, min_size: int = 0, max_size: int = float('inf')) -> List[str]:
        """
        Filter files by size
        
        Args:
            min_size: Minimum file size in bytes
            max_size: Maximum file size in bytes
            
        Returns:
            List of files within the size range
        """
        if not self.files:
            self.find_files()
            
        filtered_files = []
        for filename in self.files:
            try:
                size = os.path.getsize(filename)
                if min_size <= size <= max_size:
                    filtered_files.append(filename)
            except OSError:
                continue
                
        return filtered_files