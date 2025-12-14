---
title: 'Discursive Socratic Questioning: Evaluating the Faithfulness of Language Models’ Understanding of Discourse Relations'
# Yisong Miao , Hongfu Liu, Wenqiang Lei, Nancy F. Chen and Min-Yen Kan (2024) Beyond Memorization: The Challenge of Random Memory Access in Language Models. In Proceedings of the Annual Meeting fof the Association of Computational Linguistics (ACL '24).

authors:
  - yisong
  - Hongfu Liu
  - wenqianglei
  - Nancy F. Chen
  - min

date: '2024-08-11T00:00:00Z'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2017-01-01T00:00:00Z'
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the Annual Meeting fof the Association of Computational Linguistics*
publication_short: In *ACL 2024*

abstract: "While large language models have significantly enhanced the effectiveness of discourse relation classifications, it remains unclear whether their comprehension is faithful and reliable. We provide DiSQ, a new method for evaluating the faithfulness of understanding discourse based on question answering. We first employ in-context learning to annotate the reasoning for discourse comprehension, based on the connections among key events within the discourse. Following this, DiSQ interrogates the model with a sequence of questions to assess its grasp of core event relations, its resilience to counterfactual queries, as well as its consistency to its previous responses. We then evaluate language models with different architectural designs using DiSQ, finding: (1) DiSQ presents a significant challenge for all models, with the top-performing GPT model attaining only 41% of the ideal performance in PDTB; (2) DiSQ is robust to domain shifts and paraphrase variations; (3) Open-source models generally lag behind their closed-source GPT counterparts, with notable exceptions being those enhanced with chat and code/math features; (4) Our analysis validates the effectiveness of explicitly signalled discourse connectives, the role of contextual information, and the benefits of using historical QA data."

# Summary. An optional shortened abstract.
summary: We propose Discursive Socratic Questioning (DiSQ), a new evaluation measure for discourse semantics. Inspired by the Socratic method, DiSQ involves asking models about key event relations, testing their robustness to counterfactuals, and ensuring consistency with equivalent questions. Experiments show that GPT-4 achieves only 41% of the DiSQ scores. We recommend using context and discourse connectives as essential linguistic features to enhance discourse comprehension.

tags: ["Natural Language Processing", "Discourse", "Large Language Models"]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://yisong.me/publications/acl24-DiSQ-CR.pdf'
url_code: 'https://github.com/YisongMiao/DiSQ-Score'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'DiSQ combines three discourse-relevant scores: (1) Targeted Score, gauging responses to key events; (2) Counterfactual Score, assessing robustness against irrelevant queries; (3) Consistency Score, measuring logical coherence to equivalent questions.'
  preview_only: false

# Associated Projects (optional).
#   Associate this publication with one or more of your projects.
#   Simply enter your project's folder or file name without extension.
#   E.g. `internal-project` references `content/project/internal-project/index.md`.
#   Otherwise, set `projects: []`.
projects:
  - discourse

# Slides (optional).
#   Associate this publication with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides: "example"` references `content/slides/example/index.md`.
#   Otherwise, set `slides: ""`.
slides: "https://yisong.me/publications/acl24-DiSQ-Slides.pdf"
---
