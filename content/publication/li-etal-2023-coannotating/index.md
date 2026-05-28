---
title: 'CoAnnotating: Uncertainty-Guided Work Allocation between Human and Large Language
  Models for Data Annotation'
authors:
- minzhi
- Taiwei Shi
- Caleb Ziems
- min
- Nancy Chen
- Zhengyuan Liu
- Diyi Yang
date: '2023-12-01'
publishDate: '2024-07-06T02:22:24.561215Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 2023 Conference on Empirical Methods in Natural
  Language Processing*'
doi: 10.18653/v1/2023.emnlp-main.92
abstract: Annotated data plays a critical role in Natural Language Processing (NLP)
  in training models and evaluating their performance. Given recent developments in
  Large Language Models (LLMs), models such as ChatGPT demonstrate zero-shot capability
  on many text-annotation tasks, comparable with or even exceeding human annotators.
  Such LLMs can serve as alternatives for manual annotation, due to lower costs and
  higher scalability. However, limited work has leveraged LLMs as complementary annotators,
  nor explored how annotation work is best allocated among humans and LLMs to achieve
  both quality and cost objectives. We propose CoAnnotating, a novel paradigm for
  Human-LLM co-annotation of unstructured texts at scale. Under this framework, we
  utilize uncertainty to estimate LLMs′ annotation capability. Our empirical study
  shows CoAnnotating to be an effective means to allocate work from results on different
  datasets, with up to 21% performance improvement over random baseline. For code
  implementation, see https://github.com/SALT-NLP/CoAnnotating.
summary: 'A human-LLM co-annotation framework that allocates labeling work by uncertainty.'
links:
- name: URL
  url: https://aclanthology.org/2023.emnlp-main.92
image:
  caption: 'CoAnnotating work allocation overview.'
  preview_only: false
---
