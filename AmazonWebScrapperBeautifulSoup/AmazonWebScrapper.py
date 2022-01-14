# importing libraries
from bs4 import BeautifulSoup
import requests
import time
import datetime
import smtplib

# connecting to amazon website
URL = 'https://www.amazon.com/dp/B0722KMYTY/?coliid=IXMBL0LIXI1G8&colid=65LKACMP95BQ&psc=1&ref_=lv_ov_lig_dp_it'
# headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

#reading the html elements in this page

response = requests.get(URL)
amazon_webpage = response.text
soup = BeautifulSoup(amazon_webpage, "html.parser")

# print(soup.prettify())
price = soup.find(id = "corePriceDisplay_desktop_feature_div")
print(price)