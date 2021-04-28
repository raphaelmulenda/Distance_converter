from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/raphael/Documents/Setup/chromedrivers/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://orteil.dashnet.org/cookieclicker/")

cookies = driver.find_element_by_id('bigCookie')

timeout = time.time() + 10
five_min = time.time() + 60 * 5  # 5minutes

#prices = driver.find_element_by_xpath('//*[@id="product1"]//*[@id="productPrice1"]')

price = driver.find_element_by_css_selector("#store span")
print(price.text)


#game_on = True
#while game_on:
#    cookies.click()
#
#    if time.time() > timeout:
#        price = driver.find_element_by_css_selector("div[class='title']span[class='price']")
#        print(price.text)
#