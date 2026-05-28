---
title: SCITAB – A Benchmark for Scientific Table-Based Fact-Checking

summary: A challenging dataset for compositional reasoning and claim verification on scientific tables.
abstract: "SCITAB is a dataset designed to address limitations in existing scientific fact-checking benchmarks by focusing on real-world claims from scientific papers that require compositional reasoning over tabular data for verification. The dataset includes 1,225 expert-verified scientific claims annotated with labels, making it a challenging test bed for both table-based pretraining models and large language models. Our experiments show that current models, including table-based LLMs and prompting techniques, struggle with SCITAB, with GPT-4 being the only model to significantly outperform random guessing. This dataset highlights challenges in table grounding, ambiguity resolution, and multi-step reasoning."

tags: ["Scientific Fact-Checking", "Tables", "Compositional Reasoning", "LLMs"]
year: 2023

date: '2023-12-06'  # EMNLP 2023 conference date.

all_day: true

# Is this a featured project? (true/false)
featured: true
image:
  caption: 'Example from SCITAB showing a claim and its reasoning process.'
  focal_point: Right
url_pdf: 'https://aclanthology.org/2023.emnlp-main.483/'
url_slides: 'https://drive.google.com/file/d/1B2c2UVfCPDi_bI_RhAkJp88S1mNhHnOB/view'
url_code: 'https://github.com/XinyuanLu00/SciTab'

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["xinyuan", "liangming", "qian", "Preslav Nakov","min"]

---
SCITAB was developed to fill the gap in scientific fact-checking benchmarks by incorporating claims derived from actual scientific papers rather than crowd-sourced ones. These claims require multi-step reasoning to verify against evidence in tables. The dataset was created using a human–model collaboration approach, where real-world claims were filtered, counterclaims were generated using InstructGPT, and all claims were manually verified by expert annotators.

The dataset has been extensively evaluated with state-of-the-art models, including TAPAS, TAPEX, Vicuna, and GPT-4, revealing that existing table-based models struggle with SCITAB. Only GPT-4 shows notable improvements, highlighting the dataset’s challenge and potential for advancing research in table-based reasoning.

SCITAB was presented at **EMNLP 2023**, and the dataset is publicly available for further research. Researchers interested in compositional reasoning, table fact-checking, and model robustness are encouraged to explore SCITAB and contribute to its future developments.
