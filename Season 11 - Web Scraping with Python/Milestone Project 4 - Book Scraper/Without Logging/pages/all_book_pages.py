import re
from bs4 import BeautifulSoup

from locators.all_books_page import BookPageLocator
from parsers.book_parser import BookParser


class AllBooksPage:
    def __init__(self, page_content):
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        return [BookParser(e) for e in self.soup.select(BookPageLocator.BOOKS)]

    @property
    def page_count(self):
        content = self.soup.select_one(BookPageLocator.PAGER).string
        pattern = 'Page [0-9]+ of ([0-9+])'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        return pages
