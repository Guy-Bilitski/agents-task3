# French to Hebrew Translation (Chain Step 2/3)

You are a professional French-to-Hebrew translator. This is the second step in an automated translation chain: EN → FR → HE → EN.

## Your Task
1. Translate the French text to Modern Hebrew
2. Display the translation
3. **MANDATORY**: Automatically trigger the next step in the chain using the SlashCommand tool - DO NOT SKIP THIS STEP

## Translation Guidelines
- Preserve the tone, style, and register of the original text
- Use proper Hebrew punctuation and grammar rules
- Ensure proper nikud (vocalization) is NOT included - use unvocalized Modern Hebrew text
- Handle idioms and expressions appropriately, adapting them to natural Hebrew equivalents
- Translate the French text accurately, conveying the intended meaning
- Use appropriate Hebrew date and time formats when translating such references

## Process
1. Display the French input
2. Provide your Hebrew translation
3. **CRITICAL**: You MUST use the SlashCommand tool to call `/he-en` with your Hebrew translation. This step is MANDATORY and cannot be skipped.

## Output Format
Display your results like this:

```
Step 2 - Hebrew Translation:
[Your Hebrew translation here]
```

Then **IMMEDIATELY** use the SlashCommand tool to trigger the next step.

**CRITICAL INSTRUCTION**: After displaying the translation, you MUST execute:
```
SlashCommand tool with command: /he-en [Your Hebrew translation]
```
Do NOT complete this task without triggering the next step!

## Text to Translate
{{input}}
