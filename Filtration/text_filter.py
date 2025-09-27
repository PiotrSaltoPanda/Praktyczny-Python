"""
Text Filter Module - Utilities for filtering and processing text content

Based on the sentiment analysis and text processing functionality from M03 module.
"""

import re
from typing import List, Set, Optional, Dict


class TextFilter:
    """Class for filtering and processing text content"""
    
    DEFAULT_PUNCTUATION = ",<>/;:\\|()*!?."
    
    def __init__(self, punctuation: str = DEFAULT_PUNCTUATION):
        """
        Initialize TextFilter
        
        Args:
            punctuation: String of punctuation characters to filter
        """
        self.punctuation = punctuation
    
    def clean_text(self, text: str, to_lower: bool = True, 
                   remove_punctuation: bool = True, 
                   remove_html: bool = True) -> str:
        """
        Clean text by removing unwanted characters and formatting
        
        Args:
            text: Text to clean
            to_lower: Convert to lowercase
            remove_punctuation: Remove punctuation characters
            remove_html: Remove HTML tags
            
        Returns:
            Cleaned text
        """
        result = text
        
        if remove_html:
            result = result.replace('<br />', ' ')
            result = re.sub(r'<[^>]+>', '', result)
        
        if to_lower:
            result = result.lower()
            
        if remove_punctuation:
            for punct in self.punctuation:
                result = result.replace(punct, ' ')
        
        # Clean up extra whitespace
        result = ' '.join(result.split())
        
        return result
    
    def extract_words(self, text: str, min_length: int = 1) -> List[str]:
        """
        Extract words from text
        
        Args:
            text: Text to extract words from
            min_length: Minimum word length
            
        Returns:
            List of words
        """
        cleaned_text = self.clean_text(text)
        words = cleaned_text.split()
        
        return [word for word in words if len(word) >= min_length]
    
    def filter_words(self, words: List[str], 
                    min_length: Optional[int] = None,
                    max_length: Optional[int] = None,
                    exclude_words: Optional[Set[str]] = None,
                    include_only: Optional[Set[str]] = None) -> List[str]:
        """
        Filter a list of words based on various criteria
        
        Args:
            words: List of words to filter
            min_length: Minimum word length
            max_length: Maximum word length
            exclude_words: Set of words to exclude
            include_only: Set of words to include (if specified, only these words are kept)
            
        Returns:
            Filtered list of words
        """
        result = words.copy()
        
        if min_length is not None:
            result = [word for word in result if len(word) >= min_length]
            
        if max_length is not None:
            result = [word for word in result if len(word) <= max_length]
            
        if exclude_words:
            result = [word for word in result if word.lower() not in exclude_words]
            
        if include_only:
            result = [word for word in result if word.lower() in include_only]
            
        return result
    
    def word_frequency(self, text: str) -> Dict[str, int]:
        """
        Calculate word frequency in text
        
        Args:
            text: Text to analyze
            
        Returns:
            Dictionary with word frequencies
        """
        words = self.extract_words(text)
        frequency = {}
        
        for word in words:
            word_lower = word.lower()
            frequency[word_lower] = frequency.get(word_lower, 0) + 1
            
        return frequency
    
    def filter_by_pattern(self, text: str, pattern: str, 
                         keep_matches: bool = True) -> str:
        """
        Filter text based on a regular expression pattern
        
        Args:
            text: Text to filter
            pattern: Regular expression pattern
            keep_matches: If True, keep matches; if False, remove matches
            
        Returns:
            Filtered text
        """
        if keep_matches:
            matches = re.findall(pattern, text)
            return ' '.join(matches)
        else:
            return re.sub(pattern, '', text)
    
    def extract_sentences(self, text: str) -> List[str]:
        """
        Extract sentences from text
        
        Args:
            text: Text to extract sentences from
            
        Returns:
            List of sentences
        """
        # Split on sentence endings
        sentences = re.split(r'[.!?]+', text)
        
        # Clean and filter empty sentences
        result = []
        for sentence in sentences:
            cleaned = sentence.strip()
            if cleaned:
                result.append(cleaned)
                
        return result
    
    def filter_common_words(self, words: List[str], 
                           common_words: Optional[Set[str]] = None) -> List[str]:
        """
        Filter out common words (stop words)
        
        Args:
            words: List of words to filter
            common_words: Set of common words to remove (default: basic Polish/English stop words)
            
        Returns:
            Filtered list of words
        """
        if common_words is None:
            # Basic stop words in Polish and English
            common_words = {
                'i', 'a', 'o', 'w', 'na', 'do', 'z', 'ze', 'po', 'od', 'dla', 'przez',
                'się', 'nie', 'to', 'że', 'jak', 'co', 'tak', 'już', 'tylko',
                'the', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for', 'of', 'with',
                'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had'
            }
        
        return [word for word in words if word.lower() not in common_words]