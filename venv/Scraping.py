import requests
import urllib.request
from bs4 import BeautifulSoup
import time
import  xlsxwriter
import csv
import io
from datetime import date
from xml.etree import ElementTree
from lxml import html
import re
from datetime import datetime
from fake_useragent import UserAgent
from urllib.error import HTTPError
from urllib.error import URLError
import threading


if __name__ == '__main__':
    # while True:
    def run_check():
        threading.Timer(55.0, run_check).start()
        ua = UserAgent()
        header = {'user-agent': ua.chrome}
        url = 'https://www.dsebd.org/latest_share_price_scroll_by_change.php'
        try:
            page = requests.get(url, headers=header).text
        except requests.exceptions.RequestException:
            time.sleep(300)
        soup = BeautifulSoup(page, 'lxml')
        time.sleep(15)
        s = soup.findAll('table')[5]
        a = len(s.findAll('table'))
        print(a)
        #
        for i in range(0, a):
            tbl = s.findAll('table')[i].text
            tbl2 = tbl.split(None, 1)[0]
            # print(tbl2, end=",")
            tb = tbl.split(None, 1)[1]
            # print(tb)
            tbl3 = tb.split(None, 1)[0]
            # print(tbl3)
            tbl4 = tb.split(None, 1)[1]
            tbl5 = tbl4.split(None, 1)[0]
            # print(tbl5)
            tbl6 = tbl4.split(None, 1)[1]
            # print(tbl6)
            final_data = [[],
                          [datetime.now(), tbl2, tbl3, tbl5, tbl6]]
            myfile = open('F:\data_saving\Sunday21-7-19.csv', 'a+', newline='')
            with myfile:
                writer = csv.writer(myfile)
                writer.writerows(final_data)

    # time.sleep(40)
    run_check()