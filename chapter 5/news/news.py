from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
import csv
import time


service = Service(
    "E:/Work/Python/python_masterclass_projects/chromedriver-win64/chromedriver.exe"
)

driver = webdriver.Chrome(service=service)
driver.get("https://www.bbc.com/news")

time.sleep(3)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, "html.parser")

headlines = soup.find_all("h2")

with open("headlines.csv", mode="w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for h in headlines:
        text = h.get_text(strip=True)
        if text:
            writer.writerow([text])

print("Headlines have been saved in headlines.csv")
