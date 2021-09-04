import requests

headers = {"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36"}
res = requests.get("http://nadocoding.tistory.com")
print(res.status_code)

res.raise_for_status()


print("웹스크래핑을 진행합니다")

with open("nadocoding.html", "w", encoding="utf8") as f :
    f.write(res.text)