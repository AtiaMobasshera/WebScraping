import requests
import urllib.request
from bs4 import BeautifulSoup
import time
import  xlsxwriter
import csv
import io
from datetime import date

class Scraping:
    website_url = requests.get('https://www.dsebd.org/latest_share_price_scroll_l.php').text
    soup = BeautifulSoup(website_url, 'lxml')
    # [tag['href'] for tag in soup.find_all('a', {'class': "a37 ga_tracking"})]  #for getting href
    # table =  soup.find_all('a', {'class':"ab1"})
    # for i in table:
    #  print(i.text)#get the text only


    # a = soup.find("td", text="TRADING CODE").find_next_sibling("td").text
    # a = soup.find("td", text="TRADING CODE").find("table")
    tbl = soup.findAll('table')[5].text
    

    print(tbl)


    # for table in root.xpath('/html/body/table[1]/tbody/tr[4]/td[1]')
     #get the text only


     # with io.open("Debenture", mode='a', encoding='utf-8') as f:
         # with io.open(str(date.today()+'%s.txt'%(link)), mode='w', encoding='utf-8') as f:
         # f.write("%s\n" %(i))
     # today = date.today()
    # print(today)


    # rows = table_body.findall('tr')
    # for row in rows:
    #     cols = row.findall('td')
    #     cols = [x.text.strip() for x in cols]
    #     print(cols)
    #
    #
    # for link in car_type_link:
    #     def carDetails(link):
    #         website_url = requests.get('http://carinfo.findlocality.com' + link).text
    #         soup = BeautifulSoup(website_url, 'lxml')
    #         car_title = soup.findAll('div',{'class':'title'})
    #         car_title = car_title.text.replace(" ","")
    #         car_specification  = soup.find('div',{'class':'specification'})
    #         image_tags = soup.findAll('img')
    #         for image_tag in image_tags:
    #              image_link = ("http://carinfo.findlocality.com"+ image_tag.get('src'))
    #              print(image_link)
    #         print(car_title)
    #         print(car_specification)
    #
    #
    #     time.sleep(1)
    #     carDetails(link)




if __name__ == '__main__':
    Scraping()
