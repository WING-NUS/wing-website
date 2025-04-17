---
title: M^3Check: A Demonstration System for Multilingual Multi-clue Multi-Hop Fact-Checking

summary: Fact-checking real-world claims often requires complex, multi-step reasoning due to the absence of direct evidence to support or refute them. M^3Check guides the model's reasoning process by constructing a structured, supervised, and verified chain of clues for verifying a claim, fostering a transparent, explainable, and user-friendly fact-checking process for multiple languages.

tags: ["Multilingual NLP", "Fact-checking", "RAG", "Supervised COT"]
year: 2025

date: '2025-01-01'

all_day: true

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors:
- barid
- Xinyuan Lu
- Liangming Pan
- Tianyi Zhu
- Sahej Agarwal
- Mahardika Krisna Ihsani
- min

---
Imagine that, while we cannot simply Google a complex claim, we can still find some relevant clues to help us. The question is,  how can we use these clues to verify the input claim?  M^3Check is a RAG model that follows three major steps: 1) break down the claim into clues,  2) verify each clue based on articles, and 3) conclude, check, and reason the claim based on a structured, supervised, and verified chain of clues. This project leverages findings from multiple projects, offering a good example of how research outcomes can be applied to address a real-world problem.
