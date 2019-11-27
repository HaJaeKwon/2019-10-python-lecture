import pandas as pandas
import requests
from bs4 import BeautifulSoup
import pandas


def get_movie_point(start, end):
    results = []

    for i in range(start, end + 1):

        url = "https://movie.naver.com/movie/board/review/list.nhn?&page={}".format(i)
        r = requests.get(url)
        bs = BeautifulSoup(r.text, "lxml")

        trs = bs.select("table.list_table_1 > tbody > tr")
        for tr in trs:
            tds = tr.select("td")
            if len(tds) != 6:
                continue
            movie = tds[0].select("a")[0].text
            author = tds[2].select("a")[0].text
            point = tds[3].select("div > div > img")[0]["alt"]

            results.append([movie, author, point])

            # results.append({
            #     "movie": movie,
            #     "point": point,
            #     "author": author
            # })

    return results

column = ["영화제목", "평점", "작성자"]
results = get_movie_point(0,10)

dataframe = pandas.DataFrame(data=results, columns=column)
print(dataframe)

dataframe.to_excel("movie.xlsx",
                   sheet_name="네이버영화",
                   header=True,
                   startrow=0)