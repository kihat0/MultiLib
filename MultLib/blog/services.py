import requests
from bs4 import BeautifulSoup
from django.core.exceptions import ValidationError
import logging
import time
from .models import Book
from urllib.parse import urljoin

def parse_gutenberg_catalog():

    # Страница с популярными книгами
    catalog_url = "https://www.gutenberg.org/browse/scores/top"
    response = requests.get(catalog_url, timeout=10)
    bs = BeautifulSoup(response.content, 'html.parser')

    # Находим ссылки на книги (селектор может меняться)
    book_links = bs.select('a[href^="/ebooks/"]')
    parsed_count = 0

    for link in book_links:
        # Извлекаем ID книги из URL
        book_url = urljoin(catalog_url, link['href'])
        book_id = book_url.split('/')[-1]

        if book_id.isdigit():  # проверяем, что это число
            # Используем уже готовую функцию парсинга
            parse_single_book(book_id)
            parsed_count += 1
            # Пауза между книгами
            time.sleep(3)

    return parsed_count

def parse_single_book(book_id):
    """Функция для парсинга одной книги — переиспользуем из Варианта 1"""
    url = f"https://www.gutenberg.org/ebooks/{book_id}"
    response = requests.get(url, timeout=10)

    bs = BeautifulSoup(response.content, 'html.parser')
    title_tag = bs.find('h1', itemprop='name')
    book_title = title_tag.text.strip() if title_tag else f"Книга {book_id} (без названия)"

    description_tag = bs.find('span', class_='readmore-container')
    book_description = description_tag.get_text(strip=True) if description_tag else 'Описание отсутствует'

    book = Book.objects.create(
        book_title=book_title,
        #book_slug=book_title.lower().replace(' ', '-')[:150],
        book_description=book_description,
    book_pages=0,
    book_language='Английский',
    book_age=0
    )
    return book