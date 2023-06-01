import requests
from bs4 import BeautifulSoup
import json

# Set up the necessary variables
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"  # KakaoTalk API endpoint
admin_key = "a82294170899393972cc8005d7369926"  # KakaoTalk Admin key
chat_link = "https://open.kakao.com/o/gAMek9lf"  # KakaoTalk chat link

# Function to send a message using KakaoTalk API
def send_kakao_message(text):
    headers = {
        "Authorization": f"KakaoAK {admin_key}",
        "Content-Type": "application/x-www-form-urlencoded;charset=utf-8"
    }
    data = {
        "template_object": json.dumps({
            "object_type": "text",
            "text": text,
            "link": {
                "web_url": chat_link
            }
        })
    }
    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        print("Message sent successfully!")
    else:
        print("Failed to send message.")

# Get the notices from the website
res = requests.get("https://dtsc.dongduk.ac.kr/bbs_shop/list.htm?board_code=board3")
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")

# Find the notice elements
notice_list = soup.select("ul.board_list li")

# Load the last checked notice from a file
try:
    with open("last_notice.txt", "r") as file:
        last_notice = file.read().strip()
except FileNotFoundError:
    last_notice = ""

# Check each notice and send to KakaoTalk chat if it's a new notice
for notice in notice_list:
    title = notice.select_one("a.list_tit").get_text().strip()
    link = notice.select_one("a.list_tit")["href"]
    notice_url = f"https://dtsc.dongduk.ac.kr{link}"
    message = f"공지사항: {title}\n링크: {notice_url}"
    
    # Check if it's a new notice by comparing with the last checked notice
    if title != last_notice:
        send_kakao_message(message)
        print(f"Sent message: {message}")