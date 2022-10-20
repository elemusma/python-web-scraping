from bs4 import BeautifulSoup
import requests

url = 'https://seekingalpha.com/market-news'
# url = 'https://seekingalpha.com/symbol/TSLA/analysis'
# url = 'https://seeking-alpha.p.rapidapi.com/analysis/TSLA/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

titles = soup.select('a.qfE')

titlesAll = titles[:10]

for anchor in titlesAll:
    print('hello')
    print(anchor.text)


# print(titles)

# news = soup.find(name="ul", attrs={'class':'item-list','id':'latest-news-list'})
# root = 'https://seekingalpha.com'

# root = 'https://seekingalpha.com'

# id_list = [i.text for i in news.find_all(name='li',attrs={'class':'item'})]
