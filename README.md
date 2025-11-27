# Multi-Agent Translation Chain: Semantic Preservation Analysis

## Overview

This project implements a multi-stage translation pipeline using CLI-based AI agents to evaluate how spelling errors affect semantic preservation through a three-language translation chain: **English → French → Hebrew → English**.

The system demonstrates autonomous agent chaining, where each translation agent automatically triggers the next, and measures the semantic drift between the original and final English output using vector embeddings.

## Task Objectives

This project was designed to:

1. **Create a multi-step translation pipeline** using CLI-based agents
2. **Test impact of spelling errors** on translation quality (0% to 50% error rates)
3. **Measure semantic drift** using vector embeddings to compare original vs. final output
4. **Visualize the relationship** between input error rates and translation quality degradation

## System Architecture

### Translation Chain

```
Input: English sentence (with spelling errors)
    ↓
Agent 1: /en-fr (English → French)
    ↓ [auto-triggers next agent]
Agent 2: /fr-he (French → Hebrew)
    ↓ [auto-triggers next agent]
Agent 3: /he-en (Hebrew → English)
    ↓
Output: Final English sentence
```

### Key Features

- **Autonomous Chain Execution**: Each agent automatically triggers the next (no manual intervention)
- **Intelligent Error Handling**: Agents translate based on intended meaning, not literal misspellings
- **CLI-Based**: Entire workflow runs through Claude Code using slash commands
- **Semantic Analysis**: Python utilities calculate embedding distances to measure quality

## Quick Start

### Prerequisites

1. **Claude Code** installed and running
2. **Python 3.8+** with pip
3. **Required Python packages**:
   ```bash
   pip install -r requirements.txt
   ```

### Running a Translation Chain

Simply use the `/en-fr` slash command with your English sentence:

```bash
/en-fr The quick brown fox jumps over the lazy dog.
```

The system will automatically:
1. Translate English to French
2. Auto-trigger French to Hebrew translation
3. Auto-trigger Hebrew back to English
4. Display all intermediate and final translations

**Example Output:**
```
=== TRANSLATION CHAIN STARTED ===

Original English:
The quick brown fox jumps over the lazy dog.

Step 1 - French Translation:
Le renard brun rapide saute par-dessus le chien paresseux.

Step 2 - Hebrew Translation:
השועל החום המהיר קופץ מעל הכלב העצלן.

Step 3 - Final English Translation:
The quick brown fox jumps over the lazy dog.

=== TRANSLATION CHAIN COMPLETE ===
```

## Task Requirements

### Input Specifications

- **Sentence count**: 1-2 English sentences
- **Sentence length**: Minimum 15 words per sentence
- **Spelling errors**: At least 25% of words must contain spelling mistakes

### Experimental Requirements

To complete this project, you must:

1. **Prepare test sentences** with multiple error levels:
   - 0% errors (perfect spelling - baseline)
   - 10% errors
   - 25% errors (minimum required)
   - 30% errors
   - 40% errors
   - 50% errors

2. **Run translation chains** for each error level:
   - Execute `/en-fr [sentence]` for each variant
   - Collect French, Hebrew, and final English translations
   - Record all data in `translation_experiments.csv`

3. **Calculate embedding distances**:
   - Use the Python utilities in `utils.ipynb`
   - Compare original sentence (0% error version) with final English output
   - Record distance for each error level

4. **Generate visualization**:
   - Create a graph with:
     - X-axis: Spelling error percentage (0% to 50%)
     - Y-axis: Embedding distance (semantic drift)
   - Save as PNG image

## Project Structure

```
agents-task3/
├── README.md                          # This file - primary documentation
├── instructions.md                    # Detailed usage guide
├── translation_experiments.csv        # Experimental data (TO BE FILLED)
├── utils.ipynb                        # Python utilities for analysis
├── requirements.txt                   # Python dependencies
│
├── .claude/
│   └── commands/
│       ├── en-fr.md                   # English → French agent
│       ├── fr-he.md                   # French → Hebrew agent
│       └── he-en.md                   # Hebrew → English agent
│
└── .github/
    └── agents/                        # Archive (original Copilot agents)
```

## Step-by-Step Experimental Workflow

### Step 1: Prepare Input Sentences

Create variants of your base sentence(s) with different spelling error rates.

**Example Base Sentence (43 words):**
> "The Trump administration is eager to use the momentum of talks with Ukrainian and Russian officials to try and force both Presidents Volodymyr Zelensky and Vladimir Putin to the table on an initial ceasefire deal, those sources said."

**Error Variants:**
- **0% errors**: [perfect spelling]
- **10% errors**: 4 words misspelled (e.g., "administation", "momemtum", "Russain", "Vladmir")
- **25% errors**: 11 words misspelled (minimum required)
- **30% errors**: 13 words misspelled
- **40% errors**: 17 words misspelled
- **50% errors**: 22 words misspelled

### Step 2: Run Translation Chains

For each error variant:

```bash
# Example with 25% errors
/en-fr The Trump adminstration is egar to use the momemtum of talks with Ukrianian and Russain officals to try and force both President Volodymyr Zelensky and Vladmir Putin to the tabel on an inital ceasefire deal, thoze sources said.
```

**Collect the outputs:**
- French translation (from Agent 1)
- Hebrew translation (from Agent 2)
- Final English translation (from Agent 3)

### Step 3: Calculate Embedding Distances

Open `utils.ipynb` and run:

```python
from utils import calculate_embedding_distance

# Use the 0% error version as the "original"
original = "The Trump administration is eager to use the momentum..."

# Use the final English output from the translation chain
final = "The Trump administration is eager to use the momentum..."

distance = calculate_embedding_distance(original, final)
print(f"Embedding Distance: {distance:.4f}")
```

### Step 4: Record Data in CSV

Fill `translation_experiments.csv` with your results:

```csv
original_sentence,spelling_error_ratio,french_translation,hebrew_translation,final_english_translation,embedding_distance
[0% sentence],0.0,[French],[Hebrew],[Final English],[distance]
[10% sentence],0.1,[French],[Hebrew],[Final English],[distance]
[25% sentence],0.25,[French],[Hebrew],[Final English],[distance]
[30% sentence],0.3,[French],[Hebrew],[Final English],[distance]
[40% sentence],0.4,[French],[Hebrew],[Final English],[distance]
[50% sentence],0.5,[French],[Hebrew],[Final English],[distance]
```

**IMPORTANT**: All columns must be filled - no empty cells!

### Step 5: Generate Visualization

Add this code to `utils.ipynb` (or create a separate script):

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv('translation_experiments.csv')

# Create plot
plt.figure(figsize=(10, 6))
plt.scatter(df['spelling_error_ratio'] * 100, df['embedding_distance'],
           s=100, c='steelblue', edgecolors='black', linewidth=1.5)
plt.plot(df['spelling_error_ratio'] * 100, df['embedding_distance'],
        'r--', alpha=0.5, linewidth=2)

plt.xlabel('Spelling Error Percentage (%)', fontsize=12)
plt.ylabel('Embedding Distance (Cosine)', fontsize=12)
plt.title('Impact of Spelling Errors on Translation Quality\n(English → French → Hebrew → English)',
         fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.xlim(-5, 55)
plt.xticks([0, 10, 20, 25, 30, 40, 50])

plt.savefig('translation_error_impact.png', dpi=300, bbox_inches='tight')
plt.show()

print(f"Graph saved as: translation_error_impact.png")
```

## Required Deliverables

### Must Submit

- [ ] **Input sentences** with documented word counts (≥15 words each)
- [ ] **Error variants** for 0%, 10%, 25%, 30%, 40%, 50% spelling error levels
- [ ] **Complete CSV** with all translation data (no empty cells):
  - Original sentences
  - Spelling error ratios
  - French translations
  - Hebrew translations
  - Final English translations
  - Embedding distances
- [ ] **Visualization graph** showing error percentage vs. embedding distance
- [ ] **Agent definitions** (already provided in `.claude/commands/`)

### CSV Validation

Before submission, verify:
- ✅ At least 6 rows (one per error level)
- ✅ All columns filled (no empty cells)
- ✅ Spelling error ratios correctly calculated
- ✅ Embedding distances computed for all rows

## Available Slash Commands

| Command | Description | Usage |
|---------|-------------|-------|
| `/en-fr` | English → French (chain starter, auto-triggers next) | `/en-fr [English text]` |
| `/fr-he` | French → Hebrew (usually auto-triggered) | `/fr-he [French text]` |
| `/he-en` | Hebrew → English (usually auto-triggered) | `/he-en [Hebrew text]` |
| `/translate-chain` | Complete chain in single command (alternative) | `/translate-chain [English text]` |

**Note**: You can either:
- Use `/en-fr` which auto-triggers the full chain through /fr-he and /he-en
- Use `/translate-chain` to execute all three steps in one command
- Call individual commands for manual step-by-step translation (breaks auto-chain)

## Python Utilities Reference

### Calculate Embedding Distance

```python
from utils import calculate_embedding_distance

distance = calculate_embedding_distance(text1, text2)
# Returns: float between 0.0 (identical) and 2.0 (opposite)
```

### Calculate Spelling Error Ratio

```python
from utils import calculate_spelling_error_ratio

ratio = calculate_spelling_error_ratio(original, misspelled)
# Returns: float between 0.0 (identical) and 1.0 (completely different)
```

### Get All Metrics

```python
from utils import calculate_translation_quality_metrics

metrics = calculate_translation_quality_metrics(original, translated)
# Returns: dict with 'spelling_error_ratio', 'embedding_distance', 'embedding_similarity'
```

## Technical Details

### Intelligent Error Handling

The translation agents are designed to handle spelling errors intelligently:
- Agents infer the **intended meaning** from context
- Example: "The qiuck brown fox" → correctly understood as "The quick brown fox"
- Misspellings are corrected through context-aware translation
- This allows testing how errors affect semantic preservation through multiple translation steps

### Embedding Model

- **Model**: `all-MiniLM-L6-v2` (sentence-transformers)
- **Dimensions**: 384
- **Metric**: Cosine distance (1 - cosine_similarity)
- **Range**: 0.0 (identical meaning) to 2.0 (opposite meaning)

### Why This Translation Chain?

The English → French → Hebrew → English chain was chosen to:
1. Test semantic preservation across **linguistically diverse** languages
2. Include both **Romance** (French) and **Semitic** (Hebrew) language families
3. Maximize potential for **semantic drift** detection
4. Test robustness of modern translation systems

## Troubleshooting

### Chain Not Auto-Triggering

If agents don't automatically trigger the next step:
- Ensure you're using Claude Code (not GitHub Copilot)
- Verify slash command files exist in `.claude/commands/`
- Check that agent prompts include `SlashCommand` tool usage

### Embedding Calculation Errors

```bash
# Reinstall dependencies
pip install --upgrade sentence-transformers numpy scipy

# If CUDA errors occur (optional GPU acceleration)
pip install torch --index-url https://download.pytorch.org/whl/cpu
```

### Empty CSV Columns

Common issue: Forgetting to run the translation chains!
- You must actually execute `/en-fr` for each error variant
- Copy/paste the French, Hebrew, and final English outputs
- Don't skip any error levels (need all 6)

## Expected Results

Based on similar experiments, you should observe:
- **0-10% errors**: Minimal semantic drift (distance < 0.05)
- **25-30% errors**: Moderate drift (distance 0.05-0.15)
- **40-50% errors**: Higher drift (distance 0.15-0.30)

The graph should show an **increasing trend**: as spelling error percentage increases, embedding distance (semantic drift) generally increases.

## Credits and Implementation

- **Framework**: Claude Code (Anthropic)
- **Embedding Model**: sentence-transformers (all-MiniLM-L6-v2)
- **Translation**: Claude Sonnet 4.5
- **Visualization**: matplotlib

## Additional Resources

- **Detailed usage guide**: See `instructions.md`
- **Python utilities**: Open `utils.ipynb` in Jupyter
- **Agent specifications**: Check `.claude/commands/` directory

## Quick Reference

**To run a complete experiment:**
1. Prepare 6 sentence variants (0%, 10%, 25%, 30%, 40%, 50% errors)
2. Run `/en-fr [sentence]` for each variant
3. Record French, Hebrew, and final English outputs
4. Calculate embedding distances in Python
5. Fill `translation_experiments.csv` completely
6. Generate graph with matplotlib
7. Verify all deliverables are complete

**Time estimate**: 60-90 minutes for full experimental workflow

---

**Ready to start?** Try running:
```bash
/en-fr The quick brown fox jumps over the lazy dog in the beautiful garden during the sunny afternoon.
```
