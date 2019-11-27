import requests
from bs4 import BeautifulSoup


def get_search_naver_blog(query, start_page=1, end_page=None):
    # 11 = 2
    # 21 = 3 = (3-1) * 10 + 1
    start = (start_page - 1) * 10 + 1
    url = "https://search.naver.com/search.naver?where=post&query={}&start={}".format(query, start)
    print(url)
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")

    results = []

    if end_page is None:
        # tot_counts = bs.select("span.title_num")[0].text
        # tot_counts = tot_counts.split("/")[-1]
        # tot_counts.replace("건", "").replace(",", "").strip()
        tot_counts = int(bs.select("span.title_num")[0].text.split("/")[-1].replace("건", "").replace(",", "").strip())
        end_page = tot_counts / 10

        if end_page > 900:
            end_page = 900

    lis = bs.select("li.sh_blog_top")
    for li in lis:
        try:
            title = li.select("dl > dt > a")[0]
            summery = li.select("dl > dd.sh_blog_passage")[0].text
            thumbnail = li.select("img")[0]["src"]      # 예외처리를 해줘야함

            title_link = title["href"]
            title_text = title.text

            results.append((thumbnail, title_text, title_link, summery))
        except:
            continue

    if start_page < end_page:
        start_page += 1
        results.extend(get_search_naver_blog(query, start_page, end_page))

    return results


results = get_search_naver_blog("파이썬강좌", start_page=1, end_page=10)
for result in results:
    print(result)
