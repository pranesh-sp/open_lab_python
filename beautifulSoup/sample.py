import urllib3.request
from bs4 import BeautifulSoup
import requests
result=requests.get("http://www.google.com")
print(result.status_code)
print(result.headers)
src=result.content
#print(src)
soup=BeautifulSoup(src ,"lxml")
link=soup.find_all('a')
print(link)
#extracting the link that has text image, bilt in fr
for l in link:
    if "About" in l.text:
        print(l)
        print(l.attrs['href'])
