"""
parsing.py

Модуль сбора данных: парсинг HTML, извлечение текста и изображений.
"""

import requests
from bs4 import BeautifulSoup

class Parser:
    def __init__(self):
        """Инициализация парсера."""
        pass

    def fetch_html(self, url):
        """
        Загружает HTML-код страницы.

        :param url: URL целевого сайта.
        :type url: str
        :return: HTML-код страницы.
        :rtype: str | None
        """
        response = requests.get(url)
        return response.text if response.status_code == 200 else None

    def parse_content(self, html):
        """
        Извлекает текстовое содержимое страницы.

        :param html: HTML-код страницы.
        :type html: str
        :return: Текстовое содержимое.
        :rtype: str
        """
        soup = BeautifulSoup(html, "html.parser")
        return soup.get_text()

    def extract_images(self, html):
        """
        Извлекает URL изображений с веб-страницы.

        :param html: HTML-код страницы.
        :type html: str
        :return: Список URL изображений.
        :rtype: list[str]
        """
        soup = BeautifulSoup(html, "html.parser")
        return [img["src"] for img in soup.find_all("img") if "src" in img.attrs]

    def analyze_keywords(self, text):
        """
        Анализирует частоту ключевых слов на странице.

        :param text: Текстовое содержимое сайта.
        :type text: str
        :return: Словарь с частотой слов.
        :rtype: dict[str, int]
        """
        words = text.split()
        word_freq = {word: words.count(word) for word in set(words)}
        return dict(sorted(word_freq.items(), key=lambda x: x[1], reverse=True))
