import requests
from bs4 import BeautifulSoup

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'cookie': 'session-id=137-6421210-9596741; session-id-time=2082787201l; i18n-prefs=USD; lc-main=en_US; sp-cdn="L5Z9:PK"; ubid-main=134-0830044-7014519; session-token=V1n4n1z4zLaZJVJKehT75pxeiB564vAM9MiaYzDjDIXBVhSkbmbXbOUTvvXU6Fk3Bpo0KowescJ338rzIUAMKElDhRkGi/FXFOkuovm/TmOyqDePhMMc9lIZS9MUyMZ8lisEO6fcZhjzsD3PIjLMYBqQRC2ZQXVUruFnRALEE0A+izBnGWR9uLKBKMxPaD3b; skin=noskin; csm-hit=tb:0FCJ5B5Z8KPR3G148CVD+s-77A6FMJR2Y8CTKJ06ZNN|1633708931030&t:1633708931030&adb:adblk_no',
    'downlink': '1',
    'ect': '3g',
    'referer': 'https://www.amazon.com/',
    'rtt': '300',

    'sec-ch-ua-mobile': '?0',
    'psec-ch-ua-platform': 'Windows',

    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Safari/537.36'}
for x in range(1,3):
    url = f'https://www.amazon.com/s?k=hpspectrex360+15t&page={x}&crid=2A0YW6DH3L0GK&qid=1633779821&sprefix=hpspectre%2Caps%2C897&ref=sr_pg_{x}'
    html_text = requests.get(url, headers=headers).text
    soup = BeautifulSoup(html_text, 'html.parser')
    products = soup.findAll('div',{'class':'s-result-item s-asin sg-col-0-of-12 sg-col-16-of-20 sg-col s-widget-spacing-small sg-col-12-of-16'})
    for item in products:
        links_1 = item.findAll('h2',{'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'})
        #print(links_1)
        list_1 = []
        for item_links in links_1:
            links = item_links.find('a')['href']
            v='https://www.amazon.com'+links
            print(v)
            html_text_1 = requests.get(v, headers=headers).text
            soup_1 = BeautifulSoup(html_text_1, 'html.parser')
            products_name = soup_1.find('span', {'id': 'productTitle'}).text
            try:
                products_price = soup_1.find('span', {'id': 'priceblock_ourprice'}).text
                #print(products_price)
                list_1.append(products_price)
            except:
                no_price =("None")
                list_1.append(no_price)

            list_1.append(products_name)
            list_1 = list(map(lambda a:a.strip(), list_1))

            print("Names/Specs :", list_1[1])
            print("prices :", list_1[0])

            img_2 = soup_1.find('div', {'class': 'imgTagWrapper'})
            img2_link = img_2.find('img')['src']
            list_1.append(img2_link)
            print("Image :",img2_link)
            print("                                        !!! -------------------------------------------------- !!!                                            "                                  )