import requests
from bs4 import BeautifulSoup

url = "https://comic.naver.com/webtoon/weekday.nhn"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

def d() :
    rank = []
    rank.append(soup.find("li",attrs={"class":"rank01"}))
    for l in range(10) :
        rank.append(rank[l].find_next_sibling("li"))
        print(f"{l+1}위 :",rank[l].a.get_text())

while True :
    input1 = input("wef")
    if input1 == "0" :
        print("0dla")
        d()
    if input1 == "1" :
        print("!")