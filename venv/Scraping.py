import requests
import urllib.request
from bs4 import BeautifulSoup
import time

class Scraping:
    website_url = requests.get('http://carinfo.findlocality.com/find-a-car/honda/vezel').text
    soup = BeautifulSoup(website_url, 'lxml')
    car_type = soup.find('div',{'class':'year-package'})
    car_type_link =[a['href'] for a in car_type.find_all('a')]
    for link in car_type_link:
        def carDetails(link):
            website_url = requests.get('http://carinfo.findlocality.com' + link).text
            soup = BeautifulSoup(website_url, 'lxml')
            car_title = soup.find('div',{'class':'title'})
            car_title = car_title.text.replace(" ","")
            car_specification  = soup.find('div',{'class':'specification'})
            image_tags = soup.findAll('img')
            for image_tag in image_tags:
                image_link = ("http://carinfo.findlocality.com"+ image_tag.get('src'))
                print(image_link)
            print(car_title)
            print(car_specification)

        time.sleep(1)
        carDetails(link)





if __name__ == '__main__':
    Scraping()