from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from integrations.scraping.base_scraper import BaseScraper

class SeleniumScraper(BaseScraper):
    def __init__(self, headless=True):
        options = Options()
        if headless:
            options.add_argument('--headless')
        self.driver = webdriver.Chrome(options=options)

    def get_content(self, url):
        self.driver.get(url)
        return self.driver.page_source

    def parse_content(self, content):
        # Since we're using Selenium, we can interact directly with the driver
        elements = self.driver.find_elements(By.TAG_NAME, 'h2')
        data = [element.text for element in elements]
        return data

    def extract_data(self, url):
        self.get_content(url)
        data = self.parse_content(None)  # Content is fetched via the driver
        return data

    def __del__(self):
        self.driver.quit()

