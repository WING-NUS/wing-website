---
title: Fact-Checking Complex Claims with Program-Guided Reasoning
authors:
- liangming
- Xiaobao Wu
- xinyuan
- Anh Tuan Luu
- William Yang Wang
- min
- Preslav Nakov
date: '2023-07-01'
publishDate: '2024-07-06T02:22:24.639283Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 61st Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)*'
doi: 10.18653/v1/2023.acl-long.386
abstract: Fact-checking real-world claims often requires collecting multiple pieces
  of evidence and applying complex multi-step reasoning. In this paper, we present
  Program-Guided Fact-Checking (ProgramFC), a novel fact-checking model that decomposes
  complex claims into simpler sub-tasks that can be solved using a shared library
  of specialized functions. We first leverage the in-context learning ability of large
  language models to generate reasoning programs to guide the verification process.
  Afterward, we execute the program by delegating each sub-task to the corresponding
  sub-task handler. This process makes our model both explanatory and data-efficient,
  providing clear explanations of its reasoning process and requiring minimal training
  data. We evaluate ProgramFC on two challenging fact-checking datasets and show that
  it outperforms seven fact-checking baselines across different settings of evidence
  availability, with explicit output programs that benefit human debugging. Our codes
  and data are publicly available at https://github.com/mbzuai-nlp/ProgramFC.
summary: 'A program-guided fact-checking model that decomposes complex claims into executable sub-tasks.'
links:
- name: URL
  url: https://aclanthology.org/2023.acl-long.386
image:
  caption: 'ProgramFC workflow overview.'
  preview_only: false
---
