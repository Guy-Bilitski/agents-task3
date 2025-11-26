# GitHub Copilot Custom Agents

This project includes specialized translation agents that form an autonomous chain for EN→FR→HE→EN translation experiments.

## Available Agents

### @en-fr - English to French Translator (Chain Initiator)
Professional translator specialized in English-to-French translation. Provides accurate, natural French translations while maintaining tone and style. Intelligently handles spelling errors by translating intended meaning.

**Role in chain:** First agent - receives English input and automatically triggers @fr-he

**Usage:** `@en-fr Your English sentence here`

**Output:** French translation + automatic chain continuation to @fr-he

**Agent file:** `agents/en-fr-translator.md`

---

### @fr-he - French to Hebrew Translator (Chain Middle)
Professional translator specialized in French-to-Hebrew translation. Provides accurate Modern Hebrew translations preserving the original meaning and nuance.

**Role in chain:** Second agent - receives French from @en-fr and automatically triggers @he-en

**Output:** Hebrew translation + automatic chain continuation to @he-en

**Agent file:** `agents/fr-he-translator.md`

---

### @he-en - Hebrew to English Translator (Chain Terminator)
Professional translator specialized in Hebrew-to-English translation. Converts Modern Hebrew text into natural, fluent English.

**Role in chain:** Final agent - receives Hebrew from @fr-he and outputs final English translation

**Output:** Final English translation (chain ends here)

**Agent file:** `agents/he-en-translator.md`

---

### @validator - Agent Specification Validator
Expert in reviewing and improving agent specification files. Validates agent design, identifies issues, and recommends enhancements.

**Agent file:** `agents/agent-validator.md`

---

## Quick Reference

**For translation chain:** Use `@en-fr Your English text` - the chain runs automatically
**For single translations:** Call any agent individually with appropriate language input
**For agent review:** Use `@validator`

See `instructions.md` for complete documentation.
