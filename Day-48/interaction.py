from selenium import webdriver
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "/home/raphael/Documents/Setup/chromedrivers/chromedriver"

driver = webdriver.Chrome(executable_path=chrome_driver_path)
#driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("http://secure-retreat-92358.herokuapp.com/")

#num = driver.find_element_by_xpath('//*[@id="articlecount"]/a[1]')
#print(num.text)
#num.click()

first_name = driver.find_element_by_name("fName")
print(first_name.text)
first_name.send_keys("Raphael")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("Mulenda")
email = driver.find_element_by_name("email")
email.send_keys("mulenda@yahoo.fr")
button = driver.find_element_by_class_name("btn")
button.click()

#driver.quit()