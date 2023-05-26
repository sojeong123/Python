import time
import requests
from bs4 import BeautifulSoup
from pykakao import KakaoTalk

# 카카오톡 봇 설정
KAKAO_EMAIL = 'betty1367@naver.com'
KAKAO_PASSWORD = 'sj4032515!'
ROOM_ID = 'gAMek9lf'

# 대상 웹페이지 URL
TARGET_URL = 'https://dtsc.dongduk.ac.kr/bbs_shop/list.htm?board_code=board3'

# 최종 발송할 메시지 변수
message = ''

# 이전에 발송한 공지사항 저장 변수
last_notice = ''

def send_kakao_message(content):
    # 카카오톡 로그인
    kakao = KakaoTalk()
    kakao.login(email=KAKAO_EMAIL, password=KAKAO_PASSWORD)

    # 카카오톡 메시지 발송
    kakao.send_text(room=ROOM_ID, content=content)

def scrape_website():
    global last_notice

    # 웹페이지 요청
    response = requests.get(TARGET_URL)
    soup = BeautifulSoup(response.text, 'html.parser')

    # 공지사항 가져오기
    notices = soup.select('.tbl_board tbody tr')
    for notice in notices:
        title = notice.select_one('td:nth-child(2)').text.strip()
        link = notice.select_one('td:nth-child(2) a')['href']

        # 가장 최신 공지사항만 체크
        if title != last_notice:
            message = f'{title}\n{link}'
            send_kakao_message(message)
            last_notice = title
            break

while True:
    scrape_website()
    time.sleep(900)  # 15분(900초) 간격으로 스크래핑 수행