---
title: Zero-shot Fact Verification by Claim Generation
authors:
- liangming
- Wenhu Chen
- Wenhan Xiong
- min
- William Yang Wang
date: '2021-08-01'
publishDate: '2024-07-11T07:40:56.240829Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 59th Annual Meeting of the Association for Computational
  Linguistics and the 11th International Joint Conference on Natural Language Processing
  (Volume 2: Short Papers)*'
doi: 10.18653/v1/2021.acl-short.61
abstract: Neural models for automated fact verification have achieved promising results
  thanks to the availability of large, human-annotated datasets. However, for each
  new domain that requires fact verification, creating a dataset by manually writing
  claims and linking them to their supporting evidence is expensive. We develop QACG,
  a framework for training a robust fact verification model by using automatically
  generated claims that can be supported, refuted, or unverifiable from evidence from
  Wikipedia. QACG generates question-answer pairs from the evidence and then converts
  them into different types of claims. Experiments on the FEVER dataset show that
  our QACG framework significantly reduces the demand for human-annotated training
  data. In a zero-shot scenario, QACG improves a RoBERTa model′s F1 from 50% to 77%,
  equivalent in performance to 2K+ manually-curated examples. Our QACG code is publicly
  available.
summary: 'A claim-generation framework that improves zero-shot fact verification with synthetic training data.'
image:
  caption: 'QACG framework overview.'
  preview_only: false
links:
- name: URL
  url: https://aclanthology.org/2021.acl-short.61
---
