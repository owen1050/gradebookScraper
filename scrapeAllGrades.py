from selenium import webdriver
import time

class GradeScraper:

	def __init__(self, loginURL, username, password):
		self.url = loginURL
		self.un = username
		self.pw = password

	def getAllGrades(self, classList, headless = True, printUpdates = True):

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


		#type username
		nameXpath = '/html/body/section[1]/article[2]/div/div/form/div[1]/div/div/div[1]/input'
		unameBox = driver.find_element_by_xpath(nameXpath)

		unameBox.send_keys(self.un)

		#type password
		pwXpath = '/html/body/section[1]/article[2]/div/div/form/div[1]/div/div/div[2]/input'
		pwBox = driver.find_element_by_xpath(pwXpath)

		pwBox.send_keys(self.pw)


		signInXpath = "/html/body/section[1]/article[2]/div/div/form/div[1]/div/div/div[4]/button"
		signInButton = driver.find_element_by_xpath(signInXpath)
		  
		signInButton.click()

		driver.set_window_size(1800, 800)

		#wait for load
		time.sleep(2)

		firstStudentNameXpath = 	'/html/body/div[4]/div[5]/div[4]/div[2]/div/div[2]/table/tbody/tr[{index}]/td[2]/a[1]'
		firstStudentPerXpath = 		'/html/body/div[4]/div[5]/div[4]/div[2]/div/div[2]/table/tbody/tr[{index}]/td[3]'
		firstStudentLetterXpath = 	'/html/body/div[4]/div[5]/div[4]/div[2]/div/div[2]/table/tbody/tr[{index}]/td[4]/div/span'
																									#STUDNET INDEX
		secondStudentNamXpath = 	'/html/body/div[4]/div[5]/div[4]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/a[1]'

		gradebooksOptionsXpath = '/html/body/div[4]/nav[1]/div/ul/li[2]/a'

		onlyOnceGradebookIsSelectedFirstClassXpath = 	'/html/body/div[4]/nav[1]/div/ul/li[2]/div/ul/li[{index}]/a'
		onlyOnceGradebookIsSelectedSecondClassXpath =	'/html/body/div[4]/nav[1]/div/ul/li[2]/div/ul/li[2]/a'

		nameOfClassXPATH =							 	'/html/body/div[4]/nav[1]/div/ul/li[2]/div/ul/li[{index}]/a/span[1]'
		classDescXPATH = 								'/html/body/div[4]/nav[1]/div/ul/li[2]/div/ul/li[{index}]/a/span[2]'

		classs = classList

		allGrades = {}

		for c in classs:
			grades = []
			gradebookButton = driver.find_element_by_xpath(gradebooksOptionsXpath)
			gradebookButton.click()

			time.sleep(2)

			firstClassButton = driver.find_element_by_xpath(onlyOnceGradebookIsSelectedFirstClassXpath.format(index=c))

			classNameHTML = driver.find_element_by_xpath(nameOfClassXPATH.format(index=c))
			className = classNameHTML.get_attribute('innerHTML')

			classDescHTML = driver.find_element_by_xpath(classDescXPATH.format(index=c))
			classDesc = classDescHTML.get_attribute('innerHTML')
			
			classNamePlusDesc = className + ":" + classDesc
			if(printUpdates):
				print("Getting grades for: " + classNamePlusDesc)


			firstClassButton.click()
			
			time.sleep(5)
			student = 1
			while(True):
				try:
					firstStudnetHTML = driver.find_element_by_xpath(firstStudentNameXpath.format(index=student))
					name = firstStudnetHTML.get_attribute('innerHTML')

					firstPerHTML = driver.find_element_by_xpath(firstStudentPerXpath.format(index=student))
					per = firstPerHTML.get_attribute('innerHTML')

					firstLetterHTML = driver.find_element_by_xpath(firstStudentLetterXpath.format(index=student))
					letter = firstLetterHTML.get_attribute('innerHTML')
					student = student + 1

					grades.append([name, per,  letter])

				except:
					break

			allGrades[classNamePlusDesc] = grades

			time.sleep(1)

		driver.quit()
		return allGrades