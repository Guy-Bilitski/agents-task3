# Translation Chain Experiments - Instructions

This project implements an autonomous translation chain (English → French → Hebrew → English) using self-triggering AI agents in Claude Code.

## Overview

The system tests how well meaning is preserved when translating through multiple languages. The translation chain:
1. Takes an English sentence (possibly with spelling errors)
2. Automatically translates it through French and Hebrew back to English
3. Each agent in the chain triggers the next agent automatically

## Quick Start - Autonomous Chain

### Initiate the Chain with /en-fr

Simply call the **/en-fr** slash command with your English sentence, and the entire chain executes automatically:

```bash
/en-fr Your English sentence here.
```

The chain will execute these steps automatically:
1. **/en-fr** translates English to French and triggers /fr-he
2. **/fr-he** translates French to Hebrew and triggers /he-en
3. **/he-en** translates Hebrew back to English and displays the result

**No manual intervention required!** Each agent automatically passes its output to the next.

### Example

```bash
/en-fr The quick brown fox jumps over the lazy dog.
```

Expected output:
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

## How It Works

### Agent Chain Architecture

The translation system uses three autonomous agents that form a self-executing chain:

1. **/en-fr (Chain Initiator)**
   - Receives English input (misspellings are corrected by understanding intent)
   - Translates to French
   - Automatically triggers /fr-he with the French translation

2. **/fr-he (Chain Middle)**
   - Receives French input from /en-fr
   - Translates to Hebrew
   - Automatically triggers /he-en with the Hebrew translation

3. **/he-en (Chain Terminator)**
   - Receives Hebrew input from /fr-he
   - Translates back to English
   - Displays final result (chain ends)

### Key Features
- **Zero manual intervention:** Each agent automatically calls the next
- **Intelligent error handling:** Misspellings are corrected by translating intended meaning
- **Clean output:** Each agent displays only the translation, then triggers the next
- **Transparent process:** All intermediate translations are visible

## Available Slash Commands

### Translation Chain Commands
- **/en-fr** - English to French translator | Chain initiator | Auto-triggers /fr-he
- **/fr-he** - French to Hebrew translator | Chain middle | Auto-triggers /he-en
- **/he-en** - Hebrew to English translator | Chain terminator | Outputs final result

### Agent Behavior
Each translator agent:
- Outputs the translated text clearly
- Automatically triggers the next agent in the chain (except /he-en)
- Intelligently handles spelling errors by translating the intended meaning
- Maintains tone, style, and nuance of the original text
- Uses proper punctuation and grammar rules for the target language

## Testing Translation Quality

To evaluate the translation chain quality, you can:

1. **Visual Comparison:** Compare original English with final English output
2. **Semantic Analysis:** Use external tools to measure similarity
3. **Manual Review:** Check if meaning, tone, and nuance are preserved

### Example Test Cases

**Perfect Spelling:**
```bash
/en-fr The quick brown fox jumps over the lazy dog.
```

**With Spelling Errors:**
```bash
/en-fr Ther's a reeson legandary formr Liverpool managr Bill Shankly once proclamed footbal was 'the peopel's game'.
```

**Complex Sentence:**
```bash
/en-fr Despite the unprecedented challenges we faced, the team demonstrated remarkable resilience and creativity.
```

## Project Structure

```
agents-task3/
├── README.md                          # Primary documentation
├── instructions.md                    # This file - detailed usage guide
├── translation_experiments.csv        # Experiment results (TO BE FILLED)
├── utils.ipynb                        # Python utilities for analysis
├── requirements.txt                   # Python dependencies
│
├── .claude/
│   └── commands/
│       ├── en-fr.md                   # English → French translator (/en-fr)
│       ├── fr-he.md                   # French → Hebrew translator (/fr-he)
│       └── he-en.md                   # Hebrew → English translator (/he-en)
│
└── .github/
    └── agents/                        # Archive (original Copilot agents)
```

## Manual Slash Command Calls

If you need to call commands individually (breaks the automatic chain):

```bash
# Single translation only - no chain continuation
/en-fr Your English sentence

# Or start from French
/fr-he Votre texte français

# Or start from Hebrew
/he-en הטקסט שלך בעברית
```

**Note:** When calling commands individually, you must manually copy/paste between steps. For automatic chaining, always use `/en-fr` as the entry point.

## Testing the System

**Test 1 - Perfect spelling:**
```bash
/en-fr The quick brown fox jumps over the lazy dog.
```

**Test 2 - With spelling errors:**
```bash
/en-fr Ther's a reeson legandary formr Liverpool managr Bill Shankly once proclamed footbal was the peopel's game.
```

The system should:
1. Translate based on intended meaning (not literal misspellings)
2. Automatically chain through all three translations
3. Produce a final English translation that corrects the errors
4. Display all intermediate translations for transparency
