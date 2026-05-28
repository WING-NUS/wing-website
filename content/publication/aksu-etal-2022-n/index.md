---
title: N-Shot Learning for Augmenting Task-Oriented Dialogue State Tracking
authors:
- taha
- Zhengyuan Liu
- min
- nancy
date: '2022-05-01'
publishDate: '2024-07-05T17:09:42.588862Z'
publication_types:
- paper-conference
publication: '*Findings of the Association for Computational Linguistics: ACL 2022*'
doi: 10.18653/v1/2022.findings-acl.131
abstract: Augmentation of task-oriented dialogues has followed standard methods used
  for plain-text such as back-translation, word-level manipulation, and paraphrasing
  despite its richly annotated structure. In this work, we introduce an augmentation
  framework that utilizes belief state annotations to match turns from various dialogues
  and form new synthetic dialogues in a bottom-up manner. Unlike other augmentation
  strategies, it operates with as few as five examples. Our augmentation strategy
  yields significant improvements when both adapting a DST model to a new domain,
  and when adapting a language model to the DST task, on evaluations with TRADE and
  TOD-BERT models. Further analysis shows that our model performs better on seen values
  during training, and it is also more robust to unseen values. We conclude that exploiting
  belief state annotations enhances dialogue augmentation and results in improved
  models in n-shot training scenarios.
summary: 'A belief-state-driven dialogue augmentation method that improves n-shot task-oriented DST.'
image:
  caption: 'Dialogue augmentation framework.'
  preview_only: false
links:
- name: URL
  url: https://aclanthology.org/2022.findings-acl.131
---
