from xml.sax.saxutils import prepare_input_source
import requests
from bs4 import BeautifulSoup

URL = 'https://www.amazon.com/ULANZI-Flexible-Detachable-Octopus-Compatible/dp/B09ZY23WZN/ref=mp_s_a_1_8_sspa?crid=32TY9UDMZQEWH&keywords=flexible+tripod&qid=1662133101&sprefix=flexible+tripod%2Caps%2C164&sr=8-8-spons&psc=1'

headers ={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"}

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'lxml')

#title = soup.find(id = "productTitle").get_text()

price = soup.find({'class': 'a-price-whole'}).get_text()



#converted_price = float(price[:-3])

#print(converted_price)