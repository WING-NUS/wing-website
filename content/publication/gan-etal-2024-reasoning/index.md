---
title: "Reasoning Robustness of LLMs to Adversarial Typographical Errors"
subtitle: ""
authors:
- esther
- Yiran Zhao
- Liying Cheng
- Mao Yancan
- Anirudh Goyal
- kenji
- min
- qizhe

doi: "10.18653/v1/2024.emnlp-main.584"

# Schedule page publish date (NOT publication's date).
date: '2024-11-12'
publishDate: '2024-11'
publication_types:
- paper-conference

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the 2024 Conference on Empirical Methods in Natural Language Processing*

abstract: "Large Language Models (LLMs) have demonstrated impressive capabilities in reasoning using Chain-of-Thought (CoT) prompting. However, CoT can be biased by users' instruction. In this work, we study the reasoning robustness of LLMs to typographical errors, which can naturally occur in users' queries. We design an Adversarial Typo Attack (ATA) algorithm that iteratively samples typos for words that are important to the query and selects the edit that is most likely to succeed in attacking. It shows that LLMs are sensitive to minimal adversarial typographical changes. Notably, with 1 character edit, Mistral-7B-Instruct's accuracy drops from 43.7% to 38.6% on GSM8K, while with 8 character edits the performance further drops to 19.2%. To extend our evaluation to larger and closed-source LLMs, we develop the R2ATA benchmark, which assesses models' Reasoning Robustness to ATA. It includes adversarial typographical questions derived from three widely-used reasoning datasets---GSM8K, BBH, and MMLU---by applying ATA to open-source LLMs. R2ATA demonstrates remarkable transferability and causes notable performance drops across multiple super large and closed-source LLMs."
summary: 'An EMNLP 2024 study showing that adversarial typos can substantially degrade LLM reasoning and introducing the R2ATA robustness benchmark.'

# Display this page in the Featured widget?
featured: true

url_pdf: 'https://aclanthology.org/2024.emnlp-main.584.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: 'https://esther-gan.github.io/r2ata-web/'
url_slides: ''
url_source: ''
url_video: ''

image:
  caption: 'Figure from Gan et al. (2024).'
  preview_only: false
---
