"""
download and parse a random page from runscape.wiki
"""
from bs4 import BeautifulSoup
import urllib.request
import re
# as per recommendation from @freylis, compile once only
CLEANR = re.compile('<.*?>') 

def cleanhtml(raw_html):
  cleantext = re.sub(CLEANR, '', raw_html)
  return cleantext

class RunscapeFetcher:
    def __init__(self):
        pass
    
    def fetch_random_page(self):
        url = "https://runescape.wiki/w/Special:Random/main"
        user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
        headers = {'User-Agent': user_agent}

        req = urllib.request.Request(url, {}, headers)

        with urllib.request.urlopen(req) as f:
            return f.read()

    def make_soup(self, html):
        return BeautifulSoup(html, 'html.parser')

    def get_page_content(self, soup):
        selector = ".mw-parser-output > p"
        return soup.select(selector)

    def get_content_text(self, content):
        text = " ".join([tag.get_text() for tag in content])
        return cleanhtml(text)

    def get_text(self):
        html = self.fetch_random_page()
        soup = self.make_soup(html)
        content = self.get_page_content(soup)
        text = self.get_content_text(content)
        return text