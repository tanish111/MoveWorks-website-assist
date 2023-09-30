import re
import json
from sklearn.model_selection import train_test_split
import requests
from bs4 import BeautifulSoup
import pandas as pd
import requests
import xml.etree.ElementTree as ET
sitemap_url = 'https://moveworks.com/sitemap.xml'  # Replace with the URL of the sitemap you want to scrape

# Send an HTTP GET request to the sitemap.xml URL
response = requests.get(sitemap_url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the sitemap XML content
    root = ET.fromstring(response.text)
    all_texth = []
    all_textp=[]
    # Iterate through each URL in the sitemap
    for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}loc'):
        url1 = url.text.strip()
        response = requests.get(url1)
        with open(r'C:\Users\opvv1\OneDrive\Desktop\move\headings.json') as f:
            data = json.load(f)

        def build_text_files(data_json, dest_path):
            f = open(dest_path, 'w')
            data = ''
            for texts in data_json:
                summary = str(texts[url1]).strip()
                summary = re.sub(r"\s", " ", summary)
                data += summary + "  "
            f.write(data)

train, test = train_test_split(data,test_size=0.15)

build_text_files(train,'train_dataset.txt')
build_text_files(test,'test_dataset.txt')

print("Train dataset length: "+str(len(train)))
print("Test dataset length: "+ str(len(test)))

#Train dataset length: 10361
#Test dataset length: 1829
