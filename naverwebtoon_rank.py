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

def todayRank() :
    rank = []
    rank.append(soup.find("li",attrs={"class":"rank01"}))
    for l in range(10) :
        rank.append(rank[l].find_next_sibling("li"))
        print(f"{l+1}위 :",rank[l].a.get_text())

def dayRank() :
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


        

while True :

    input1 = input("요일별 순위 보기(1), 오늘 전체 순위 보기(2)\n")

    if input1 == "1" :
        dayRank()
    elif input1 == "2" :
        todayRank()
    else :
        print("1 또는 2 를 눌러주십시오.")
    print("\n\n\n")