---
title: "Prompt Optimization via Adversarial In-Context Learning"
subtitle: ""
authors:
- long
- Yiran Zhao
- Hannah Brown
- yuxi
- James Xu Zhao
- nancy
- kenji
- qizhe
- Junxian He

author_notes: [Equal Contribution, Equal Contribution, Equal Contribution]
doi: ""

# Schedule page publish date (NOT publication's date).
date: '2024-08-08'
publishDate: '2024-08'
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *62nd Annual Meeting of the Association for Computational Linguistics (Volume 1, Long Papers), Bangkok, Thailand August 11–16, 2024*

abstract: "We propose a new method, Adversarial In-Context Learning (adv-ICL), to optimize prompts for in-context learning (ICL). Inspired by adversarial learning, adv-ICL is implemented as a two-player game between a generator and discriminator, with LLMs acting as both. In each round, given an input prefixed by task instructions and several exemplars, the generator produces an output. The discriminator then classifies the generator’s input-output pair as model-generated or real data. Based on the discriminator’s loss, a prompt modifier LLM proposes possible edits to the generator and discriminator prompts, and the edits that most improve the adversarial loss are selected. We show that applying adv-ICL results in significant improvements over state-of-the-art prompt optimization techniques for both open and closed-source models on 13 generation and classification tasks including summarization, arithmetic reasoning, machine translation, data-to-text generation, and the MMLU and big-bench hard benchmarks. In addition, our method is computationally efficient, easily extensible to other LLMs and tasks, and effective in low-resource settings."
summary: 'An ACL 2024 method that optimizes in-context learning prompts through an adversarial generator-discriminator game.'

# Display this page in the Featured widget?
featured: true

url_pdf: 'https://aclanthology.org/2024.acl-long.395.pdf'
url_code: ''
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

image:
  caption: 'Adversarial In-Context Learning overview from Long et al. (2024).'
  preview_only: false
---
