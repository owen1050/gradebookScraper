from selenium import webdriver
import time

class GradeScraper:

	def __init__(self, url):
		self.url = url

	def getUrl(self, headless = True, printUpdates = True):

		options = webdriver.ChromeOptions()
		if(headless):
			options.add_argument('--headless')
			if(printUpdates):
				print("Launching chromedrive headlessly")
		else:
			if(printUpdates):
				print("Launching chromedrive")

		driver = webdriver.Chrome('chromedriver.exe', options=options)

		# driver.get method() will navigate to a page given by the URL address
		driver.get(self.url)




		driver.quit()
		return 0