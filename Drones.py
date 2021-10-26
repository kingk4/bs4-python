import requests
from bs4 import BeautifulSoup
import pandas as pd

products_list = []
url = 'https://www.jessops.com/drones'
header={'Referer': 'https://www.jessops.com/drones ' ,
'Upgrade-Insecure-Requests': '1' ,
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}
html_text = requests.get(url, headers=header).text
soup = BeautifulSoup(html_text, 'html.parser')
page_data = soup.find('ul', {'class':'main-nav-links'})
li_list = page_data.findAll('li', {'class':'has-menu'})
#print(len(li_list))
main_list = []
list =[]
for links in li_list:
    link = links.find('a')['href']
    links_1=('https://www.jessops.com'+link)
    if links_1 not in list:
        list.append(links_1)
list.remove('https://www.jessops.com#')
#print(list)
count = 0
for i in list:
    count = count+1
    if count < 8:
        pass
        #print(i)
        html_text_2 = requests.get(i, headers=header).text
        soup_1 = BeautifulSoup(html_text_2, 'html.parser')
        data = soup_1.findAll('div', {'class': 'details-pricing'})
        for data_2 in data:
            product_link = data_2.find('a')['href']
            product_name = data_2.find('a').text
            price = data_2.find('p', {'class': 'price larger'}).text
            discription = data_2.find('ul', {'class': 'f-list j-list'}).text
            products_dict = {
                "Product Name": product_name,
                "Product Price": price,
                "Product Discription": discription,
                "Product link": product_link
            }
            #print(products_dict)
            products_list.append(products_dict)
#print(products_list)
df = pd.DataFrame(products_list)
print(df)
df.to_csv('Drones.csv')

### csv format in pandas-python section    !!! Drones.csv
