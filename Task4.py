import requests
from bs4 import BeautifulSoup
import pandas as pd

BASE_URL = "http://books.toscrape.com/catalogue/category/books/"

def get_category_url(category_name):
    url = "http://books.toscrape.com/catalogue/category/books_1/index.html"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    categories = soup.select("ul.nav.nav-list ul li a")
    for cat in categories:
        name = cat.get_text(strip=True).lower()
        href = cat["href"]
        if category_name.lower() == name:
            return "http://books.toscrape.com/catalogue/category/books/" + href
    return None

def scrape_category(category_url):
    books = []
    while category_url:
        response = requests.get(category_url)
        soup = BeautifulSoup(response.text, "html.parser")
        articles = soup.find_all("article", class_="product_pod")
        for article in articles:
            title = article.h3.a["title"]
            price = article.find("p", class_="price_color").text
            rating_word = article.p["class"][1]
            rating_map = {'One':1, 'Two':2, 'Three':3, 'Four':4, 'Five':5}
            rating = rating_map.get(rating_word, 0)
            image_url = "http://books.toscrape.com/" + article.find("img")["src"].replace("../", "")
            books.append({"Title": title, "Price": price, "Rating": rating, "Image URL": image_url})

        # check next page
        next_btn = soup.select_one("li.next a")
        if next_btn:
            next_href = next_btn["href"]
            category_url = "/".join(category_url.split("/")[:-1]) + "/" + next_href
        else:
            category_url = None
    return books

if __name__ == "__main__":
    category = input("Enter a book category (e.g., Travel, Mystery, Poetry): ")
    category_url = get_category_url(category)

    if not category_url:
        print(f"❌ Category '{category}' not found. Try another one.")
    else:
        books = scrape_category(category_url)
        if books:
            filename = f"c:/SkillCraft/{category.lower()}_books.csv"
            df = pd.DataFrame(books)
            df.to_csv(filename, index=False)
            print(f"✅ Found {len(books)} books in '{category}' category.")
            print(f"📂 Data saved to {filename}")
        else:
            print(f"⚠️ No books found in '{category}' category.")
