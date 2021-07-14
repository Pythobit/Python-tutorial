from bs4 import BeautifulSoup

from locators.quote_page_locators import QuotePageLocator
from parsers.quote import QuoteParser


class QuotePage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def quotes(self):
        locator = QuotePageLocator.QUOTE
        quote_tags = self.soup.select(locator)
        return [QuoteParser(e) for e in quote_tags]
