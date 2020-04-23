import selenium
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from lxml import html
import requests
import credentials #create a file named credentials.py which stores credentials as username = "" and password= ""


browser = webdriver.Chrome("C:\\Users\\Anshul\\Desktop\\Instagram\\chromedriver_win32\\chromedriver.exe") #Chrome WebDriver
browser.maximize_window()
# browser = webdriver.Edge("C:\\Users\\Anshul\\Desktop\\Instagram\\edgedriver_win64\\msedgedriver.exe")   #Edge WebDriver
# time.sleep(1)

link = 'https://instagram.com/' + credentials.username
browser.get("https://www.instagram.com/accounts/login/?hl=en&source=auth_switcher")
time.sleep(1)

username = browser.find_element_by_name('username')
time.sleep(1)
username.send_keys(credentials.username)
time.sleep(1)

password = browser.find_element_by_name('password')
password.send_keys(credentials.password)
password.submit()
time.sleep(4)

target = 'https://www.instagram.com/'+credentials.target+'/'

browser.get(target)
page = requests.get(target)
soup = BeautifulSoup(page.text, "html.parser")
for i in soup.find_all(name="meta", attrs={"property": "og:description"}):
        rawData = i['content'].split()
        
with open ("soup.txt", "w") as file: #saving source code of target's profile to scrape the details.
        file.write(str(soup))

# print(rawData) #details in raw format (list)

followers = rawData[0] + " Followers"
following = rawData[2] + " Following"
posts = rawData[4] + " Posts"
username = rawData[15]

print(username)
print(followers)
print(following)
print(posts)

browser.quit()

