## Core Essential Tools for Professional Python Projects

These are the **most commonly used external libraries** across analytics, data, and AI projects.
They are not part of the standard library — install them as needed using `uv add <package>` or `pip install <package>`.

| Category | Package | Purpose |
|-----------|----------|----------|
| **Core Management** | [`pip`](https://pypi.org/project/pip/), [`setuptools`](https://pypi.org/project/setuptools/), [`wheel`](https://pypi.org/project/wheel/) | Package installation, building, and distribution. |
| **Documentation** | [`mkdocs`](https://pypi.org/project/mkdocs/) | Simple, fast static site generator for project documentation. |
| **Logging** | [`loguru`](https://pypi.org/project/loguru/) | Modern, colorized logging with rotation and context. |
| **HTTP & Environment** | [`httpx`](https://pypi.org/project/httpx/), [`python-dotenv`](https://pypi.org/project/python-dotenv/) | Send modern HTTP/HTTPS requests (sync or async) and manage `.env` configuration. |
| **Data Analysis** | [`numpy`](https://pypi.org/project/numpy/), [`pandas`](https://pypi.org/project/pandas/), [`polars`](https://pypi.org/project/polars/) | Numeric computing, dataframes, and high-speed analysis. |
| **Visualization** | [`matplotlib`](https://pypi.org/project/matplotlib/), [`seaborn`](https://pypi.org/project/seaborn/) | Static and statistical visualizations. |
| **Jupyter Ecosystem** | [`jupyterlab`](https://pypi.org/project/jupyterlab/), [`ipython`](https://pypi.org/project/ipython/), [`ipykernel`](https://pypi.org/project/ipykernel/) | Notebook authoring, interactive shell, and VS Code kernel support. |
| **Databases & Orchestration** | [`duckdb`](https://pypi.org/project/duckdb/)| Lightweight database. |
| **Machine Learning** | [`scikit-learn`](https://pypi.org/project/scikit-learn/), [`statsmodels`](https://pypi.org/project/statsmodels/) | Classical ML, regression, and statistical modeling. |
| **Natural Language Processing** | [`spacy`](https://pypi.org/project/spacy/), [`nltk`](https://pypi.org/project/nltk/) | Text preprocessing, tokenization, and linguistic analysis. |

Notes:

1. `httpx` replaces `requests` as the modern, async-capable HTTP client for Python. Existing `requests` examples work with minor or no changes.
---

For the full curated reference (including Excel, orchestration, streaming, and alerts), see
**[Essential External Tools](py-packages.md)** in the documentation site.
