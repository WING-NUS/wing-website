---
title: "DATATALES: A Benchmark for Real-World Intelligent Data Narration"

summary: A challenging dataset for compositional reasoning and claim verification on scientific tables.
abstract: "We introduce DATATALES, a novel benchmark designed to assess the proficiency of language models in data narration, a task crucial for transforming complex tabular data into accessible narratives. Existing benchmarks often fall short in capturing the requisite analytical complexity for practical applications. DATATALES addresses this gap by offering 4.9k financial reports paired with corresponding market data, showcasing the demand for models to create clear narratives and analyze large datasets while understanding specialized terminology in the field. Our findings highlight the significant challenge that language models face in achieving the necessary precision and analytical depth for proficient data narration, suggesting promising avenues for future model development and evaluation methodologies."

tags: ["Data-to-text", "Tables", "Complex Reasoning", "LLMs"]
year: 2024

date: '2024-11-12'  # EMNLP 2024 conference date.

all_day: true

# Is this a featured project? (true/false)
featured: true
image:
  caption: 'DATATALES example featuring a report and tabular data on 28 equity market entities, with 7 columns.'
  focal_point: Right
url_pdf: 'https://aclanthology.org/2024.emnlp-main.601/'
# url_slides: ''
url_code: 'https://github.com/yajingyang/DataTales/'

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["yajing", "qian", "yunshan", "min"]

---
DATATALES was developed to address the limitations of existing benchmarks in evaluating language models' proficiency in data narration. Unlike traditional data-to-text tasks that focus on basic information transformation, DATATALES captures the complex analytical reasoning required to transform tabular financial data into coherent, insightful narratives.

The benchmark consists of 4.9k financial market reports paired with comprehensive market data, sourced from diverse professional outlets. These reports demonstrate real-world data narration challenges, requiring models to not just describe data but analyze trends, explore causality, and make predictions using specialized financial terminology. Extensive evaluation of state-of-the-art language models on DATATALES reveals significant challenges in achieving the necessary precision and analytical depth required for effective data narration.

DATATALES was presented at **EMNLP 2024**, and the dataset is publicly available for further research. Researchers interested in data narration, complex reasoning over tabular data, and financial text generation are encouraged to explore DATATALES and contribute to advancing model capabilities in transforming complex data into accessible narratives.