from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/National_Pro_Grid_League"
r = requests.get(url)
soup = BeautifulSoup(r.content)

# print(soup)

heading = soup.find(id='Active_teams')

print(heading)

teams = heading.find_next('ul')

print(teams)

# for team in teams:
#     print team.string
