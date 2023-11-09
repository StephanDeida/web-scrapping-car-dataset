from selenium import webdriver
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import mariadb
from datetime import date

from selenium.webdriver.common.action_chains import ActionChains

chrome_options = Options()
#chrome_options.add_argument('--headless')

chrome_options.add_argument("user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/Profile99")
chrome_options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36")
# create a new Chrome browser instance with headless mode
browser = webdriver.Chrome(options=chrome_options)

# Set up the driver (you may need to download and install the driver for your browser)

# Navigate to the webpage with the button
browser.get("https://auto.mercadolibre.com.mx/MLM-1975289257-kia-forte-2017-_JM#position=26&search_layout=grid&type=item&tracking_id=8c5dc14b-ff05-4fc5-ad02-88bf01b82373")

# Wait for the page to finish loading
wait = WebDriverWait(browser, 100)  # Maximum wait time of 10 seconds
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

print("first step")
time.sleep(10)
# Find the button element by its ID, class name, or other selector
btn_container = browser.find_element(By.ID, ':Rmdba5icd:')
link = None
while not link:
    action = ActionChains(browser)
    action.click_and_hold(btn_container)
    # Initiate click and hold action on button
    action.perform()
    # Release button
    time.sleep(0.5)
    action.release(btn_container)
    time.sleep(3)
    try:
        link = browser.find_element(By.ID, 'recaptcha-anchor')
    except:
        link = None
if (link):
    print("second_step")