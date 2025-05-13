"""
Модуль для загрузки и предобработки данных
"""
import pandas as pd
from typing import List, Tuple
import pdfplumber
import os

try:
    import docx
except ImportError:
    docx = None

def load_raw_texts(path: str) -> List[str]:
    """Загрузка исходных текстов из файла/папки"""
    # TODO: реализовать
    pass

def prepare_qa_dataset(texts: List[str]) -> pd.DataFrame:
    """Генерация датасета вопрос-ответ для extractive QA"""
    # TODO: реализовать
    pass

def extract_text_from_pdf(pdf_path: str) -> str:
    """Извлечение текста из PDF-файла"""
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_text_from_docx(docx_path: str) -> str:
    """Извлечение текста из DOCX-файла"""
    if docx is None:
        raise ImportError("Для работы с DOCX установите пакет python-docx")
    doc = docx.Document(docx_path)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])

def extract_text_from_txt(txt_path: str) -> str:
    """Извлечение текста из TXT-файла"""
    with open(txt_path, encoding="utf-8") as f:
        return f.read()

def extract_text_from_file(file_path: str) -> str:
    """Универсальная функция для извлечения текста из PDF, DOCX, TXT"""
    ext = os.path.splitext(file_path)[-1].lower()
    if ext == ".pdf":
        return extract_text_from_pdf(file_path)
    elif ext == ".docx":
        return extract_text_from_docx(file_path)
    elif ext == ".txt":
        return extract_text_from_txt(file_path)
    else:
        raise ValueError(f"Неподдерживаемый формат файла: {ext}")
