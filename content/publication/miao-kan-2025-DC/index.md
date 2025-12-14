---
title: 'Discursive Circuits: How Do Language Models Understand Discourse Relations?'
# Yisong Miao , Hongfu Liu, Wenqiang Lei, Nancy F. Chen and Min-Yen Kan (2024) Beyond Memorization: The Challenge of Random Memory Access in Language Models. In Proceedings of the Annual Meeting fof the Association of Computational Linguistics (ACL '24).

authors:
  - yisong
  - min

date: '2025-11-04'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the 2025 Conference on Empirical Methods in Natural Language Processing (EMNLP 2025)*
# publication_short: In *EMNLP 2025*

abstract: "Which components in transformer language models are responsible for discourse understanding? We hypothesize that sparse computational graphs, termed as discursive circuits, control how models process discourse relations. Unlike simpler tasks, discourse relations involve longer spans and complex reasoning. To make circuit discovery feasible, we introduce a task called Completion under Discourse Relation (CuDR), where a model completes a discourse given a specified relation. To support this task, we construct a corpus of minimal contrastive pairs tailored for activation patching in circuit discovery. Experiments show that sparse circuits (≈0.2% of a full GPT-2 model) recover discourse understanding in the English PDTB-based CuDR task. These circuits generalize well to unseen discourse frameworks such as RST and SDRT. Further analysis shows lower layers capture linguistic features such as lexical semantics and coreference, while upper layers encode discourse-level abstractions. Feature utility is consistent across frameworks (e.g., coreference supports Expansion-like relations)."

# Summary. An optional shortened abstract.
summary: We introduce a new task, Completion under Discourse Relation (CuDR), to reveal the underlying transformer circuits responsible for discourse understanding.

tags: ["Natural Language Processing", "Discourse", "Large Language Models", "Transformer Models", "Circuit Discovery", "Computational Linguistics", "Mechanistic Interpretability"]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://aclanthology.org/2025.emnlp-main.1657/'
url_code: 'https://github.com/YisongMiao/Discursive-Circuits'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Task Overview: The CuDR task enables discovery of discursive circuits by contrasting model predictions under minimal changes to the discourse connectives. Activation patching reveals components causally responsible for shifting the model’s prediction.'
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
  - discourse

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: "https://yisong.me/publications/emnlp25-DC-Slides.pdf"
---
