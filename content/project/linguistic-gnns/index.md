---
title: Linguistics Informed Natural Language Processing with Graph Networks

summary: Question-Answering with Linguistics-Based Graph Attention Networks.
abstract: Extractive question answering involves identifying a span of text within a given passage that directly answers a question. We address this task by enhancing traditional QA pipelines with structured representations, first by converting each passage into a constituency-based graph and then enriching it with predicted semantic links from a knowledge graph model. The resulting graph is then processed by a heterogeneous graph transformer to extract accurate and explainable answers.

tags: ["Graph Neural Networks", "Extractive Question Answering", "NLP"]
year: 2024
# Talk start and end times.
#   End time can optionally be hidden by prefixing the line with `#`.
date: "2024-08-01"
date_end: "2025-05-01"
all_day: true

# Is this a featured project? (true/false)
featured: false
#image:
#  caption: 'Image credit: Jesse Gozali Prabawa'
#  focal_point: Right
url_pdf: ""
url_slides: "https://docs.google.com/presentation/d/1yid7pz1SAXtl1QoTAB1__tVuhELnQdDM3LGBsLrqSNQ/edit?usp=sharing"
url_code: "https://github.com/shirshoFYP/"

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["shirsho", "min"]
---

This project tackles the challenge of extractive question answering (QA), where the goal is to find a precise span of text from a passage that answers a given question. Traditional models often rely on deep language representations but may overlook the underlying syntactic and semantic structure of the context. By addressing this gap, the project aims to create more interpretable and linguistically aware QA systems that can better understand how information is organized and related within text.

To achieve this, we first parse each context passage into a constituency tree using a stack Bi-LSTM, forming the backbone of a graph representation. We then enrich this graph with semantic relationships predicted by a knowledge graph link prediction model. The combined structure is processed by a heterogeneous graph transformer integrating both syntactic and semantic cues for answer extraction. This approach allows for more explainable reasoning and provides a structured way to incorporate external knowledge into the QA process.
