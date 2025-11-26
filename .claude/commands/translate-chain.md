# Full Translation Chain: EN → FR → HE → EN

Execute the complete translation chain for testing semantic preservation through multiple languages.

## Your Task
1. Translate the input English text to French
2. Translate the French result to Hebrew
3. Translate the Hebrew result back to English
4. Display all intermediate translations clearly

## Process
For the following English text, execute all three translation steps:

**Original English:**
{{input}}

Perform these translations sequentially:
1. **English → French**: Translate the input to French (handle spelling errors by translating intended meaning)
2. **French → Hebrew**: Translate the French result to Modern Hebrew (unvocalized)
3. **Hebrew → English**: Translate the Hebrew result back to English

## Translation Guidelines
- For English → French: Infer correct words from misspellings and translate intended meaning
- For French → Hebrew: Use unvocalized Modern Hebrew text
- For Hebrew → English: Produce natural, fluent English
- Preserve tone, style, and nuance throughout all translations
- Use proper punctuation rules for each target language

## Output Format
Display results in this format:

```
=== TRANSLATION CHAIN RESULTS ===

Original English:
[original input]

Step 1 - French Translation:
[French translation]

Step 2 - Hebrew Translation:
[Hebrew translation]

Step 3 - Final English Translation:
[final English translation]

=== CHAIN COMPLETE ===
```
