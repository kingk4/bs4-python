import requests
from bs4 import BeautifulSoup
import pandas as pd

headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'cookie': 'zguid=23|%2469390d90-86fc-4443-92a6-f625cac66dde; _ga=GA1.2.1634312021.1632749255; zjs_anonymous_id=%2269390d90-86fc-4443-92a6-f625cac66dde%22; _gcl_au=1.1.877263714.1632749257; _pxvid=aefba7dd-1f96-11ec-a2f7-466f686f4b76; __pdst=371ed644ea1e46d99ad931f758b079de; _fbp=fb.1.1632749258795.557920679; __gads=ID=b6000cbd145d1193:T=1632749300:S=ALNI_Mb-ZKzAr5GJO0-MNIL5SR6hQinUpQ; _pin_unauth=dWlkPU4yUXdOakJpWkdZdFpqTXhNQzAwWm1ReExUbGhZVFF0WXpBd05UWTNNVEZpWWpkaw; G_ENABLED_IDPS=google; zjs_user_id=%22X1-ZUslakn5s541e1_2m43c%22; loginmemento=1|e14b97590a935a396340a6a4f1cecc849c97061f15e3b0a321643e56ef023298; userid=X|3|77e4a2d57de5a229%7C10%7CsLDyIUhFGsDtKKdGTD-SnEX76l-MmhAV; zgsession=1|6c0c97ba-acd6-4326-8ac5-e7ba109f5237; ZILLOW_SID=1|AAAAAVVbFRIBVVsVEhoGICJAiiikPb75Uf76xI6xwZf23Qmq9JaTt4MoYPxnvlKYkypskLxyLJuyYg1Fq%2BPpkqoh4RaK; _gid=GA1.2.1401103273.1636831516; KruxPixel=true; DoubleClickSession=true; JSESSIONID=0F4FE74CE5D5A20A1A34DFB264A61259; KruxAddition=true; utag_main=v_id:017c277084350049f83046eacfd805072001706a007e8$_sn:5$_se:1$_ss:1$_st:1636833321370$dc_visit:5$ses_id:1636831521370%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_event:1%3Bexp-session$dc_region:eu-central-1%3Bexp-session$ttd_uuid:313b729e-63e9-4533-848a-39e1da0b60c1%3Bexp-session; _gat=1; _pxff_bsco=1; _px3=7b6dc70706a5fe5532aa0da46233ca639f2c9a43bfb8597f586f8bb87549a146:hSOEDYb18jwfMklTj4iN8lyKk05hwzeHGcs2EieE15qtmd2MbApaNAQXr5yujKLgi6F3Sq9XQ49ZHczbTsPPaQ==:1000:t24T5N2U5yQ5iYrinnnH0L0KL+bNL6N4dlppTzsdYHdjro1ozHexaTRxLVPm7KAzj4/aIVU5c6nCSjqZikOt9SL1GpVCapGxQsjxAqnF1MgrvJqHVbAyKfRNqJ+5xgK9QlX8aOpmfu9U62Je976Ayuidv5wz/rE8BN4Kd2+GHdcZo+jk/uHJOix/6wAarlKUD32Y55rajkIk7C02VQGLEA==; _uetsid=7074833044b711ec8fad377ec567fb67; _uetvid=ae9777001f9611eca0a0470c9c985125; AWSALB=tM/4hY6zI6DMZFQzhDTtbJCdd8WYjay/9TokaVMsKb0+XMtc0UmrrT8JIPPaBVwOnt7VE+vS+FYHxSG1RmiWHupFyLYu/7U2jvgVh+ZHKx3/yWur/Z64AhF7OOG0; AWSALBCORS=tM/4hY6zI6DMZFQzhDTtbJCdd8WYjay/9TokaVMsKb0+XMtc0UmrrT8JIPPaBVwOnt7VE+vS+FYHxSG1RmiWHupFyLYu/7U2jvgVh+ZHKx3/yWur/Z64AhF7OOG0; search=6|1639423789386%7Crect%3D41.07910723423421%252C-73.40735408300782%252C40.33059596702689%252C-74.54855891699219%26rid%3D6181%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Ddays%26z%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%26excludeNullAvailabilityDates%3D0%09%096181%09%09%09%09%09%09',
'referer': 'https://www.zillow.com/',
'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'}
params = {'searchQueryState': '{"pagination":{},"usersSearchTerm":"New York, NY","mapBounds":{"west":-74.54855891699219,"east":-73.40735408300782,"south":40.33059596702689,"north":41.07910723423421},"regionSelection":[{"regionId":6181,"regionType":6}],"isMapVisible":true,"filterState":{"ah":{"value":true}},"isListVisible":true}'}

zillow_list = []
for i in range(10):
    url = f'https://www.zillow.com/new-york-ny/3_p/?searchQueryState=%7B%22pagination%22%3A%7B%22currentPage%22%3A{i}%7D%2C%22usersSearchTerm%22%3A%22New%20York%2C%20NY%22%2C%22mapBounds%22%3A%7B%22west%22%3A-74.78133174414063%2C%22east%22%3A-73.17458125585938%2C%22south%22%3A40.33059596702689%2C%22north%22%3A41.07910723423421%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A6181%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%7D'
    html_text = requests.get(url, headers=headers, params=params).text
    soup = BeautifulSoup(html_text, 'html.parser')
    ul_list = soup.findAll('ul', {'class':'photo-cards_extra-attribution'})
    for li_list in ul_list:
        li = li_list.findAll('li')

        for info in li:
            init = info.findAll('div', {'class':'list-card-info'})
            for inform in init:
                try:
                    prices = inform.find('div',{'class':'list-card-price'}).text
                    link = inform.find('a')['href']
                    main_info = inform.find('ul',{'class':'list-card-details'}).text

                    zillow_dict = {
                        "Price": prices,
                        "Link" : link,
                        "More_info" : main_info

                    }
                    zillow_list.append(zillow_dict)
                except:
                    pass


df = pd.DataFrame(zillow_list)
print(df)
df.to_csv('zillow.csv')

#                                                        "!!!{//csv in pandas reposritory}!!!"
