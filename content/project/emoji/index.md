---
title: Emoji Composition

summary: We provide language resource for emoji composition. 
abstract: "Can emojis be composed to convey intricate meanings like English phrases? As a pioneering study, we present
the Emoji-Lexical Composition (ELCo) dataset, a new resource that offers parallel annotations of emoji sequences
corresponding to English phrases. Our dataset contains 1,655 instances, spanning 209 diverse concepts from tangible
ones like “right man” ( ) to abstract ones such as “full attention” ( , illustrating a metaphoric composition of
a focusing face and writing hand). ELCo enables the analysis of the patterns shared between emoji and lexical
composition. Through a corpus study, we discovered that simple strategies like direct representation and reduplication
are sufficient for conveying certain concepts, but a richer, metaphorical strategy is essential for expressing more
abstract ideas. We further introduce an evaluative task, Emoji-based Textual Entailment (EmoTE), to assess the
proficiency of NLP models in comprehending emoji compositions. Our findings reveals the challenge of understanding
emoji composition in a zero-shot setting for current models, including ChatGPT. Our analysis indicates that the intricacy
of metaphorical compositions contributes to this challenge. Encouragingly, models show marked improvement
when fine-tuned on the ELCo dataset, with larger models excelling in deciphering nuanced metaphorical compositions."

tags: ["CL", "Emoji", "NLP", "LLM", "Computational Linguistics"]
year: 2024

date: '2024-05-20' # LREC-COLING 24's conference date. 

all_day: true

# Is this a featured project? (true/false)
featured: true
image:
  caption: 'Data samples from the ELCo dataset.'
  focal_point: Right
url_pdf: 'https://aclanthology.org/2024.lrec-main.1381/'
url_slides: 'https://yisong.me/publications/ELCo@LREC-COLING24-Oral.pdf'
url_code: 'https://github.com/WING-NUS/ELCo'

# Markdown Slides (optional).
#   Associate this talk with Markdown slides.
#   Simply enter your slide deck's filename without extension.
#   E.g. `slides = "example-slides"` references `content/slides/example-slides.md`.
#   Otherwise, set `slides = ""`.
# slides:

authors: ["yisong", "ziyun", "valentin", "min"]

---
The project began when Yisong, intrigued by [the Emoji Mashup Bot](https://x.com/EmojiMashupBot), explored the question: Can emojis be composed to convey meanings like English phrases? With the support of his advisor, Prof. Min, he recruited an undergraduate student, Zi Yun Yang, to collaborate on the project. Ms. Yang built an annotation platform to collect emoji compositions and their corresponding English phrases from her peers. After her graduation, Yisong and the team added another layer of annotation on composition types and formalized an emoji-based textual entailment task (EmoTE).  

The first iteration of this work was published at [LREC-COLING 2024](https://lrec-coling-2024.org). Prof. Min was not listed as an author due to his role as a conference chair, but this project cannot be finished without his guidance. The project continues to gain interest, particularly among undergraduates, with many students from our local NLP course using the emoji dataset for their final projects. 
