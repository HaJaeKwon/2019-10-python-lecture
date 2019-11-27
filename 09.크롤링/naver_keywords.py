import requests
from bs4 import BeautifulSoup
import time


# lxml 이 20퍼센트 가량 빠르다

def time_function(f):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = f(*args, **kwargs)
        end_time = time.time() - start_time
        print("{} {} time {}".format(f.__name__, args[1], end_time))
        return result
    return wrapper


@time_function
def r_find_all(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    lists = bs.find_all("li", {"class": "ah_item"})

    titles = []
    for li in lists:
        title = li.find("span", {"class": "ah_k"}).text
        titles.append(title)
    return titles


@time_function
def r_select(url, parser):
    r = requests.get(url)
    bs = BeautifulSoup(r.text, parser)
    lists = bs.select("li.ah_item")

    titles = []
    for li in lists:
        title = li.select("span.ah_k")[0].text
        titles.append(title)
    return titles


url = "https://www.naver.com"
r_find_all(url, "html.parser")
r_select(url, "html.parser")

r_find_all(url, "lxml")
r_select(url, "lxml")
#
# r = requests.get("https://www.naver.com")
# # bs = BeautifulSoup(r.text, "html.parser")
# bs = BeautifulSoup(r.text, "lxml")
#
# # lists = bs.find_all("li", {"class": "ah_item"})
# #
# # for li in lists:
# #     # print(li)
# #     title = li.find("span", {"class": "ah_k"}).text
# #     print(title)
#
# lists = bs.select("li.ah_item")
# for li in lists:
#     title = li.select("span.ah_k")[0].text      # select 는 항상 list 형태를 리턴
#     print(title)

