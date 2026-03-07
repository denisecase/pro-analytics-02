# Suggested Datasets: Web Mining and NLP

Good datasets for Web Mining and Natural Language Processing
typically contain **collections of text** that can be analyzed
for patterns, topics, sentiment, or structure.

These datasets help analysts explore how language is used
across websites, documents, conversations, or social platforms.

These are only suggestions.

## Choosing a Dataset

Choose datasets where **each row contains meaningful text**
such as a sentence, paragraph, comment, or document and contain
**plain text that can be easily extracted and processed**.

Good datasets usually have:

- text that can be copied or downloaded as **plain text or HTML**
- many rows or documents to analyze
- meaningful language (articles, conversations, books, comments)

Try to avoid datasets where:

- the text is embedded in **PDF files**
- the data consists mainly of **images or scanned documents**
- the text is extremely short (for example: single keywords)

Look for **real language data** that can be tokenized, counted, and explored using Python.

## Index

These datasets work well for exploring web mining and NLP techniques.
More information appears in the sections below.

| Dataset                  | Text Source                  | Good For Modules |
| ------------------------ | ---------------------------- | ---------------- |
| Project Gutenberg Books  | Books and literature         | 2, 3             |
| News Headlines           | News media text              | 2, 3             |
| Movie Reviews            | Opinion and sentiment text   | 2, 3             |
| Reddit Comments          | Online discussion forums     | 2, 3, 4          |
| Wikipedia Articles       | Structured knowledge text    | 2, 3             |
| GitHub Issue Discussions | Technical collaboration text | 3, 4             |
| MIT Shakespeare Page     | Structured literary text     | 2, 3, 5          |
| Web Page Text            | HTML page content            | 3, 4, 5          |

## 1. Project Gutenberg Books

Source:
https://www.gutenberg.org/

Project Gutenberg provides thousands of public domain books
that can be downloaded as plain text.

Example uses:

- word frequency analysis
- tokenization
- text cleaning
- topic exploration

Questions to explore:

- What are the most common words in a text?
- How does vocabulary vary across authors?
- What words characterize different genres?

Works well for modules:

- Module 2: Text Preprocessing
- Module 3: Text Exploration

## 2. News Headlines

Example dataset:

https://www.kaggle.com/datasets/rmisra/news-category-dataset

This dataset contains thousands of news headlines across many topics.

Example fields:

- headline
- category
- date

Possible analyses:

- word frequency by topic
- keyword extraction
- topic exploration

Questions to explore:

- Which words appear most frequently in news headlines?
- How does language differ across news categories?
- What topics dominate the dataset?

Works well for modules:

- Module 2: Text Preprocessing
- Module 3: Text Exploration

## 3. Movie Reviews

Example dataset:

https://ai.stanford.edu/~amaas/data/sentiment/

Movie review datasets contain opinion text written by viewers.

Example fields:

- review_text
- sentiment label (positive/negative)

Possible analyses:

- sentiment words
- word frequency in positive vs negative reviews
- common phrases

Questions to explore:

- What words are associated with positive reviews?
- What words appear frequently in negative reviews?
- Are there common phrases across many reviews?

Works well for modules:

- Module 2: Text Preprocessing
- Module 3: Text Exploration

## 4. Reddit Comments

Example dataset:

https://www.kaggle.com/datasets/reddit/reddit-comments-may-2015

Reddit comment datasets contain conversations from online forums.

Example fields:

- comment_text
- subreddit
- timestamp

Possible analyses:

- frequent discussion topics
- vocabulary differences between communities
- conversation language patterns

Questions to explore:

- What topics appear frequently in a subreddit?
- How does language vary between communities?
- What keywords characterize discussions?

Works well for modules:

- Module 2: Text Preprocessing
- Module 3: Text Exploration
- Module 4: API or Structured Data Workflows

## 5. Wikipedia Articles

Source:
https://dumps.wikimedia.org/

Wikipedia articles provide structured informational text.

Example fields:

- article_title
- article_text

Possible analyses:

- keyword extraction
- topic exploration
- vocabulary analysis

Questions to explore:

- What keywords define an article topic?
- How does language differ between article types?
- What vocabulary appears frequently across many articles?

Works well for modules:

- Module 2: Text Preprocessing
- Module 3: Text Exploration

## 6. GitHub Issue Discussions

Example dataset:

https://www.githubarchive.org/

GitHub issue comments contain technical discussions between developers.

Example fields:

- issue_title
- comment_text
- repository
- timestamp

Possible analyses:

- technical vocabulary frequency
- common problem descriptions
- developer discussion topics

Questions to explore:

- What problems appear most frequently in issues?
- What words characterize technical discussions?
- How does language vary across repositories?

Works well for modules:

- Module 3: Text Exploration
- Module 4: API Data Workflows

## 7. MIT Shakespeare Page (Complete Works)

Source:
https://shakespeare.mit.edu/

The MIT Shakespeare site provides the complete works of Shakespeare
organized by play, act, and scene. The text is available in simple HTML pages,
which makes it easy to retrieve and analyze.

Example text sources:

- play titles
- character dialogue
- scene descriptions

Possible analyses:

- word frequency across plays
- vocabulary differences between characters
- keyword extraction for themes
- comparison of language across tragedies and comedies

Questions to explore:

- Which words appear most frequently across Shakespeare's works?
- Do different characters use different vocabulary?
- Are certain words associated with particular plays or themes?

Works well for modules:

- Module 2: Text Preprocessing
- Module 3: Text Exploration
- Module 5: Web Document Structure

## 8. Web Page Text

Example source:

Any public website page retrieved with a web request.

Example fields extracted from HTML:

- page_title
- headings
- paragraphs

Possible analyses:

- keyword extraction
- word frequency
- content structure

Questions to explore:

- What topics appear on a web page?
- Which keywords characterize a website?
- How does page structure affect text analysis?

Works well for modules:

- Module 3: Text Exploration
- Module 4: API Data Workflows
- Module 5: Web Document Structure
