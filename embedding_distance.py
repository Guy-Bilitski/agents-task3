"""
Calculate embeddings distance between two English texts.
Uses sentence-transformers for generating embeddings and cosine similarity for distance.
"""

import numpy as np
from sentence_transformers import SentenceTransformer
from scipy.spatial.distance import cosine, euclidean


def calculate_embeddings_distance(text1: str, text2: str, model_name: str = 'all-MiniLM-L6-v2'):
    """
    Calculate the distance between embeddings of two texts.
    
    Args:
        text1: First text string
        text2: Second text string
        model_name: Name of the sentence transformer model to use
        
    Returns:
        dict: Dictionary containing cosine distance, cosine similarity, and euclidean distance
    """
    # Load the model
    model = SentenceTransformer(model_name)
    
    # Generate embeddings
    embedding1 = model.encode(text1)
    embedding2 = model.encode(text2)
    
    # Calculate distances
    cosine_dist = cosine(embedding1, embedding2)
    cosine_sim = 1 - cosine_dist
    euclidean_dist = euclidean(embedding1, embedding2)
    
    return {
        'cosine_distance': cosine_dist,
        'cosine_similarity': cosine_sim,
        'euclidean_distance': euclidean_dist
    }


def calculate_distance(text1: str, text2: str) -> float:
    """
    Simple wrapper that returns only cosine distance.
    Used for CSV logging.
    """
    results = calculate_embeddings_distance(text1, text2)
    return results['cosine_distance']


if __name__ == "__main__":
    import sys
    
    # Check for command-line arguments
    if len(sys.argv) == 3:
        text1 = sys.argv[1]
        text2 = sys.argv[2]
    else:
        # Example usage
        text1 = "The cat sits on the mat."
        text2 = "A feline rests on the rug."
    
    print("Text 1:", text1)
    print("Text 2:", text2)
    print("\nCalculating embeddings distance...\n")
    
    results = calculate_embeddings_distance(text1, text2)
    
    print(f"Cosine Distance: {results['cosine_distance']:.4f}")
    print(f"Cosine Similarity: {results['cosine_similarity']:.4f}")
    print(f"Euclidean Distance: {results['euclidean_distance']:.4f}")
