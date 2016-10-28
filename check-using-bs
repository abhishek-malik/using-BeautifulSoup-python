import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.johnlewis.com/john-lewis-office-chair-black/p447855")
content = request.content
soup = BeautifulSoup(content,"html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
string_price = element.text.strip()
price_without_symbol = string_price[1:]
price=float(price_without_symbol)
if price < 200 :
    print("Buy the chair")
else:
    print("Do not buy the chair")
