---
title: Unsupervised Multi-hop Question Answering by Question Generation
authors:
- liangming
- Wenhu Chen
- Wenhan Xiong
- min
- William Yang Wang
date: '2021-06-01'
publishDate: '2024-07-11T07:40:56.233397Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 2021 Conference of the North American Chapter of
  the Association for Computational Linguistics: Human Language Technologies*'
doi: 10.18653/v1/2021.naacl-main.469
abstract: Obtaining training data for multi-hop question answering (QA) is time-consuming
  and resource-intensive. We explore the possibility to train a well-performed multi-hop
  QA model without referencing any human-labeled multi-hop question-answer pairs,
  i.e., unsupervised multi-hop QA. We propose MQA-QG, an unsupervised framework that
  can generate human-like multi-hop training data from both homogeneous and heterogeneous
  data sources. MQA-QG generates questions by first selecting/generating relevant
  information from each data source and then integrating the multiple information
  to form a multi-hop question. Using only generated training data, we can train a
  competent multi-hop QA which achieves 61% and 83% of the supervised learning performance
  for the HybridQA and the HotpotQA dataset, respectively. We also show that pretraining
  the QA system with the generated data would greatly reduce the demand for human-annotated
  training data. Our codes are publicly available at https://github.com/teacherpeterpan/Unsupervised-Multi-hop-QA.
summary: 'An unsupervised multi-hop QA framework that generates synthetic training data from heterogeneous sources.'
image:
  caption: 'MQA-QG bridge-type question generation framework.'
  preview_only: false
links:
- name: URL
  url: https://aclanthology.org/2021.naacl-main.469
---
