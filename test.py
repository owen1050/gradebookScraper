# import web driver
from scrapeAllGrades import GradeScraper

username = "buslero@villawalsh.org"
#read password from file so its not on github
f = open("password", "r")
password = f.read()
f.close()

url = "https://gb5.plusportals.com/login/loginView?qstr=JQwDzcIrLUDwAbJIIqftfpnaY2o/4a2YbuA6r0VqlTIEtEQ6R19uOLvbazYgIpUH"

gs = GradeScraper(url, username, password)

grades = gs.getAllGrades([1,2,3,4], headless=False, printUpdates=False)
print(grades)
