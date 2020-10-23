from bs4 import BeautifulSoup
import requests
res = requests.get('https://news.ycombinator.com/news')

soup = BeautifulSoup(res.text,'html.parser')
print(soup.select('.score'))

