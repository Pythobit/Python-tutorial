# Splitting HTML locators out of our python class..!

import re
from bs4 import BeautifulSoup

Item_html = '''<html><head></head><body>
<li class="col-xs-6 col-sm-4 col-md-3 col-lg-3">
    <article class="product_pod">
            <div class="image_container">
                    <a href="catalogue/a-light-in-the-attic_1000/index.html"><img src="media/cache/2c/da/2cdad67c44b002e7ead0cc35693c0e8b.jpg" alt="A Light in the Attic" class="thumbnail"></a>
            </div>
                <p class="star-rating Three">
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                    <i class="icon-star"></i>
                </p>
            <h3><a href="catalogue/a-light-in-the-attic_1000/index.html" title="A Light in the Attic">A Light in the ...</a></h3>
            <div class="product_price">
        <p class="price_color">£51.77</p>
<p class="instock availability">
    <i class="icon-ok"></i>
        In stock
</p>
    <form>
        <button type="submit" class="btn btn-primary btn-block" data-loading-text="Adding...">Add to basket</button>
    </form>
            </div>
    </article>
</li>
</body></html>
'''

class ParsedItemLocators:
    """
    Locators for an item in an HTML page

    This allows us to easily see what our code will be looking at
    as well as change it quickly, if we notice it is now different.
    """
    NAME_LOCATOR = 'article.product_pod h3 a'
    PAGE_LOCATOR = 'article.product_pod h3 a'
    PRICE_LOCATOR = 'article.product_pod p.price_color'
    RATING_LOCATOR = 'article.product_pod p.star-rating'


class ParsedItem:
    """
    A class that takes in an HTML (or parts of it), and find the properties of an item in it.
    """

    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    @property
    def name(self):
        locator = ParsedItemLocators.NAME_LOCATOR
        item_link = self.soup.select_one(locator)
        item_name = item_link.attrs['title']
        return item_name

    @property
    def page(self):
        locator = ParsedItemLocators.PAGE_LOCATOR
        page_link = self.soup.select_one(locator).attrs['href']
        return page_link

    @property
    def price(self):
        locator = ParsedItemLocators.PRICE_LOCATOR
        item_price = self.soup.select_one(locator).string    #£51.77

        pattern = '£([0-9]+\.[0-9]+)'
        matcher = re.search(pattern, item_price)
        return matcher.group(0)
        # return float(matcher.group(1))
        # return float(matcher.group(1)) * 0.8    # price with 20% discount, because it's a number and not a string.

    @property
    def rating(self):
        locator = ParsedItemLocators.RATING_LOCATOR
        rating_tag = self.soup.select_one(locator)
        classes = rating_tag.attrs['class']     # ['star-rating', 'Three']

        # Two ways to get class ['Three'] without ['star-rating']
        rating_classes = [r for r in classes if r not in 'star-rating']     # List Comprehension
        # rating_classes = filter(lambda x: x != 'star-rating', classes)      # filter function
        return rating_classes[0]


item = ParsedItem(Item_html)
print(item.price)

