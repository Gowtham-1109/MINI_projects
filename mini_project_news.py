import requests
from bs4 import BeautifulSoup



url="https://news.ycombinator.com/"
response=requests.get(url)
bs=BeautifulSoup(response.text,"html.parser")


news=bs.find_all("span",class_="titleline")

for h in news[:5]:
    print("\n",h.text)