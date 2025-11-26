# 🧠 Multi-Stage Translation Analysis using AI Agents

## 🎯 Project Goal

This project aims to **demonstrate a multi-stage translation pipeline** using three dedicated AI Agents. The core objective is to analyze the **impact of spelling errors** on the final translation quality by calculating the **vector distance** (semantic distance) between the original sentence and the final, round-trip translated sentence.

---

## 🧩 System Components and Architecture

The solution must be implemented as an automated workflow executed via a **Command Line Interface (CLI)**.

### 1. The Translation Agents (The Pipeline)

You must implement **three distinct translation agents**, each dedicated to a single, sequential step in the chain. Agents should not attempt to correct spelling or grammar, but only perform the specified translation.

| Agent | Task | Input | Output |
| :---: | :--- | :--- | :--- |
| **Agent 1** | English to French | English | French |
| **Agent 2** | French to Hebrew | French | Hebrew |
| **Agent 3** | Hebrew back to English | Hebrew | English |

### 2. Translation Process Workflow

1.  **Input:** Start with **one or two English sentences** that meet the following criteria:
    * Minimum length of **15 words** per sentence.
    * Must contain at least **25% intentional spelling errors** (e.g., in a 20-word sentence, at least 5 words must be misspelled).
2.  **Execution:** The input sentence must pass sequentially through **Agent 1** $\rightarrow$ **Agent 2** $\rightarrow$ **Agent 3**.
3.  **Output:** The final output is an English sentence.
4.  **Comparison:** The final English sentence is compared against the original English input.

---

## 📏 Metrics and Experimentation

The primary goal of this task is to run a controlled experiment and measure the degradation of semantic quality.

### 1. Vector Distance Calculation

The quality metric will be the **vector distance** (or semantic distance) between the original English sentence and the final English sentence.

* This calculation must be performed using **Python** (or similar language with embedding capabilities) by:
    1.  Generating the **embedding** (vector representation) for the original sentence.
    2.  Generating the **embedding** for the final translated sentence.
    3.  Calculating the distance (e.g., Cosine Similarity or Euclidean Distance) between the two vectors.

### 2. Experiment Setup

You must run the translation pipeline and calculate the vector distance for **multiple levels of spelling errors** in the original English input.

* **Error Range:** Run tests from **0%** errors up to **50%** errors.
* **Documentation:** Record the vector distance for each error level.

### 3. Data Visualization

A **graph** must be generated to display the experimental results:

* **X-Axis:** Percentage of Spelling Errors (0% – 50%)
* **Y-Axis:** Vector Distance (Semantic Loss) between the Original and Final sentences.

---

## 💾 Deliverables and Submission

The final submission must include the following artifacts:

* **Input Data:** The original English sentences used, including all versions with spelling errors (0% through 50%).
* **Agent Configuration:** A clear description or configuration details (e.g., prompts, "skills") used for each of the three translation agents.
* **The Results Graph:** The plot showing the relationship between error percentage and vector distance.

---

## 🧾 Proposed Workflow Summary

1.  **Preparation:** Define the three agents and their respective prompts/configurations.
2.  **Input Generation:** Prepare the base English sentence(s) and generate variants with error levels from 0% to 50%.
3.  **Execution:** Run the translation pipeline for each error level, passing the output of Agent $N$ as the input to Agent $N+1$.
4.  **Analysis:** Calculate the embeddings and vector distances for all results.
5.  **Reporting:** Generate the comparative graph and compile the final report document.