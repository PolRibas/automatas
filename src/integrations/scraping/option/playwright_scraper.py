from integrations.scraping.base_scraper import BaseScraper
from playwright.sync_api import sync_playwright # type: ignore

class PlaywrightScraper(BaseScraper):
    def __init__(self, headless=True):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(headless=headless)
        self.page = self.browser.new_page()

    def get_content(self, url):
        self.page.goto(url)
        return self.page.content()

    def parse_content(self, content):
        # Use the page object to interact with the DOM
        elements = self.page.query_selector_all('h2')
        data = [element.inner_text() for element in elements]
        return data

    def extract_data(self, url):
        self.get_content(url)
        data = self.parse_content(None)  # Content is fetched via the page object
        return data

    def __del__(self):
        self.browser.close()
        self.playwright.stop()
