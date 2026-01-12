import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/category/books/travel_2/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/141.0.0.0 Safari/537.36 OPR/125.0.0.0"
}

response = requests.get(url, headers=headers)
html = response.content
soup = BeautifulSoup(html, "html.parser")

# Ürünlerin bulunduğu li etiketleri
books = soup.find_all("li", class_="col-xs-6 col-sm-4 col-md-3 col-lg-3")

count = 1

for book in books:
    name = book.h3.a["title"]
    link = book.h3.a["href"]
    price = book.find("p", class_="price_color").text

    print(f"{count}. Ürün adı: {name} | Fiyat: {price}")
    count += 1
