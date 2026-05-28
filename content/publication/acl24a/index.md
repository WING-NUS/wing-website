---
title: 'Beyond Memorization: The Challenge of Random Memory Access in Language Models'
# Tongyao Zhu, Qian Liu, Liang Pang, Zhengbao Jiang, Min-Yen Kan and Min Lin (2024) Beyond Memorization: The Challenge of Random Memory Access in Language Models. In Proceedings of the Annual Meeting fof the Association of Computational Linguistics (ACL '24).

authors:
  - tongyao
  - qian
  - Liang Pang
  - Zhengbao Jiang
  - min
  - Min Lin

date: '2024-08-11T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the Annual Meeting fof the Association of Computational Linguistics*
publication_short: In *ACL 2024*

abstract: Recent developments in Language Models (LMs) have shown their effectiveness in NLP tasks, particularly in knowledge-intensive tasks. However, the mechanisms underlying knowledge storage and memory access within their parameters remain elusive. In this paper, we investigate whether a generative LM (e.g., GPT- 2) is able to access its memory sequentially or randomly. Through carefully-designed synthetic tasks, covering the scenarios of full recitation, selective recitation and grounded question answering, we reveal that LMs manage to sequentially access their memory while encountering challenges in randomly accessing memorized content. We find that techniques including recitation and permutation improve the random memory access capability of LMs. Furthermore, by applying this intervention to realistic scenarios of open-domain question answering, we validate that enhancing random access by recitation leads to notable improvements in question answering. The code to reproduce our experiments can be found at https://github. com/sail-sg/lm-random-memory-access.

# Summary. An optional shortened abstract.
summary: we investigate whether a generative LM (e.g., GPT- 2) is able to access its memory sequentially or randomly. Through carefully-designed synthetic tasks, we reveal that LMs manage to sequentially access their memory while encountering challenges in randomly accessing memorized content.

tags: ["Natural Language Processing", "Large Language Models"]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://www.comp.nus.edu.sg/~kanmy/papers/2403.07805v2.pdf'
url_code: 'https://github.com/sail-sg/lm-random-memory-access'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'A illustration of our investigation of memory access pattern in language models. We find that the model accesses its parametric memory largely in a sequential manner, and faces difficulty in randomly accessing the content in the middle of memorized strings.'
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
  - example

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
# slides: example
---
