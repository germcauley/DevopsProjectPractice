from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('/usr/bin/chromedriver',chrome_options=chrome_options)


# Visit my app hosted on aws
driver.get("http://devopsassignment-env.eba-mx9qvtf8.eu-west-1.elasticbeanstalk.com/")

title = driver.find_element_by_tag_name('h1')
messagelink = driver.find_element_by_tag_name('h1')
time.sleep(5)

assert title.text =="Welcome to Message app Fail"

# assert messagelink.text == "Hello"
driver.close()
