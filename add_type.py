import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/catalogue/category/books/fantasy_19/index.html"
category = "Fantasy"

response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")

    # Extract book titles and prices
    titles = soup.find_all("h3")
    book_titles = [title.a.attrs["title"] for title in titles]

    prices = soup.find_all("p", class_="price_color")
    book_prices = [price.text.strip() for price in prices]

    # Export the data to a CSV file with an additional column "Type" for Fantasy
    with open("fantasy_books_data.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Title", "Price", "Type"])  # Write the header row

        # Write each book title, price, and type as a row in the CSV file
        for title, price in zip(book_titles, book_prices):
            writer.writerow([title, price, category])

    print(f"Data for {category} books has been saved to 'fantasy_books_data.csv'.")
else:
    print("Failed to retrieve the web page.")
