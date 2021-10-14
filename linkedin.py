import requests
from bs4 import BeautifulSoup

for i in range(0,5):
    url = f'https://www.linkedin.com/jobs/search?keywords=Python%20Developer&location=United%20States&geoId=103644278&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum={i}'
    html_text = requests.get(url).text
    #print(html_text)
    soup_1 = BeautifulSoup(html_text, 'html.parser')

    jobs = soup_1.find('ul', {'class':'jobs-search__results-list'})
    job = jobs.findAll('li')
    list= []
    for links in job:
        link = links.find('a')['href']
        list.append(link)
    for linkk in list:
        print("Applylinkk :", linkk)
        html_text_1 = requests.get(linkk).text
        soup = BeautifulSoup(html_text_1, 'html.parser')
        li = soup.findAll('li', {'class': 'description__job-criteria-item'})
        try:
            job = soup.find('h1', {'class': 'top-card-layout__title topcard__title'}).text
            print("Job :" , job)
        except:
            pass
        list_2 =[]
        for data2 in li:
            main = data2.find('h3', {'class' : 'description__job-criteria-subheader'}).text
            mian_yy = data2.find('span',{'class':'description__job-criteria-text description__job-criteria-text--criteria'}).text
            print(main, mian_yy)

        try :
            posted_jobs = soup.find('span', {'class':'posted-time-ago__text topcard__flavor--metadata'}).text.strip()
            list_2.append(posted_jobs)
        except:
            pass

        print("Posted_jobs :", list_2)
        print("                                                               ----------------------------------                             ")
