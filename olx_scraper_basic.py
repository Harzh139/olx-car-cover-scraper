import requests
from bs4 import BeautifulSoup
import csv

# URL to search "car cover" on OLX
BASE_URL = "https://www.olx.in/items/q-car-cover"

# Headers to mimic a browser visit
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

def fetch_olx_listings(url):
    response = requests.get(url, headers=HEADERS)
    soup = BeautifulSoup(response.text, "html.parser")

    listings = []

    # Scrape listing data
    for item in soup.select("li.EIR5N"):
        title_tag = item.select_one("span._2tW1I")
        price_tag = item.select_one("span._89yzn")
        location_tag = item.select_one("span._2FcNR")

        title = title_tag.text.strip() if title_tag else "N/A"
        price = price_tag.text.strip() if price_tag else "N/A"
        location = location_tag.text.strip() if location_tag else "N/A"

        listings.append([title, price, location])

    return listings

def save_to_csv(data, filename="olx_car_cover_results.csv"):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Location"])
        writer.writerows(data)

if __name__ == "__main__":
    print("Fetching OLX listings for 'Car Cover'...")
    listings = fetch_olx_listings(BASE_URL)
    save_to_csv(listings)
    print(f"Saved {len(listings)} listings to 'olx_car_cover_results.csv'")
      
