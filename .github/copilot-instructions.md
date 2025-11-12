# GitHub Copilot Custom Agents

This project includes specialized translation and validation agents for automated translation chain experiments.

## Available Agents

### @orchestrator - Translation Chain Orchestrator
**The main agent for running translation experiments!** Fully automates the EN→FR→HE→EN translation chain, calculates metrics, and saves results to CSV. Just give it an English sentence and it handles everything.

**What it does:**
1. Calculates spelling error ratio from the original sentence
2. Writes initial row to CSV with original + spelling ratio
3. Calls translator agents sequentially (EN→FR→HE→EN)
4. Calculates embedding distance
5. Updates CSV with complete translation chain and metrics

**Usage:** `@orchestrator Run translation experiment for: Your sentence here.`

**Agent file:** `agents/translation-orchestrator.md`

---

### @en-fr - English to French Translator
Professional translator specialized in English-to-French translation. Provides accurate, natural French translations while maintaining tone and style. Intelligently handles spelling errors by translating intended meaning.

**Output:** Returns ONLY the French translation (no extra text)

**Agent file:** `agents/en-fr-translator.md`

---

### @fr-he - French to Hebrew Translator
Professional translator specialized in French-to-Hebrew translation. Provides accurate Modern Hebrew translations preserving the original meaning and nuance.

**Output:** Returns ONLY the Hebrew translation (no extra text)

**Agent file:** `agents/fr-he-translator.md`

---

### @he-en - Hebrew to English Translator
Professional translator specialized in Hebrew-to-English translation. Converts Modern Hebrew text into natural, fluent English.

**Output:** Returns ONLY the English translation (no extra text)

**Agent file:** `agents/he-en-translator.md`

---

### @validator - Agent Specification Validator
Expert in reviewing and improving agent specification files. Validates agent design, identifies issues, and recommends enhancements.

**Agent file:** `agents/agent-validator.md`

---

## Quick Reference

**For translation experiments:** Use `@orchestrator` exclusively
**For manual translation:** Use `@en-fr`, `@fr-he`, `@he-en` individually  
**For agent review:** Use `@validator`

See `instructions.md` for complete documentation.
