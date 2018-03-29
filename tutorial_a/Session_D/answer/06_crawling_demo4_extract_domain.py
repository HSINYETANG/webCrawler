import requests
import re

from bs4 import BeautifulSoup
from urllib.parse import urljoin
from urllib.parse import urlparse
from tldextract import extract

wait_list = ['https://afuntw.github.io/demo-crawling/demo-page/ex4/index1.html']
viewed_list = []
h2_answer = []

# 當 wait list 裏面還有網址發生的情況
while wait_list != []:

    # 取出 wait list 裏面的第一個網址
    url = wait_list.pop(0)
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    print('Current website: {}'.format(url))

    # 將當前頁面存入已經看過的清單
    viewed_list.append(url)

    # 取得當前頁面中的 h2 tag 並將結果存入 h2_answer
    h2 = soup.find_all('h2')
    for tag in h2:
        h2_answer.append(tag.text)

    # 取得頁面中的 a tag
    links = soup.find_all('a', href=True)
    for link in links:

        new_url = urljoin(url, link['href'])

        # 過濾錨點, 不需要再對相同的網頁送 request
        check_anchor = not re.match('#.*', link['href'])

        # 過濾程式碼
        check_code = not re.match('^javascript.*', link['href'])

        # 過濾協定, 只取 http 或是 https
        # Hint: 若原本 href 是相對路徑則沒有協定, 要先透過 urljoin 取得絕對路徑
        check_protocol = urlparse(new_url).scheme in ['http', 'https']

        # 實際過濾的判斷式
        if check_anchor and check_code and check_protocol:

            # 對當前 url 與新的 url 做 extract 分析網域
            root_url = extract(url)
            current_url = extract(new_url)
            print('root_url extract: {}'.format(root_url))
            print('current_url extract: {}'.format(current_url))

            # 檢查 subdomain 是 www 或是與當前頁面的 subdomain 相同
            check_subdomain = current_url.subdomain == 'www' or current_url.subdomain == root_url.subdomain

            # 檢查新的 url 要與當前頁面的 domain 相同, 且符合 subdomain 需求
            if root_url.domain == current_url.domain and check_subdomain:

                # 新的 url 要符合的條件
                # 1. wait_list 裏面沒有出現
                # 2. viewed_list 也沒有出現
                if new_url not in wait_list and new_url not in viewed_list:

                    # 將新發現的超連結存入 wait list
                    wait_list.append(new_url)

    print('Get h2 tags: {}'.format(h2_answer))
    print('URL wait list: {}'.format(wait_list))
    print('URL viewed list: {}'.format(viewed_list))
    print()
