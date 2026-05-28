---
title: 'Prompter: Zero-shot Adaptive Prefixes for Dialogue State Tracking Domain Adaptation'
authors:
- taha
- min
- nancy
date: '2023-07-01'
publishDate: '2024-07-06T02:22:24.632344Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)*'
doi: 10.18653/v1/2023.acl-long.252
abstract: A challenge in the Dialogue State Tracking (DST) field is adapting models
  to new domains without using any supervised data --- zero-shot domain adaptation.
  Parameter-Efficient Transfer Learning (PETL) has the potential to address this problem
  due to its robustness. However, it has yet to be applied to the zero-shot scenarios,
  as it is not clear how to apply it unsupervisedly. Our method, Prompter, uses descriptions
  of target domain slots to generate dynamic prefixes that are concatenated to the
  key and values at each layer′s self-attention mechanism. This allows for the use
  of prefix-tuning in zero-shot. Prompter outperforms previous methods on both the
  MultiWOZ and SGD benchmarks. In generating prefixes, our analyses find that Prompter
  not only utilizes the semantics of slot descriptions but also how often the slots
  appear together in conversation. Moreover, Prompter′s gains are due to its improved
  ability to distinguish ″none″-valued dialogue slots, compared against baselines.
summary: 'A zero-shot prefix-tuning method that adapts dialogue state tracking to new domains using slot descriptions.'
links:
- name: URL
  url: https://aclanthology.org/2023.acl-long.252
image:
  caption: 'Prompter overview figure.'
  preview_only: false
---
