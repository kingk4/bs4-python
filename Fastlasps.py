import requests
import bs4

from bs4 import BeautifulSoup

url = 'https://fastestlaps.com/makes'
html_text = requests.get(url).text
soup = BeautifulSoup(html_text, 'html.parser')

tag = soup.findAll('div', {'class': 'col-xs-6'})

urls_list = []
for ul in tag:
    ul_lists = ul.findAll('ul')

    for li_lists in ul_lists:
        llist = li_lists.findAll('li')

        for links in llist:
            link = links.find('a')['href']
            urls_list.append('https://fastestlaps.com' + link)

# print(urls_list)

for x in urls_list:
    html_text_1 = requests.get(x).text
    soup_1 = BeautifulSoup(html_text_1, 'html.parser')

    tag_1 = soup_1.findAll('div', {'class': 'col-xs-6'})

    urls_list_1 = []
    for uls in tag_1:
        uls_lists = uls.findAll('ul')

        for lis_lists in uls_lists:
            llists = lis_lists.findAll('li')

            for llinkk in llists:
                llinks = llinkk.find('a')['href']
                # print('https://fastestlaps.com'+llinks)
                urls_list_1.append('https://fastestlaps.com' + llinks)

    # print(urls_list_1)

    for y in urls_list_1:
        html_text_2 = requests.get(y).text
        soup = BeautifulSoup(html_text_2, 'html.parser')

        info = soup.find('div', {'class': 'col-sm-6'})
        car_name = info.find('h1', {'class': 'margin-top'}).text
        print("Car_name :", car_name)

        img = info.find('img')['src']
        print(img)

        tables = soup.findAll('table', {'class': 'table fl-datasheet'})
        for tr in tables:
            table = tr.findAll('tr')

            list1 = []
            for td in table:
                td1 = td.findAll('td')
                for data in td1:
                    v = data.text
                    list1.append(v)

                    list1 = list(map(lambda a: a.strip(), list1))
            print(list1)
            for jj in list1:
                print(jj)
        print("------------------------------------------------------------------------------------")
        print("------------------------------------------------------------------------------------")