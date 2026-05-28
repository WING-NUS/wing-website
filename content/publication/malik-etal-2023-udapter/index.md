---
title: UDAPTER - Efficient Domain Adaptation Using Adapters
authors:
- Bhavitvya Malik
- abhinav
- min
- soujanya
date: '2023-05-01'
publishDate: '2024-07-06T02:22:24.610292Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 17th Conference of the European Chapter of the Association
  for Computational Linguistics*'
doi: 10.18653/v1/2023.eacl-main.165
abstract: 'We propose two methods to make unsupervised domain adaptation (UDA) more
  parameter efficient using adapters -- small bottleneck layers interspersed with
  every layer of the large-scale pre-trained language model (PLM). The first method
  deconstructs UDA into a two-step process: first by adding a domain adapter to learn
  domain-invariant information and then by adding a task adapter that uses domain-invariant
  information to learn task representations in the source domain. The second method
  jointly learns a supervised classifier while reducing the divergence measure. Compared
  to strong baselines, our simple methods perform well in natural language inference
  (MNLI) and the cross-domain sentiment classification task. We even outperform unsupervised
  domain adaptation methods such as DANN and DSN in sentiment classification, and
  we are within 0.85% F1 for natural language inference task, by fine-tuning only
  a fraction of the full model parameters. We release our code at this URL.'
summary: 'Two adapter-based methods for parameter-efficient unsupervised domain adaptation.'
links:
- name: URL
  url: https://aclanthology.org/2023.eacl-main.165
image:
  caption: 'UDAPTER domain adaptation overview.'
  preview_only: false
---
