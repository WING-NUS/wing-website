---
title: "Self-Improving and Self-Adapting Agents"

summary: "We study test-time scaling (TTS) methods for self-improving and self-adapting agents, advancing a new paradigm of artificial intelligence in which autonomous systems do not merely act, but evolve reliably through learning from experience, refining behavior in real time, and autonomously modifying their own learning mechanisms."
abstract: "Although modern foundation models (FMs) like ChatGPT are extraordinarily capable, they remain largely fragile: small variations in input (aka ``prompts''), such as subtle phrasing changes or unintended noise, can lead to contradictory or ungrounded reasoning. This limits their broader deployment in high-stakes domains like healthcare, law, science, and governance, where precision, reliability, and interpretability are essential. 

In this project, we aim to build the next generation of FM systems that can continually assess and correct their behavior at test time, making them more trustworthy and capable. Our studies span three main aspects: 
- **(1) Understand Fragility of FMs**: How can we interpretably understand model behavior through the lens of prompts to improve FMs reliably? ([NLPromptEval @ ACL'25](https://aclanthology.org/2025.acl-long.292/), [FormatBiasEval @ NAACL'25](https://aclanthology.org/2025.naacl-long.15/)) 

- **(2) Study TTS Methods**: With the above understanding, how can we develop TTS to enhance model effectively and reliably? ([Multi-Expert Prompting @ EMNLP'24](https://aclanthology.org/2024.emnlp-main.1135/), [adv-ICL @ ACL'24](https://aclanthology.org/2024.acl-long.395/), [Chain-of-Opinion @ COLING'25](https://aclanthology.org/2025.coling-main.172/))

- **(3) Self-Improving Agents**: How can we build powerful TTS-powered agentic systems that critique and refine their own behavior, ultimately enabling autonomous self-improvement? ([LongGuide (Self-Adapting Agent) @ ACL'25](https://aclanthology.org/2025.findings-acl.176/), [VISTA (Self-Improving Agent)](https://g-vista.github.io/))

Our findings so far have offered a foundation for building foundation model agents that improve through interaction, feedback, and structure-aware test-time methods—without reliance on additional gradient-based training."

tags: ["Multi-Agent System", "Evolution", "LLM", "Machine Learning"]
year: 2025
date: '2025-08-01' 

all_day: true

# Is this a featured project? (true/false)
featured: true
# image:
#   caption: 'The workflow of Discursive Socratic Questioning (left) and the evaluation results (right).'
#   focal_point: Right
# url_pdf: 'https://arxiv.org/abs/2506.06950'  # Replace with actual publication URL
# url_slides: 'https://your-slides-url.pdf'  # Optional: link to presentation slides
# url_video: ''

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["long", "hai", "duy", "trong", "wangyiwen", "anhnguyen", "min"]

---

**🎯 Overview**: We study test-time scaling (TTS) methods for self-improving and self-adapting agents, advancing a new paradigm of artificial intelligence in which autonomous systems do not merely act, but evolve reliably through learning from experience, refining behavior in real time, and autonomously modifying their own learning mechanisms.

**🧠 Abstract**: Although modern foundation models (FMs) like ChatGPT are extraordinarily capable, they remain largely fragile: small variations in input (aka ``prompts''), such as subtle phrasing changes or unintended noise, can lead to contradictory or ungrounded reasoning. This limits their broader deployment in high-stakes domains like healthcare, law, science, and governance, where precision, reliability, and interpretability are essential. 

In this project, we aim to build the next generation of FM systems that can continually assess and correct their behavior at test time, making them more **trustworthy** and **capable**. Our studies span three main aspects: 
- **(1) Understand Fragility of FMs**: How can we interpretably understand model behavior through the lens of prompts to improve FMs reliably? ([NLPromptEval @ ACL'25](https://aclanthology.org/2025.acl-long.292/), [FormatBiasEval @ NAACL'25](https://aclanthology.org/2025.naacl-long.15/)) 

- **(2) Study TTS Methods**: With the above understanding, how can we develop TTS to enhance model effectively and reliably? ([Multi-Expert Prompting @ EMNLP'24](https://aclanthology.org/2024.emnlp-main.1135/), [adv-ICL @ ACL'24](https://aclanthology.org/2024.acl-long.395/), [Chain-of-Opinion @ COLING'25](https://aclanthology.org/2025.coling-main.172/))

- **(3) Self-Improving Agents**: How can we build powerful TTS-powered agentic systems that critique and refine their own behavior, ultimately enabling autonomous self-improvement? ([LongGuide (Self-Adapting Agent) @ ACL'25](https://aclanthology.org/2025.findings-acl.176/), [VISTA (Self-Improving Agent)](https://g-vista.github.io/))

Our findings so far have offered a foundation for building foundation model agents that improve through interaction, feedback, and structure-aware test-time methods—without reliance on additional gradient-based training.

**🔥 News**: We are expanding our studies towards multiple directions. Please review our work above. If you have a strong interest in the topics listed and a solid background in mathematics and programming, and optionally in research, come to join us!



