import requests
from bs4 import BeautifulSoup
import csv

# Function to scrape data from a given URL
def scrape_books_data(url):
    response = requests.get(url)

    if response.status_code == 200:
        html_content = response.text
        soup = BeautifulSoup(html_content, "html.parser")

        # Extract book titles and prices
        titles = soup.find_all("h3")
        book_titles = [title.a.attrs["title"] for title in titles]

        prices = soup.find_all("p", class_="price_color")
        book_prices = [price.text.strip() for price in prices]

        return book_titles, book_prices
    else:
        print(f"Failed to retrieve the web page: {url}")
        return [], []

# URLs for Fiction and Classics categories
fiction_url = "https://books.toscrape.com/catalogue/category/books/fiction_10/index.html"
classics_url = "https://books.toscrape.com/catalogue/category/books/classics_6/index.html"

# Scrape data from both URLs
fiction_titles, fiction_prices = scrape_books_data(fiction_url)
classics_titles, classics_prices = scrape_books_data(classics_url)

# Combine the data from both categories
combined_titles = fiction_titles + classics_titles
combined_prices = fiction_prices + classics_prices

# Export the combined data to a CSV file
with open("Classics_books_data.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
