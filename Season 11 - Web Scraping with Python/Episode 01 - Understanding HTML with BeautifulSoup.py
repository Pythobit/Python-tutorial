# Understanding HTML with BeautifulSoup

from bs4 import BeautifulSoup

Simple_html = '''
<html>
<head></head>
<body>
<h1>Hii, Welcome to Python Tutorial</h1>
<p class="subtitle">This is a paragraph tag with a class.</p>
<p>This is a paragraph tag without class.</p>
<ul>
    <li>Meer</li>
    <li>Jay</li>
    <li>Kesh</li>
</ul>
</body>
</html>
'''

simple_soup = BeautifulSoup(Simple_html, 'html.parser')


def find_title():
    h1_tag = simple_soup.find('h1').string
    print(h1_tag)


def find_lists():
    lists_items = simple_soup.find_all('li')
    list_contents = [e.string for e in lists_items]
    print(list_contents)


def find_subtitle():
    subtitle_para = simple_soup.find('p', {'class' : 'subtitle'}).string
    print(subtitle_para)


def find_paragraphs():
    paragraph = simple_soup.find_all('p')
    other_para = [p for p in paragraph if 'subtitle' not in p.attrs.get('class', [])]
    print(other_para[0].string)


find_title()
find_lists()
find_subtitle()
find_paragraphs()
