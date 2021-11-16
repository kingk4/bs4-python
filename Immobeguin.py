import pandas as pd
import requests
from bs4 import BeautifulSoup
import pandas

main_list = []
property_list = []
for x in range(1,10):
    url = f'https://www.immobeguin.be/nl/recentste-aanbod?view=list&page={x}&view=list'
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')
    pages = soup.findAll('div', {'class':'property-list items_4'})
    #print(pages)
    for datas in pages:
        data = datas.findAll('div', {'class':'span3 property'})
        #print(data)
        for info in data:
            links = info.find('a')['href']
            properlinks = 'https://www.immobeguin.be'+links
            property_list.append(properlinks)

        data = datas.findAll('div', {'class': 'span3 property last'})
        # print(data)
        for info_1 in data:
            links_1 = info_1.find('a')['href']
            properlinks_1 = 'https://www.immobeguin.be' + links_1
            property_list.append(properlinks_1)

#for i in property_list:
#    print(i)
for i in property_list:
    html_text_1 = requests.get(i).text
    soup_1 = BeautifulSoup(html_text_1, 'html.parser')
    name = soup_1.find('h3', {'class': 'pull-left leftside'}).text
    price = soup_1.find('h3', {'class': 'pull-right rightside'}).text

    more_info = soup_1.find('div', {'class': 'group'}).text

    property_dict = {
        "Name": name,
        "Price": price,
        "Link": i
    }
    main_list.append(property_dict)
    #print(property_dict)

df = pd.DataFrame(main_list)
df.to_csv('Property_csv')
