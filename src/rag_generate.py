"""
Генерация ответа на основе найденных фрагментов и вопроса
"""
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
from typing import List

# TODO: реализовать функцию генерации ответа

def generate_answer(question, context, model_name="sberbank-ai/rugpt3small_based_on_gpt2"):
    # TODO: реализовать генерацию
    pass

def generate_answer_rag(question: str, context_sentences: List[str], model_name="sberbank-ai/rugpt3small_based_on_gpt2", max_new_tokens: int = 64) -> str:
    """Генерирует ответ на вопрос, используя найденные предложения как контекст (RAG)"""
    context = " ".join(context_sentences)
    prompt = f"Вопрос: {question}\nКонтекст: {context}\nОтвет:"
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    input_ids = tokenizer(prompt, return_tensors="pt").input_ids
    with torch.no_grad():
        output = model.generate(input_ids, max_new_tokens=max_new_tokens, do_sample=True, top_p=0.95, top_k=50)
    answer = tokenizer.decode(output[0], skip_special_tokens=True)
    # Обрезаем prompt, чтобы оставить только ответ
    return answer[len(prompt):].strip()
