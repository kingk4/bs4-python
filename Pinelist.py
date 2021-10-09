import requests
import bs4

from bs4 import BeautifulSoup

for x in range(10):
    url = f'https://www.thepinnaclelist.com/design/type/homes/page/{x}/'
    html_text = requests.get(url).text

    soup = BeautifulSoup(html_text, 'html.parser')

    homes = soup.findAll('li', {'class': 'gridplex-metro-48-item'})

    list = []
    for links in homes:
        link = links.find('a')['href']
        list.append(link)

    for i in list:
        html_text1 = requests.get(i).text
        soup = BeautifulSoup(html_text1, 'html.parser')

        entry = soup.find('div', {'class': 'entry-content'})
        name = soup.find('h1', {'class': 'entry-title'}).text
        more_info = entry.find('ul').text
        dis = entry.find('p').text
        print("Title :", name)
        print("Information :", more_info)
        print("Discription :", dis)

        img = soup.find('div', {'class': 'mosaic-content'})
        img_link = img.find('a')['href']
        print(img_link)
        print("---------------------")
