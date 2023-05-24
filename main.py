import json
import re
import asyncio
import requests

from bs4 import BeautifulSoup


author_list = []
unique_author = set()   # допоміжний сет для збирання тільки "унікальних" авторів
quote_list = []
page_list = []  # для формування списку url, на яких будемо парсити


def get_info_about_author(about_link):
    pass


def one_page_parse(url):
    pass


async def main():
    pass


if __name__ == "__main__":
    asyncio.run(main())
