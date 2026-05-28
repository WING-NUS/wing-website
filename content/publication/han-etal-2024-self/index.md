---
title: Self-Adaptive Sampling for Accurate Video Question Answering on Image Text
  Models
authors:
- Wei Han
- Hui Chen
- min
- Soujanya Poria
date: '2024-06-01'
publishDate: '2024-07-05T17:09:42.578623Z'
publication_types:
- paper-conference
publication: '*Findings of the Association for Computational Linguistics: NAACL 2024*'
abstract: Image--text models (ITMs) is the prevalent architecture to solve video question--answering
  tasks, which requires only a few input frames to save huge computational cost compared
  to video--language models.However, we find existent ITM video question--answering
  solutions either 1) adopt simplistic and unintentional sampling strategies, which
  may miss key frames to offer the answer clues; or 2) sample a large number of frames
  into divided groups, which the computational sources can not accommodate. In this
  work, we aim at an efficient sampling method towards the few-frame situations.We
  first summarize a family of prior sampling methods based on question--frame correlation
  into a unified one, dubbed *Most Implied Frames* (MIF). Through some primary results
  and analysis, Through analysis, we form a hypothesis that question-aware sampling
  is not necessary, from which we further propose the other method *Most Dominant
  Frames* (MDF).Experimental results on four public datasets and three advanced ITMs
  demonstrate that our proposed strategies can boost the performance for image--text
  pretrained models, and have a wide application scenario in terms of model architectures
  and dataset types. Our code is available at https://github.com/declare-lab/Sealingr̆lhttps://github.com/declare-lab/Sealing.
summary: 'A NAACL Findings paper proposing efficient frame sampling strategies that improve video question answering with image-text models.'
links:
- name: URL
  url: https://aclanthology.org/2024.findings-naacl.162
image:
  caption: 'Existing sampling strategies for video question-answering tasks from Han et al. (2024).'
  preview_only: false
---
