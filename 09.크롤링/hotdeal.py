import requests
import json
from bs4 import BeautifulSoup
import time

KAKAO_TOKEN = "eyJRndotB5stK5ucKuOiAGnj1nNGuydG9HQVNQo9eCMAAAFu61z8aQ"
# 실제로 사용하려면 Refresh Token 을 받아서 써야한다

"""
curl -v -X POST "https://kapi.kakao.com/v2/api/talk/memo/default/send" \
    -H "Authorization: Bearer xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" \
    -d 'template_object={
        "object_type": "text",
        "text": "텍스트 영역입니다. 최대 200자 표시 가능합니다.",
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        },
        "button_title": "바로 확인"
    }'
"""
def send_kakao(text):
    header = {"Authorization": "Bearer " + KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type": "text",
            "text": text,
            "link": {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url": "https://developers.kakao.com"
            },
            "button_title": "바로 확인"
    }
    data = {"template_object": json.dumps(post)}

    r = requests.post(url, headers=header, data=data)

def get_hotdeal(keyword):
    url = "https://slickdeals.net/newsearch.php?page=2&src=SearchBarV2&q={}&searcharea=deals&searchin=first"

    r = requests.get(url.format(keyword))
    bs = BeautifulSoup(r.text, "lxml")
    rows = bs.select("div.resultRow")

    results = []

    for r in rows:
        link = r.select("a.dealTitle")[0]
        href = link.get('href') # href 가 없을 수도 있으니...get 으로 꺼냈을때 없으면 에러는 안나고 None이 된다
        if href is None:
            continue
        href = "http://slickdeals.net" + href
        title = link.text

        price = r.select("span.price")[0].text.replace("$", "").replace("Free", "").strip()
        if price.find("/") >= 0 or price == "":
            continue
        price = float(price)
        hot = len(r.select("span.icon-fire"))
        results.append((title, href, price, hot))
    return results


send_list = []


def main():
    keyword = "ipad"
    max_price = 200.0

    while True:
        results = get_hotdeal(keyword)
        if results is not None:
            for result in results:
                title, href, price, hot = result
                if send_list.count(title) > 0:
                    continue
                if price < max_price:
                    msg = "{} {} {} {}".format(title, price, hot, href)
                    send_kakao(msg)
                    send_list.append(title)
        time.sleep(60 * 5)

        
main()
