import re
import logging

from locators.book_locators import BookLocators

logger = logging.getLogger('scraping.book_parser')


class BookParser:

    RATINGS = {
        'One': 1,
        'Two': 2,
        'Three': 3,
        'Four': 4,
        'Five': 5
    }

    def __init__(self, parent):
        self.parent = parent

    def __repr__(self):
        return f'Book - {self.name}, £{self.price} ({self.rating} stars)'

    @property
    def name(self):
        logger.debug('Finding Book Name...')
        locator = BookLocators.NAME_LOCATOR
        item_name = self.parent.select_one(locator).attrs['title']
        logger.debug(f'Found Book Name `{item_name}`.')
        return item_name

    @property
    def link(self):
        logger.debug('Finding Book Book Link...')
        locator = BookLocators.LINK_LOCATOR
        item_link = self.parent.select_one(locator).attrs['href']
        logger.debug(f'Found Book link `{item_link}`.')
        return item_link

    @property
    def price(self):
        logger.debug('Finding Book Price...')
        locator = BookLocators.PRICE_LOCATOR
        item_price = self.parent.select_one(locator).string

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        float_price = float(matcher.group(1))
        logger.debug(f'Found Book price `{float_price}`.')
        return float_price

    @property
    def rating(self):
        logger.debug('Finding Book Rating...')
        locator = BookLocators.RATING_LOCATOR
        star_rating_tag = self.parent.select_one(locator)
        classes = star_rating_tag.attrs['class']
        rating_classes = [r for r in classes if r != 'star-rating']
        rating_number = BookParser.RATINGS.get(rating_classes[0])
        logger.debug(f'Found Book Rating `{rating_number}`.')
        return rating_number
