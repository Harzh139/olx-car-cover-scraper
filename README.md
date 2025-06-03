# OLX Car Cover Scraper

This project contains a Python script to scrape "Car Cover" listings from [OLX.in](https://www.olx.in/items/q-car-cover).

## 🔧 Scripts

### 1. `olx_scraper_basic.py`
- Uses `requests` + `BeautifulSoup`
- Limitations: OLX listings are dynamically loaded via JavaScript, so this script returns 0 results.

### 2. `olx_scraper_selenium.py`
- Uses `Selenium` to render JavaScript content
- Accurately fetches listing titles, prices, and locations

## 🛠 Requirements

Install required libraries:

```bash
pip install requests beautifulsoup4 selenium

