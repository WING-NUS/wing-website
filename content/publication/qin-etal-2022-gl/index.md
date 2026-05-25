---
title: 'GL-CLeF: A Global--Local Contrastive Learning Framework for Cross-lingual
  Spoken Language Understanding'
authors:
- Libo Qin
- Qiguang Chen
- Tianbao Xie
- Qixin Li
- Jian-Guang Lou
- Wanxiang Che
- min
date: '2022-05-01'
publishDate: '2024-07-05T17:09:42.638128Z'
publication_types:
- paper-conference
publication: '*Proceedings of the 60th Annual Meeting of the Association for Computational
  Linguistics (Volume 1: Long Papers)*'
doi: 10.18653/v1/2022.acl-long.191
abstract: Due to high data demands of current methods, attention to zero-shot cross-lingual
  spoken language understanding (SLU) has grown, as such approaches greatly reduce
  human annotation effort. However, existing models solely rely on shared parameters,
  which can only perform implicit alignment across languages. We present Global-Local
  Contrastive Learning Framework (GL-CLeF) to address this shortcoming. Specifically,
  we employ contrastive learning, leveraging bilingual dictionaries to construct multilingual
  views of the same utterance, then encourage their representations to be more similar
  than negative example pairs, which achieves to explicitly align representations
  of similar sentences across languages. In addition, a key step in GL-CLeF is a proposed
  Local and Global component, which achieves a fine-grained cross-lingual transfer
  (i.e., sentence-level Local intent transfer, token-level Local slot transfer, and
  semantic-level Global transfer across intent and slot). Experiments on MultiATIS++
  show that GL-CLeF achieves the best performance and successfully pulls representations
  of similar sentences across languages closer.
summary: 'A contrastive cross-lingual SLU framework with global and local alignment components.'
image:
  caption: 'GL-CLeF cross-lingual alignment framework.'
  preview_only: false
links:
- name: URL
  url: https://aclanthology.org/2022.acl-long.191
---
