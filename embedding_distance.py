"""
Calculate embeddings distance between two English texts.
DEPRECATED: This module is maintained for backward compatibility.
Please use utils.py for all new code.
"""

# Import from utils for backward compatibility
from utils import (
    calculate_embedding_distance,
    calculate_embeddings_distance,
    calculate_distance
)


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
