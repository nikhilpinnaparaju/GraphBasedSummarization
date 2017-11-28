from bs4 import BeautifulSoup
import requests

url = raw_input("Enter a website to extract the URL's from: ")
r  = requests.get(url)

data = r.text

# print data

soup = BeautifulSoup(data)

# print soup

# for link in soup.find_all('p'):
#     # print(link.get('href'))

page = soup.find_all('p')

# print page

fname = url.split("/")

fname = fname[len(fname)-1]

fname = fname + ".txt"

f = open(fname, 'w+')

for i in page:
    w = i.getText()
    f.write(w.encode('utf8'))

f.close