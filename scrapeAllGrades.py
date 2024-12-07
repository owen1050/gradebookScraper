from selenium import webdriver
import time

driver = webdriver.Chrome('chromedriver.exe', options=options)

# driver.get method() will navigate to a page given by the URL address
driver.get(self.url)
time.sleep(3)

gifElement = driver.find_element_by_xpath("//*[@id=\"main-page-content\"]/section/div[1]/div[2]/div[2]/img[1]")
urlName = gifElement.get_attribute('src')
driver.quit()
print(urlName)
