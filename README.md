# Project Title: Scraping and Visualizing Website Data with Python and BeautifulSoup

## Description:
This little project demonstrates how to use Python and BeautifulSoup to scrape data from the website "https://books.toscrape.com/". The scraped data is then cleaned and combined into a dataset to visualize the correlation between book prices and their types.

## Roadmap:

1. **Install Necessary Libraries:**
   Ensure you have Python installed on your system. Additionally, install the required libraries:
   - BeautifulSoup: To parse HTML and extract data.
   - Requests: To send HTTP requests to the website.

2. **Import the Required Modules:**
   Import the necessary modules into your Python script. Make sure to include the required libraries mentioned above.
```
import requests
from bs4 import BeautifulSoup
```
3. **Send a GET Request to the Website and Parse the HTML Content:**
   Use the Requests library to send a GET request to the target website. Receive the HTML content as a response and parse it using BeautifulSoup.
```
url = "https://books.toscrape.com/"
response = requests.get(url)

if response.status_code == 200:
    html_content = response.text
    soup = BeautifulSoup(html_content, "html.parser")
else:
    print("Failed to retrieve the web page.")
```

5. **Extract Data from the Parsed HTML:**
```
titles = soup.find_all("h3")
book_titles = [title.a.attrs["title"] for title in titles]

prices = soup.find_all("p", class_="price_color")
book_prices = [price.text.strip() for price in prices]
```

5. **Request Data as Required and Export Data to CSV File:**
   Display the extracted data or process it as needed for further analysis. Save the data into a CSV file to create the dataset.
```
for title, price in zip(book_titles, book_prices):
    print(f"Title: {title}, Price: {price}")
```
6. **Clean and Combine the Raw Data:**
   Perform any necessary data cleaning steps, such as removing duplicates or handling missing values. Combine the scraped data into a single dataset.
```
# Read data from each CSV file
csv_files = [
    "fiction_books_data.csv",
    "classics_books_data.csv",
    "fantasy_books_data.csv",
    "music_books_data.csv",
    "science_books_data.csv",
]

dfs = []
for file in csv_files:
    df = pd.read_csv(file)
    # Extract the book type from the file name
    book_type = file.split("_")[0].capitalize()
    df["Type"] = book_type
    dfs.append(df)
```

8. **Create a Bar Chart:**
   Use a data visualization library, such as Matplotlib or Seaborn, to create a bar chart that showcases the correlation between book prices and their types.
```
`
df_combined = pd.concat(dfs, ignore_index=True)

# Clean and convert the "Price" column to numeric data
df_combined["Price"] = df_combined["Price"].str.replace("£", "").str.replace("Â", "")
df_combined["Price"] = pd.to_numeric(df_combined["Price"])

# Create a bar chart
plt.figure(figsize=(10, 6))
sns.barplot(x="Type", y="Price", data=df_combined)
plt.xlabel("Book Type")
plt.ylabel("Price")
plt.title("Price Comparison: Fiction, Classics, Fantasy, Music, and Science")
plt.tight_layout()
plt.show()
```

