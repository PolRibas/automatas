import requests
from bs4 import BeautifulSoup
from integrations.scraping.base_scraper import BaseScraper

class RequestsScraper(BaseScraper):
    def __init__(self, headers=None):
        self.session = requests.Session()
        if headers:
            self.session.headers.update(headers)
        else:
            self.session.headers.update({
                'User-Agent': 'MyScraperBot/1.0 (+https://www.mywebsite.com)'
            })

    def get_content(self, url):
        response = self.session.get(url)
        response.raise_for_status()
        return response.text

    def parse_content(self, content):
        soup = BeautifulSoup(content, 'html.parser')
        # Implement your parsing logic here
        data = []
        for element in soup.find_all('h2'):
            data.append(element.get_text())
        return data

    def extract_data(self, url):
        content = self.get_content(url)
        data = self.parse_content(content)
        return data
