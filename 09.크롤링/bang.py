import requests
from bs4 import BeautifulSoup
import json
import pprint


def get_bang(query):
    url = "https://apis.zigbang.com/search?q={}".format(query)
    r = requests.get(url)
    result = json.loads(r.text) # json 을 그냥 출력하면 공백, 인덴트로 구분되지 않아 가독성이 떨어짐

    if result["success"]:
        lat = result["items"][0]["lat"]
        lng = result["items"][0]["lng"]

    # 직방 API가 강의에 나오는 것과 버전이 다름

    url = "https://apis.zigbang.com/v2/aparts/items?{}_in={}&domain=zigbang&geohash=wydmd&sales_type_in={}".format("거래구분", "매매", "매매")
    r = requests.get(url)
    result = json.loads(r.text)

    itemIds = []
    for item in result["items"]:
        if len(item["itemIds"]) > 0:
            itemIds.extend(item["itemIds"])

    url = "https://apis.zigbang.com/v2/items/list"
    data = {
        "domain": "zigbang",
        "item_ids": itemIds,
        "withCoalition": True
    }
    r = requests.post(url, json=data)
    result = json.loads(r.text)

    bang_list = []

    for i in result["items"]:
        title = i["title"]
        addr = i["address"]
        addr1 = i["address1"]
        addr2 = i["address2"]
        addr3 = i["address3"]
        deposit = i["deposit"]
        rent = i["rent"]
        size1 = i["공급면적"]
        size2 = i["전용면적"]
        bang_list.append((title, addr, addr1, addr2, addr3, deposit, rent, size1, size2))

    return bang_list


for i in get_bang("서울시 종로구"):
    print(i)



