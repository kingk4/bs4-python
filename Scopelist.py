import requests
import bs4

from bs4 import BeautifulSoup

url = 'https://www.scopelist.com/'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

main = soup.find_all('li', {'class':'dropdown'})

links_data = []
for link in main:
    links = link.find('a')['href']
    links_data.append(url+links)
#print(links_data)


for i in links_data:
    html_text1 = requests.get(i).text
    soup = BeautifulSoup(html_text1, 'html.parser')
    item1 = soup.findAll('div', {'class':'no-slide'})

    list2 = []
    for products1 in item1:
        #title = products1.find('a')['title']
        product = products1.find('a')['href']
        #stock = products1.find('strong', {'class':'in-stock'}).text
        #price = products1.find('p',{'class':'pro-count'}).text

        #print(title)

        list2.append(url+product)


    for x in list2:
        html_text3 = requests.get(x).text
        soup3 = BeautifulSoup(html_text3, 'html.parser')
        specification = soup3.find('table', {'class': 'table table-striped'}).text
        price = soup3.find('strong', {'class' : 'latest-price'}).text
        name  = soup3.find('span', {'id':'ctl00_MainContentHolder_lblName'}).text
        #rating = soup.find('span',  {'class':'star-rating'})


        print("Product_name :", name),
        print("Price", price),
        print("specification : ", specification)

print("-----------------------------------------------------------------------------------------------------------------------------------------------")


