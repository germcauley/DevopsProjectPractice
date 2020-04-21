from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


options = webdriver.ChromeOptions()
options.binary_location = '/opt/google/chrome/google-chrome'
service_log_path = "{}/chromedriver.log".format(outputdir)
service_args = ['--verbose']
driver = webdriver.Chrome('/usr/bin/chromedriver',
        chrome_options=options,
        service_args=service_args,
        service_log_path=service_log_path)

# Visit my app hosted on aws
driver.get("http://devopsassignment-env.eba-mx9qvtf8.eu-west-1.elasticbeanstalk.com/")

title = driver.find_element_by_tag_name('h1')
messagelink = driver.find_element_by_tag_name('h1')
time.sleep(5)

assert title.text =="Welcome to Message app"

# assert messagelink.text == "Hello"
driver.close()
