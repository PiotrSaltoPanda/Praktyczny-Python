"""
Data Filter Module - Utilities for filtering and processing data structures

Provides filtering functionality for lists, dictionaries, and other data structures.
"""

from typing import List, Dict, Any, Callable, Optional, Union


class DataFilter:
    """Class for filtering various data structures"""
    
    @staticmethod
    def filter_list(data: List[Any], condition: Callable[[Any], bool]) -> List[Any]:
        """
        Filter a list based on a condition function
        
        Args:
            data: List to filter
            condition: Function that returns True for items to keep
            
        Returns:
            Filtered list
        """
        return [item for item in data if condition(item)]
    
    @staticmethod
    def filter_dict(data: Dict[str, Any], key_condition: Optional[Callable[[str], bool]] = None,
                   value_condition: Optional[Callable[[Any], bool]] = None) -> Dict[str, Any]:
        """
        Filter a dictionary based on key and/or value conditions
        
        Args:
            data: Dictionary to filter
            key_condition: Function to filter keys
            value_condition: Function to filter values
            
        Returns:
            Filtered dictionary
        """
        result = {}
        
        for key, value in data.items():
            keep_key = key_condition(key) if key_condition else True
            keep_value = value_condition(value) if value_condition else True
            
            if keep_key and keep_value:
                result[key] = value
                
        return result
    
    @staticmethod
    def filter_numeric(data: List[Union[int, float]], 
                      min_val: Optional[Union[int, float]] = None,
                      max_val: Optional[Union[int, float]] = None) -> List[Union[int, float]]:
        """
        Filter numeric data by range
        
        Args:
            data: List of numeric values
            min_val: Minimum value (inclusive)
            max_val: Maximum value (inclusive)
            
        Returns:
            Filtered list of numeric values
        """
        result = data.copy()
        
        if min_val is not None:
            result = [x for x in result if x >= min_val]
        
        if max_val is not None:
            result = [x for x in result if x <= max_val]
            
        return result
    
    @staticmethod
    def filter_strings(data: List[str], 
                      contains: Optional[str] = None,
                      starts_with: Optional[str] = None,
                      ends_with: Optional[str] = None,
                      min_length: Optional[int] = None,
                      max_length: Optional[int] = None) -> List[str]:
        """
        Filter strings based on various criteria
        
        Args:
            data: List of strings to filter
            contains: String must contain this substring
            starts_with: String must start with this prefix
            ends_with: String must end with this suffix
            min_length: Minimum string length
            max_length: Maximum string length
            
        Returns:
            Filtered list of strings
        """
        result = data.copy()
        
        if contains:
            result = [s for s in result if contains in s]
            
        if starts_with:
            result = [s for s in result if s.startswith(starts_with)]
            
        if ends_with:
            result = [s for s in result if s.endswith(ends_with)]
            
        if min_length is not None:
            result = [s for s in result if len(s) >= min_length]
            
        if max_length is not None:
            result = [s for s in result if len(s) <= max_length]
            
        return result
    
    @staticmethod
    def unique_values(data: List[Any]) -> List[Any]:
        """
        Get unique values from a list while preserving order
        
        Args:
            data: List with potential duplicates
            
        Returns:
            List with unique values in original order
        """
        seen = set()
        result = []
        
        for item in data:
            if item not in seen:
                seen.add(item)
                result.append(item)
                
        return result
    
    @staticmethod
    def group_by(data: List[Dict[str, Any]], key: str) -> Dict[str, List[Dict[str, Any]]]:
        """
        Group list of dictionaries by a specific key
        
        Args:
            data: List of dictionaries
            key: Key to group by
            
        Returns:
            Dictionary with grouped data
        """
        groups = {}
        
        for item in data:
            if key in item:
                group_key = str(item[key])
                if group_key not in groups:
                    groups[group_key] = []
                groups[group_key].append(item)
                
        return groups