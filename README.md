# Spacy-Models-Setup-and-Testing
A Python utility for downloading, storing, and testing Spacy language models for English and Chinese NLP tasks.

# Spacy Models Setup and Testing

A Python utility for downloading, storing, and testing Spacy language models for English and Chinese NLP tasks.

## Overview

This repository contains scripts to automate the setup and testing of Spacy language models, specifically:
- English: `en_core_web_sm`
- Chinese: `zh_core_web_sm`, `zh_core_web_md`, `zh_core_web_lg`

The models are downloaded and stored in a custom directory (`./data/models/`) for easy access and management.

## Model Sizes
- zh_core_web_sm: ~12MB
- zh_core_web_md: ~23MB
- zh_core_web_lg: ~46MB
- en_core_web_sm: ~12MB

## Requirements

```bash
pip install spacy
```

## Directory Structure

.
├── README.md
├── setup_spacy_models.py
└── data/
    └── models/
        ├── en_core_web_sm/
        ├── zh_core_web_sm/
        ├── zh_core_web_md/
        └── zh_core_web_lg/


## Usage
import spacy

# Load English model
nlp_en = spacy.load('./data/models/en_core_web_sm')

# Load Chinese model (large)
nlp_zh = spacy.load('./data/models/zh_core_web_lg')

# Process text
doc_en = nlp_en("This is a test sentence.")
doc_zh = nlp_zh("这是一个测试句子。")



•Automated download and installation of Spacy models
•Custom directory storage
•Model testing with sample texts
•Token and POS tag demonstration
•Named Entity Recognition testing
•Error handling and validation


