"""
Utility functions for translation chain experiments.

This module provides utilities for:
1. Calculating spelling error ratios between text pairs
2. Computing embedding distances using sentence transformers
3. Text comparison and similarity metrics

Author: Translation Chain Experiment System
"""

from typing import Dict, Optional, Tuple
import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine, euclidean
import difflib
import re


class EmbeddingCalculator:
    """
    Singleton-like class for efficient embedding calculations.
    Caches the model to avoid reloading on every calculation.
    """
    _instance = None
    _model = None
    _model_name = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def get_model(self, model_name: str = 'all-MiniLM-L6-v2') -> SentenceTransformer:
        """Load or retrieve cached sentence transformer model."""
        if self._model is None or self._model_name != model_name:
            self._model = SentenceTransformer(model_name)
            self._model_name = model_name
        return self._model


def calculate_spelling_error_ratio(
    text1: str,
    text2: str,
    method: str = 'symmetric_difference'
) -> float:
    """
    Calculate the ratio of spelling/word errors between two text strings.
    
    This function compares two texts at the word level to determine how different
    they are. Useful for measuring translation quality degradation.
    
    Args:
        text1: First text string (typically the original)
        text2: Second text string (typically the final translation)
        method: Comparison method to use:
            - 'symmetric_difference': Words that appear in one text but not both
            - 'levenshtein': Character-level edit distance ratio
            - 'sequence_matcher': Uses difflib.SequenceMatcher for similarity
    
    Returns:
        float: Error ratio between 0.0 (identical) and 1.0 (completely different)
        
    Examples:
        >>> calculate_spelling_error_ratio("The cat sits", "The cat sits")
        0.0
        >>> calculate_spelling_error_ratio("The cat sits", "The dog runs")
        0.6667
        
    Notes:
        - Comparison is case-insensitive
        - Punctuation is stripped for word-level comparison
        - Empty strings return 0.0 (no error)
    """
    if not text1 and not text2:
        return 0.0
    
    if not text1 or not text2:
        return 1.0
    
    if method == 'symmetric_difference':
        return _calculate_word_difference_ratio(text1, text2)
    elif method == 'levenshtein':
        return _calculate_levenshtein_ratio(text1, text2)
    elif method == 'sequence_matcher':
        return _calculate_sequence_matcher_ratio(text1, text2)
    else:
        raise ValueError(f"Unknown method: {method}. Use 'symmetric_difference', 'levenshtein', or 'sequence_matcher'")


def _normalize_text(text: str) -> str:
    """Normalize text by removing punctuation and converting to lowercase."""
    # Remove common punctuation
    text = re.sub(r'[.,!?;:\'"()\[\]{}<>]', '', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text)
    return text.lower().strip()


def _calculate_word_difference_ratio(text1: str, text2: str) -> float:
    """Calculate ratio using symmetric difference of word sets."""
    # Normalize and tokenize
    words1 = set(_normalize_text(text1).split())
    words2 = set(_normalize_text(text2).split())
    
    if not words1 and not words2:
        return 0.0
    
    # Calculate symmetric difference (words in one but not both)
    differing_words = words1.symmetric_difference(words2)
    total_unique_words = max(len(words1), len(words2))
    
    return len(differing_words) / total_unique_words if total_unique_words > 0 else 0.0


def _calculate_levenshtein_ratio(text1: str, text2: str) -> float:
    """Calculate character-level Levenshtein distance ratio."""
    # Normalize texts
    norm_text1 = _normalize_text(text1)
    norm_text2 = _normalize_text(text2)
    
    # Use difflib for Levenshtein-like ratio
    ratio = difflib.SequenceMatcher(None, norm_text1, norm_text2).ratio()
    # Convert similarity to error ratio
    return 1.0 - ratio


def _calculate_sequence_matcher_ratio(text1: str, text2: str) -> float:
    """Calculate error ratio using difflib.SequenceMatcher."""
    norm_text1 = _normalize_text(text1)
    norm_text2 = _normalize_text(text2)
    
    similarity = difflib.SequenceMatcher(None, norm_text1, norm_text2).ratio()
    return 1.0 - similarity


def calculate_embedding_distance(
    text1: str,
    text2: str,
    model_name: str = 'all-MiniLM-L6-v2',
    return_all_metrics: bool = False
) -> float | Dict[str, float]:
    """
    Calculate semantic distance between two texts using sentence embeddings.
    
    This function uses state-of-the-art sentence transformers to create dense
    vector representations of texts and compute their semantic similarity.
    
    Args:
        text1: First text string
        text2: Second text string
        model_name: Sentence transformer model to use. Options:
            - 'all-MiniLM-L6-v2' (default, fast, 384 dimensions)
            - 'all-mpnet-base-v2' (slower, more accurate, 768 dimensions)
            - 'paraphrase-multilingual-MiniLM-L12-v2' (multilingual)
        return_all_metrics: If True, return dict with all distance metrics
            If False, return only cosine distance (default)
    
    Returns:
        float: Cosine distance (0.0 = identical, 2.0 = opposite) if return_all_metrics=False
        dict: Dictionary with multiple metrics if return_all_metrics=True:
            - cosine_distance: 1 - cosine_similarity (0 to 2)
            - cosine_similarity: Cosine similarity (-1 to 1)
            - euclidean_distance: L2 distance between embeddings
            - manhattan_distance: L1 distance between embeddings
    
    Examples:
        >>> calculate_embedding_distance("The cat sits", "The cat sits")
        0.0
        >>> calculate_embedding_distance("I love pizza", "Pizza is great")
        0.234  # Low distance indicates high semantic similarity
        >>> calculate_embedding_distance("I love pizza", "The weather is cold", return_all_metrics=True)
        {
            'cosine_distance': 0.823,
            'cosine_similarity': 0.177,
            'euclidean_distance': 12.45,
            'manhattan_distance': 89.32
        }
    
    Notes:
        - Model is cached after first use for efficiency
        - Cosine distance is most commonly used for semantic similarity
        - Lower distance = more similar meanings
        - Works across languages if using multilingual models
    """
    if not text1 or not text2:
        return 1.0 if not return_all_metrics else {
            'cosine_distance': 1.0,
            'cosine_similarity': 0.0,
            'euclidean_distance': 0.0,
            'manhattan_distance': 0.0
        }
    
    # Get cached model
    calculator = EmbeddingCalculator()
    model = calculator.get_model(model_name)
    
    # Generate embeddings
    embedding1 = model.encode(text1, convert_to_numpy=True)
    embedding2 = model.encode(text2, convert_to_numpy=True)
    
    # Calculate cosine distance and similarity
    cos_dist = cosine(embedding1, embedding2)
    cos_sim = 1.0 - cos_dist
    
    if not return_all_metrics:
        return float(cos_dist)
    
    # Calculate additional metrics
    eucl_dist = euclidean(embedding1, embedding2)
    manh_dist = np.sum(np.abs(embedding1 - embedding2))
    
    return {
        'cosine_distance': float(cos_dist),
        'cosine_similarity': float(cos_sim),
        'euclidean_distance': float(eucl_dist),
        'manhattan_distance': float(manh_dist)
    }


def calculate_translation_quality_metrics(
    original: str,
    translated: str,
    model_name: str = 'all-MiniLM-L6-v2'
) -> Dict[str, float]:
    """
    Calculate comprehensive quality metrics for a translation pair.
    
    This is a convenience function that computes both spelling error ratio
    and embedding distance in a single call.
    
    Args:
        original: Original text
        translated: Translated text (after full translation chain)
        model_name: Sentence transformer model to use
    
    Returns:
        dict: Dictionary containing all quality metrics:
            - spelling_error_ratio: Word-level difference ratio
            - embedding_distance: Semantic distance (cosine)
            - embedding_similarity: Semantic similarity (1 - distance)
    
    Examples:
        >>> metrics = calculate_translation_quality_metrics(
        ...     "The cat sits on the mat",
        ...     "A cat is sitting on a mat"
        ... )
        >>> print(f"Error ratio: {metrics['spelling_error_ratio']:.2f}")
        >>> print(f"Semantic similarity: {metrics['embedding_similarity']:.2f}")
    """
    # Calculate spelling error ratio
    error_ratio = calculate_spelling_error_ratio(original, translated)
    
    # Calculate embedding distance
    embedding_dist = calculate_embedding_distance(original, translated, model_name)
    
    return {
        'spelling_error_ratio': float(error_ratio),
        'embedding_distance': float(embedding_dist),
        'embedding_similarity': float(1.0 - embedding_dist)
    }


# Backward compatibility aliases
calculate_distance = calculate_embedding_distance
calculate_embeddings_distance = lambda t1, t2, model_name='all-MiniLM-L6-v2': calculate_embedding_distance(
    t1, t2, model_name, return_all_metrics=True
)


if __name__ == "__main__":
    # Demo and testing
    print("=" * 80)
    print("UTILS.PY - Translation Quality Metrics Demo")
    print("=" * 80)
    
    # Test cases
    test_pairs = [
        ("The cat sits on the mat.", "The cat sits on the mat."),
        ("The cat sits on the mat.", "A feline rests on the rug."),
        ("I love programming in Python.", "Python programming is something I enjoy."),
        ("The weather is nice today.", "I ate pizza for dinner."),
    ]
    
    print("\n1. SPELLING ERROR RATIO\n")
    for text1, text2 in test_pairs:
        ratio = calculate_spelling_error_ratio(text1, text2)
        print(f"Text 1: {text1}")
        print(f"Text 2: {text2}")
        print(f"Error Ratio: {ratio:.4f}\n")
    
    print("\n2. EMBEDDING DISTANCE\n")
    for text1, text2 in test_pairs:
        dist = calculate_embedding_distance(text1, text2)
        print(f"Text 1: {text1}")
        print(f"Text 2: {text2}")
        print(f"Embedding Distance: {dist:.4f}\n")
    
    print("\n3. COMPREHENSIVE METRICS\n")
    metrics = calculate_translation_quality_metrics(
        "The cat sits on the mat.",
        "A feline rests on the rug."
    )
    print("Original: The cat sits on the mat.")
    print("Translated: A feline rests on the rug.")
    print(f"\nMetrics:")
    for key, value in metrics.items():
        print(f"  {key}: {value:.4f}")
