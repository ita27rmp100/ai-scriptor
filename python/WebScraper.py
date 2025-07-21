import requests
from bs4 import BeautifulSoup

class WebScraper:
    def __init__(self, url):
        self.url = url

    def send_request(self):
        try:
            response = requests.get(self.url)
            return response
        except Exception as e:
            print(str(e))
            return None

    def parse_html(self, response):
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup

    def extract_data(self, soup, tag):
        data = soup.find_all(tag)
        return data

    def scrape(self, tag):
        response = self.send_request()
        if response is not None and response.status_code == 200:
            soup = self.parse_html(response)
            data = self.extract_data(soup, tag)
            return data
        else:
            return None

def main():
    url = 'http://example.com'
    tag = 'p'
    web_scraper = WebScraper(url)
    data = web_scraper.scrape(tag)
    if data is not None:
        for item in data:
            print(item.text)

if __name__ == "__main__":
    main()
