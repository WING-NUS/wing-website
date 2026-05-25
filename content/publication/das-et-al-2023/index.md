---
title: 'Statistical Machine Translation for Indic Languages'
authors:
- Sudhansu Bala Das
- divyajyoti
- Tapas Kumar Mishra
- Bidyut Kumar Patra
date: '2024-06-03'
publishDate: '2024-08-02T16:08:01.479Z'
publication_types:
- article
publication: '*Natural Language Processing*'
abstract: Statistical Machine Translation (SMT) systems use various probabilistic and statistical Natural Language Processing (NLP) methods to automatically translate from one language to another language while retaining the originality of the context. This paper aims to discuss the development of bilingual SMT models for translating English into fifteen low-resource Indic languages (ILs) and vice versa. The process to build the SMT model is described and explained using a workflow diagram. Samanantar and OPUS corpus are utilized for training, and Flores200 corpus is used for fine-tuning and testing purposes. The paper also highlights various preprocessing methods used to deal with corpus noise. The Moses open-source SMT toolkit is being investigated for the system’s development. The impact of distance-based reordering and Morpho-syntactic Descriptor Bidirectional Finite-State Encoder (msd-bidirectional-fe) reordering on ILs is compared in the paper. This paper provides a comparison of SMT models with Neural Machine Translation (NMT) for ILs. All the experiments assess the translation quality using standard metrics such as BiLingual Evaluation Understudy, Rank-based Intuitive Bilingual Evaluation Score, Translation Edit Rate, and Metric for Evaluation of Translation with Explicit Ordering. From the result, it is observed that msd-bidirectional-fe reordering performs better than the distance-based reordering model for ILs. It is also noticed that even though the IL-English and English-IL systems are trained using the same corpus, the former performs better for all the evaluation metrics. The comparison between SMT and NMT shows that across various languages, SMT performs better in some cases, while NMT outperforms in others.
summary: 'A Cambridge NLP article building and evaluating SMT baselines for English-Indic and Indic-English translation across 15 low-resource Indic languages.'
links:
- name: URL
  url: https://www.cambridge.org/core/journals/natural-language-processing/article/statistical-machine-translation-for-indic-languages/022C193C28525D1C88A731C35DF1C388
image:
  caption: 'Workflow of the Statistical Machine Translation model from Das et al. (2024).'
  preview_only: false
---
