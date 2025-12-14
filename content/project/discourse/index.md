---
title: Discourse and LLMs

summary: We measure and enhance LLMs’ discourse understanding, focusing on faithfulness and mechanistic interpretability.
abstract: "Large language models (LLMs) can now generate coherent text, but can they truly understand language? In this project, we explore discourse understanding, a foundational objective in natural language processing (NLP). In the first part, we refine the notion of understanding as faithful behavior under a series of Socratic-style questions (appeared at ACL 2024). In the second part, we take a causal approach to mechanistically interpret the key components of transformer models in discourse processing (appeared at EMNLP 2025)."

tags: ["CL", "Discourse", "NLP", "LLM", "Computational Linguistics", "Mechanistic Interpretability", "Circuit Discovery", "Transformer Models"]
year: 2025

date: '2025-11-04' # EMNLP 25's conference date. 

all_day: true

# Is this a featured project? (true/false)
featured: true
image:
  caption: 'The workflow of Discursive Socratic Questioning (left) and the evaluation results (right).'
  focal_point: Right
url_pdf: 'https://aclanthology.org/2024.acl-long.341/'
url_slides: 'https://yisong.me/publications/acl24-DiSQ-Slides.pdf'
url_code: 'https://github.com/YisongMiao/DiSQ-Score'
# url_video: ''

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["yisong", "min"]

---
Large language models (LLMs) can now generate coherent text, but can they truly understand language? In this project, we explore discourse understanding, a foundational objective in natural language processing (NLP). In the first part, we refine the notion of understanding as faithful behavior under a series of Socratic-style questions (appeared at ACL 2024). In the second part, we take a causal approach to mechanistically interpret the key components of transformer models in discourse processing (appeared at EMNLP 2025).

Yisong, a PhD student at WING, began his research journey by tackling the fundamental question: Do language models truly understand text? Over time, he refined this broad inquiry into the specific challenge of discourse understanding. In his recent work, advised by Prof. Min, they introduced a more precise framework for measuring discourse comprehension from three discourse-specific perspectives, while also contributing insights into broader LLM challenges such as logical consistency. Currently, Yisong and Min are delving deeper into the mechanisms behind how models process and understand discourse, and they discovered that sparse computational graphs, termed as "discursive circuits", control how models process discourse relations.
