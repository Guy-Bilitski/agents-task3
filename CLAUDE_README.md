# Translation Chain Experiments - Claude Code Edition

This project has been adapted to work with **Claude Code** for executing autonomous translation chain experiments.

## Overview

The system tests how well meaning is preserved when translating through multiple languages. The translation chain:
1. Takes an English sentence (possibly with spelling errors)
2. Translates it through French and Hebrew back to English
3. Measures semantic drift using vector distance calculations

## Quick Start with Claude Code

### Method 1: Using Slash Commands (Recommended)

Claude Code now includes custom slash commands for the translation chain:

#### Full Automatic Chain
```bash
/translate-chain The quick brown fox jumps over the lazy dog in the beautiful garden.
```

This will automatically execute all three translations and display the complete chain.

#### Individual Translation Steps
```bash
# Step 1: English to French
/en-fr Your English sentence here

# Step 2: French to Hebrew (copy the French result from above)
/fr-he Votre texte français ici

# Step 3: Hebrew to English (copy the Hebrew result from above)
/he-en הטקסט שלך בעברית
```

### Method 2: Direct Conversation with Claude

You can also ask Claude Code directly in conversation:

```
Please translate this sentence through the full chain (English → French → Hebrew → English):
"The quick brown fox jumps over the lazy dog."
```

Claude will execute all three translation steps and show you the results.

## Available Slash Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `/translate-chain` | Full EN→FR→HE→EN chain | `/translate-chain <English text>` |
| `/en-fr` | English to French only | `/en-fr <English text>` |
| `/fr-he` | French to Hebrew only | `/fr-he <French text>` |
| `/he-en` | Hebrew to English only | `/he-en <Hebrew text>` |

## Testing with Spelling Errors

The system is designed to handle spelling errors intelligently:

**Test with perfect spelling (0% errors):**
```bash
/translate-chain The quick brown fox jumps over the lazy dog in the beautiful garden during the sunny afternoon.
```

**Test with spelling errors (25% errors):**
```bash
/translate-chain The qiuck brown fox jmups over the laazy dog in the garen during a beutiful sunny afternooon.
```

**Test with high error rate (40% errors):**
```bash
/translate-chain Ther's a reeson legandary formr Liverpool managr Bill Shankly once proclamed footbal was the peopel's game becaus it belngs to the fans.
```

## Collecting Experimental Data

### Step 1: Run Translations

Use the `/translate-chain` command with different error levels (0% to 50%) and collect the results.

### Step 2: Calculate Embedding Distance

Use the provided Python utilities to calculate semantic distance:

```python
# In utils.ipynb or Python script
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')

# Your sentences
original = "The quick brown fox jumps over the lazy dog."
final = "The quick brown fox jumps over the lazy dog."

# Calculate embeddings
emb1 = model.encode(original)
emb2 = model.encode(final)

# Calculate distance
distance = np.linalg.norm(emb1 - emb2)
print(f"Embedding distance: {distance}")
```

### Step 3: Record Results

Save results to `translation_experiments.csv`:

| original_sentence | spelling_error_ratio | french_translation | hebrew_translation | final_english_translation | embedding_distance |
|-------------------|---------------------|--------------------|--------------------|---------------------------|-------------------|
| Your sentence | 0.0 | French result | Hebrew result | Final English | 0.123 |

### Step 4: Generate Visualization

Create a graph showing error percentage vs. embedding distance to analyze semantic drift.

## How It Works

### Translation Chain Architecture

1. **English → French**: Claude translates English to French, intelligently handling misspellings by inferring intended meaning
2. **French → Hebrew**: Claude translates French to Modern Hebrew (unvocalized)
3. **Hebrew → English**: Claude translates Hebrew back to English, completing the chain

### Intelligent Error Handling

- Spelling errors are corrected through context-aware translation
- Example: "The qiuck brown fox" is understood as "The quick brown fox"
- Semantic meaning is preserved throughout the chain
- This allows testing how errors affect final translation quality

## Differences from GitHub Copilot Version

### GitHub Copilot (Original)
- Used custom agents defined in `.github/agents/`
- Agents automatically triggered each other via tool calls
- Syntax: `@en-fr`, `@fr-he`, `@he-en`

### Claude Code (This Version)
- Uses slash commands in `.claude/commands/`
- Can execute full chain in single command or step-by-step
- Syntax: `/translate-chain`, `/en-fr`, `/fr-he`, `/he-en`
- Also supports direct conversational requests to Claude

## Project Structure

```
agents-task3/
├── .claude/
│   └── commands/
│       ├── translate-chain.md        # Full automatic chain
│       ├── en-fr.md                  # English → French
│       ├── fr-he.md                  # French → Hebrew
│       └── he-en.md                  # Hebrew → English
├── .github/
│   └── agents/                       # Original Copilot agents (for reference)
├── CLAUDE_README.md                  # This file - Claude Code documentation
├── instructions.md                   # Original documentation
├── translation_experiments.csv       # Experiment results
├── utils.ipynb                       # Python utilities for analysis
└── requirements.txt                  # Python dependencies

```

## Example Workflow

1. **Start Claude Code** in this directory

2. **Run a translation chain:**
   ```bash
   /translate-chain The quick brown fox jumps over the lazy dog in the beautiful garden.
   ```

3. **Collect the results:**
   - Original: "The quick brown fox jumps over the lazy dog in the beautiful garden."
   - French: "Le renard brun rapide saute par-dessus le chien paresseux dans le magnifique jardin."
   - Hebrew: "השועל החום המהיר קופץ מעל הכלב העצלן בגן היפה."
   - Final English: "The quick brown fox jumps over the lazy dog in the beautiful garden."

4. **Calculate embedding distance** using Python

5. **Repeat** with different spelling error levels (0%, 10%, 25%, 30%, 40%, 50%)

6. **Generate graph** showing error percentage vs. semantic drift

## Advanced Usage

### Running Multiple Experiments

You can ask Claude Code to help automate the entire experimental process:

```
Please help me run translation experiments with the following sentences at 0%, 25%, and 50% error levels:
1. "The quick brown fox jumps over the lazy dog in the beautiful garden."
2. "Machine learning models require large datasets for training purposes."

For each experiment:
- Run the translation chain
- Calculate the embedding distance
- Add the results to translation_experiments.csv
```

Claude Code can execute this entire workflow for you, including running the translations, calculating metrics, and organizing the data.

## Tips for Best Results

1. **Sentence Length**: Use sentences with at least 15 words for meaningful analysis
2. **Error Distribution**: Spread spelling errors throughout the sentence
3. **Error Types**: Include different types of errors (transpositions, omissions, substitutions)
4. **Consistency**: Use the same base sentences across different error levels for comparison
5. **Documentation**: Keep detailed notes on your experimental setup

## Getting Help

- For Claude Code features: Use `/help` or ask Claude directly
- For translation issues: The system handles most spelling errors automatically
- For analysis help: The `utils.ipynb` notebook contains example code
- For bugs or issues: Check the original `instructions.md` for the project specification

## Next Steps

1. ✅ Claude Code is set up with translation commands
2. 🔄 Run translation experiments with various error levels
3. 📊 Collect data in CSV format
4. 📈 Calculate embedding distances
5. 📉 Generate visualization graph
6. 📝 Analyze results and draw conclusions

Ready to start? Try running:
```bash
/translate-chain The quick brown fox jumps over the lazy dog in the beautiful garden during the sunny afternoon.
```
