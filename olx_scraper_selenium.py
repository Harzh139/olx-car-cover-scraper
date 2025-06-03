from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import csv
import time

# Set up headless Chrome
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')

driver = webdriver.Chrome(options=options)

# Open OLX car cover listings
url = "https://www.olx.in/items/q-car-cover"
driver.get(url)
time.sleep(5)  # wait for JS to load

soup = BeautifulSoup(driver.page_source, 'html.parser')

listings = []

# Parse results
for item in soup.select("li.EIR5N"):
    title = item.select_one("span._2tW1I")
    price = item.select_one("span._89yzn")
    location = item.select_one("span._2FcNR")

    listings.append([
        title.text.strip() if title else "N/A",
        price.text.strip() if price else "N/A",
        location.text.strip() if location else "N/A"
    ])

# Save to CSV
with open("olx_car_cover_results.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price", "Location"])
    writer.writerows(listings)

print(f"Saved {len(listings)} listings to 'olx_car_cover_results.csv'")

driver.quit()
