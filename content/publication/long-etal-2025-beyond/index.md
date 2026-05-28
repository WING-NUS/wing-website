---
title: "Beyond In-Context Learning: Aligning Long-form Generation of Large Language Models via Task-Inherent Attribute Guidelines"
subtitle: ""
authors:
- long
- Duong Ngoc Yen
- trong
- Anh Tuan Luu
- Kenji Kawaguchi
- shafiq
- min
- nancy

doi: ""

# Schedule page publish date (NOT publication's date).
date: '2025-08-01'
publishDate: '2025-08'
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *Findings of the 63nd Annual Meeting of the Association for Computational Linguistics, Vienna, Austria, July 27–August 1st, 2025*

abstract: "In-context learning (ICL) is an important yet not fully understood ability of pre-trained large language models (LLMs). It can greatly enhance task performance using a few examples, termed demonstrations, without fine-tuning. Although effective in question answering, ICL often underperforms in long-form generation tasks such as summarization. Under appropriately realistic assumptions, we empirically and theoretically show that ICL demonstrations alone are insufficient to teach LLMs the task’s language and format distributions for generation. We argue for explicit exposure to the task distributions and hypothesize that defining them by prompting enhances model performance. To this end, we present LongGuide, which efficiently generates two parallel streams of guidelines capturing task language and format properties: (i) Metric Guidelines (MGs) that instruct models to optimize self-evaluated metrics; and (ii) Output Constraint Guidelines (OCGs) that constrain generation at both token and sentence levels. LongGuide automatically selects the best combination of guidelines, improving both strong open- and closed-source LLMs by over 5% in both zero- and few-shot settings. We show that LongGuide is generalizable, learnable by weak models to enhance strong ones, and integrates synergistically with automatic prompt optimizers."
summary: 'LongGuide generates task-inherent metric and output-constraint guidelines to improve long-form LLM generation beyond demonstrations alone.'

# Display this page in the Featured widget?
featured: true

url_pdf: 'https://aclanthology.org/2025.findings-acl.176.pdf'
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
