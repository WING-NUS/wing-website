---
title: "LLMs Are Biased Towards Output Formats! Systematically Evaluating and Mitigating Output Format Bias of LLMs"
subtitle: ""
authors:
- long
- hai
- Tiviatis Sim
- Hieu Dao
- Shafiq Joty
- Kenji Kawaguchi
- Nancy F. Chen
- min

doi: ""

# Schedule page publish date (NOT publication's date).
date: '2025-05-05'
publishDate: '2025-05'
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *2025 Annual Conference of the Nations of the Americas Chapter of the Association for Computational Linguistics, Albuquerque, New Mexico April 29–May 4, USA, 2025*

abstract: "We present the first systematic evaluation examining format bias in performance of large language models (LLMs). Our approach distinguishes between two categories of an evaluation metric under format constraints to reliably and accurately assess performance: one measures performance when format constraints are adhered to, while the other evaluates performance regardless of constraint adherence. We then define a metric for measuring the format bias of LLMs and establish effective strategies to reduce it. Subsequently, we present our empirical format bias evaluation spanning four commonly used categories---multiple-choice question-answer, wrapping, list, and mapping---covering 15 widely-used formats. Our evaluation on eight generation tasks uncovers significant format bias across state-of-the-art LLMs. We further discover that improving the format-instruction following capabilities of LLMs across formats potentially reduces format bias. Based on our evaluation findings, we study prompting and fine-tuning with synthesized format data techniques to mitigate format bias. Our methods successfully reduce the variance in ChatGPT's performance among wrapping formats from 235.33 to 0.71 (%^2)"
summary: 'A systematic evaluation of output-format bias in LLMs, with prompting and fine-tuning strategies for reducing format sensitivity.'

# Display this page in the Featured widget?
featured: true

url_pdf: 'https://aclanthology.org/2025.naacl-long.15.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

image:
  caption: 'Figure from Long et al. (2025).'
  preview_only: false
---
