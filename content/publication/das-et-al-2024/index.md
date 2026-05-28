---
title: 'Multilingual Neural Machine Translation for Indic to Indic Languages'
authors:
- Sudhansu Bala Das
- divyajyoti
- Tapas Kumar Mishra
- Bidyut Kumar Patra
- Asif Ekbal
date: '2024-05-10'
publishDate: '2024-08-02T16:12:33.521Z'
publication_types:
- article
publication: '*ACM Transactions on Asian and Low-Resource Language Information Processing*'
abstract: The method of translation from one language to another without human intervention is known as Machine Translation (MT). Multilingual neural machine translation (MNMT) is a technique for MT that builds a single model for multiple languages. It is preferred over other approaches, since it decreases training time and improves translation in low-resource contexts, i.e., for languages that have insufficient corpus. However, good-quality MT models are yet to be built for many scenarios such as for Indic-to-Indic Languages (IL-IL). Hence, this article is an attempt to address and develop the baseline models for low-resource languages i.e., IL-IL (for 11 Indic Languages (ILs)) in a multilingual environment. The models are built on the Samanantar corpus and analyzed on the Flores-200 corpus. All the models are evaluated using standard evaluation metrics i.e., Bilingual Evaluation Understudy (BLEU) score (with the range of 0 to 100). This article examines the effect of the grouping of related languages, namely, East Indo-Aryan (EI), Dravidian (DR), and West Indo-Aryan (WI) on the MNMT model. From the experiments, the results reveal that related language grouping is beneficial for the WI group only while it is detrimental for the EI group and it shows an inconclusive effect on the DR group. The role of pivot-based MNMT models in enhancing translation quality is also investigated in this article. Owing to the presence of large good-quality corpora from English (EN) to ILs, MNMT IL-IL models using EN as a pivot are built and examined. To achieve this, English-Indic Language (EN-IL) models are developed with and without the usage of related languages. Results show that the use of related language grouping is advantageous specifically for EN to ILs. Thus, related language groups are used for the development of pivot MNMT models. It is also observed that the usage of pivot models greatly improves MNMT baselines. Furthermore, the effect of transliteration on ILs is also analyzed in this article. To explore transliteration, the best MNMT models from the previous approaches (in most of cases pivot model using related groups) are determined and built on corpus transliterated from the corresponding scripts to a modified Indian language Transliteration script (ITRANS). The outcome of the experiments indicates that transliteration helps the models built for lexically rich languages, with the best increment of BLEU scores observed in Malayalam (ML) and Tamil (TA), i.e., 6.74 and 4.72, respectively. The BLEU score using transliteration models ranges from 7.03 to 24.29. The best model obtained is the Punjabi (PA)-Hindi (HI) language pair trained on PA-WI transliterated corpus.
summary: 'An ACM TALLIP article developing multilingual neural baselines, pivot models, language grouping, and transliteration strategies for Indic-to-Indic translation.'
links:
- name: URL
  url: https://dl.acm.org/doi/full/10.1145/3652026
---
