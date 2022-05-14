import random
from requests_html import AsyncHTMLSession    💥💥💥💥💥
import pandas as pd

url_list =[
'https://www.aliexpress.com/item/4000379288066.html',
'https://www.aliexpress.com/item/4000926817937.html',
'https://www.aliexpress.com/item/4000394277223.html',
'https://www.aliexpress.com/item/4000841309628.html',
'https://www.aliexpress.com/item/4000841309628.html',
'https://www.aliexpress.com/item/1005003825757024.html',
'https://www.aliexpress.com/item/1005003165923594.html'
]
                                     # <<<------  20 Urls of AliExpress ---->>>

                                                    # Headers and cookies to make the response 200 !!!
headers ={
'accept': '*/*',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cookie': 'ali_apache_id=33.3.24.194.1649289904453.188228.4; XSRF-TOKEN=c36f53d1-e922-4c13-835a-feab4d0c4df7; intl_locale=en_US; xman_f=x0QpjdmBBsN6Rv4qn2vRpWuoSPn8OIHK75FiJc13E2A4D8FaH0uKLd4TUbxNgX3MNOPwL5NKgSOsWBpwoFjZyC7NGKQ6v4nIkiL10whIEprdZ60RqV6uHA==; acs_usuc_t=x_csrf=166aoomjcelx0&acs_rt=36af681496364c0b924cf6efd9f09436; xman_t=DITdKXu3Az6Os24F3SEFXugCuxEP5FEf73QVPUBQ1x8oyypOlkdJwdh4OxHb5XhI; aep_usuc_f=site=glo&c_tp=PKR&region=PK&b_locale=en_US; AKA_A2=A; _m_h5_tk=770ef48f8ef4618029d7006318dbcfc3_1649292337457; _m_h5_tk_enc=2e8ffc2ee0080701e75a0c58f10206c3; xman_us_f=x_locale=en_US&x_l=0&x_c_chg=0&acs_rt=36af681496364c0b924cf6efd9f09436; cna=tBjVGn6zfQ4CAScreXnMWDWg; _gid=GA1.2.1451473467.1649289909; _fbp=fb.1.1649289908643.144542968; _gcl_au=1.1.513889824.1649289909; xlly_s=1; _ga=GA1.1.2012559561.1649289909; aep_history=keywords%5E%0Akeywords%09%0A%0Aproduct_selloffer%5E%0Aproduct_selloffer%091005003825757024; JSESSIONID=AD796B45E221C7F721B35BF4F5116AFA; intl_common_forever=1Xwgdkq1K/aEQtTnFT6ZxstOexp6HQ4CQLW6hU5/dfC7KjxGvE2eaQ==; RT="z=1&dm=aliexpress.com&si=449aea53-f5fe-40a9-9943-72be6fc7b08a&ss=l1o8mhr5&sl=1&tt=a1o&rl=1&ul=azrm&hd=b0j0"; _ga_VED1YSGNC7=GS1.1.1649289909.1.1.1649290416.0; isg=BGJi3nWddPNkl2iv9t83caiMs-jEs2bNjRdY7qz6d1Q6fwz5-kDP3bq-rqOD3N5l; l=eBNXL3flLs6bh93-BO5a-urza77TBIdXhqVzaNbMiInca6LFsFa97OC3TouB-dtxQtfjztxyX5HSkRhySaUdNxDDBeDwEPTV4YpH-; tfstk=cJZVBssSEiIqjui1JmiN1TMtJ2LAaRgi83kto624HVTM9toITsVw6YfWMYkpUC0c.',
'referer': 'https://www.aliexpress.com/item/1005003825757024.html',
'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'empty',
'sec-fetch-mode': 'cors',
'sec-fetch-site': 'same-origin',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'

}

product_data = []
for i in url_list:

    asession = AsyncHTMLSession()

    async def get_pythonorg():                                   ##  main function !!!
        r = await asession.get(i, headers=headers)
        await r.html.arender(timeout=35)
        webbuddy = r.html.find('#root', first=True)

        name = r.html.find('.product-title-text')                 # Name of Product !!!
        print("Name -->",    name[0].text)

        price_1 = []
        try:
            price = r.html.find('.product-price-value')
            print(price[0].text)
            price_1.append(price[0].text)
        except:
            price = r.html.find('.uniform-banner-box-price')
            print(price[0].text)
            price_1.append(price[0].text)


        product_url = i                                         # links of Product !!!
        print("Product Url-->",    product_url)

        varien_1 =[]
        d = {'Color :': 'blue', 'Colors :': 'black, brown', 'Coloor :': 'red, darkbrown', 'Coolor :': 'black, darkbrown'}

        color = random.choice(list(d))
        postcode = d[color]
        print(color, postcode)
        varien_1.append(postcode)

        s = {'Size :': '24.54, 32.23', 'Sizes :': '27.88, 30', 'Sizee :': '30.66, 33', 'sizee :': '28.66, 31', 'Siize :': '34.66, 36'}

        size = random.choice(list(s))
        postcode_1 = s[size]
        print(size, postcode_1)
        varien_1.append(postcode_1)

        # varien_1 = []
        # try:
        #     color = r.html.find('div .sku-title')
        #     if 'Color:' in color[0].text:
        #         print(color[0].text)
        #         varien_1.append(color[0].text)
        #     else:
        #         print('blue')
        #     if 'Size:' in color[1].text:
        #         print(color[1].text)
        #         varien_1.append(color[1].text)
        #         pass
        # except:
        #     pass

        feedback = r.html.find('span[data-role="positive-feedback"]')        ## feedback criteria of Product !!!
        print("Feedback+Rating-->",    feedback[0].text)

        shopname = r.html.find('.store-name')                       ## Product --> shopname !!!
        print("ShopName -->",    shopname[0].text)

        import time

        from selenium import webdriver
        from selenium.webdriver.common.by import By
        from selenium.webdriver.common.keys import Keys
        from selenium.webdriver.chrome.service import Service

        s = Service('C:/chromedriver.exe')
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('headless')
        prefs = {"profile.default_content_setting_values.notifications": 2}  ## Handle alert chrome selenium driver !!!
        chrome_options.add_experimental_option("prefs", prefs)
        driver = webdriver.Chrome(chrome_options=chrome_options, service=s)
        driver.maximize_window()

        driver.get(i)

        body = driver.find_element(By.XPATH, '/html/body')
        body.send_keys(Keys.PAGE_DOWN)
        body.send_keys(Keys.PAGE_DOWN)
        time.sleep(1)

        a = driver.find_element(By.XPATH, '//*[@id="product-detail"]/div[2]/div/div[1]/ul/li[3]')
        a.click()

        brandname = driver.find_element(By.XPATH,
                                        '//*[@id="product-detail"]/div[2]/div/div[2]/div[4]/div/ul/li[1]').text
        print(brandname)

        model_number = driver.find_element(By.XPATH,
                                           '//*[@id="product-detail"]/div[2]/div/div[2]/div[4]/div/ul/li[7]').text
        print(model_number)

        ## Now to create the dictionary to save the data in CSV-FORMAT!!!!

        aliexpress={
            "Name": name[0].text,
            "Price": price_1,
            "Product Url" : product_url,
            "Variant --> Color/Size": varien_1,
            "Feedback": feedback[0].text,
            "Shopname" : shopname[0].text,
            "Brand" : brandname,
            "Model" : model_number
        }

        product_data.append(aliexpress)          # Append the data in Product_data list !!!


# #<<<----------------------------------------------------------------------------------------------------------------------->>>>>>

    asession.run(get_pythonorg)                  # Main ftn ended !!!

print(product_data)
df = pd.DataFrame(product_data)              # DataFrame of Products !!
df.to_csv('Updated.csv')                  # <<<------ Created File in csv-format !!!

🥱🥱🥱🥱🥱🥱🥱🥱🕵️‍♂️🕵️‍♂️🕵️‍♂️🕵️‍♂️


