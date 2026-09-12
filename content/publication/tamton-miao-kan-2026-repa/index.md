---
title: 'REPA: Reproducibility Evaluation via an Autonomous Pipeline Architecture'

authors:
  - nura
  - yisong
  - min

# Publication date listed on OpenReview.
date: '2026-07-07'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2026-07-06T00:00:00Z'
publication_types: ['paper-conference']

# Workshop title from the OpenReview BibTeX record.
publication: '*ICML 2026 AI for Science Workshop*'
publication_short: '*ICML 2026 AI4Science*'

abstract: "We present REPA, a framework to autonomously reproduce text classification experiments from paper descriptions, without access to reference code or repositories, through a pipeline that runs autonomously after a single human review checkpoint on the extracted configuration. Unlike prior AI Scientist systems, REPA targets the reproduction problem directly by deconstructing it as a four-stage process incorporating protocol extraction, input preparation, experiment generation, and evaluation. On a favorable set of ten well-documented text classification papers, REPA replicates eight studies when instantiated with a GPT-4o backend, and five with Qwen3-Coder-30B. Compared to a replication rate of zero via direct prompting, our results with REPA establish a performance ceiling for current LLM automation as of mid-2026 and the importance of template scaffolding in scientific reproduction success."

# Summary. An optional shortened abstract.
summary: We introduce REPA, an LLM-powered pipeline that reproduces text classification experiments from paper descriptions through protocol extraction, input preparation, experiment generation, and evaluation.

# Keywords listed on OpenReview.
tags: ["AI Scientist", "Reproducibility", "LLMs"]

# Display this page in the Featured widget?
featured: true

links:
  - name: OpenReview
    url: 'https://openreview.net/forum?id=lfOyOMFZ4d'

url_pdf: 'https://openreview.net/pdf?id=lfOyOMFZ4d'
url_code: 'https://github.com/nuratamton/ai-scientist-reproducibility'

# Featured image (optional).
image:
  caption: ''
  preview_only: false

# Associated Projects (optional).
projects:
  - aiscientist

# External slides (optional).
url_slides: ''
---
