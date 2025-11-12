# Translation Chain Experiments - Instructions

This project implements a translation chain (English → French → Hebrew → English) with automated experiment tracking and analysis using AI agents.

## Overview

The system tests how well meaning is preserved when translating through multiple languages. Each experiment:
1. Takes an English sentence (possibly with spelling errors)
2. Translates it through French and Hebrew back to English
3. Measures both spelling accuracy and semantic preservation

## Quick Start - Automated Workflow

### Use the Orchestrator Agent (Recommended)

The **@orchestrator** agent fully automates the entire translation chain:

```bash
@orchestrator Run translation experiment for: Your English sentence here.
```

The orchestrator will execute these steps automatically:
1. ✅ Calculate spelling error ratio from the original sentence
2. ✅ Write initial row to CSV with original sentence and spelling ratio
3. ✅ Call English→French translator agent
4. ✅ Call French→Hebrew translator agent  
5. ✅ Call Hebrew→English translator agent
6. ✅ Calculate embedding distance between original and final English
7. ✅ Update CSV row with all translations and embedding distance
8. ✅ Display a formatted summary

**That's it!** No manual copying between agents required.

### Example

```bash
@orchestrator Run translation experiment for: The quick brown fox jumps over the lazy dog.
```

Expected output:
```
✅ Translation Chain Complete
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📝 Original (EN):  The quick brown fox jumps over the lazy dog.
🇫🇷 French:         Le renard brun rapide saute par-dessus le chien paresseux.
🇮🇱 Hebrew:         השועל החום המהיר קופץ מעל הכלב העצלן.
🔄 Final (EN):     The quick brown fox jumps over the lazy dog.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📊 Metrics:
   • Spelling Error Ratio:  0.0000
   • Embedding Distance:    0.000000
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💾 Saved to translation_experiments.csv
```

## How It Works

### Workflow Details

1. **Spelling Error Ratio Calculation**
   - The orchestrator analyzes the original English sentence for spelling errors
   - Calculates ratio: `misspelled_words / total_words`
   - This is written to CSV immediately

2. **Translation Chain**
   - **EN→FR**: The sentence is translated to French (misspellings are corrected by understanding intent)
   - **FR→HE**: French is translated to Hebrew
   - **HE→EN**: Hebrew is translated back to English
   - Each translator agent returns ONLY the translated text

3. **Embedding Distance Calculation**
   - After getting the final English translation, semantic similarity is measured
   - Uses sentence-transformers model to calculate cosine distance
   - Lower values = better semantic preservation

4. **CSV Storage**
   - Results are saved to `translation_experiments.csv`
   - Each row contains the complete translation chain plus metrics

## CSV Format

The `translation_experiments.csv` file contains:

| Column | Description | Example |
|--------|-------------|---------|
| `original_sentence` | Input English text (may have spelling errors) | "The quik brown fox..." |
| `spelling_error_ratio` | Ratio of misspelled words (0.0 = perfect) | 0.1111 |
| `french_translation` | Output from EN→FR translation | "Le renard brun rapide..." |
| `hebrew_translation` | Output from FR→HE translation | "השועל החום המהיר..." |
| `final_english_translation` | Output from HE→EN translation | "The quick brown fox..." |
| `embedding_distance` | Semantic distance (0.0 = identical meaning) | 0.023456 |

### CSV Workflow
1. When orchestrator starts, it writes a row with `original_sentence` and `spelling_error_ratio`, leaving other fields empty
2. After translation chain completes, it updates the same row with all translations and `embedding_distance`
3. This ensures data is captured even if the translation process fails midway

## Available Agents

### Translation Agents
- **@orchestrator** - Main orchestrator that automates the full EN→FR→HE→EN chain with metrics and CSV logging
- **@en-fr** - English to French translator (returns only French text)
- **@fr-he** - French to Hebrew translator (returns only Hebrew text)
- **@he-en** - Hebrew to English translator (returns only English text)

### Utility Agents
- **@validator** - Agent specification validator for reviewing agent files

### Agent Behavior
Each translator agent:
- Returns ONLY the translated text (no explanations or formatting)
- Intelligently handles spelling errors by translating the intended meaning
- Maintains tone, style, and nuance of the original text
- Uses proper punctuation and grammar rules for the target language

## Metrics Explained

### Spelling Error Ratio
- Measures the proportion of misspelled words in the original English sentence
- Calculated BEFORE translation begins
- Formula: `number_of_misspelled_words / total_words`
- **0.0000** = perfect spelling
- **0.2500** = 25% of words misspelled
- **1.0000** = all words misspelled

### Embedding Distance
- Measures semantic similarity between original and final English translations
- Calculated AFTER translation chain completes
- Uses `sentence-transformers` library with `all-MiniLM-L6-v2` model
- Metric: Cosine distance between sentence embeddings
- **0.000000** = semantically identical
- **0.100000** = slight semantic drift
- **0.500000+** = significant meaning change

## Project Structure

```
.github/agents/
├── translation-orchestrator.md      # Main orchestrator agent (use @orchestrator)
├── en-fr-translator.md              # English to French translator (@en-fr)
├── fr-he-translator.md              # French to Hebrew translator (@fr-he)
└── he-en-translator.md              # Hebrew to English translator (@he-en)

├── instructions.md                  # This file - complete project documentation
├── translation_experiments.csv      # Experiment results database
├── embedding_distance.py            # Semantic distance calculator
├── add_experiment.py                # Manual experiment entry script (legacy)
└── run_translation_experiments.py   # Batch processing script (legacy)
```

## Alternative: Manual Workflow

If you need to run steps manually (not recommended):

```bash
# Step 1: English → French
@en-fr Your English sentence here

# Step 2: French → Hebrew  
@fr-he [paste French translation]

# Step 3: Hebrew → English
@he-en [paste Hebrew translation]

# Step 4: Add to CSV manually
python add_experiment.py
```

## Dependencies

Install required packages:

```bash
pip install -r requirements.txt
```

Required packages:
- `sentence-transformers` - For semantic embeddings
- `scipy` - For distance calculations
- `numpy` - For numerical operations

## Testing the System

Try with a sentence containing spelling errors:

```bash
@orchestrator Run translation experiment for: Ther's a reeson legandary formr Liverpool managr Bill Shankly once proclamed footbal was 'the peopel's game' – and that's becaus it belngs to the fans.
```

The system should:
1. Detect spelling errors and calculate the ratio
2. Translate based on intended meaning (not literal misspellings)
3. Produce a final translation that corrects the errors
4. Show both spelling ratio and embedding distance metrics
