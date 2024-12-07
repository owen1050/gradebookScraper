# import web driver
from scrapeAllGrades import GradeScraper


url = "https://www.wunderground.com/maps/satellite/regional-infrared/usaec"

gs = GradeScraper(url)

grades = gs.getUrl()
print(grades)
