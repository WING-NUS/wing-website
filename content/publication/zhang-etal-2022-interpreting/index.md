---
title: Interpreting the Robustness of Neural NLP Models to Textual Perturbations
authors:
- yunxiang
- liangming
- samson
- min
date: '2022-05-01'
publishDate: '2024-07-05T17:09:42.596004Z'
publication_types:
- paper-conference
publication: '*Findings of the Association for Computational Linguistics: ACL 2022*'
doi: 10.18653/v1/2022.findings-acl.315
abstract: Modern Natural Language Processing (NLP) models are known to be sensitive
  to input perturbations and their performance can decrease when applied to real-world,
  noisy data. However, it is still unclear why models are less robust to some perturbations
  than others. In this work, we test the hypothesis that the extent to which a model
  is affected by an unseen textual perturbation (robustness) can be explained by the
  learnability of the perturbation (defined as how well the model learns to identify
  the perturbation with a small amount of evidence). We further give a causal justification
  for the learnability metric. We conduct extensive experiments with four prominent
  NLP models --- TextRNN, BERT, RoBERTa and XLNet --- over eight types of textual
  perturbations on three datasets. We show that a model which is better at identifying
  a perturbation (higher learnability) becomes worse at ignoring such a perturbation
  at test time (lower robustness), providing empirical support for our hypothesis.
summary: 'A learnability-based explanation of why NLP models are brittle to textual perturbations.'
image:
  caption: 'Robustness and learnability analysis.'
  preview_only: false
links:
- name: URL
  url: https://aclanthology.org/2022.findings-acl.315
---
