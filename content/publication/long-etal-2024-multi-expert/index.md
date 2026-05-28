---
title: "Multi-expert Prompting Improves Reliability, Safety and Usefulness of Large Language Models"
subtitle: ""
authors:
- long
- Duong Ngoc Yen
- Anh Tuan Luu
- Kenji Kawaguchi
- min
- Nancy F. Chen

doi: ""

# Schedule page publish date (NOT publication's date).
date: '2024-12-12'
publishDate: '2024-12'
publication_types: 
- paper-conference

# Publication name and optional abbreviated publication name.
publication: In *2024 Conference on Empirical Methods in Natural Language Processing, November 12 –16 Miami, Florida, USA, 2024*

abstract: "We present Multi-expert Prompting, a novel enhancement of ExpertPrompting (Xu et al., 2023), designed to improve the large language model (LLM) generation. Specifically, it guides an LLM to fulfill an input instruction by simulating multiple experts, aggregating their responses, and selecting the best among individual and aggregated responses. This process is performed in a single chain of thoughts through our seven carefully designed subtasks derived from the Nominal Group Technique (Ven and Delbecq, 1974), a well-established decision-making framework. Our evaluations demonstrate that Multi-expert Prompting significantly outperforms ExpertPrompting and comparable baselines in enhancing the truthfulness, factuality, informativeness, and usefulness of responses while reducing toxicity and hurtfulness. It further achieves state-of-the-art truthfulness by outperforming the best baseline by 8.69% with ChatGPT. Multi-expert Prompting is efficient, explainable, and highly adaptable to diverse scenarios, eliminating the need for manual prompt construction."
summary: 'An EMNLP 2024 prompting method that simulates and aggregates multiple expert responses to improve LLM reliability, safety, and usefulness.'

# Display this page in the Featured widget?
featured: true

url_pdf: 'https://aclanthology.org/2024.emnlp-main.1135.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

image:
  caption: 'Overview of Multi-expert Prompting from Long et al. (2024).'
  preview_only: false
---
