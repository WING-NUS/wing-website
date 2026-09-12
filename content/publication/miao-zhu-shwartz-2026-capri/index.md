---
title: 'LLMs Infer Cultural Context but Fail to Apply It When Responding'

authors:
  - yisong
  - Jian Zhu
  - Vered Shwartz

date: '2026-10-25'
doi: ''

# Schedule page publish date (NOT publication's date).
publishDate: '2026-09-10T00:00:00Z'
publication_types: ['paper-conference']

# Publication name and optional abbreviated publication name.
publication: In *Proceedings of the 2026 Conference on Empirical Methods in Natural Language Processing (EMNLP 2026)*
# publication_short: In *EMNLP 2026*

abstract: "Recent work has shown that LLMs overrepresent dominant cultures, particularly Western ones, while marginalizing others. We investigate whether this affects models' ability to generate culturally adapted responses by evaluating their use of local measurement units based on the user's perceived cultural background. We introduce Cultural and Pragmatic Response Inference (CAPRI), a dataset of conversations with varying levels of cultural cues. Experiments with state-of-the-art LLMs show that models can infer cultural background and recall relevant conventions, but often fail to utilize the information to adapt their answers to the relevant cultural conventions, unless explicitly prompted to perform the tasks sequentially. We further evaluate adaptation to the interpretation of time and quantity expressions, two subjective language grounding dimensions that are affected by culture. We find that models increasingly adapt their answers as cultural cues accumulate, but their priors are not culture-neutral, sometimes aligning with the model's country of origin. Overall, CAPRI provides a resource for future research aimed at narrowing the gap between cultural knowledge and culturally adaptive language generation. *(Work done during Yisong’s Vector Institute research internship with UBC NLP.)*"

# Summary. An optional shortened abstract.
summary: We introduce Cultural and Pragmatic Response Inference (CAPRI), a dataset showing that LLMs infer users’ cultural backgrounds but often fail to adapt their responses accordingly.

tags: ["Pragmatic Speaker Model", "LLMs' Cultural Competence", "Language Grounding", "Vision and Language", "Discourse and Pragmatics"]

# Display this page in the Featured widget?
featured: true

# Custom links (uncomment lines below)
# links:
# - name: Custom Link
#   url: http://example.org

url_pdf: 'https://arxiv.org/abs/2606.17688'
url_code: 'https://github.com/YisongMiao/CAPRI'

# Featured image
# To use, add an image named `featured.jpg/png` to your page's folder.
image:
  caption: 'Task Overview: CAPRI tests whether models infer a user’s cultural background from conversational cues (Task 1) and apply it in visual question answering (Task 2), such as choosing culturally appropriate temperature units.'
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
url_slides: "https://yisong.me/publications/emnlp26-CAPRI-Slides.pdf"
---
