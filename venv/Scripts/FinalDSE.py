import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
from lxml import html
import io
from xml.etree import ElementTree
import time
from datetime import datetime
import csv
import schedule
from urllib.error import HTTPError
from urllib.error import URLError
# class FinalDSE:







if __name__ == '__main__':

    while True:
        def URL(url):
            ua = UserAgent()
            header = {'user-agent': ua.chrome}
            try:
                page = requests.get(url, headers=header).text
            except requests.exceptions.RequestException:
                time.sleep(300)
            soup = BeautifulSoup(page, 'lxml')
            return soup


        site_url = URL('https://www.dsebd.org/latest_share_price_scroll_by_change.php')
        for i in range(6,349):
            table = site_url.findAll('table')[5].text

            company_name = table.split(None, 1)[0]
            # print(company_name, end=",")
            table_data = table.split(None, 1)[1]
            # print(table_data)
            last_trading_price = table_data.split(None, 1)[0]
            # print(tbl3)
            changes = table_data.split(None, 1)[1]
            change = changes.split(None, 1)[0]
            # print(tbl5)
            percentage_change = changes.split(None, 1)[1]
            # print(tbl6)

            final_data = [[],
                          [datetime.now(), company_name, last_trading_price, change, percentage_change]]
            myfile = open('data4.csv', 'a+', newline='')
            with myfile:
                writer = csv.writer(myfile)
                writer.writerows(final_data)

    time.sleep(60)
