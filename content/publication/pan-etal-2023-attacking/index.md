---
title: Attacking Open-domain Question Answering by Injecting Misinformation
authors:
- liangming
- Wenhu Chen
- min
- William Yang Wang
date: '2023-11-01'
publishDate: '2024-07-06T02:22:24.540512Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 13th International Joint Conference on Natural Language
  Processing and the 3rd Conference of the Asia-Pacific Chapter of the Association
  for Computational Linguistics (Volume 1: Long Papers)*'
doi: 10.18653/v1/2023.ijcnlp-main.35
abstract: "With a rise in false, inaccurate, and misleading information in propaganda, news, and social media, real-world question answering systems face the challenges of synthesizing and reasoning over misinformation-polluted contexts to derive correct answers. This urgency gives rise to the need to make QA systems robust to misinformation, a topic previously unexplored. We study the risk of misinformation to QA models by investigating the sensitivity of open-domain QA models to corpus pollution with misinformation documents. We curate both human-written and model-generated false documents that we inject into the evidence corpus of QA models, and assess the impact on the performance of these systems. Experiments show that QA models are vulnerable to even small amounts of evidence contamination brought by misinformation, with large absolute performance drops on all models. Misinformation attack brings more threat when fake documents are produced at scale by neural models or the attacker targets hacking specific questions of interest. To defend against such a threat, we discuss the necessity of building a misinformation-aware QA system that integrates question answering and misinformation detection in a joint fashion."
summary: 'A study showing that misinformation injection can seriously degrade open-domain QA and outlining defenses.'
links:
- name: URL
  url: https://aclanthology.org/2023.ijcnlp-main.35
image:
  caption: 'Misinformation attack pipeline.'
  preview_only: false
---
