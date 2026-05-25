---
title: "Adaptive Multi-Modalities Fusion in Sequential Recommendation Systems"
authors:
  - hengchang
  - Wei Guo
  - Yong Liu
  - min
date: "2023-10-21"
publishDate: "2024-07-11T07:40:56.306034Z"
publication_types:
  - "paper-conference"
publication: "*Proceedings of the 32nd ACM International Conference on Information and Knowledge Management (CIKM '23)*"
abstract: >
  In sequential recommendation, multi-modal information (e.g., text or image) can provide a more comprehensive view of an item’s profile. The optimal stage (early or late) to fuse modality features into item representations is still debated. We propose a graph-based approach (named MMSR) to fuse modality features in an adaptive order, enabling each modality to prioritize either its inherent sequential nature or its interplay with other modalities. MMSR represents each user’s history as a graph, where the modality features of each item in a user’s history sequence are denoted by cross-linked nodes. The edges between homogeneous nodes represent intra-modality sequential relationships, and the ones between heterogeneous nodes represent inter-modality interdependence relationships. During graph propagation, MMSR incorporates dual attention, differentiating homogeneous and heterogeneous neighbors. To adaptively assign nodes with distinct fusion orders, MMSR allows each node’s representation to be asynchronously updated through an update gate. In scenarios where modalities exhibit stronger sequential relationships, the update gate prioritizes updates among homogeneous nodes. Conversely, when the interdependent relationships between modalities are more pronounced, the update gate prioritizes updates among heterogeneous nodes. Consequently, MMSR establishes a fusion order that spans a spectrum from early to late modality fusion. In experiments across six datasets, MMSR consistently outperforms state-of-the-art models, and our graph propagation methods surpass other graph neural networks. Additionally, MMSR naturally manages missing modalities. The code is available at: https://github.com/HoldenHu/MMSR.
summary: 'A graph-based multimodal recommender that adaptively fuses modality signals across a user''s interaction sequence.'
links:
  - name: "URL"
    url: "https://dl.acm.org/doi/pdf/10.1145/3583780.3614775"
image:
  caption: 'MMSR framework overview.'
  preview_only: false
---
