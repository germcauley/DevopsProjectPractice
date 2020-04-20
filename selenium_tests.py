from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver")

# Visit my app hosted on aws
driver.get("http://devopsassignment-env.eba-mx9qvtf8.eu-west-1.elasticbeanstalk.com/")

title = driver.find_element_by_tag_name('h1')
messagelink = driver.find_element_by_tag_name('h1')
time.sleep(5)

assert title.text =="Welcome to Message app"

# assert messagelink.text == "Hello"
driver.close()
