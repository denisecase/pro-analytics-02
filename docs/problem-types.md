# Problem Types in Analytics, Web Mining, NLP, and Machine Learning

Understanding data problems starts with identifying **what you are trying to predict, find, or explain.**
All analytics and machine learning tasks fall into a few broad families of questions.

---

## 1. Descriptive Problems - *What happened?*

**Goal:** Summarize or describe data that already exists.
**Common Tools:** Pandas, Statsmodels, Matplotlib, Seaborn.

| Example Question | Plain-English Description |
|------------------|---------------------------|
| How many sales did we make each month? | Counting totals over time to find trends. |
| Which products are most popular by region? | Summarizing and comparing results across groups. |
| What words occur most often in reviews? | Finding frequent patterns or terms in text. |

Descriptive analysis builds **understanding and trust** in data.
It forms the foundation of reports, dashboards, and exploratory analysis.

---

## 2. Diagnostic Problems - *Why did it happen?*

**Goal:** Identify relationships or possible causes behind outcomes.
**Common Tools:** Correlation analysis, regression models, visualization.

| Example Question | Plain-English Description |
|------------------|---------------------------|
| Why did sales drop last quarter? | Comparing data to find what changed - pricing, weather, ads, etc. |
| What predicts student success? | Examining which factors relate most strongly to outcomes. |

Diagnostic work connects **inputs (factors)** to **outputs (results)** and helps explain variation.

---

## 3. Predictive Problems - *What is likely to happen next?*

**Goal:** Use past data to estimate future or unknown outcomes.
**Common Tools:** Scikit-learn, XGBoost, LightGBM, Time Series Forecasting.

| Example Question | Plain-English Description |
|------------------|---------------------------|
| Will this loan applicant repay on time? | Predicting outcomes based on historical patterns. |
| How many people will click on this ad? | Estimating future behavior from past interactions. |
| What will next month's sales be? | Forecasting future values from historical data. |

Predictive modeling is **the core of machine learning** - using examples to generalize to new cases.

---

## 4. Prescriptive Problems - *What should we do?*

**Goal:** Recommend or optimize decisions based on data.
**Common Tools:** Optimization, simulation, reinforcement learning.

| Example Question | Plain-English Description |
|------------------|---------------------------|
| Which ad should we show this user? | Selecting the best option to achieve a goal. |
| What price should we set for best profit? | Balancing trade-offs between demand and revenue. |

Prescriptive analysis combines predictions with **decision-making** to suggest actions.

---

## Specialized Domains

Different types of data lead to different specialties within data science.

---

### A. Web Mining

**Data Type:** Web pages, links, clicks, and online text.
**Goal:** Extract, clean, and analyze web-based information.

| Problem Type | Example |
|---------------|----------|
| Information extraction | Pull article titles or authors from news sites. |
| Web scraping | Convert messy web pages into structured datasets. |
| Trend detection | Track how topics rise or fall over time. |
| Network analysis | Map relationships among sites, users, or links. |

Web mining focuses on **discovering structure and behavior** in online data.

---

### B. Natural Language Processing (NLP)

**Data Type:** Text, speech, or documents.
**Goal:** Understand, organize, and generate language data.

| Problem Type | Example |
|---------------|----------|
| Text classification | Label emails as spam or not spam. |
| Sentiment analysis | Detect whether a review is positive or negative. |
| Summarization | Create a short summary of a long article. |
| Entity recognition | Identify names of people, places, or organizations. |
| Topic modeling | Discover major themes in large text collections. |

Traditional NLP (e.g., NLTK, spaCy) teaches language structure.
Modern NLP and LLMs extend these tasks with **semantic understanding and text generation**.

---

### C. Machine Learning (ML)

**Data Type:** Any structured dataset with examples.
**Goal:** Learn patterns automatically to make predictions or group data.

| Problem Type | Example |
|---------------|----------|
| Classification | Decide if an email is spam or not spam. |
| Regression | Predict a continuous value (e.g., sales, temperature). |
| Clustering | Group similar items without predefined labels. |
| Recommendation | Suggest products, videos, or articles to users. |
| Anomaly detection | Identify unusual events (fraud, defects, outliers). |

Machine learning is **pattern recognition at scale** - it finds relationships that may not be obvious to humans.

---

### D. Deep Learning and Generative Models (LLMs)

**Data Type:** Images, audio, and large text sequences.
**Goal:** Recognize, describe, or generate complex content directly from raw data.

| Problem Type | Example |
|---------------|----------|
| Image recognition | Identify objects or faces in photos. |
| Speech recognition | Convert spoken words into text. |
| Text generation | Produce natural-sounding paragraphs or answers. |
| Translation | Convert text between languages. |

Deep learning powers **modern AI systems** that can perceive and generate content - from ChatGPT to computer vision models.

---

## Table

| Goal | Type of Question | Typical Tools | Example |
|------|------------------|----------------|----------|
| **Describe** | What happened? | Pandas, Matplotlib | What are the monthly sales trends? |
| **Diagnose** | Why did it happen? | Statsmodels, Seaborn | What factors influenced the drop in sales? |
| **Predict** | What will happen next? | Scikit-learn, XGBoost | Which customers are likely to repurchase? |
| **Prescribe** | What should we do? | Optimization, Simulation | What pricing strategy maximizes profit? |

---

## Mapping to Python Packages

This section links common problem types to relevant Python tools introduced elsewhere in the documentation.

| Problem Type | Typical Python Packages | Notes |
|---------------|------------------------|-------|
| **Descriptive** | `pandas`, `numpy`, `matplotlib`, `seaborn` | Summarizing, aggregating, and visualizing data. |
| **Diagnostic** | `statsmodels`, `scikit-learn`, `seaborn` | Correlations, regressions, and explanatory plots. |
| **Predictive** | `scikit-learn`, `xgboost`, `lightgbm`, `catboost` | Classification, regression, and forecasting. |
| **Prescriptive** | `scipy.optimize`, `pulp`, `simpy` | Optimization and decision simulation. |
| **Web Mining** | `requests`, `beautifulsoup4`, `lxml`, `regex` | Web scraping, extraction, and cleanup. |
| **NLP** | `textblob`, `nltk`, `spacy`, `sentence-transformers`, `transformers` | Text processing, sentiment, and embeddings. |
| **Deep Learning / LLMs** | `torch`, `tensorflow`, `transformers`, `langchain`, `openai` | Image, speech, and text generation models. |

---

**Key Idea:**
All analytics and ML projects start with a clear question.
Once you know *what kind of question you're asking*, the right tools, models, and techniques naturally follow.
