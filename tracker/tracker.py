import requests
from bs4 import BeautifulSoup

class Tracker():
    
    def __init__(self, URL, target_price):
        page = requests.get(URL, headers={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:61.0) Gecko/20100101 Firefox/"})
        soup0 = BeautifulSoup(page.content, "html.parser")
        soup = BeautifulSoup(soup0.prettify(), "html.parser")

        self.URL = URL
        self.soup = soup
        self.price = self.soup.find(class_="a-offscreen").get_text().strip()
        self.int_price = float(self.price.strip().replace("€", "").replace(",", "."))
        self.target_price = float(target_price)
        self.title = self.soup.find(id="productTitle").get_text()
