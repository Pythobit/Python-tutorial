from locators.quote_locators import QuoteLocators


class QuoteParser:
    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'< Quote : {self.content} by {self.author} >'

    @property
    def content(self):
        locator = QuoteLocators.CONTENT
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def author(self):
        locator = QuoteLocators.AUTHOR
        return self.parent.find_element_by_css_selector(locator).text

    @property
    def tags(self):
        locator = QuoteLocators.TAGS
        return [
            e.string
            for e in self.parent.find_elements_by_css_selector(locator)
        ]
