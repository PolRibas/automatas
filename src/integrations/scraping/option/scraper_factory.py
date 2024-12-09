from integrations.scraping.option.requests_scraper import RequestsScraper
from integrations.scraping.option.selenium_scraper import SeleniumScraper
from integrations.scraping.option.playwright_scraper import PlaywrightScraper

def get_scraper(scraper_type='requests', **kwargs):
    if scraper_type == 'requests':
        return RequestsScraper(**kwargs)
    elif scraper_type == 'selenium':
        return SeleniumScraper(**kwargs)
    elif scraper_type == 'playwright':
        return PlaywrightScraper(**kwargs)
    else:
        raise ValueError(f"Unknown scraper type: {scraper_type}")
