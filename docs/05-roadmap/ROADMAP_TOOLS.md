# ROADMAP: Tools to Know

For Python Data Analytics, Business Intelligence, Machine Learning, and more.

All tools listed are free unless noted. Check the boxes as you add skills.

---

## Core Setup

- [ ] Visual Studio Code (VS Code) - Modern IDE with Python, Markdown, and Git support. Use to edit code, run notebooks, and manage projects.
- [ ] Python - Primary programming language for scripting, data analysis, and BI automation.
- [ ] Markdown - Simple formatting language for README files, documentation, and Jupyter notes.
- [ ] Jupyter Notebooks / JupyterLab - Interactive notebooks that combine code, output, and formatted text. Essential for data exploration and storytelling.
- [ ] VS Code Jupyter Extension - Rich notebook editing in VS Code, with support for Markdown, plots, and cell output.
- [ ] uv (Astral) - Modern Python package and environment manager. Replaces `pip`, `venv`, and `virtualenv`.

---

## Version Control and Project Management

- [ ] Git and GitHub - Version control and collaboration platform. Track changes, share code, and publish projects.
- [ ] .gitignore / pyproject.toml / virtual environments - Tools to manage dependencies and keep projects clean and reproducible.
- [ ] pre-commit – Automates linting, formatting, and static analysis before commits.
- [ ] GitHub Actions - Automate checks, deployments, and other tasks from GitHub.
- [ ] TortoiseGit - Windows only, integrates Git with Windows File Explorer.

---

## Terminals

- [ ] PowerShell - Use on Windows Machines. Also a very popular cross-platform automation tool for Mac/Linux.
- [ ] Windows Subsystem for Linux (WSL/WSL2) - Linux environment on Windows machines. Strongly recommended or required when testing advanced Apache and open-source data tools.
- [ ] bash / zsh / Git Bash - Common terminal interfaces for Mac/Linux. Git Bash provides a bash shell for Windows.
- [ ] uvx CLI – Run Python tools without installing them permanently.

---

## Data Manipulation & In-Memory Processing

- [ ] Pandas - Core library for tabular data manipulation and analysis in Python.
- [ ] Polars - High-performance DataFrame library (written in Rust). Fast and efficient, especially for large datasets.
- [ ] PyArrow – Python interface for Apache Arrow, powering Polars, DuckDB, and Parquet interoperability.

---

## Modern Analytics Data Engineering Tools

- [ ] dbt - Transform and test SQL-based analytics workflows in a modular way.
- [ ] SQLMesh - Modern data transformation and version control for SQL-based workflows. Allows modular and repeatable ETL development.
- [ ] Datafold – Data diffing and validation for analytics CI/CD workflows.

---

## In-Process SQL & Columnar Data

- [ ] DuckDB - In-process SQL engine. Run fast queries directly on CSVs and Parquet files.
- [ ] Apache Arrow – Columnar data format enabling high-speed data exchange between tools like Polars, DuckDB, and Spark.


---

## Distributed Computing & Big Data Processing

- [ ] Apache Spark - Distributed processing engine for big data and analytics. Uses micro-batching, good for iterative machine learning tasks, mature ecosystem with extensive community support.
- [ ] PySpark - Python API for working with Apache Spark.
- [ ] Apache Flink - Highly scalable stream processing engine for exactly once event processing, real-time analytics, and complex events.
- [ ] Ray – Distributed Python for machine learning, model serving, and parallel computing.

---

## Data Lakehouse & Table Formats

- [ ] Delta Lake - open source framework for data lakes
- [ ] Apache Iceberg - High-performance table format for huge analytic datasets, enabling fast data lake queries and ACID transactions.
- [ ] Apache Hudi - Real-time data lake platform for incremental data processing and streaming ingestion.
- [ ] Apache XTable - Multi-format table abstraction layer, enabling seamless conversion between Iceberg, Delta Lake, and Hudi.
- [ ] OneTable – Unifies schema and metadata across Iceberg, Delta, and Hudi.

---

## Data Pipelines & Quality

- [ ] Apache NiFi - Visual tool to build and manage automated data flows.
- [ ] Prefect - Orchestrate and schedule ETL pipelines. Great for managing dependencies and retries in production environments. See also Apache Airflow.
- [ ] Pandera - open source DataFrame validator tool
- [ ] Tableau Prep - (Paid, but free for students via Tableau for Students) Visual tool to clean, shape, and join data before loading into Tableau dashboards.
- [ ] Great Expectations, GX Cloud - Tool for validating and testing data quality in pipelines or notebooks. Used in enterprise-grade pipelines to ensure data reliability.
- [ ] Marquez – Open-source metadata and lineage tracking for pipelines.
- [ ] Great Expectations (GX) – Modernized framework for data validation and testing in pipelines.

---

## Streaming & Real-Time Processing

- [ ] WebSockets - Real-time communication in dashboards and live apps.
- [ ] Python socket.io - real-time bidirectional event-based communication between clients (e.g., web browsers) and a server.
- [ ] Apache Kafka - High-throughput distributed messaging system for real-time data.
- [ ] Apache Pulsar - Cloud-native distributed messaging and event streaming platform for high-throughput, low-latency real-time processing.
- [ ] Faust – Python stream processing library compatible with Kafka for event-driven analytics.

---

## Web Scraping & APIs

- [ ] requests - Simple HTTP library for making API calls.
- [ ] BeautifulSoup - HTML parser for web scraping and structured data extraction.
- [ ] Scrapy - Open-source scraping and extraction framework.
- [ ] FastAPI - High-performance web framework for building APIs in Python.
- [ ] Flask - Lightweight microframework for building web apps and data services.
- [ ] httpx – Modern async HTTP client for Python.
  Often used with FastAPI for high-performance API calls.
- [ ] FastAPI (Pydantic v2) – Fully compatible with Pydantic v2 for fast, type-safe API validation.

---

## Data Visualization: Core

- [ ] Matplotlib - Core plotting library for Python.
- [ ] Seaborn - Statistical data visualization built on top of Matplotlib.
- [ ] Plotly - Interactive charts and graphs, browser-based.
- [ ] Altair – Declarative visualization library built on Vega-Lite.
- [ ] Polars LazyFrame Plotting (Experimental) – Integrates with Polars for lightweight analytics visualizations.

---

## Data Visualization: Interactive Web Apps

- [ ] Streamlit - Create interactive web apps directly from Python scripts.
- [ ] Plotly Dash - Build analytical web applications with no front-end experience required.

---

## Data Visualization: Interactive and Dashboarding Tools

- [ ] PyShiny - Reactive Python dashboard framework (inspired by the popular R Shiny).
- [ ] Apache Superset - Open-source BI tool for building interactive dashboards and data exploration.
- [ ] Power BI - (Free for students and basic use) - Professional Windows-only dashboarding tool used widely in business.
- [ ] Tableau - (Paid, but free for students via Tableau for Students) - Leading BI dashboard platform used in many companies.
- [ ] Apache Superset v4 – Includes a semantic layer and embedded dashboard capabilities.

---

## Cloud Tools & Deployment

- [ ] GitHub Codespaces – Cloud-based VS Code with `uv` and Jupyter preinstalled.
- [ ] Google Colab - Free hosted Jupyter notebooks with built-in libraries and GPU support.
- [ ] ShinyLive - Host interactive Shiny applications directly in the browser without servers.
- [ ] Streamlit Cloud - Host Streamlit dashboards and apps online with a free account.
- [ ] Render- Platform for deploying FastAPI, Flask, and Python web apps easily.
- [ ] Railway - Platform for deploying web apps and microservices easily.
- [ ] AWS Lambda - Run Python functions in the cloud without managing servers. Free tier available.
- [ ] Microsoft Azure Functions) - Cloud-based serverless function execution from Microsoft. Free tier available.
- [ ] Modal – Run and scale Python functions in the cloud without infrastructure setup.
- [ ] Hugging Face Spaces – Free hosting for Streamlit, Gradio, and Shiny apps.

---

## AI & Semantic Tools (Advanced or Optional)

- [ ] Chroma (ChromaDB) - Open-source vector database for storing and searching embeddings (semantic search). Used in AI pipelines for tasks like document search, RAG apps, and chatbots.
- [ ] LangChain – Framework for building LLM-powered applications and workflows.
- [ ] LlamaIndex – Framework for connecting structured/unstructured data to LLMs (RAG).
- [ ] Ollama – Run and serve local LLMs like Llama 3 and Mistral on macOS, Windows, or Linux.
- [ ] OpenAI API / Anthropic Claude API – Cloud APIs for state-of-the-art LLMs used in production applications.

