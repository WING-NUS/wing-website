---
title: "Self-Improving and Self-Adapting Agents"

summary: "We study test-time scaling (TTS) methods for self-improving and self-adapting agents, advancing a new paradigm of artificial intelligence in which autonomous systems do not merely act, but evolve reliably -- learning from experience, refining behavior in real time, and autonomously modifying their own learning mechanisms."
abstract: "Although modern foundation models (FMs) like ChatGPT are extraordinarily capable, they remain largely fragile: small variations in input (aka ``prompts''), such as subtle phrasing changes or unintended noise, can lead to contradictory or ungrounded reasoning. This limits their broader deployment in high-stakes domains like healthcare, law, science, and governance, where precision, reliability, and interpretability are essential. Our goal is to build FM systems that can continually assess and correct their behavior at test time, making them more **trustworthy** and \textbf{capable}. This requires moving beyond parameter scaling toward inference-time mechanisms that verify, reflect, and adapt. While Test-Time Scaling (TTS) \citep{snell2024scaling} shows that additional compute can improve reasoning, existing methods rely mainly on self-consistency and do not generalize well beyond math and code. During my PhD, I have developed TTS methods that embed domain-specific verification into the inference loop, enabling models to iteratively reason, critique, and refine their outputs across natural language and vision tasks:


As foundation models are increasingly deployed in real-world and high-stakes settings, understanding and improving their behavior through test-time methods has become a central research challenge. 

In this project, we examine how foundation models can self-adapt and self-improve without additional training through structured test-time interventions. We study three main aspects: (1) Understanding 

First, we propose a human- and property-centric evaluation framework grounded in a meta-analysis of over 150 papers, identifying 21 core properties of natural language prompts and analyzing their underexplored influence across models and tasks. Building on these insights, we introduce LongGuide, a method that automatically generates dual-stream guidelines to steer generation toward desired language and output distributions. We further present the first systematic study of format bias in LLMs and propose actionable strategies to reduce over-reliance on superficial input formats. To enhance reasoning and robustness, we propose Multi-expert input modeling, which simulates collaborative agent decision-making, and Adversarial In-Context Learning, a competitive setup that iteratively refines inputs through generator–discriminator interactions. Across 20+ tasks, these methods significantly outperform strong baselines in truthfulness, generalization, and robustness. Our findings offer a comprehensive foundation for building adaptable LLM agents that improve through interaction, feedback, and structure-aware test-time methods—without reliance on additional gradient-based training."

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

**🔥 News**: We are expanding our studies towards multiple directions. Please review our work above. If you have a strong interest in the topics listed and a solid background in mathematics, programming, and research, we encourage you to join us!



