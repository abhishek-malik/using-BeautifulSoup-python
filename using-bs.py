import requests
from bs4 import BeautifulSoup

request = requests.get("http://www.johnlewis.com/john-lewis-office-chair-black/p447855")
content = request.content
soup = BeautifulSoup(content,"html.parser")
element = soup.find("span", {"itemprop": "price", "class": "now-price"})
print(element.text)
