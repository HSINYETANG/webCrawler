import os
import sys
import requests
from bs4 import BeautifulSoup
from selenium import webdriver

# 對範例網站送出 request 並把回應的網頁內容送到解析器
url = 'https://afuntw.github.io/demo-crawling/demo-page/ex4/index1.html'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

# 搜尋 id 是 first 的 h2 tag
h2 = soup.find_all('h2', id="first")
print('static get:', h2[0].text)



# Selenium
# 打開 Chrome 瀏覽器
# Linux/ Windows/ MAC
if sys.platform == 'linux':
    driver = webdriver.Chrome(os.path.abspath('../webdriver/linux/chromedriver'))
elif sys.platform == 'win32':
    driver = webdriver.Chrome(os.path.abspath('../webdriver/windows/chromedriver.exe'))
elif sys.platform == 'darwin':
    driver = webdriver.Chrome(os.path.abspath('../webdriver/mac/chromedriver'))

# 將瀏覽器視窗最大化


# 對目標網站送 request


# 搜尋 id 是 first 的 h2 tag
selenium_h2 = 
print('selenium get: ', )

# 關掉瀏覽器
driver.quit()
