# Question Answering System

[![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![Transformers](https://img.shields.io/badge/🤗%20Transformers-FF6F00?style=for-the-badge)](https://huggingface.co/docs/transformers)
[![FAISS](https://img.shields.io/badge/FAISS-Vector%20Search-5299CC?style=for-the-badge)](https://faiss.ai)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

Система вопросно-ответного анализа, объединяющая **Extractive QA** (fine-tuned BERT) с **Retrieval-Augmented Generation (RAG)** через векторный поиск FAISS. Модульный pipeline с веб-интерфейсом.

## Архитектура

```mermaid
flowchart TD
    A[User Question] --> B{Retrieval Mode?}
    
    B -->|Direct QA| C[Fine-tuned BERT]
    C --> D[Extractive Answer]
    
    B -->|RAG Mode| E[Query Encoding]
    E --> F[FAISS Vector Search]
    F --> G[Top-K Document Chunks]
    G --> H[Context + Question]
    H --> I[QA Model]
    I --> J[Contextual Answer]
    
    D --> K[Answer Formatter]
    J --> K
    K --> L[Final Answer + Sources]
```

## Возможности

- **Extractive QA** — Fine-tuned BERT для прямого вопрос-ответа
- **RAG Pipeline** — Retrieval-Augmented Generation с FAISS vector index
- **Индексация документов** — Поиск по PDF, DOCX и текстовым файлам
- **Интерактивный UI** — Streamlit и Gradio интерфейсы
- **Привязка к источникам** — Ответы со ссылками на исходные документы
- **Модульная архитектура** — Indexing, search, training и inference независимы

## Структура проекта

```
Question-answering/
├── src/
│   ├── app.py              # Streamlit/Gradio веб-интерфейс
│   ├── train_qa.py         # Fine-tuning QA модели
│   ├── rag_index.py        # Построитель FAISS индекса
│   ├── rag_search.py       # Векторный поиск
│   ├── rag_generate.py     # RAG генератор ответов
│   └── data_utils.py       # Загрузка и preprocessing данных
├── notebooks/              # Ноутбуки
├── requirements.txt
└── README.md
```

## Установка

```bash
git clone https://github.com/HolSoul/Question-answering.git
cd Question-answering

python -m venv .venv
.venv\Scripts\activate  # Windows
source .venv/bin/activate  # macOS/Linux

pip install -r requirements.txt
```

## Использование

### Запуск веб-интерфейса

```bash
streamlit run src/app.py
# или
gradio src/app.py
```

### Обучение QA модели

```bash
python src/train_qa.py
```

### Построение FAISS индекса

```bash
python src/rag_index.py --data_path /путь/к/документам
```

### Поиск через RAG

```bash
python src/rag_search.py --query "Ваш вопрос"
```

## Детали pipeline

### Обработка данных
- Парсинг документов (PDF, DOCX, TXT)
- Разбиение на чанки с перекрытием
- Генерация эмбеддингов через Sentence-BERT

### Extractive QA
- Fine-tuned BERT (distilbert/bert-base) на SQuAD-совместимых датасетах
- Token classification для стартовой/конечной позиции ответа
- Confidence scoring

### RAG Pipeline
1. Кодирование запроса в вектор
2. Поиск top-K похожих чанков в FAISS
3. Подача чанков + вопроса в QA модель
4. Возврат ответа с указанием источников

## Tech Stack

- **NLP Framework**: 🤗 Transformers, Sentence-Transformers
- **Vector Search**: FAISS (cpu)
- **Machine Learning**: PyTorch, scikit-learn
- **Data**: pandas, numpy, nltk
- **UI**: Streamlit, Gradio
- **Document Processing**: pdfplumber, python-docx

## Лицензия

MIT License
