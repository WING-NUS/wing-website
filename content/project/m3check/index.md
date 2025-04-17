---
title: Is Knowledge in Multilingual Language Models Cross-Lingually Consistent?

summary: Cross-lingual consistency should be considered to assess cross-lingual transferability, maintain the factuality of the model knowledge across languages, and preserve the parity of language model performance. Inspired by the classic linguistic theory that the reference of a sentence is its truth value,  we evaluate cross-lingual consistency for factual knowledge by substituting an entity with an equivalent one in other languages that shares the same reference.

tags: ["Multilingual and Cross-lingual NLP", "Knowledge Consistency", "Code-switching", "Model Parity and Consistency"]
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
- Mahardika Krisna Ihsani
- min

---
Few works study the variation and cross-lingual consistency of factual knowledge embedded in multilingual models. However, cross-lingual consistency should be considered to assess cross-lingual transferability, maintain the factuality of the model knowledge across languages, and preserve the parity of language model performance. We are thus interested in analyzing, evaluating, and interpreting cross-lingual consistency for factual knowledge. We apply interpretability approaches to analyze the behavior of a model in cross-lingual contexts, discovering that multilingual models show different levels of consistency, subject to language families or linguistic factors. In addition, we identify a bottleneck in cross-lingual consistency on a particular layer. To mitigate this problem, we try vocabulary expansion, adding biases from monolingual inputs, and different types of supervision consisting of additional cross-lingual word alignment objective, instruction tuning, and code-switching training. We find that among these methods, code-switching training and cross-lingual word alignment objective show the most promising results, emphasizing the noteworthiness of cross-lingual alignment supervision for cross-lingual consistency enhancement.
