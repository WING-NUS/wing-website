---
title: Mind Your Inflections! Improving NLP for Non-Standard Englishes with Base-Inflection
  Encoding
authors:
- samson
- shafiq
- Lav Varshney
- min
date: '2020-11-01'
publishDate: '2024-07-11T07:40:56.262379Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 2020 Conference on Empirical Methods in Natural
  Language Processing (EMNLP)*'
doi: 10.18653/v1/2020.emnlp-main.455
abstract: Inflectional variation is a common feature of World Englishes such as Colloquial
  Singapore English and African American Vernacular English. Although comprehension
  by human readers is usually unimpaired by non-standard inflections, current NLP
  systems are not yet robust. We propose Base-Inflection Encoding (BITE), a method
  to tokenize English text by reducing inflected words to their base forms before
  reinjecting the grammatical information as special symbols. Fine-tuning pretrained
  NLP models for downstream tasks using our encoding defends against inflectional
  adversaries while maintaining performance on clean data. Models using BITE generalize
  better to dialects with non-standard inflections without explicit training and translation
  models converge faster when trained with BITE. Finally, we show that our encoding
  improves the vocabulary efficiency of popular data-driven subword tokenizers. Since
  there has been no prior work on quantitatively evaluating vocabulary efficiency,
  we propose metrics to do so.
links:
- name: URL
  url: https://aclanthology.org/2020.emnlp-main.455
---
