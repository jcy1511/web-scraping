import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")


def day(day) :
    days = soup.find("h4", attrs={"class":day}).parent.find_all("a",{"class":"title"})
    for i in range(len(days)) :
        print(f"{i+1}위 :",days[i].get_text())




for k in ["mon","tue","wed","thu","fri","sat","sun"] :

    if k=="mon" :
        print("<월요일 웹툰 순위>")
    elif k=="tue" :
        print("<화요일 웹툰 순위>")
    elif k=="wed" :
        print("<수요일 웹툰 순위>")
    elif k=="thu" :
        print("<목요일 웹툰 순위>")
    elif k=="fri" :
        print("<금요일 웹툰 순위>")
    elif k=="sat" :
        print("<토요일 웹툰 순위>")
    elif k=="sun" :
        print("<일요일 웹툰 순위>")
    
    day(k)
    print("""
------------------------
    """)


