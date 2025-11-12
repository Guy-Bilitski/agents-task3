"""
Translation Chain Experiment Runner

This script runs English sentences through a translation chain (EN->FR->HE->EN),
calculates spelling error ratios, embedding distances, and logs results to CSV.

Usage:
    python run_translation_experiments.py "Your sentence here"
    python run_translation_experiments.py --file sentences.txt
"""

import csv
import os
import sys
from pathlib import Path

# Import from utils module
from utils import calculate_spelling_error_ratio, calculate_embedding_distance


def run_translation_chain(sentence: str) -> dict:
    """
    Run a sentence through the full translation chain.
    
    NOTE: This is a placeholder. In practice, you would call the custom agents:
    - @en-fr for English to French
    - @fr-he for French to Hebrew  
    - @he-en for Hebrew to English
    
    For now, this returns a template that needs manual agent invocation.
    """
    print(f"\n{'='*70}")
    print(f"Starting translation chain for: {sentence}")
    print(f"{'='*70}\n")
    
    print("Step 1: Call the English to French agent")
    print(f"   @en-fr {sentence}")
    french = input("Enter French translation: ").strip()
    
    print("\nStep 2: Call the French to Hebrew agent")
    print(f"   @fr-he {french}")
    hebrew = input("Enter Hebrew translation: ").strip()
    
    print("\nStep 3: Call the Hebrew to English agent")
    print(f"   @he-en {hebrew}")
    final_english = input("Enter final English translation: ").strip()
    
    return {
        'original': sentence,
        'french': french,
        'hebrew': hebrew,
        'final_english': final_english
    }


def append_to_csv(result: dict, csv_path: str = 'translation_experiments.csv'):
    """Append experiment results to CSV file."""
    
    # Calculate metrics
    spelling_ratio = calculate_spelling_error_ratio(
        result['original'], 
        result['final_english']
    )
    
    embedding_dist = calculate_embedding_distance(
        result['original'],
        result['final_english']
    )
    
    # Prepare row
    row = {
        'original_sentence': result['original'],
        'spelling_error_ratio': f"{spelling_ratio:.4f}",
        'french_translation': result['french'],
        'hebrew_translation': result['hebrew'],
        'final_english_translation': result['final_english'],
        'embedding_distance': f"{embedding_dist:.6f}"
    }
    
    # Check if file exists
    file_exists = os.path.exists(csv_path)
    
    # Append to CSV
    with open(csv_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=row.keys())
        
        if not file_exists:
            writer.writeheader()
        
        writer.writerow(row)
    
    print(f"\n✓ Results appended to {csv_path}")
    print(f"  - Spelling error ratio: {spelling_ratio:.4f}")
    print(f"  - Embedding distance: {embedding_dist:.6f}")
    
    return row


def main():
    """Main execution function."""
    
    if len(sys.argv) < 2:
        print("Usage: python run_translation_experiments.py \"Your sentence here\"")
        print("   or: python run_translation_experiments.py --file sentences.txt")
        sys.exit(1)
    
    # Handle file input
    if sys.argv[1] == '--file':
        if len(sys.argv) < 3:
            print("Error: Please provide a file path")
            sys.exit(1)
        
        file_path = sys.argv[2]
        with open(file_path, 'r', encoding='utf-8') as f:
            sentences = [line.strip() for line in f if line.strip()]
    else:
        # Single sentence from command line
        sentences = [' '.join(sys.argv[1:])]
    
    # Process each sentence
    for sentence in sentences:
        result = run_translation_chain(sentence)
        append_to_csv(result)
        print()


if __name__ == '__main__':
    main()
