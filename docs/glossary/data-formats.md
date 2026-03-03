# data-formats.md

# Data Formats Glossary

A reference for some file formats found in data analytics projects.

## CSV (Comma-Separated Values)

A plain-text file format where each row is a record and columns are separated by commas.
First row is typically a header row with column names.
Common format for sharing and storing tabular data.
Extension: `.csv`

## TSV (Tab-Separated Values)

Like CSV but columns are separated by tabs instead of commas.
Extension: `.tsv`

## JSON (JavaScript Object Notation)

A plain-text format for structured data using key-value pairs and nested objects.
Common for API responses and configuration files.
Extension: `.json`
Example:

```json
{ "sensor_id": "A1", "temperature": 98.6, "status": "normal" }
```

## TOML (Tom's Obvious Minimal Language)

A plain-text configuration file format designed to be easy to read and write.
Used for `pyproject.toml` in Python projects.
Extension: `.toml`

## Markdown (MD)

A plain-text format for writing structured documents using simple syntax.
Headings: `# H1`, `## H2`
Lists: `- item`
Code blocks: ` ``` `
Links: `[text](url)`
Extension: `.md`
Rendered automatically on GitHub and in many editors.

## Log File

A plain-text file recording timestamped messages written during program execution.
Used for debugging, auditing, and verifying that a program ran correctly.
Extension: `.log`

## Parquet

A binary columnar file format optimized for large datasets and analytical queries.
More efficient than CSV for large data. Common in data engineering pipelines.
Extension: `.parquet`

## YAML (YAML Ain't Markup Language)

A plain-text format for configuration files, similar to TOML but more flexible.
Common in CI/CD pipelines (GitHub Actions uses `.yml` files).
Extension: `.yml` or `.yaml`

## Tabular Data

Data organized into rows and columns, like a spreadsheet or database table.
CSV is the most common plain-text format for tabular data.

### Header Row

The first row of a CSV file containing column names.

### Record

A single row in a tabular dataset representing one observation or event.

### Field

A single column in a tabular dataset representing one attribute of each record.

## Delimiter

The character used to separate fields in a text file.
CSV uses comma; TSV uses tab. Other delimiters (pipe `|`, semicolon `;`) also exist.

## Encoding (UTF-8)

The system used to represent characters as bytes in a text file.
UTF-8 is the standard encoding for many files.
Encoding mismatches cause garbled characters when reading files.

## Binary File

A file stored in a non-human-readable format (example: Parquet, Excel `.xlsx`).
Requires specific tools to read and write. Cannot be opened meaningfully in a text editor.

## Plain Text File

A file stored as human-readable characters (example: CSV, JSON, Markdown, TOML).
Can be opened and read in any text editor.
