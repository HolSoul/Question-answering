"""
Интерактивное приложение для QA-системы (Streamlit)
"""
import streamlit as st

# TODO: реализовать загрузку моделей, индекса и обработку запросов

def main():
    st.title("Система Вопрос-Ответ (QA)")
    question = st.text_input("Введите вопрос:")
    if st.button("Получить ответ"):
        # TODO: реализовать обработку вопроса и вывод ответа
        st.write("Ответ: ...")

if __name__ == "__main__":
    main()
