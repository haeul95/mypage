# 순위 곡정보 가수 이름 나타내기

import requests
from bs4 import BeautifulSoup

# '웹에 접속 하는 친구 requests , 솎아내는 친구 beautifulsoup


headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=M&rtm=N&ymd=20210701',headers=headers)

soup = BeautifulSoup(data.text, 'html.parser')


#body-content > div.newest-list > div > table > tbody > tr:nth-child(1) > td.info > a.artist.ellipsis

trs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')

for tr in trs:
    title=tr.select_one('td.info > a.title.ellipsis').text.strip()
    rank = tr.select_one('td.number').text[0:2]
    artist= tr.select_one(' td.info > a.artist.ellipsis').text

    print(rank, title, artist)
