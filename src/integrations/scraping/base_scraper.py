from abc import ABC, abstractmethod

class BaseScraper(ABC):
    @abstractmethod
    def get_content(self, url):
        """Fetch the content from the given URL."""
        pass

    @abstractmethod
    def parse_content(self, content):
        """Parse the content and extract the required data."""
        pass

    @abstractmethod
    def extract_data(self, url):
        """High-level method to fetch and parse content from the given URL."""
        pass
