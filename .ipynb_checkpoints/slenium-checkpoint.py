from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver=webdriver.Chrome("/Users/gerd/Downloads/chromedriver")

driver.get("https://www.google.com/maps/place/Augenklinik+Dr.+Hoffmann/@52.2555789,10.5275976,15z/data=!4m2!3m1!1s0x0:0xe66ee9e189648187?sa=X&ved=2ahUKEwiUrOzD5_DuAhVLDOwKHUVOACkQ_BIwDHoECBgQBQ")

time.sleep(5)

element=driver.find_element_by_tag_name("body")

while True:
    element.send_keys(Keys.PAGE_DOWN)
    time.sleep(3)


