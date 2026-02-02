from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(
    "E:/Work/Python/python_masterclass_projects/chromedriver-win64/chromedriver.exe"
)

driver = webdriver.Chrome(service=service)
driver.get("https://www.python.org")