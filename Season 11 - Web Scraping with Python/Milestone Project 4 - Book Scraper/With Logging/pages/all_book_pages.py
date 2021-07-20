import re
import logging

from bs4 import BeautifulSoup

from locators.books_page_locators import BookPageLocator
from parsers.book_parser import BookParser

logger = logging.getLogger('scraping.all_book_pages')


class AllBooksPage:
    def __init__(self, page_content):
        logger.debug('Parsing page content with BeautifulSoup HTML Parser.')
        self.soup = BeautifulSoup(page_content, 'html.parser')

    @property
    def books(self):
        logger.debug(f'finding all books in the page using `{BookPageLocator.BOOKS}`.')
        return [BookParser(e) for e in self.soup.select(BookPageLocator.BOOKS)]

    @property
    def page_count(self):
        logger.debug('Finding all the number of catalogue pages available...')
        content = self.soup.select_one(BookPageLocator.PAGER).string
        logger.debug(f'Found number of pages available: `{content}`.')
        pattern = 'Page [0-9]+ of ([0-9+])'
        matcher = re.search(pattern, content)
        pages = int(matcher.group(1))
        logger.debug(f'Extracted number of pages : `{pages}`.')
        return pages
