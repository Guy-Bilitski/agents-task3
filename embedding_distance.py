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


if __name__ == "__main__":
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
    
    # You can also provide your own texts
    print("\n" + "="*50)
    print("Provide your own texts:")
    user_text1 = input("\nEnter first text: ").strip()
    user_text2 = input("Enter second text: ").strip()
    
    if user_text1 and user_text2:
        results = calculate_embeddings_distance(user_text1, user_text2)
        print(f"\nCosine Distance: {results['cosine_distance']:.4f}")
        print(f"Cosine Similarity: {results['cosine_similarity']:.4f}")
        print(f"Euclidean Distance: {results['euclidean_distance']:.4f}")
