# import web driver
from selenium import webdriver
import time

username = "buslero@villawalsh.org"

#read password from file so its not on github
f = open("password", "r")
password = f.read()
f.close()

# specifies the path to the chromedriver.exe
driver = webdriver.Chrome('chromedriver.exe')

# driver.get method() will navigate to a page given by the URL address
driver.get('https://gb5.plusportals.com/login/loginView?qstr=JQwDzcIrLUDwAbJIIqftfpnaY2o/4a2YbuA6r0VqlTIEtEQ6R19uOLvbazYgIpUH')


#type username
nameXpath = '/html/body/section[1]/article[2]/div/div/form/div[1]/div/div/div[1]/input'
unameBox = driver.find_element_by_xpath(nameXpath)

unameBox.send_keys(username)

#type password
pwXpath = '/html/body/section[1]/article[2]/div/div/form/div[1]/div/div/div[2]/input'
pwBox = driver.find_element_by_xpath(pwXpath)

pwBox.send_keys(password)


signInXpath = "/html/body/section[1]/article[2]/div/div/form/div[1]/div/div/div[4]/button"
signInButton = driver.find_element_by_xpath(signInXpath)
  
signInButton.click()

#wait for load
time.sleep(5)


firstStudentNameXpath = 	'/html/body/div[4]/div[5]/div[4]/div[2]/div/div[2]/table/tbody/tr[1]/td[2]/a[1]'
firstStudentPerXpath = 		'/html/body/div[4]/div[5]/div[4]/div[2]/div/div[2]/table/tbody/tr[1]/td[3]'
firstStudentLetterXpath = 	'/html/body/div[4]/div[5]/div[4]/div[2]/div/div[2]/table/tbody/tr[1]/td[4]/div/span'
																							#STUDNET INDEX
secondStudentNamXpath = 	'/html/body/div[4]/div[5]/div[4]/div[2]/div/div[2]/table/tbody/tr[2]/td[2]/a[1]'

gradebooksOptionsXpath = '/html/body/div[4]/nav[1]/div/ul/li[2]/a'

onlyOnceGradebookIsSelectedFirstClassXpath = '/html/body/div[4]/nav[1]/div/ul/li[2]/div/ul/li[1]/a'
onlyOnceGradebookIsSelectedSecondClassXpath = '/html/body/div[4]/nav[1]/div/ul/li[2]/div/ul/li[2]/a'