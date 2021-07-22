from selenium import webdriver

from pages.quote_page import QuotePage,InvalidTagForAuthorError

try:
    author = input("Enter the author you'd like quotes from : ")
    tag = input('Enter your tag: ')

    chrome = webdriver.Chrome(executable_path='C:/Chromedriver/chromedriver.exe')
    chrome.get('http://quotes.toscrape.com/search.aspx')
    page = QuotePage(chrome)

    print(page.search_for_quotes(author, tag))
except InvalidTagForAuthorError as e:
    print(e)
except Exception as e:
    print(e)
    print('An Unknown Error Occurred..!')
