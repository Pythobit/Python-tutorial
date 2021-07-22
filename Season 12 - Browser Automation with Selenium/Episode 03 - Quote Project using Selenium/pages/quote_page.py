from typing import List

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions

from locators.quote_page_locators import QuotePageLocator
from parsers.quote_parser import QuoteParser


class QuotePage:
    def __init__(self, browser):
        self.browser = browser

    @property
    def quotes(self) -> List[QuoteParser]:
        return [
            QuoteParser(e)
            for e in self.browser.find_elements_by_css_selector(
                QuotePageLocator.QUOTE
            )
        ]

    @property
    def author_dropdown(self) -> Select:
        element = self.browser.find_element_by_css_selector(
            QuotePageLocator.AUTHOR_DROPDOWN
        )
        return Select(element)

    def select_author(self, author_name):
        self.author_dropdown.select_by_visible_text(author_name)

    @property
    def tag_dropdown(self) -> Select:
        elements = self.browser.find_element_by_css_selector(
            QuotePageLocator.TAG_DROPDOWN
        )
        return Select(elements)

    def select_tag(self, tags: str):
        self.tag_dropdown.select_by_visible_text(tags)

    def get_available_tags(self) -> List[str]:
        return [option.text.strip() for option in self.tag_dropdown.options]

    @property
    def search_button(self):
        return self.browser.find_element_by_css_selector(
            QuotePageLocator.SEARCH_BUTTON
        )

    def search_for_quotes(self, author_name: str, tag_name: str) -> List[QuoteParser]:
        self.select_author(author_name)

        WebDriverWait(self.browser, 10).until(
            expected_conditions.presence_of_element_located(
                (By.CSS_SELECTOR, QuotePageLocator.TAG_DROPDOWN_VALUE_OPTION)
            )
        )

        try:
            self.select_tag(tag_name)
        except NoSuchElementException:
            raise InvalidTagForAuthorError(
                f"Author '{author_name}' does not have any quotes tagged with '{tag_name}'."
            )
        self.search_button.click()
        return self.quotes


class InvalidTagForAuthorError(ValueError):
    pass
