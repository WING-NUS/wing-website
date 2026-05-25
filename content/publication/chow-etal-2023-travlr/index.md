---
title: 'TraVLR: Now You See It, Now You Don′t! A Bimodal Dataset for Evaluating Visio-Linguistic
  Reasoning'
authors:
- kengji
- samson
- min
date: '2023-05-01'
publishDate: '2024-07-06T02:22:24.618335Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 17th Conference of the European Chapter of the Association
  for Computational Linguistics*'
doi: 10.18653/v1/2023.eacl-main.242
abstract: Numerous visio-linguistic (V+L) representation learning methods have been
  developed, yet existing datasets do not adequately evaluate the extent to which
  they represent visual and linguistic concepts in a unified space. We propose several
  novel evaluation settings for V+L models, including cross-modal transfer. Furthermore,
  existing V+L benchmarks often report global accuracy scores on the entire dataset,
  making it difficult to pinpoint the specific reasoning tasks that models fail and
  succeed at. We present TraVLR, a synthetic dataset comprising four V+L reasoning
  tasks. TraVLR′s synthetic nature allows us to constrain its training and testing
  distributions along task-relevant dimensions, enabling the evaluation of out-of-distribution
  generalisation. Each example in TraVLR redundantly encodes the scene in two modalities,
  allowing either to be dropped or added during training or testing without losing
  relevant information. We compare the performance of four state-of-the-art V+L models,
  finding that while they perform well on test examples from the same modality, they
  all fail at cross-modal transfer and have limited success accommodating the addition
  or deletion of one modality. We release TraVLR as an open challenge for the research
  community.
summary: 'A bimodal benchmark for probing visio-linguistic reasoning and cross-modal transfer.'
links:
- name: URL
  url: https://aclanthology.org/2023.eacl-main.242
image:
  caption: 'TraVLR reasoning example figure.'
  preview_only: false
---
