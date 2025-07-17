import re

from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/Zillow-Clone/")

soup = BeautifulSoup(response.text, "html.parser")

#House Addresses
houses = soup.select("a.StyledPropertyCardDataArea-anchor")
house_address_list = [item.get_text(strip=True) for item in houses]

#House Prices
house_prices = soup.select("span.PropertyCardWrapper__StyledPriceLine")
house_prices_list = []
for item in house_prices:
    text = item.get_text(strip=True)
    match = re.search(r'\$\d{1,3}(?:,\d{3})*',text)
    if match:
        price = match.group(0)
        house_prices_list.append(price)

#House Links
links = []
for tag in houses:
    links.append(tag['href'])
