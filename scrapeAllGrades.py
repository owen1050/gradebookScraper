import requests, time
from lxml import html

url = "https://www.wunderground.com/maps/satellite/regional-infrared/usaec"
xpath = "//*[@id=\"main-page-content\"]/section/div[1]/div[2]/div[2]/img[1]"

response = requests.get(url)

# Parse the HTML content
tree = html.fromstring(response.content)
#print(response.content)

# Find the element using the XPath
element = tree.find_class("map ng-star-inserted")
print(element)
# Extract the 'src' attribute
src = element[0][0].values()

print(src)