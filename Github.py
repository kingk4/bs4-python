import requests
from bs4 import BeautifulSoup
import pandas as pd

headers={'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
'accept-encoding': 'gzip, deflate, br',
'accept-language': 'en-US,en;q=0.9',
'cache-control': 'max-age=0',
'cookie': '_octo=GH1.1.881622094.1633366957; _device_id=c10bb2de5136015737d6014fa138a559; user_session=A2JIM108M1Smfa8pkY2aXOdlUsSSN0-qMH6QA9dxoXlDThrb; __Host-user_session_same_site=A2JIM108M1Smfa8pkY2aXOdlUsSSN0-qMH6QA9dxoXlDThrb; logged_in=yes; dotcom_user=kingk4; has_recent_activity=1; color_mode=%7B%22color_mode%22%3A%22auto%22%2C%22light_theme%22%3A%7B%22name%22%3A%22light%22%2C%22color_mode%22%3A%22light%22%7D%2C%22dark_theme%22%3A%7B%22name%22%3A%22dark%22%2C%22color_mode%22%3A%22dark%22%7D%7D; tz=Asia%2FKarachi; _gh_sess=Q4YA%2BHFxhdEHFRm3wBNAT7854RHfh41pRaLaFPfZJV5h1EYrmKBqLP6fCLVtnKVtCbPv33JXIrRDvK79k2xunWJ%2F5EBLUdzVvfmh%2FJD%2FnKUUCLShtMaBD1IXb3dAqG1zLOhz8O8l%2BPjtMYPUyROnG5F86Iv6g9I%2B0erkQi2q6VU%3D--Pd29VuY%2BbvFvvx%2Bn--zNg2UIxLtaxmCeKLXAnFLA%3D%3D',
'if-none-match': 'W/"1631c1a50ee628d602399c6f2add57e1"',
'referer': 'https://github.com/topics',
'sec-ch-ua': '"Google Chrome";v="95", "Chromium";v="95", ";Not A Brand";v="99"',
'sec-ch-ua-mobile': '?0',
'sec-ch-ua-platform': '"Windows"',
'sec-fetch-dest': 'document',
'sec-fetch-mode': 'navigate',
'sec-fetch-site': 'same-origin',
'sec-fetch-user': '?1',
'upgrade-insecure-requests': '1',
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}


url = 'https://github.com/topics'
html_text = requests.get(url).text
soup =BeautifulSoup(html_text, 'html.parser')
name_list_1 = []
data_1 = soup.findAll('div', {'class':'py-4 border-bottom'})
link_list_1 =[]
for links in data_1:
    link_1 = links.find('a')['href']
    #print('https://github.com' + link_1)
    link_list_1.append('https://github.com'+link_1)
#print(link_list_1)

for i in link_list_1:
    html_text_2 = requests.get(i, headers=headers).text
    soup_1 = BeautifulSoup(html_text_2, 'html.parser')
    items_1 = soup_1.findAll('article', {'class':'border rounded color-shadow-small color-bg-subtle my-4'})
    #print(len(items_1))

    for titles in items_1:
        title = titles.findAll('div',{'class':'d-flex flex-justify-between my-3'})
        for sub_title in title:
            repository_name = sub_title.find('a',{'data-view-component':'true'}).text
            repository_boldname = sub_title.find('a', {'class':'text-bold wb-break-word'}).text
            repositories_links = sub_title.find('a')['href']
            repositories_links_1 ='https://github.com'+repositories_links
            stars = sub_title.find('a', {'class':'social-count float-none'}).text
            github_dict={
                "Repository Name":str(repository_boldname).rstrip().lstrip() ,
                "UserName" : str(repository_name).rstrip().lstrip(),
                "Star_rating" : stars ,
                "Repositories link" : repositories_links_1
            }
            #print(github_dict)
            name_list_1.append(github_dict)

df =pd.DataFrame(name_list_1)
print(df)
df.to_csv('Github.csv')
