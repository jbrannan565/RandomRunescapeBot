"""
download and parse a random page from runscape.wiki
"""
from bs4 import BeautifulSoup
import urllib.request


class RunscapeFetcher:
    def __init__(self):
        pass
    
    def fetch_random_page(self):
        opener = urllib.request.FancyURLopener({})
        url = ""
        f = opener.open(url)
        html = f.read()
        return html 

    def make_soup(self, html):
        return BeautifulSoup(html, 'html.parser')

    def get_page_content(self, soup):
        selector = "#mw-content-text > div > section > p"
        return soup.find_all(selector)

    def get_content_text(self, content):
        return " ".join([tag.get_text() for tag in content])

    def get_text(self):
        html = self.fetch_random_page()
        soup = self.make_soup(html)
        content = self.get_content_text(soup)
        return self.get_content_text(content)