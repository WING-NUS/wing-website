---
title: "ToXCL: A Unified Framework for Toxic Speech Detection and Explanation"
subtitle: ""
authors:
- nhat
- Do Xuan Long
- Duc Anh Do
- Duc Anh Vu
- Anh Tuan Luu
author_notes: [Equal Contribution, Equal Contribution]
doi: ""

# Schedule page publish date (NOT publication's date).
publishDate: '2024-03-26T00:00:00Z'
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *2024 Annual Conference of the North American Chapter of the Association for Computational Linguistics*
publication_short: In *NAACL 2024*

abstract: "The proliferation of online toxic speech is a pertinent problem posing threats to demographic groups. While explicit toxic speech contains offensive lexical signals, implicit one consists of coded or indirect language. Therefore, it is crucial for models not only to detect implicit toxic speech but also to explain its toxicity. This draws a unique need for unified frameworks that can effectively detect and explain implicit toxic speech. Prior works mainly formulated the task of toxic speech detection and explanation as a text generation problem. Nonetheless, models trained using this strategy can be prone to suffer from the consequent error propagation problem. Moreover, our experiments reveal that the detection results of such models are much lower than those that focus only on the detection task. To bridge these gaps, we introduce ToXCL, a unified framework for the detection and explanation of implicit toxic speech. Our model consists of three modules: a (i) Target Group Generator to generate the targeted demographic group(s) of a given post; an (ii) Encoder-Decoder Model in which the encoder focuses on detecting implicit toxic speech and is boosted by a (iii) Teacher Classifier via knowledge distillation, and the decoder generates the necessary explanation. ToXCL achieves new state-of-the-art effectiveness, and outperforms baselines significantly."
summary: 'A NAACL 2024 framework that jointly detects implicit toxic speech, identifies target groups, and generates explanations through ToXCL.'

# Display this page in the Featured widget?
featured: true

url_pdf: 'https://arxiv.org/abs/2403.16685'
url_code: 'https://github.com/NhatHoang2002/ToXCL'
url_dataset: ''
url_poster: ''
url_project: ''
url_slides: ''
url_source: ''
url_video: ''

image:
  caption: "A sample input post and its ground truth explanation from the Implicit Hate Corpus test set were fed into two models. The baseline RoBERTa model failed to detect the implicit toxic speech, while our proposed ToXCL model successfully detected it and generated a toxic explanation closely matching the ground truth."
  preview_only: false
---
