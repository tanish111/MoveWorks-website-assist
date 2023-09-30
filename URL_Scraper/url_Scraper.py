from bs4 import BeautifulSoup
import requests
import csv
url_list = {}
field_names= ['URL', 'Count']
def get_url(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content,'html.parser')
    for a in soup.find_all('a',href=True):
        single_url = a['href']
        if(single_url[0]=='/'):
            single_url = URL+single_url[1:]
        if single_url not in url_list:
            url_list[single_url] = 1
        else:
            url_list[single_url] = url_list[single_url]+1
BaseURL = "https://www.moveworks.com/"
get_url(BaseURL)
url2 = list(url_list)
for i in url2:
    get_url(i)
    print(len(url_list))
with open('URLs.csv', 'w') as f:
    f.write("URL,Count\n")
    for key in url_list.keys():
        f.write("%s,%s\n"%(key,url_list[key]))


