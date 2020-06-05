# 지니뮤직의 1~50 순위 곡들을 스크래핑 하기

import requests
from bs4 import BeautifulSoup

# *여기 밑에서 지니뮤직 사이트 들어가서 검사 창으로 tr들 불러오는 direction 만 바꾸면 될 듯

# URL을 읽어서 HTML를 받아오고,
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
data = requests.get('https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200403&hh=23&rtm=N&pg=1',headers=headers)

# HTML을 BeautifulSoup이라는 라이브러리를 활용해 검색하기 용이한 상태로 만듦
soup = BeautifulSoup(data.text, 'html.parser')

# select를 이용해서, tr들을 불러오기
songs = soup.select('#body-content > div.newest-list > div > table > tbody > tr')
rank = 0
# movies (tr들) 의 반복문을 돌리기
for song in songs:
    # movie 안에 a 가 있으면,
    a_tag = song.select_one('td.info > a.title.ellipsis')
    if a_tag is not None: 
        # print (a_tag.text) #이름만 나오게 (text 부분만 나오게) 하기 ; 속성 부분은 제외하고
        rank = rank + 1 # img 태그의 alt 속성값을 가져오기 #td.ac 대신 td:nth-child(1)을 넣어도 됨  
        title = a_tag.text.strip()                                     # a 태그 사이의 텍스트를 가져오기
        singer = song.select_one('td.info > a.artist.ellipsis').text.strip()
        #별점은 한 항목이므로 _one을 해줘야함 # td 태그 사이의 텍스트를 가져오기
        #그리고 이미 a_tag가 td.title > div > a 으로 명시되어 있으므로 그앞에는 제외하고 하위 항목인 td.point를 써주면 됨
        
        print(rank,title,singer) #프린트할때 한 줄에 쓰여짐 (형식)
    


