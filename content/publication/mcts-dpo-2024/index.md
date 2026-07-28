---
title: 'Monte Carlo Tree Search Boosts Reasoning via Iterative Preference Learning'
authors:
- yuxi
- Anirudh Goyal
- Wenyue Zheng
- min
- Timothy P. Lillicrap
- kenji
- qizhe
date: '2024-12-14'
publishDate: '2026-07-27T00:00:00Z'
publication_types:
- paper-conference
publication: '*NeurIPS 2024 Workshop on System-2 Reasoning at Scale*'
abstract: 'This paper enhances LLM reasoning through an iterative preference learning process inspired by AlphaZero. Monte Carlo Tree Search collects preference data iteratively, using its look-ahead ability to break instance-level rewards into step-level signals, while outcome validation and stepwise self-evaluation keep intermediate steps consistent, and Direct Preference Optimization updates the policy on the resulting step-level preferences. Theoretical analysis shows the importance of on-policy sampled data, and the method lifts Mistral-7B accuracy to 81.8% on GSM8K, 34.7% on MATH, and 76.4% on ARC-C.'
summary: 'A NeurIPS 2024 workshop paper on boosting reasoning with MCTS-driven iterative preference learning.'
links:
- name: OpenReview
  url: https://openreview.net/forum?id=s004OmYP2P
- name: arXiv
  url: https://arxiv.org/abs/2405.00451
url_pdf: https://openreview.net/pdf?id=s004OmYP2P
url_code: https://github.com/YuxiXie/MCTS-DPO
---
