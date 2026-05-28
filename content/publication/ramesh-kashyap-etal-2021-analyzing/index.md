---
title: Analyzing the Domain Robustness of Pretrained Language Models, Layer by Layer
authors:
- abhinav
- Laiba Mehnaz
- Bhavitvya Malik
- Abdul Waheed
- Devamanyu Hazarika
- min
- Rajiv Ratn Shah
date: '2021-04-01'
publishDate: '2024-07-11T07:40:56.223020Z'
publication_types:
- paper-conference
publication: '*Proceedings of the Second Workshop on Domain Adaptation for NLP*'
abstract: The robustness of pretrained language models(PLMs) is generally measured
  using performance drops on two or more domains. However, we do not yet understand
  the inherent robustness achieved by contributions from different layers of a PLM.
  We systematically analyze the robustness of these representations layer by layer
  from two perspectives. First, we measure the robustness of representations by using
  domain divergence between two domains. We find that i) Domain variance increases
  from the lower to the upper layers for vanilla PLMs; ii) Models continuously pretrained
  on domain-specific data (DAPT)(Gururangan et al., 2020) exhibit more variance than
  their pretrained PLM counterparts; and that iii) Distilled models (e.g., DistilBERT)
  also show greater domain variance. Second, we investigate the robustness of representations
  by analyzing the encoded syntactic and semantic information using diagnostic probes.
  We find that similar layers have similar amounts of linguistic information for data
  from an unseen domain.
summary: 'A layer-by-layer study of how pretrained language model representations vary across domains.'
image:
  caption: 'Domain divergence across PLM layers.'
  preview_only: false
links:
- name: URL
  url: https://aclanthology.org/2021.adaptnlp-1.23
---
