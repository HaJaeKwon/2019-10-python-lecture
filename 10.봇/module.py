import os
import requests
from bs4 import BeautifulSoup


def get_dir_list(dir):
    str_list = ""
    if os.path.exists(dir):
        file_list = os.listdir(dir)
        file_list.sort()
        for f in file_list:
            full_path = os.path.join(dir, f)
            if os.path.isdir(full_path):
                f = "[" + f + "]"
            str_list += f
            str_list += "\n"
    str_list.strip()
    return str_list

def get_weather(where):
    url = "https://search.naver.com/search.naver?query={}+%EB%82%A0%EC%94%A8"
    r = requests.get(url.format(where))
    bs = BeautifulSoup(r.text, "lxml")

    result = ""

    main_info = bs.select("div.today_area > div.main_info")
    if len(main_info) > 0:
        temperature = bs.select("span.todaytemp")
        cast_text = bs.select("p.cast_txt")
        indicator = bs.select("span.indicator")

        if len(temperature) > 0 and len(cast_text) > 0 and len(indicator) > 0:
            temperature = temperature[0].text.strip()
            cast_text = cast_text[0].text.strip()
            indicator = indicator[0].text.strip()

            result += "{}℃\r\n{}\r\n{}".format(temperature, cast_text, indicator)

    sub_info = bs.select("div.today_area > div.sub_info")
    if len(sub_info) > 0:
        fine_dust = bs.select("dd.lv3 > span.num")
        if len(fine_dust) > 0:
            fine_dust = fine_dust[0].text.strip()
            result += "\r\n미세먼지 : {}".format(fine_dust)

    return result


MONEY_NAME = {
    "달러": "미국 USD",
    "유로": "유렵연합 EUR",
    "엔": "일본 JPY (100엔)",
    "위안": "중국 CNY",
    "홍콩달라": "홍콩 HKD",
    "타이완달라": "대만 TWD",
    "파운드": "영국 GBP"
}


def get_exchange_info():
    url = "https://finance.naver.com/marketindex/exchangeList.nhn"
    r = requests.get(url)
    bs = BeautifulSoup(r.text, "lxml")

    EXCHANGE_INFO = {}

    trs = bs.select("table.tbl_exchange > tbody > tr")
    for tr in trs:
        country = tr.select("td.tit > a")[0].text.strip()
        currency = tr.select("td.sale")[0].text.strip().replace(",", "")
        EXCHANGE_INFO[country] = currency

    return EXCHANGE_INFO


def money_translate(keyword):
    EXCHANGE_INFO = get_exchange_info()
    keywords = []
    for m in MONEY_NAME.keys():
        if m in keyword:
            keywords.append(keyword[0:keyword.find(m)].strip())
            keywords.append(m)
            break
    if len(keywords) > 0:
        country = MONEY_NAME[keywords[1]]

        if country in EXCHANGE_INFO:
            money = float(EXCHANGE_INFO[country])
            if country == "일본 JPY (100엔)":
                money /= 100

            money = format(round(float(money) * float(keywords[0]), 3), ",")
            output = "{} 원".format(money)
            return output


