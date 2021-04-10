import requests
from bs4 import BeautifulSoup

url = requests.get("http://ced.kmutnb.ac.th/")

soup = BeautifulSoup(url.content, 'html.parser')
find_word = soup.find_all("h4",{"class":"card-header font-weight-bold"})

for i in find_word:
    print(i.text)
    